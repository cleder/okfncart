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

    def test_cartobjject_loadproducts(self):
        here = os.path.abspath(os.path.dirname(__file__))
        file_name = os.path.join(here, 'tests', 'products.csv')
        prods = getproducts.loadproducts(file_name)
        my_cart = cart.Cart(None)
        self.assertEqual(my_cart._products, None)
        my_cart.load_products(file_name)
        self.assertEqual(my_cart._products,prods)



class BasicCartTestCase(unittest.TestCase):

    def test_add_to_cart(self):
        """
        add some quantity of a product to the cart
        """
        products =  {'snickers bar': 0.7, 'strawberries': 2.0,
                    'apple': 0.15, 'ice cream': 3.49}
        my_cart = cart.Cart(products)
        for p in products:
            my_cart.add(product=p, quantity=1)
        self.assertEqual(my_cart.contents.keys(), products.keys())
        for item in my_cart.contents.items():
            self.assertEqual(item[1],1)
        #ok add some more
        for p in products:
            my_cart.add(product=p, quantity=2)
        for item in my_cart.contents.items():
            self.assertEqual(item[1],3)
        my_cart.add('apple', 5)
        self.assertEqual(my_cart.contents['apple'], 8)

    def test_compute_cart_value(self):
        """
        calculate the total cost of the cart
        """
        products =  {'snickers bar': 0.7, 'strawberries': 2.0,
                    'apple': 0.15, 'ice cream': 3.49}
        my_cart = cart.Cart(products)
        self.assertEqual(my_cart.get_price(),0)
        pass


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ProductLoadTestCase))
    suite.addTest(unittest.makeSuite(BasicCartTestCase))
    return suite

if __name__ == '__main__':
    unittest.main()
