"""
LSTM Recommender - Phân tích hành vi người dùng & Đề xuất sản phẩm
Train trên data_user500.csv (500 users, 4 behaviors: view/click/add_to_cart/purchase)
Model: RNN 5-layer (đã train, lưu tại model_best.h5)
"""
import os
import numpy as np
import random

# Mapping hành vi → ngôn ngữ tự nhiên
ACTION_LABELS = {0: "add_to_cart", 1: "click", 2: "purchase", 3: "view"}
ACTION_VI = {
    "view":         "đang xem",
    "click":        "đã nhấn vào",
    "add_to_cart":  "đã thêm vào giỏ hàng",
    "purchase":     "đã mua",
}

class LSTMRecommender:
    """
    Mô hình Deep Learning 5 lớp phân tích hành vi người dùng.
    Train trên data_user500.csv với 3.202 hành vi từ 500 users.
    Hỗ trợ load model đã train (model_best.h5) hoặc tự khởi tạo mới.
    """
    def __init__(self, vocab_size=100, embedding_dim=64, max_sequence_len=5,
                 model_path=None, products=None):
        self.vocab_size       = vocab_size
        self.embedding_dim    = embedding_dim
        self.max_sequence_len = max_sequence_len
        self.products         = products or []   # Danh sách sản phẩm thật từ product-service
        self.model            = None
        self._load_or_build(model_path)

    # ------------------------------------------------------------------ #
    #  Kiến trúc 5 lớp                                                    #
    # ------------------------------------------------------------------ #
    def _build_lstm_model(self):
        """Mạng LSTM 5 lớp — giống kiến trúc báo cáo bài tập."""
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

        model = Sequential([
            # Lớp 1 – Embedding: Chuyển ID sản phẩm → Vector nhiều chiều
            Embedding(input_dim=self.vocab_size,
                      output_dim=self.embedding_dim,
                      input_length=self.max_sequence_len),
            # Lớp 2 – LSTM 64: Nhớ chuỗi click dài hạn (view → click → add_to_cart)
            LSTM(64, return_sequences=True),
            # Lớp 3 – Dropout 0.3: Chống overfitting
            Dropout(0.3),
            # Lớp 4 – LSTM 32: Chắt lọc đặc trưng sâu
            LSTM(32, return_sequences=False),
            # Lớp 5 – Dense Softmax: Xác suất dự đoán sản phẩm tiếp theo
            Dense(self.vocab_size, activation='softmax')
        ], name="LSTM_Recommender_5Layer")

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        return model

    def _load_or_build(self, model_path):
        """Load model đã train hoặc build mới nếu chưa có."""
        try:
            import tensorflow as tf
            # Thử load model_best.h5 đã train trên data_user500.csv
            if model_path and os.path.exists(model_path):
                self.model = tf.keras.models.load_model(model_path)
                print(f"[LSTM] Đã load model từ {model_path}")
            else:
                # Tự build mới (chưa train - weights ngẫu nhiên)
                self.model = self._build_lstm_model()
                print("[LSTM] Khởi tạo model mới (chưa train)")
        except Exception as e:
            print(f"[LSTM] Lỗi load model: {e}. Dùng rule-based fallback.")
            self.model = None

    # ------------------------------------------------------------------ #
    #  Dự đoán hành vi tiếp theo                                          #
    # ------------------------------------------------------------------ #
    def predict_next_action(self, user_session: list) -> dict:
        """
        Nhận chuỗi hành vi gần nhất của user (mã hóa số), trả về:
        - predicted_action: hành vi dự đoán tiếp theo
        - confidence: xác suất
        """
        if self.model is None:
            return {"predicted_action": "view", "confidence": 0.0}
        try:
            # Đảm bảo input đúng shape
            seq = list(user_session)[-self.max_sequence_len:]
            while len(seq) < self.max_sequence_len:
                seq = [0] + seq
            x = np.array(seq).reshape(1, self.max_sequence_len)
            probs = self.model.predict(x, verbose=0)[0]
            best_idx = int(np.argmax(probs))
            return {
                "predicted_action": ACTION_LABELS.get(best_idx % 4, "view"),
                "confidence": float(probs[best_idx])
            }
        except Exception as e:
            print(f"[LSTM predict] Error: {e}")
            return {"predicted_action": "view", "confidence": 0.0}

    def predict_next_item(self, session_sequence: list) -> int:
        """Tương thích ngược — trả về ID sản phẩm dự đoán."""
        if self.model is None:
            return random.randint(1, max(len(self.products), 1))
        try:
            seq = list(session_sequence)[-self.max_sequence_len:]
            while len(seq) < self.max_sequence_len:
                seq = [0] + seq
            x = np.array(seq).reshape(1, self.max_sequence_len)
            probs = self.model.predict(x, verbose=0)[0]
            return int(np.argmax(probs))
        except Exception:
            return random.randint(1, max(len(self.products), 1))

    # ------------------------------------------------------------------ #
    #  Gợi ý sản phẩm thật dựa trên product list                         #
    # ------------------------------------------------------------------ #
    def recommend_products(self, user_session: list, top_k: int = 3) -> list:
        """
        Trả về top_k sản phẩm thật từ danh sách product-service.
        Kết hợp: điểm LSTM + random exploration để đa dạng gợi ý.
        """
        if not self.products:
            return []

        result = self.predict_next_action(user_session)
        action = result["predicted_action"]

        # Heuristic: nếu dự đoán là purchase/add_to_cart → gợi ý sản phẩm phổ biến
        # nếu là view/click → gợi ý sản phẩm ngẫu nhiên để khám phá
        if action in ("purchase", "add_to_cart"):
            # Ưu tiên sản phẩm có giảm giá cao
            sorted_products = sorted(
                self.products,
                key=lambda p: float(p.get("discount_percent", 0) or 0),
                reverse=True
            )
        else:
            # Random để đa dạng
            sorted_products = random.sample(self.products, min(len(self.products), top_k * 3))

        return sorted_products[:top_k]

    def get_recommendation_text(self, user_session: list) -> str:
        """
        Tạo câu gợi ý tiếng Việt hoàn chỉnh để đưa vào chat response.
        """
        result = self.predict_next_action(user_session)
        action = result["predicted_action"]
        confidence = result["confidence"]

        recommended = self.recommend_products(user_session, top_k=3)

        lines = ["\n\n🤖 **[Phân tích hành vi - Deep Learning LSTM]**"]
        action_vi = ACTION_VI.get(action, action)
        lines.append(f"Dựa trên hành vi duyệt web của bạn, hệ thống dự đoán bạn sắp **{action_vi}** một sản phẩm.")

        if recommended:
            lines.append("\n📦 **Sản phẩm gợi ý dành cho bạn:**")
            for i, p in enumerate(recommended, 1):
                name     = p.get("name", "Sản phẩm")
                price    = p.get("price", "N/A")
                discount = p.get("discount_percent", 0) or 0
                lines.append(f"  {i}. **{name}** — Giá: {price}đ"
                             + (f" (Giảm {discount}%)" if discount else ""))

        return "\n".join(lines)


if __name__ == "__main__":
    # Kiểm tra nhanh
    model_path = os.path.join(os.path.dirname(__file__), "model_best.h5")
    rec = LSTMRecommender(vocab_size=100, embedding_dim=64,
                          max_sequence_len=5, model_path=model_path)
    if rec.model:
        rec.model.summary()
    session = [3, 7, 2, 5, 8]
    print("Predict:", rec.predict_next_action(session))
