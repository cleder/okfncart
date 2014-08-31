# -*- coding: utf-8 -*-
# Copyright (C) 2014  Christian Ledermann
#
import os
import unittest
from . import getproducts

class ProductLoadTestCase(unittest.TestCase):
    """ our products load gives back a dictionary
    {'name':'some product', 'price:': 0.0}
    """

    def test_load_product_names(self):
        here = os.path.abspath(os.path.dirname(__file__))
        file_name = os.path.join(here, 'tests', 'products.csv')
        prods = getproducts.loadproducts(file_name)
        self.assertTrue('apple' in prods.keys())
        self.assertTrue('strawberries' in prods.keys())
        self.assertTrue('ice cream' in prods.keys())
        self.assertTrue('snickers bar' in prods.keys())




def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ProductLoadTestCase))
    return suite

if __name__ == '__main__':
    unittest.main()
