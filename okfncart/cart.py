# -*- coding: utf-8 -*-
# Copyright (C) 2014  Christian Ledermann
#

class Cart(object):

    def __init__(self, products):
        self._contents = {}
        self._products = products

    def add(self, product, quantity):
        # initialize the product in the basket, this could also be done
        # with a collection.defaultdict
        if product not in self._contents:
            self._contents[product] = 0
        self._contents[product] += quantity

    @property
    def contents(self):
        return self._contents

    def get_price(self):
        price = 0.0
        for content in self.contents.items():
            price += self._products[content[0]] * content[1]
        return price
