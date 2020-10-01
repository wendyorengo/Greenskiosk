from django.db import models
from catalogue.models import Product
from customers.models import Customer



# Create your models here.

class Cart(models.Model):
    products = models.ManyToManyField(Product)
    date_created = models.DateTimeField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=100)


    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                      'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())



    def __str__(self):
        return self.status

class Order(models.Model):
    order_number = models.IntegerField()
    date_placed = models.DateTimeField()
    status = models.CharField(max_length=60)
    basket = models.ForeignKey(Cart, on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment= models.ForeignKey('Payment', on_delete=models.CASCADE, related_name='+') 
    delivery_time = models.DateTimeField()
    shipping_provider = models.ForeignKey('shipping.ShippingProvider', on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=6, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.order_number

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='+')
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date_of_payment = models.DateTimeField()

    def __str__(self):
        return self.customer.get_full_name()



