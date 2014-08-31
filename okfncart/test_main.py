# -*- coding: utf-8 -*-
# Copyright (C) 2014  Christian Ledermann
#
import os
import unittest
from . import getproducts
from . import cart

class ProductLoadTestCase(unittest.TestCase):
    """ our products load gives back a dictionary
    {'name':'some product', 'price:': 0.0}

    apple,0.15
    ice cream,3.49
    strawberries,2.00
    snickers bar,0.70

    """

    def test_load_product_names(self):
        here = os.path.abspath(os.path.dirname(__file__))
        file_name = os.path.join(here, 'tests', 'products.csv')
        prods = getproducts.loadproducts(file_name)
        self.assertTrue('apple' in prods.keys())
        self.assertTrue('strawberries' in prods.keys())
        self.assertTrue('ice cream' in prods.keys())
        self.assertTrue('snickers bar' in prods.keys())
        self.assertFalse(None in prods.keys())
        self.assertFalse('' in prods.keys())

    def test_product_prices(self):
        here = os.path.abspath(os.path.dirname(__file__))
        file_name = os.path.join(here, 'tests', 'products.csv')
        prods = getproducts.loadproducts(file_name)
        self.assertEqual(prods['apple'],0.15)
        self.assertEqual(prods['strawberries'],2.0)
        self.assertEqual(prods['ice cream'],3.49)
        self.assertEqual(prods['snickers bar'],0.7)
        self.assertEqual(prods, {'snickers bar': 0.7, 'strawberries': 2.0,
                    'apple': 0.15, 'ice cream': 3.49})

class BasicCartTestCase(unittest.TestCase):

    def test_add_to_cart(self):
        """
        add some quantity of a product to the cart
        """
        products =  {'snickers bar': 0.7, 'strawberries': 2.0,
                    'apple': 0.15, 'ice cream': 3.49}
        my_cart = {}
        for p in products:
            my_cart = cart.add_to_cart(product=p, quantity=1)
        self.assertEqual(my_cart.keys(), products.keys())

    def test_compute_cart_value(self):
        """
        calculate the total cost of the cart
        """
        products =  {'snickers bar': 0.7, 'strawberries': 2.0,
                    'apple': 0.15, 'ice cream': 3.49}
        my_cart = {}
        self.assertEqual(cart.compute_cart_price(my_cart, products), 0)
        pass


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ProductLoadTestCase))
    return suite

if __name__ == '__main__':
    unittest.main()
