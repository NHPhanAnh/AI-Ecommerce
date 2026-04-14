import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_service.settings')
django.setup()

from app.models import Product
import random

def seed_db():
    print("Clearing old data...")
    Product.objects.all().delete()
    
    categories = [
        "Laptop", "Điện thoại", "Máy tính bảng", "Đồng hồ thông minh",
        "Tai nghe", "Loa Bluetooth", "Màn hình", "Bàn phím",
        "Chuột", "Cáp sạc"
    ]
    
    print("Seeding new categories...")
    
    products = []
    for cat_idx, cat in enumerate(categories):
        for i in range(1, 11):
            discount = random.choice([0, 5, 10, 15, 20])
            if cat == "Laptop":
                name = f"Laptop Pro {i}"
                img = "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500"
                price = random.choice([15990000, 18500000, 22000000, 25990000, 32000000, 45000000])
            elif cat == "Điện thoại":
                name = f"Smartphone X{i}"
                img = "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500"
                price = random.choice([5990000, 8500000, 12990000, 21000000, 28990000])
            elif cat == "Máy tính bảng":
                name = f"Tablet Ultra {i}"
                img = "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=500"
                price = random.choice([7500000, 10990000, 16990000, 23000000])
            elif cat == "Đồng hồ thông minh":
                name = f"Smartwatch Series {i}"
                img = "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500"
                price = random.choice([1500000, 2990000, 5500000, 9990000])
            elif cat == "Tai nghe":
                name = f"Earbuds Pro {i}"
                img = "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"
                price = random.choice([450000, 890000, 1500000, 4500000])
            elif cat == "Loa Bluetooth":
                name = f"Speaker Max {i}"
                img = "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500"
                price = random.choice([690000, 1290000, 2500000, 5990000])
            elif cat == "Màn hình":
                name = f"Monitor 27-inch V{i}"
                img = "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500"
                price = random.choice([2500000, 3990000, 5500000, 12000000])
            elif cat == "Bàn phím":
                name = f"Mechanical Keyboard K{i}"
                img = "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500"
                price = random.choice([550000, 990000, 1800000, 3500000])
            elif cat == "Chuột":
                name = f"Wireless Mouse M{i}"
                img = "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500"
                price = random.choice([150000, 350000, 890000, 1500000])
            else:
                name = f"Fast Charger {i}W"
                img = "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500"
                price = random.choice([150000, 250000, 450000, 890000])
                
            price += random.randint(0, 9) * 10000
                
            products.append(Product(
                category=cat,
                name=name,
                price=price,
                stock=random.randint(10, 100),
                discount_percent=discount,
                description=f"Chiếc {name} thuộc dòng {cat} cực xịn xò với thiết kế ấn tượng.",
                image_url=img
            ))
            
    Product.objects.bulk_create(products)
    print(f"Successfully created {len(products)} products across {len(categories)} categories!")

if __name__ == '__main__':
    seed_db()
