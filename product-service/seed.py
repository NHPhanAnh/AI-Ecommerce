"""
Seed dữ liệu sản phẩm thật cho Tech Store
Bao gồm: Laptop, Điện thoại, Máy tính bảng, Smartwatch, Tai nghe,
         Loa Bluetooth, Màn hình, Bàn phím, Chuột, Cáp sạc
Giá theo thị trường Việt Nam (đã bao gồm VAT, đơn vị: VNĐ)
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_service.settings')
django.setup()

from app.models import Product

def seed_db():
    print("Clearing old data...")
    Product.objects.all().delete()

    # ==============================================================
    # Danh sách sản phẩm THẬT theo từng danh mục
    # ==============================================================
    real_products = [

        # ==================== LAPTOP ====================
        {"category": "Laptop", "name": "MacBook Air M3 13 inch 2024",
         "price": 28490000, "stock": 25, "discount_percent": 5,
         "description": "Chip Apple M3 8-core CPU / 10-core GPU, RAM 8GB Unified, SSD 256GB, màn 13.6\" Liquid Retina, pin 18h, trọng lượng 1.24kg, màu Midnight.",
         "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500"},

        {"category": "Laptop", "name": "MacBook Pro M3 Pro 14 inch",
         "price": 52990000, "stock": 12, "discount_percent": 0,
         "description": "Chip Apple M3 Pro 11-core CPU / 14-core GPU, RAM 18GB, SSD 512GB, màn 14.2\" Liquid Retina XDR ProMotion 120Hz, MagSafe 3, pin 22h.",
         "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500"},

        {"category": "Laptop", "name": "Dell XPS 15 9530 Core i9",
         "price": 48990000, "stock": 8, "discount_percent": 10,
         "description": "Intel Core i9-13900H, RAM 32GB DDR5, SSD 1TB NVMe, RTX 4070 8GB, màn 15.6\" OLED 3.5K 60Hz, trọng lượng 1.86kg, Windows 11 bản quyền.",
         "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500"},

        {"category": "Laptop", "name": "ASUS ROG Zephyrus G14 2024",
         "price": 39990000, "stock": 15, "discount_percent": 8,
         "description": "AMD Ryzen 9 8945HS, RAM 32GB LPDDR5X, SSD 1TB PCIe 4.0, RTX 4070 8GB, màn 14\" QHD+ 165Hz, trọng lượng 1.65kg, sạc nhanh 100W.",
         "image_url": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=500"},

        {"category": "Laptop", "name": "Lenovo ThinkPad X1 Carbon Gen 12",
         "price": 42990000, "stock": 10, "discount_percent": 5,
         "description": "Intel Core Ultra 7 165H, RAM 32GB LPDDR5, SSD 1TB, màn 14\" IPS 2.8K OLED 120Hz, bảo mật vân tay + IR camera, trọng lượng 1.12kg.",
         "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500"},

        {"category": "Laptop", "name": "HP Envy x360 14 2-in-1 2024",
         "price": 21990000, "stock": 20, "discount_percent": 15,
         "description": "Intel Core Ultra 5 125U, RAM 16GB DDR5, SSD 512GB, màn cảm ứng 14\" OLED 2.8K 120Hz, bút stylus, xoay 360°, Windows 11 Home.",
         "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500"},

        {"category": "Laptop", "name": "Acer Swift Go 14 Core Ultra",
         "price": 18490000, "stock": 30, "discount_percent": 10,
         "description": "Intel Core Ultra 5 125H, RAM 16GB LPDDR5, SSD 512GB, màn 14\" 2.8K OLED 90Hz, pin 12h, trọng lượng 1.25kg, hỗ trợ AI NPU.",
         "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500"},

        {"category": "Laptop", "name": "MSI Katana 15 B13V RTX 4060",
         "price": 26990000, "stock": 18, "discount_percent": 12,
         "description": "Intel Core i7-13620H, RAM 16GB DDR5, SSD 512GB NVMe, RTX 4060 8GB, màn 15.6\" FHD 144Hz, tản nhiệt Cooler Boost 5.",
         "image_url": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=500"},

        {"category": "Laptop", "name": "Samsung Galaxy Book4 Pro 360",
         "price": 34990000, "stock": 7, "discount_percent": 0,
         "description": "Intel Core Ultra 7 155H, RAM 16GB, SSD 512GB, màn cảm ứng 16\" AMOLED 2.8K 120Hz, bút S Pen tặng kèm, tích hợp AI Samsung.",
         "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500"},

        {"category": "Laptop", "name": "Gigabyte G5 KF RTX 4060",
         "price": 22490000, "stock": 22, "discount_percent": 20,
         "description": "Intel Core i5-13500H, RAM 16GB DDR5, SSD 512GB PCIe 4.0, RTX 4060 8GB, màn 15.6\" FHD 144Hz, tản nhiệt kép Windforce.",
         "image_url": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=500"},

        # ==================== ĐIỆN THOẠI ====================
        {"category": "Điện thoại", "name": "iPhone 16 Pro Max 256GB",
         "price": 34990000, "stock": 40, "discount_percent": 0,
         "description": "Chip A18 Pro 3nm, camera 48MP Fusion + 48MP Ultra Wide + 12MP Telephoto 5x, màn Super Retina XDR 6.9\" ProMotion 120Hz, pin 33h, hỗ trợ Apple Intelligence.",
         "image_url": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=500"},

        {"category": "Điện thoại", "name": "iPhone 15 128GB",
         "price": 20490000, "stock": 55, "discount_percent": 10,
         "description": "Chip A16 Bionic, Dynamic Island, camera 48MP + 12MP Ultra Wide, cổng USB-C, màn Super Retina XDR 6.1\" OLED, 5G.",
         "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500"},

        {"category": "Điện thoại", "name": "Samsung Galaxy S24 Ultra 256GB",
         "price": 33990000, "stock": 30, "discount_percent": 5,
         "description": "Snapdragon 8 Gen 3, bút S Pen tích hợp, camera 200MP + 50MP Telephoto 5x, màn Dynamic AMOLED 6.8\" 120Hz, RAM 12GB, pin 5000mAh sạc 45W.",
         "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500"},

        {"category": "Điện thoại", "name": "Samsung Galaxy S24 FE 128GB",
         "price": 13990000, "stock": 60, "discount_percent": 15,
         "description": "Exynos 2500, màn Dynamic AMOLED 6.7\" 120Hz, camera 50MP + 8MP + 10MP Telephoto 3x, pin 4700mAh sạc 25W, chống nước IP68.",
         "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500"},

        {"category": "Điện thoại", "name": "OPPO Find X8 Pro 256GB",
         "price": 28990000, "stock": 20, "discount_percent": 8,
         "description": "MediaTek Dimensity 9400, camera Hasselblad 50MP + 50MP Telephoto 3x, màn AMOLED 6.78\" 120Hz, pin 6000mAh sạc nhanh 80W + không dây 50W.",
         "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500"},

        {"category": "Điện thoại", "name": "Xiaomi Redmi Note 14 Pro+ 256GB",
         "price": 9490000, "stock": 80, "discount_percent": 10,
         "description": "Snapdragon 7s Gen 3, camera 50MP Sony IMX882 + OIS, màn AMOLED 6.67\" 120Hz, pin 5110mAh sạc nhanh 90W HyperCharge, IP68.",
         "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500"},

        {"category": "Điện thoại", "name": "OPPO Reno 12 Pro 256GB",
         "price": 12490000, "stock": 45, "discount_percent": 20,
         "description": "MediaTek Dimensity 7300-Energy, camera 50MP + 50MP Telephoto, màn AMOLED 6.7\" 120Hz, pin 5000mAh sạc 80W, RAM 12GB.",
         "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500"},

        {"category": "Điện thoại", "name": "Samsung Galaxy A55 5G 128GB",
         "price": 8490000, "stock": 90, "discount_percent": 5,
         "description": "Exynos 1480, màn Super AMOLED 6.6\" 120Hz, camera 50MP + OIS, pin 5000mAh sạc 25W, chống nước IP67, thiết kế kính Gorilla Glass Victus+.",
         "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500"},

        {"category": "Điện thoại", "name": "Vivo V40 Lite 5G 128GB",
         "price": 6490000, "stock": 70, "discount_percent": 0,
         "description": "Snapdragon 4 Gen 2, màn AMOLED 6.77\" 120Hz, camera 50MP AI, pin 5500mAh sạc 44W, Face ID + vân tay, chống nước IP64.",
         "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500"},

        {"category": "Điện thoại", "name": "Google Pixel 9 Pro 256GB",
         "price": 26990000, "stock": 15, "discount_percent": 0,
         "description": "Chip Google Tensor G4, camera 50MP Pro + 48MP Telephoto 5x, màn OLED 6.3\" 120Hz, 7 năm cập nhật OS, RAM 16GB, AI Google Gemini tích hợp.",
         "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500"},

        # ==================== MÁY TÍNH BẢNG ====================
        {"category": "Máy tính bảng", "name": "iPad Pro M4 13 inch Wi-Fi 256GB",
         "price": 36990000, "stock": 15, "discount_percent": 0,
         "description": "Chip Apple M4 10-core CPU, màn Ultra Retina XDR 13\" OLED 120Hz ProMotion, mỏng nhất từ trước đến nay 5.1mm, hỗ trợ Apple Pencil Pro và Magic Keyboard.",
         "image_url": "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=500"},

        {"category": "Máy tính bảng", "name": "iPad Air M2 11 inch Wi-Fi 128GB",
         "price": 17990000, "stock": 30, "discount_percent": 5,
         "description": "Chip Apple M2 8-core CPU, màn Liquid Retina 11\" True Tone P3, camera 12MP Ultra Wide, Face ID ngang, hỗ trợ Apple Pencil Pro.",
         "image_url": "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=500"},

        {"category": "Máy tính bảng", "name": "Samsung Galaxy Tab S10+ 256GB",
         "price": 24990000, "stock": 18, "discount_percent": 10,
         "description": "Snapdragon 8 Gen 3, màn Dynamic AMOLED 12.4\" 120Hz, bút S Pen tặng kèm, camera 13MP + 8MP, pin 10090mAh, chống nước IP68, RAM 12GB.",
         "image_url": "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=500"},

        {"category": "Máy tính bảng", "name": "Samsung Galaxy Tab A9+ 5G 64GB",
         "price": 8990000, "stock": 40, "discount_percent": 15,
         "description": "Snapdragon 695, màn IPS 11\" 90Hz, 4 loa AKG Dolby Atmos, camera 13MP, pin 7040mAh, hỗ trợ S Pen (bán riêng), RAM 8GB.",
         "image_url": "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=500"},

        {"category": "Máy tính bảng", "name": "Xiaomi Pad 7 Pro 256GB",
         "price": 12490000, "stock": 25, "discount_percent": 8,
         "description": "Snapdragon 8s Gen 3, màn LCD 11.2\" 3.2K 144Hz, pin 9000mAh sạc nhanh 45W, camera 50MP, RAM 12GB, hỗ trợ bút Xiaomi Smart Pen 3.",
         "image_url": "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=500"},

        {"category": "Máy tính bảng", "name": "Lenovo Tab P12 Pro 256GB",
         "price": 16990000, "stock": 12, "discount_percent": 0,
         "description": "MediaTek Kompanio 1300T, màn AMOLED 12.6\" 2K 120Hz, pin 10200mAh sạc 45W, camera 13MP, 4 loa JBL Dolby Atmos, RAM 8GB.",
         "image_url": "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=500"},

        {"category": "Máy tính bảng", "name": "OPPO Pad Air2 128GB",
         "price": 7490000, "stock": 35, "discount_percent": 20,
         "description": "Snapdragon 695, màn LCD 11.35\" 2.4K 90Hz, pin 8000mAh sạc 33W, camera 8MP + 5MP, bộ nhớ RAM 6GB, hỗ trợ bút cảm ứng stylus.",
         "image_url": "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=500"},

        {"category": "Máy tính bảng", "name": "iPad 10th Gen Wi-Fi 64GB",
         "price": 10990000, "stock": 50, "discount_percent": 0,
         "description": "Chip Apple A14 Bionic, màn Liquid Retina 10.9\" True Tone, camera 12MP Ultra Wide, USB-C, hỗ trợ Apple Pencil thế hệ 1, Wi-Fi 6.",
         "image_url": "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=500"},

        {"category": "Máy tính bảng", "name": "Huawei MatePad Pro 11 2024",
         "price": 14990000, "stock": 10, "discount_percent": 5,
         "description": "Kirin 9010, màn OLED 11\" 2.8K 144Hz, bút M-Pencil thế hệ 3 tặng kèm, pin 8800mAh sạc nhanh 88W, camera 13MP, RAM 8GB.",
         "image_url": "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=500"},

        {"category": "Máy tính bảng", "name": "Microsoft Surface Pro 11 Copilot+ PC",
         "price": 31990000, "stock": 8, "discount_percent": 0,
         "description": "Snapdragon X Elite X1E-80-100, màn cảm ứng 13\" 120Hz 2880x1920, phím Type Cover và bút Surface Slim Pen 2 bán riêng, RAM 16GB, SSD 512GB.",
         "image_url": "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=500"},

        # ==================== ĐỒNG HỒ THÔNG MINH ====================
        {"category": "Đồng hồ thông minh", "name": "Apple Watch Series 10 GPS 42mm",
         "price": 10990000, "stock": 35, "discount_percent": 0,
         "description": "Chip S10 SiP, màn AMOLED 42mm Always-On Retina, đo SPO2/ECG/huyết áp, watchOS 11, pin 18h, chống nước 50m, sạc từ tính nhanh.",
         "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500"},

        {"category": "Đồng hồ thông minh", "name": "Samsung Galaxy Watch 7 44mm",
         "price": 7490000, "stock": 40, "discount_percent": 10,
         "description": "Exynos W1000, màn Super AMOLED 44mm 430x430, đo đường huyết tương đối, theo dõi giấc ngủ nâng cao, pin 40h, OneUI Watch 6.",
         "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500"},

        {"category": "Đồng hồ thông minh", "name": "Garmin Forerunner 965 GPS",
         "price": 18490000, "stock": 12, "discount_percent": 0,
         "description": "GPS đa băng tần, màn AMOLED 454x454, pin 31 ngày chế độ đồng hồ / 23h GPS, đo VO2max, nhịp tim quang học, 5ATM, dành cho runner chuyên nghiệp.",
         "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500"},

        {"category": "Đồng hồ thông minh", "name": "Garmin Vivoactive 5 GPS",
         "price": 6990000, "stock": 20, "discount_percent": 5,
         "description": "AMOLED 416x416, pin 11 ngày, GPS tích hợp, 25+ chế độ thể thao, đo nhịp tim + SPO2, tương thích iOS/Android, chống nước 5ATM.",
         "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500"},

        {"category": "Đồng hồ thông minh", "name": "Xiaomi Watch S4 Sport",
         "price": 3290000, "stock": 60, "discount_percent": 15,
         "description": "AMOLED 1.43\" 466x466, pin 15 ngày, GPS GNSS đa hệ, 100+ chế độ thể thao, đo nhịp tim + SPO2, chống nước 5ATM, Alexa tích hợp.",
         "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500"},

        {"category": "Đồng hồ thông minh", "name": "Huawei Watch GT 5 Pro 46mm",
         "price": 8990000, "stock": 15, "discount_percent": 8,
         "description": "AMOLED 1.43\" sapphire glass, pin 14 ngày, GPS đa tần, đo ECG + huyết áp, 100+ chế độ thể thao, chống nước 5ATM, cuộc gọi Bluetooth.",
         "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500"},

        {"category": "Đồng hồ thông minh", "name": "OPPO Watch X Snapdragon W5+",
         "price": 7490000, "stock": 18, "discount_percent": 20,
         "description": "Snapdragon W5+ Gen 1, màn AMOLED 1.43\" 466x466, pin 12 ngày, Wear OS 4 + ColorOS Watch, GPS, đo ECG + nhịp tim, chống nước 5ATM.",
         "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500"},

        {"category": "Đồng hồ thông minh", "name": "Samsung Galaxy Watch Ultra 47mm",
         "price": 18990000, "stock": 8, "discount_percent": 0,
         "description": "Exynos W1000, khung Titan, AMOLED 480x480 cực bền, pin 60h tiết kiệm điện, 10ATM 100m, đo ECG + huyết áp + nhiệt độ da.",
         "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500"},

        {"category": "Đồng hồ thông minh", "name": "Amazfit GTR 4 Smartwatch",
         "price": 2990000, "stock": 50, "discount_percent": 10,
         "description": "AMOLED 1.43\" 466x466, pin 14 ngày, GPS 4 chòm sao, 150+ chế độ thể thao, đo SpO2 + nhịp tim, Alexa, chống nước 5ATM.",
         "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500"},

        {"category": "Đồng hồ thông minh", "name": "Apple Watch Ultra 2 GPS+Cellular 49mm",
         "price": 23990000, "stock": 5, "discount_percent": 0,
         "description": "Chip S9 SiP, khung Titan Grade 23, màn Sapphire Crystal AMOLED 2000 nit, pin 36h (60h chế độ tiết kiệm), 100m chống nước, dành cho hoạt động ngoài trời.",
         "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500"},

        # ==================== TAI NGHE ====================
        {"category": "Tai nghe", "name": "AirPods Pro 2 (USB-C) 2024",
         "price": 6290000, "stock": 50, "discount_percent": 5,
         "description": "Chip H2, chống ồn ANC 2 lần nâng cấp, Transparency Mode thích nghi, âm thanh Spatial tự động, IP54, pin 6h + 30h case sạc, MagSafe.",
         "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"},

        {"category": "Tai nghe", "name": "Sony WF-1000XM5",
         "price": 6490000, "stock": 30, "discount_percent": 15,
         "description": "ANC hàng đầu thế giới, driver Carbon Fiber 8.4mm, codec LDAC Hi-Res, pin 8h + 16h case, Speak-to-Chat thông minh, chống nước IPX4.",
         "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"},

        {"category": "Tai nghe", "name": "Sony WH-1000XM5 Over-Ear",
         "price": 7990000, "stock": 25, "discount_percent": 10,
         "description": "ANC 8 mic, driver 30mm V1, LDAC / DSEE Extreme, pin 30h, sạc nhanh 3 phút = 3h, đàm thoại 6 lần nâng cấp, gập gọn mang đi.",
         "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"},

        {"category": "Tai nghe", "name": "Samsung Galaxy Buds3 Pro",
         "price": 4990000, "stock": 40, "discount_percent": 20,
         "description": "ANC nâng cấp, driver 10.5mm + tweeter 6.1mm 2-way, codec SSC HiFi, pin 6h + 24h case, thiết kế mới Blade Idol, IP57.",
         "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"},

        {"category": "Tai nghe", "name": "Jabra Elite 10 Active ANC",
         "price": 5490000, "stock": 20, "discount_percent": 8,
         "description": "Jabra Advanced ANC+ thế hệ 2, driver 10mm, Spatial Sound tự động, pin 6h + 24h case, IP57, Multipoint 2 thiết bị cùng lúc.",
         "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"},

        {"category": "Tai nghe", "name": "Anker Soundcore Liberty 4 NC",
         "price": 1290000, "stock": 80, "discount_percent": 0,
         "description": "ANC 98.5%, driver coaxial kép 11mm + tweeter 6mm, LDAC, pin 10h + 38h case, sạc không dây, IPX4, hỗ trợ aptX Adaptive.",
         "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"},

        {"category": "Tai nghe", "name": "Nothing Ear (a) TWS",
         "price": 1990000, "stock": 60, "discount_percent": 0,
         "description": "Driver dynamic 11mm, ANC -45dB, Transparency Mode, pin 9.5h + 42.5h case, sạc nhanh (10 phút = 1h), IP54, âm thanh Hi-Res Audio Wireless.",
         "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"},

        {"category": "Tai nghe", "name": "Bose QuietComfort Ultra Earbuds",
         "price": 8490000, "stock": 15, "discount_percent": 0,
         "description": "ANC hạng nhất Bose, Bose Immersive Audio với CustomTune, driver 9.3mm, pin 9h + 24h case, IP54, 3 cỡ nút tai, kết nối 2 thiết bị.",
         "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"},

        {"category": "Tai nghe", "name": "Xiaomi Buds 5 Pro ANC",
         "price": 2490000, "stock": 70, "discount_percent": 15,
         "description": "ANC 55dB, driver dynamic 11mm + 2 BA, LHDC 5.0 Hi-Res, pin 8h + 36h case, sạc không dây Qi, IP55, latency 50ms chơi game.",
         "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"},

        {"category": "Tai nghe", "name": "OPPO Enco X3 TWS",
         "price": 2990000, "stock": 45, "discount_percent": 10,
         "description": "Co-tuned by Dynaudio, driver dynamic 10mm + BA, ANC 45dB, LDAC, pin 8h + 32h case, sạc nhanh 15 phút = 2h, IP55.",
         "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"},

        # ==================== LOA BLUETOOTH ====================
        {"category": "Loa Bluetooth", "name": "JBL Charge 5 Portable",
         "price": 3490000, "stock": 40, "discount_percent": 10,
         "description": "Công suất 40W, bass Rumbass, pin 20h, IP67 chống nước, chức năng sạc điện thoại, PartyBoost ghép nhiều loa, âm thanh 360° nổi bật.",
         "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500"},

        {"category": "Loa Bluetooth", "name": "Bose SoundLink Flex 2",
         "price": 4990000, "stock": 25, "discount_percent": 0,
         "description": "Công suất 30W, IP67, PositionIQ tự động điều chỉnh âm thanh, lướt sóng được, Bluetooth 5.3, pin 12h, sạc nhanh 20 phút = 3h.",
         "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500"},

        {"category": "Loa Bluetooth", "name": "Sony SRS-XB100",
         "price": 990000, "stock": 70, "discount_percent": 5,
         "description": "Công suất 16W, IP67, Extra Bass, pin 16h, nhỏ gọn 68x68x77mm, Hands-free mic, dây đeo đi kèm, sạc USB-C, Bluetooth 5.3.",
         "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500"},

        {"category": "Loa Bluetooth", "name": "Harman Kardon Onyx Studio 8",
         "price": 8490000, "stock": 15, "discount_percent": 5,
         "description": "Công suất 50W, 2 tweeter + woofer 133mm, pin 8h, IPX5, màn hình LED trang trí, GBT ghép loa, kết nối tới 10 thiết bị, thiết kế cao cấp.",
         "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500"},

        {"category": "Loa Bluetooth", "name": "Marshall Emberton III",
         "price": 3290000, "stock": 30, "discount_percent": 0,
         "description": "Công suất 20W loa stereo, pin 32h, IP67, Bluetooth 5.3 True Wireless Stereo, âm thanh Full Circle 360° đặc trưng Marshall, sạc USB-C.",
         "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500"},

        {"category": "Loa Bluetooth", "name": "JBL Flip 7",
         "price": 2490000, "stock": 50, "discount_percent": 8,
         "description": "Công suất 30W, IP68, pin 16h, PartyBoost ghép 100+ loa JBL, Playtime Boost mode thêm 35%, sạc nhanh USB-C, không dây Auracast.",
         "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500"},

        {"category": "Loa Bluetooth", "name": "Tribit StormBox Blast 2",
         "price": 3190000, "stock": 20, "discount_percent": 15,
         "description": "Công suất 120W peak, đèn LED RGB theo nhạc, IP67, pin 24h, XBass nâng bass, PartyAdd, Bluetooth 5.3, sạc USB-C nhanh.",
         "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500"},

        {"category": "Loa Bluetooth", "name": "Sony SRS-XG500 Party Speaker",
         "price": 6990000, "stock": 10, "discount_percent": 20,
         "description": "Công suất 90W, Extra Bass, đèn LED theo nhạc, pin 30h, IP66, Party Connect ghép 100 thiết bị, Guitar/Mic input 3.5mm, sạc USB-C.",
         "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500"},

        {"category": "Loa Bluetooth", "name": "Bang & Olufsen Beosound A1 3rd",
         "price": 9990000, "stock": 8, "discount_percent": 0,
         "description": "Công suất 30W, IP57, Adaptive Music Processing tự điều chỉnh âm, pin 36h, Auracast, thiết kế nhôm cao cấp Bang & Olufsen đặc trưng.",
         "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500"},

        {"category": "Loa Bluetooth", "name": "Xiaomi Sound 3 Outdoor Speaker",
         "price": 1490000, "stock": 80, "discount_percent": 10,
         "description": "Công suất 24W, đèn LED xoay 360°, IP67, pin 13h, kết nối 2 loa stereo, Xiaomi Share, Bluetooth 5.4, sạc USB-C 18W nhanh.",
         "image_url": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500"},

        # ==================== MÀN HÌNH ====================
        {"category": "Màn hình", "name": "Dell UltraSharp U2723QE 27\" 4K USB-C",
         "price": 16990000, "stock": 15, "discount_percent": 5,
         "description": "27\" IPS Black 4K 60Hz, DCI-P3 98% Rec 2020 95%, Delta E<2, USB-C 90W, kết nối KVM, không viền 3 cạnh, mắt xanh ComfortView Plus, VESA.",
         "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500"},

        {"category": "Màn hình", "name": "LG UltraGear 27GN950-B 4K 144Hz",
         "price": 18490000, "stock": 10, "discount_percent": 0,
         "description": "27\" Nano IPS 4K 144Hz 1ms GTG, HDR600, DCI-P3 98%, G-Sync/FreeSync Premium Pro, USB-C 94W, HDMI 2.1, DisplayPort 1.4, VESA.",
         "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500"},

        {"category": "Màn hình", "name": "ASUS ProArt PA279CRV 27\" 4K IPS",
         "price": 14990000, "stock": 12, "discount_percent": 8,
         "description": "27\" IPS 4K 60Hz, Adobe RGB 99% / sRGB 100% / DCI-P3 95%, Delta E<2, USB-C 96W, KVM, CalMAN Verified, dành cho đồ họa chết chuyên nghiệp.",
         "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500"},

        {"category": "Màn hình", "name": "Samsung Odyssey G7 32\" QHD 240Hz",
         "price": 13990000, "stock": 8, "discount_percent": 10,
         "description": "32\" IPS QHD 2560x1440 240Hz 1ms, HDR600, G-Sync/FreeSync Pro, DisplayHDR 600, HDMI 2.1, DP 1.4, loa tích hợp 5W, gaming cao cấp.",
         "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500"},

        {"category": "Màn hình", "name": "LG 27MQ780-B 27\" QHD IPS USB-C",
         "price": 8990000, "stock": 20, "discount_percent": 5,
         "description": "27\" IPS QHD 2560x1440 75Hz, sRGB 99%, USB-C 96W, RJ45 LAN, Auto KVM, Ergo Stand xoay ngả đầy đủ, HDR10, FreeSync.",
         "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500"},

        {"category": "Màn hình", "name": "Acer Nitro XV275K 27\" 4K 160Hz",
         "price": 9490000, "stock": 15, "discount_percent": 15,
         "description": "27\" IPS 4K 3840x2160 160Hz 1ms, HDR400, DCI-P3 90%, HDMI 2.1, DP 1.4, FreeSync Premium Pro, thiết kế gaming đỏ đen bắt mắt.",
         "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500"},

        {"category": "Màn hình", "name": "BenQ PD3220U 32\" 4K Thunderbolt 3",
         "price": 24990000, "stock": 5, "discount_percent": 0,
         "description": "32\" IPS 4K 60Hz, AdobeRGB 99%, Thunderbolt 3 85W, KVM, daisy chain, Hotkey Puck G3, AQCOLOR Delta E=1, dành cho nhà thiết kế chuyên nghiệp.",
         "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500"},

        {"category": "Màn hình", "name": "ViewSonic VP2776 27\" QHD IPS",
         "price": 11990000, "stock": 10, "discount_percent": 0,
         "description": "27\" IPS 2K QHD 60Hz, sRGB 100% / DCI-P3 99%, Delta E<2, USB-C 60W, HDMI 2.0, DP 1.2, giao diệu tối ưu cho thiết kế in ấn.",
         "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500"},

        {"category": "Màn hình", "name": "MSI MPG Artymis 343 UWQHD VA Curved",
         "price": 19990000, "stock": 7, "discount_percent": 20,
         "description": "34\" Curved VA UWQHD 3440x1440 165Hz 1ms MPRT, HDR400, DCI-P3 92%, USB-C 15W, PIP/PBP, KVM, tích hơp crosshair gaming.",
         "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500"},

        {"category": "Màn hình", "name": "Xiaomi 27\" QHD Fast IPS 180Hz",
         "price": 5490000, "stock": 35, "discount_percent": 5,
         "description": "27\" Fast IPS QHD 2560x1440 180Hz 1ms, sRGB 100%, AMD FreeSync Premium, HDMI 2.0 + DP 1.2, loa 2x3W tích hợp, thiết kế siêu mỏng.",
         "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500"},

        # ==================== BÀN PHÍM ====================
        {"category": "Bàn phím", "name": "Keychron Q1 Pro QMK Wireless",
         "price": 4990000, "stock": 20, "discount_percent": 0,
         "description": "Layout 75% (84 phím), Bluetooth 5.1 + USB-C, hot-swap tương thích 3/5-pin, gasket mount nhôm nguyên khối, RGB per-key, POM plate.",
         "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500"},

        {"category": "Bàn phím", "name": "Logitech MX Keys S Wireless",
         "price": 2990000, "stock": 40, "discount_percent": 10,
         "description": "Layout full size, Bluetooth 5.1, Easy-Switch 3 thiết bị, phím tròn lõm Smart backlighting tự điều chỉnh, cho máy Mac và Windows, pin 10 ngày.",
         "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500"},

        {"category": "Bàn phím", "name": "Razer BlackWidow V4 Pro Wireless",
         "price": 5990000, "stock": 15, "discount_percent": 5,
         "description": "75% Compact wireless, Razer Yellow switch im lặng, 2.4GHz + BT + wired, RGB Chroma, pin 200h không RGB, macro keys, hot-swap.",
         "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500"},

        {"category": "Bàn phím", "name": "Apple Magic Keyboard Touch ID M3",
         "price": 2490000, "stock": 30, "discount_percent": 0,
         "description": "Thiết kế mỏng thanh lịch, Touch ID tích hợp, Bluetooth 5.0, pin 1 tháng dùng liên tục, sạc Lightning, 78 phím US English, cho Mac M-series.",
         "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500"},

        {"category": "Bàn phím", "name": "Corsair K70 RGB Pro TKL",
         "price": 2290000, "stock": 25, "discount_percent": 15,
         "description": "TKL (87 phím), Cherry MX Red switch, RGB per-key, Steel plate, 8000Hz polling rate, USB passthrough, AXON Hyper Processing Architecture.",
         "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500"},

        {"category": "Bàn phím", "name": "NuPhy Air75 V2 Wireless QMK",
         "price": 3690000, "stock": 18, "discount_percent": 0,
         "description": "75% wireless, 2.4GHz + BT5.0 + USB-C, hot-swap 5-pin, low-profile switch (Gateron Wisteria), RGB backlit, foam nhét sẵn giảm tiếng ồn, nhôm.",
         "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500"},

        {"category": "Bàn phím", "name": "Samsung Smart Keyboard Trio 500",
         "price": 1490000, "stock": 50, "discount_percent": 20,
         "description": "Full-size Bluetooth 5.0, Multi-Device 3 thiết bị dễ chuyển bằng phím, dành cho Samsung DeX, pin 3 tháng, kết nối Windows/macOS/Android.",
         "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500"},

        {"category": "Bàn phím", "name": "SteelSeries Apex Pro TKL Wireless 2024",
         "price": 6490000, "stock": 10, "discount_percent": 0,
         "description": "TKL OmniPoint 3 Adjustable Magnetic Switch 14x nhanh hơn cơ học, 8000Hz Quantum 2.0, 2.4GHz + Bluetooth, OLED display, RGB, pin 45h.",
         "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500"},

        {"category": "Bàn phím", "name": "Epomaker x Aula F75 Gasket Wireless",
         "price": 2190000, "stock": 35, "discount_percent": 8,
         "description": "75% Gasket mount, Bluetooth 5.0 + 2.4G + USB-C, hot-swap 3/5-pin, RGB, foam nhét sẵn, nhôm alu nặng chắc, POM plate, Kailh switch.",
         "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500"},

        {"category": "Bàn phím", "name": "Logitech G Pro X TKL Wireless",
         "price": 3290000, "stock": 22, "discount_percent": 10,
         "description": "TKL, LIGHTSPEED 1ms wireless, hot-swap GX switch, RGB per-key LIGHTSYNC, nhôm nguyên khối, pin 50h, dành cho game thủ pro.",
         "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500"},

        # ==================== CHUỘT ====================
        {"category": "Chuột", "name": "Logitech MX Master 3S Wireless",
         "price": 2290000, "stock": 45, "discount_percent": 5,
         "description": "8K DPI, MagSpeed Electromagnetic scroll siêu nhanh, 7 nút lập trình, Bluetooth + Bolt USB, sạc USB-C, pin 70 ngày, cho Windows/Mac/Linux.",
         "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500"},

        {"category": "Chuột", "name": "Razer DeathAdder V3 HyperSpeed",
         "price": 1890000, "stock": 35, "discount_percent": 10,
         "description": "30K DPI Focus Pro sensor, HyperSpeed 2.4GHz wireless, trọng lượng 64g siêu nhẹ, 90h pin, ergonomic tay phải, 8 nút lập trình.",
         "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500"},

        {"category": "Chuột", "name": "Apple Magic Mouse USB-C",
         "price": 1990000, "stock": 30, "discount_percent": 0,
         "description": "Multi-Touch surface điều hướng cử chỉ, Bluetooth 5.0, thiết kế mỏng 22mm, sạc USB-C, nhôm phun sơn cao cấp, dành cho Mac.",
         "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500"},

        {"category": "Chuột", "name": "Logitech G502 X Plus Wireless",
         "price": 2490000, "stock": 25, "discount_percent": 8,
         "description": "25K DPI HERO sensor, LIGHTSPEED + Bluetooth, 13 nút lập trình, switch cơ học magnetic, RGB LIGHTSYNC, pin 130h, trọng lượng 106g.",
         "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500"},

        {"category": "Chuột", "name": "SteelSeries Prime Wireless",
         "price": 1790000, "stock": 40, "discount_percent": 15,
         "description": "18K DPI TrueMove Air optical, 2.4GHz Quantum 2.0 1ms, 5 nút, 100h pin, trọng lượng 73g, không RGB tiết kiệm pin, gaming FPS chuyên nghiệp.",
         "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500"},

        {"category": "Chuột", "name": "Corsair Katar Pro Wireless Ultralight",
         "price": 990000, "stock": 60, "discount_percent": 0,
         "description": "10K DPI PixArt 3335 sensor, Slipstream Wireless + Bluetooth + USB, 60g ultralight, pin 135h, 6 nút lập trình, dành cho game thủ ngân sách tốt.",
         "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500"},

        {"category": "Chuột", "name": "Asus ROG Harpe Ace Aim Lab Edition",
         "price": 3490000, "stock": 12, "discount_percent": 0,
         "description": "54K DPI ROG AimPoint Pro sensor, 8000Hz polling, 2.4GHz Tri-Mode, 54g ultralight hình dạng phân tích Aim Lab, SpeedNova switch cơ học.",
         "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500"},

        {"category": "Chuột", "name": "Xiaomi Wireless Mouse 2 Silent",
         "price": 349000, "stock": 100, "discount_percent": 0,
         "description": "1200 DPI, Bluetooth 5.0 + USB 2.4GHz dual mode, click yên tĩnh -85%, pin 1600mAh sạc micro-USB, 3 nút, nhỏ gọn 60g, phù hợp văn phòng.",
         "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500"},

        {"category": "Chuột", "name": "Logitech Lift Vertical Ergonomic",
         "price": 1490000, "stock": 28, "discount_percent": 5,
         "description": "Vertical ergonomic 57° giảm căng cổ tay, Bluetooth + Bolt USB, 400-4000 DPI, 6 nút lập trình, pin AA 2 năm, tay phải medium-large.",
         "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500"},

        {"category": "Chuột", "name": "BenQ Zowie EC2-CW Wireless",
         "price": 2790000, "stock": 15, "discount_percent": 0,
         "description": "3200 DPI PixArt 3370, 2.4GHz 1ms, trọng lượng 77g, plug-and-play không phần mềm, 5 nút, pin AA 70h, chuột gaming truyền thống FPS.",
         "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500"},

        # ==================== CÁP SẠC ====================
        {"category": "Cáp sạc", "name": "Anker 765 USB-C to USB-C 140W Thunderbolt 4",
         "price": 990000, "stock": 80, "discount_percent": 0,
         "description": "140W 48V/3A, Thunderbolt 4 data 40Gbps, video 8K@30Hz, dài 1.8m, vỏ nylon bện, chứng nhận Made for iPhone, tương thích USB-C đa năng.",
         "image_url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500"},

        {"category": "Cáp sạc", "name": "Apple USB-C to MagSafe 3 (2m)",
         "price": 890000, "stock": 50, "discount_percent": 0,
         "description": "Cáp MagSafe 3 chính hãng Apple dài 2m, hỗ trợ sạc nhanh tới 140W cho MacBook Pro 16\", braided, bảo vệ chống đứt đầu dây.",
         "image_url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500"},

        {"category": "Cáp sạc", "name": "Ugreen 100W USB-C to USB-C PD 2m",
         "price": 290000, "stock": 150, "discount_percent": 10,
         "description": "100W PD 3.0 5A, USB 2.0, dài 2m, vỏ nylon 15000+ lần uốn, chứng nhận E-Marker, tương thích laptop / điện thoại / máy tính bảng USB-C.",
         "image_url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500"},

        {"category": "Cáp sạc", "name": "Baseus 240W USB-C to USB-C 1m",
         "price": 390000, "stock": 100, "discount_percent": 5,
         "description": "240W 48V/5A, USB 2.0, E-Marker chip tích hợp, dài 1m, vỏ silicone linh hoạt, LED hiển thị công suất đang sạc, không rối cáp.",
         "image_url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500"},

        {"category": "Cáp sạc", "name": "Belkin BOOST CHARGE PRO USB-C 60W 2m",
         "price": 490000, "stock": 60, "discount_percent": 0,
         "description": "60W USB-C to USB-C PD, vỏ braid Braided, dài 2m, Made for iPhone chứng nhận, tương thích MacBook Air/iPad/iPhone/Android.",
         "image_url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500"},

        {"category": "Cáp sạc", "name": "Apple Lightning to USB-C 1m MFi",
         "price": 490000, "stock": 70, "discount_percent": 0,
         "description": "Lightning sang USB-C 1m chính hãng Apple MFi, hỗ trợ sạc nhanh 20W với adapter PD, data transfer, tương thích iPhone/AirPods.",
         "image_url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500"},

        {"category": "Cáp sạc", "name": "Anker 333 USB-C to USB-C 3-in-1 Cable",
         "price": 590000, "stock": 40, "discount_percent": 15,
         "description": "3-in-1: USB-C + Lightning + Micro-USB, 60W PD, dài 1.2m cắt bỏ được phần không dùng, nylon bện, tương thích Android/iPhone/AirPods cùng lúc.",
         "image_url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500"},

        {"category": "Cáp sạc", "name": "Xiaomi 60W USB-C Cable 1.5m",
         "price": 149000, "stock": 200, "discount_percent": 0,
         "description": "60W 3A fast charging, data USB 2.0, dài 1.5m, vỏ TPE mềm, không rối, tương thích mọi thiết bị USB-C Android/laptop, giá cực rẻ chính hãng Xiaomi.",
         "image_url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500"},

        {"category": "Cáp sạc", "name": "Samsung 45W USB-C Super Fast Charging 1.8m",
         "price": 390000, "stock": 80, "discount_percent": 10,
         "description": "45W Super Fast Charging 2.0 (PPSSF), USB-C to USB-C, dài 1.8m, tương thích Galaxy S/Note/Tab dùng sạc nhanh tốt nhất, data USB 3.0 5Gbps.",
         "image_url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500"},

        {"category": "Cáp sạc", "name": "Spigen PowerArc USB-C 180W Braided 2m",
         "price": 690000, "stock": 45, "discount_percent": 0,
         "description": "180W 36V/5A cho laptop cao cấp, USB 2.0, dài 2m, vỏ Aramid Fiber cực bền, gập 20000+ lần không gãy, tương thích Thunderbolt 4 / USB4.",
         "image_url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500"},
    ]

    print(f"Seeding {len(real_products)} real products...")

    product_objects = [
        Product(
            category=p["category"],
            name=p["name"],
            price=p["price"],
            stock=p["stock"],
            discount_percent=p["discount_percent"],
            description=p["description"],
            image_url=p["image_url"],
        )
        for p in real_products
    ]

    Product.objects.bulk_create(product_objects)
    print(f"✅ Successfully created {len(product_objects)} real products!")

    # In tóm tắt theo danh mục
    from collections import Counter
    cats = Counter(p["category"] for p in real_products)
    for cat, count in sorted(cats.items()):
        print(f"  - {cat}: {count} sản phẩm")


if __name__ == '__main__':
    seed_db()
