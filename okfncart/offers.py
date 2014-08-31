# -*- coding: utf-8 -*-
# Copyright (C) 2014  Christian Ledermann
#

def product_bogof(cart, product):
    '''
    "buy one get one free" on product
    '''
    if product in cart.contents:
        price = cart._products[product]
        num = cart.contents[product]/2
        cart._add_discount('%s bogo' % product, -1 * num * price)


def product_b2g3rdf(cart, product):
    '''
    buy of product of strawberries, and get the third free
    '''
    if product in cart.contents:
        price = cart._products[product]
        num = cart.contents[product]/3
        cart._add_discount('%s b2g3rd' % product, -1 * num * price)

def p1_p2_off(cart, product1, product2, p2_discount):
    '''
    get 20% off a Snickers bar if you buy a Mars bar at the same time
    '''
    pass
