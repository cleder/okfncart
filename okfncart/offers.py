# -*- coding: utf-8 -*-
# Copyright (C) 2014  Christian Ledermann
#


class Offer(object):

    def __init__(self):
        raise NotImplementedError

    def add_discount(self, cart):
        raise NotImplementedError

class OfferBogof(Offer):
    '''
    "buy one get one free" on product
    '''
    def __init__(self, product):
        self._product = product

    def add_discount(self, cart):
        product = self._product
        if product in cart.contents:
            price = cart._products[product]
            num = cart.contents[product]/2
            cart._add_discount('%s bogo' % product, -1 * num * price)


class OfferB2g3rdf(Offer):
    '''
    buy two of product and get the third free
    '''
    def __init__(self, product):
        self._product = product

    def add_discount(self, cart):
        product = self._product
        if product in cart.contents:
            price = cart._products[product]
            num = cart.contents[product]/3
            cart._add_discount('%s b2g3rd' % product, -1 * num * price)


class OfferP1p2XpcOff(Offer):
    '''
    get p2_discount (*100%) off product2 if you buy a product1 at the same time
    '''
    def __init__(self, product1, product2, p2_discount):
        self._product1 = product1
        self._product2 = product2
        self._p2_discount = p2_discount

    def add_discount(self, cart):
        if self._product1 in cart.contents and self._product2 in cart.contents:
            price = cart._products[self._product2] * self._p2_discount
            num = min(cart.contents[self._product1], cart.contents[self._product2])
            discount = int(self._p2_discount * 100)
            cart._add_discount('%i pc discount for  %s if you buy %s ' %
                                (discount, self._product2, self._product1),
                                -1 * num * price)
