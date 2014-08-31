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
    get p2_discount (*100%) off product2 if you buy a product1 at the same time
    '''
    if product1 in cart.contents and product2 in cart.contents:
        price = cart._products[product2] * p2_discount
        num = min(cart.contents[product1], cart.contents[product2])
        discount = int(p2_discount * 100)
        cart._add_discount('%i pc discount for  %s if you buy %s ' %
                            (discount, product2, product1),
                            -1 * num * price)
