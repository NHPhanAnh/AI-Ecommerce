from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import CartItem, Customer
import requests
import os

PRODUCT_SERVICE_URL = os.environ.get('PRODUCT_SERVICE_URL', "http://localhost:8002")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            Customer.objects.get_or_create(user=user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.get_or_create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    query = request.GET.get('q', '')
    products = []
    
    try:
        r = requests.get(f"{PRODUCT_SERVICE_URL}/products/", timeout=3)
        if r.status_code == 200: products = r.json()
    except Exception as e:
        print(f"Error fetching products: {e}")
        
    if query:
        query = query.lower()
        products = [p for p in products if query in str(p.get('name', '')).lower()]
        
    grouped_products = {}
    for item in products:
        cat = item.get('category', 'Khác')
        if cat not in grouped_products:
            grouped_products[cat] = []
            
        dp = float(item.get('discount_percent', 0))
        op = float(item['price'])
        item['original_price'] = op
        item['price'] = op * (100 - dp) / 100
        item['discount_percent'] = dp
        
        grouped_products[cat].append(item)

    return render(request, 'home.html', {'grouped_products': grouped_products, 'query': query})

@login_required
def view_all_products(request, category):
    products = []
    try:
        r = requests.get(f"{PRODUCT_SERVICE_URL}/products/?category={category}", timeout=3)
        if r.status_code == 200: products = r.json()
    except: pass
    
    for item in products:
        dp = float(item.get('discount_percent', 0))
        op = float(item['price'])
        item['original_price'] = op
        item['price'] = op * (100 - dp) / 100
        item['discount_percent'] = dp
        
    return render(request, 'product_list.html', {'items': products, 'category': category})

@login_required
def product_detail(request, product_id):
    item = None
    try:
        r = requests.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}/", timeout=3)
        if r.status_code == 200:
            item = r.json()
            dp = float(item.get('discount_percent', 0))
            op = float(item['price'])
            item['original_price'] = op
            item['price'] = op * (100 - dp) / 100
            item['discount_percent'] = dp
    except: pass
        
    if not item: return redirect('home')
        
    return render(request, 'product_detail.html', {'item': item})

@login_required
def view_cart(request):
    customer = request.user.customer_profile
    cart_items = CartItem.objects.filter(customer=customer)
    
    products_cache = {}
    
    try:
        r = requests.get(f"{PRODUCT_SERVICE_URL}/products/", timeout=3)
        if r.status_code == 200: 
            for p in r.json(): products_cache[p['id']] = p
    except: pass

    enriched_items = []
    grand_total = 0
    for item in cart_items:
        data = products_cache.get(int(item.item_id))
            
        if data:
            price = float(data.get('price', 0))
            subtotal = price * item.quantity
            grand_total += subtotal
            enriched_items.append({
                'cart_item': item,
                'name': data.get('name', 'Unknown'),
                'price': price,
                'subtotal': subtotal
            })
        else:
            enriched_items.append({
                'cart_item': item,
                'name': 'Unknown Product',
                'price': 0,
                'subtotal': 0
            })

    return render(request, 'cart.html', {
        'cart_items': enriched_items,
        'grand_total': grand_total
    })

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item_type = request.POST.get('item_type', 'product') # Legacy fallback
        customer = request.user.customer_profile
        
        cart_item, created = CartItem.objects.get_or_create(
            customer=customer, item_id=item_id, item_type=item_type
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
            
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def update_cart(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        action = request.POST.get('action')
        customer = request.user.customer_profile
        try:
            item = CartItem.objects.get(id=cart_item_id, customer=customer)
            if action == 'increase':
                item.quantity += 1
                item.save()
            elif action == 'decrease':
                item.quantity -= 1
                if item.quantity <= 0:
                    item.delete()
                else:
                    item.save()
            elif action == 'remove':
                item.delete()
        except CartItem.DoesNotExist:
            pass
    return redirect('cart')

@login_required
def checkout(request):
    if request.method == 'POST':
        customer = request.user.customer_profile
        CartItem.objects.filter(customer=customer).delete()
        return redirect('checkout_success')
    return redirect('cart')

@login_required
def checkout_success(request):
    return render(request, 'checkout_success.html')

@login_required
def profile_view(request):
    customer = request.user.customer_profile
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        new_password = request.POST.get('new_password', '')
        
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = email
        if new_password:
            request.user.set_password(new_password)
        request.user.save()
        if new_password:
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, request.user)
        
        customer.phone = phone
        customer.address = address
        customer.save()
        
        return redirect('home')
        
    return render(request, 'profile.html', {'customer': customer})
