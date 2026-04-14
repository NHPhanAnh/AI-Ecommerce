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
            price = round(random.uniform(50, 2000), 2)
            if cat == "Laptop":
                name = f"Laptop Pro {i}"
                img = "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500"
            elif cat == "Điện thoại":
                name = f"Smartphone X{i}"
                img = "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500"
            elif cat == "Máy tính bảng":
                name = f"Tablet Ultra {i}"
                img = "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=500"
            elif cat == "Đồng hồ thông minh":
                name = f"Smartwatch Series {i}"
                img = "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500"
            elif cat == "Tai nghe":
                name = f"Earbuds Pro {i}"
                img = "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"
            elif cat == "Loa Bluetooth":
                name = f"Speaker Max {i}"
                img = "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500"
            elif cat == "Màn hình":
                name = f"Monitor 27-inch V{i}"
                img = "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500"
            elif cat == "Bàn phím":
                name = f"Mechanical Keyboard K{i}"
                img = "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500"
            elif cat == "Chuột":
                name = f"Wireless Mouse M{i}"
                img = "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500"
            else:
                name = f"Fast Charger {i}W"
                img = "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500"
                
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
