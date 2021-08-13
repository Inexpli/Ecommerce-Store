from decimal import Decimal

from store.models import Product


class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, quantity, size):
        product_id = str(product.id)

        if product_id not in self.basket:
            self.basket[product_id] = {'price': int(
                product.price), 'quantity': int(quantity), 'size': int(size)}

        self.session.modified = True

    def delete(self, product):
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]

        self.session.modified = True

    def update(self, product, quantity, size):
        product_id = str(product)
        product_quantity = quantity
        product_size = size

        if product_id in self.basket:
            self.basket[product_id]['quantity'] = int(product_quantity)
            self.basket[product_id]['size'] = int(product_size)

        self.session.modified = True

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.basket.values())
