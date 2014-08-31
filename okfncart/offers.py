# -*- coding: utf-8 -*-
# Copyright (C) 2014  Christian Ledermann
#

def product_bogof(cart, product):
    if product in cart.contents:
        price = cart._products[product]
        num = cart.contents[product]/2
        cart._add_discount('%s bogo' % product, -1 * num * price)


def product_b2g3rdf(cart, product):
    if product in cart.contents:
        price = cart._products[product]
        num = cart.contents[product]/3
        cart._add_discount('%s b2g3rd' % product, -1 * num * price)
