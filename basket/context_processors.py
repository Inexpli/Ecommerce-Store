from .basket import Basket
from .models import Basket as BasketModel


def basket(request):
    return {'basket': Basket(request)}


def basketModel(request):
    return {'basketModel': BasketModel}
