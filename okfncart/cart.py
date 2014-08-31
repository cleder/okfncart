# -*- coding: utf-8 -*-
# Copyright (C) 2014  Christian Ledermann
#
from . import getproducts

class Cart(object):

    def __init__(self, products, offers=None):
        self._contents = {}
        self._products = products
        self._discounts = {}
        if not offers:
            self._offers=[]
        else:
            self._offers= offers

    def load_products(self, filename):
        self._products = getproducts.loadproducts(filename)

    @property
    def contents(self):
        return self._contents

    def add(self, product, quantity):
        # initialize the product in the basket, this could also be done
        # with a collection.defaultdict
        if product not in self._contents:
            self._contents[product] = 0
        self._contents[product] += quantity

    def _add_discount(self, name, price):
        self._discounts[name] = price

    def get_price(self):
        price = 0.0
        for content in self.contents.items():
            price += self._products[content[0]] * content[1]
        self._discounts = {}
        for offer in self._offers:
            offer.add_discount(self)
        for discount in self._discounts.items():
            price += discount[1]
        return price
