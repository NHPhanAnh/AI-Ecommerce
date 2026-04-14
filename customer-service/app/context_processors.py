def cart_count(request):
    if request.user.is_authenticated and hasattr(request.user, 'customer_profile'):
        from .models import CartItem
        # count the total sum of quantities in cart
        count = sum(item.quantity for item in CartItem.objects.filter(customer=request.user.customer_profile))
        return {'cart_item_count': count}
    return {'cart_item_count': 0}
