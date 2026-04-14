from django.shortcuts import render, redirect
import requests
import os
from django.contrib import messages

PRODUCT_SERVICE_URL = os.environ.get('PRODUCT_SERVICE_URL', "http://localhost:8002")

def manager_home(request):
    products = []
    
    try:
        r = requests.get(f"{PRODUCT_SERVICE_URL}/products/", timeout=3)
        if r.status_code == 200: products = r.json()
    except Exception as e:
        print(f"Error fetching from {PRODUCT_SERVICE_URL}: {e}")

    return render(request, 'manager_home.html', {'products': products})

def add_item(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        name = request.POST.get('name')
        price = request.POST.get('price')
        stock = request.POST.get('stock', 10)
        discount_percent = request.POST.get('discount_percent', 0)
        description = request.POST.get('description', '')
        image_url = request.POST.get('image_url', '')
        
        data = {
            'category': category,
            'name': name,
            'price': float(price),
            'stock': int(stock),
            'discount_percent': int(discount_percent),
            'description': description,
            'image_url': image_url
        }
        try:
            requests.post(f"{PRODUCT_SERVICE_URL}/products/", json=data, timeout=3)
            messages.success(request, 'Thêm sản phẩm thành công!')
        except Exception as e:
            messages.error(request, 'Lỗi khi thêm sản phẩm.')
        return redirect('manager_home')
        
    return render(request, 'add_item.html')

def product_detail_edit(request, item_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete':
            try:
                requests.delete(f"{PRODUCT_SERVICE_URL}/products/{item_id}/", timeout=3)
                messages.success(request, 'Đã xóa sản phẩm.')
            except:
                messages.error(request, 'Không thể xóa.')
            return redirect('manager_home')
            
        elif action == 'update':
            data = {
                'category': request.POST.get('category'),
                'name': request.POST.get('name'),
                'price': float(request.POST.get('price', 0)),
                'stock': int(request.POST.get('stock', 0)),
                'discount_percent': int(request.POST.get('discount_percent', 0)),
                'description': request.POST.get('description', ''),
                'image_url': request.POST.get('image_url', '')
            }
            try:
                requests.patch(f"{PRODUCT_SERVICE_URL}/products/{item_id}/", json=data, timeout=3)
                messages.success(request, 'Đã cập nhật sản phẩm.')
            except Exception as e:
                messages.error(request, f'Lỗi khi cập nhật.')
            return redirect('manager_home')

    item = None
    try:
        r = requests.get(f"{PRODUCT_SERVICE_URL}/products/{item_id}/", timeout=3)
        if r.status_code == 200:
            item = r.json()
    except Exception as e:
        print(e)
        pass

    if not item:
        messages.error(request, 'Sản phẩm không còn tồn tại.')
        return redirect('manager_home')
        
    return render(request, 'product_detail_edit.html', {'item': item})
