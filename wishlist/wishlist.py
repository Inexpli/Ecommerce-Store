from store.models import Product


class WishList():
    def __init__(self, request):
        self.session = request.session
        wishlist = self.session.get('wl')
        if 'wl' not in request.session:
            wishlist = self.session['wl'] = {}
        self.wishlist = wishlist

    def add(self, product):
        product_id = str(product.id)

        if product_id not in self.wishlist:
            self.wishlist[product_id] = {'quantity': 1}

        self.session.modified = True

    def delete(self, product):
        product_id = str(product)

        if product_id in self.wishlist:
            del self.wishlist[product_id]

        self.session.modified = True

    def __iter__(self):
        product_ids = self.wishlist.keys()
        products = Product.objects.filter(id__in=product_ids)
        wishlist = self.wishlist.copy()

        for product in products:
            wishlist[str(product.id)]['product'] = product

        for item in wishlist.values():
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.wishlist.values())
