# -*- coding: utf-8 -*-
# Copyright (C) 2014  Christian Ledermann
#
from . import getproducts


class Cart(object):

    def __init__(self, products=None, offers=None):
        # products can be added after instance init
        # products must be available in _products before they can be
        # added to the cart!
        self.contents = {}  # holds cart content quantities
        self._products = products or {}  # 'universe' of available products
        self._discounts = {}  # discounts that have been applied to the cart
        self._offers = offers or []  # 'universe' offers that can be applied

    def load_products(self, filename):
        self._products = getproducts.loadproducts(filename)

    def add(self, product, quantity):
        # product being added must be available in the available
        # _products 'universe'
        assert product in self._products
        # initialize the product in the basket
        self.contents.setdefault(product, 0)
        self.contents[product] += quantity

    def _add_discount(self, name, price):
        self._discounts[name] = price

    def get_price(self):
        price = 0.0
        for product, qty in self.contents.items():
            price += self._products[product] * qty
        for offer in self._offers:
            # pass in the this cart to the discount class
            offer.add_discount(self)
        for discount in self._discounts.values():
            price += discount
        return price
