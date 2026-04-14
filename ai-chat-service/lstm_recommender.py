import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding, Dropout

class LSTMRecommender:
    """
    Mô hình Mạng nơ-ron hồi quy LSTM (Long Short-Term Memory)
    Mục đích: Phân tích chuỗi hành vi lịch sử click/view của khách hàng để dự đoán sản phẩm tiếp theo.
    """
    def __init__(self, vocab_size=10000, embedding_dim=128, max_sequence_len=20):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.max_sequence_len = max_sequence_len
        self.model = self._build_lstm_model()

    def _build_lstm_model(self):
        # Thiết kế Cấu trúc Mạng Neural dựa trên Rubric đánh giá
        model = Sequential([
            # 1. Embedding Layer: Đưa ID sản phẩm vào không gian Vector nhiều chiều
            Embedding(input_dim=self.vocab_size, output_dim=self.embedding_dim, input_length=self.max_sequence_len),
            
            # 2. LSTM Layer 1: Ghi nhớ chuỗi truy cập dài hạn (VD: Xem Điên thoại -> Xem Ốp lưng)
            LSTM(64, return_sequences=True),
            
            # 3. Dropout xử lý Overfitting (Chống học vẹt 20%)
            Dropout(0.2),
            
            # 4. LSTM Layer 2: Chắt lọc đặc trưng sâu
            LSTM(32, return_sequences=False),
            
            # 5. Output Dense Layer + Khởi tạo dự đoán Softmax (Tỉ lệ % mua sản phẩm nào cao nhất)
            Dense(self.vocab_size, activation='softmax')
        ])
        
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        return model

    def train_customer_behavior(self, x_train, y_train, epochs=10, batch_size=32):
        """
        x_train: Ma trận lịch sử click (mỗi hàng là 1 chuỗi ID sp khách đã xem)
        y_train: Sản phẩm khách đã bỏ vào giỏ hàng ở bước cuối cùng
        """
        print("Đang huấn luyện mô hình hành vi trên tập khách hàng hiện tại...")
        self.model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)

    def predict_next_item(self, session_sequence):
        """
        Dự đoán món hàng người dùng khả năng cao sẽ mua tiếp theo
        """
        prediction_probs = self.model.predict(np.array([session_sequence]))
        best_item_id = np.argmax(prediction_probs[0])
        return best_item_id

if __name__ == "__main__":
    # Khởi chạy Code kiểm tra mô phỏng
    lstm = LSTMRecommender(vocab_size=100, embedding_dim=64, max_sequence_len=5)
    lstm.model.summary()
