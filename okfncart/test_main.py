# -*- coding: utf-8 -*-
# Copyright (C) 2014  Christian Ledermann
#
import os
import unittest
from . import getproducts
from . import cart
from . import offers

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
        my_cart.add('strawberries', 3)
        self.assertEqual(my_cart.get_price(),6)
        my_cart.add('apple', 2)
        self.assertEqual(my_cart.get_price(),6.3)


class DiscountTestCase(unittest.TestCase):
    """ We'd like to be able to configure certain kinds of "offer"
    which can be applied to the cart, affecting the resulting cost.
    Examples of the kind of offer might be as follows:

    * "buy one get one free" on ice cream
    * buy two punnets of strawberries, and get the third free
    * get 20% off a Snickers bar if you buy a Mars bar at the same time
    """

    def test_2_for_1(self):
        products =  {'snickers bar': 0.7, 'strawberries': 2.0,
                    'apple': 0.15, 'ice cream': 3.49}
        my_cart = cart.Cart(products)
        self.assertEqual(my_cart.get_price(),0)
        offers.product_bogof(my_cart, 'ice cream')
        self.assertEqual(my_cart.get_price(),0)
        my_cart.add('ice cream', 1)
        offers.product_bogof(my_cart, 'ice cream')
        self.assertEqual(my_cart.contents['ice cream'], 1)
        self.assertEqual(my_cart.get_price(),3.49)
        my_cart.add('ice cream', 1)
        self.assertEqual(my_cart.contents['ice cream'], 2)
        offers.product_bogof(my_cart, 'ice cream')
        self.assertEqual(my_cart.get_price(),3.49)
        my_cart.add('ice cream', 1)
        self.assertEqual(my_cart.contents['ice cream'], 3)
        offers.product_bogof(my_cart, 'ice cream')
        self.assertEqual(my_cart.get_price(),3.49*2)
        my_cart.add('ice cream', 1)
        self.assertEqual(my_cart.contents['ice cream'], 4)
        offers.product_bogof(my_cart, 'ice cream')
        self.assertEqual(my_cart.get_price(),3.49*2)
        my_cart.add('ice cream', 1)
        self.assertEqual(my_cart.contents['ice cream'], 5)
        offers.product_bogof(my_cart, 'ice cream')
        self.assertEqual(round(1.2, 2), round(1.200002,2))
        self.assertEqual(round(my_cart.get_price(),2),
            round(3.49*2 + 3.49,2))

    def test_3_for_2(self):
        products =  {'snickers bar': 0.7, 'strawberries': 2.0,
                    'apple': 0.15, 'ice cream': 3.49}
        my_cart = cart.Cart(products)
        self.assertEqual(my_cart.get_price(),0)
        offers.product_b2g3rdf(my_cart, 'strawberries')
        self.assertEqual(my_cart.get_price(),0)
        my_cart.add('strawberries', 1)
        offers.product_b2g3rdf(my_cart, 'strawberries')
        self.assertEqual(my_cart.contents['strawberries'], 1)
        self.assertEqual(my_cart.get_price(),2.0)
        my_cart.add('strawberries', 1)
        offers.product_b2g3rdf(my_cart, 'strawberries')
        self.assertEqual(my_cart.contents['strawberries'], 2)
        self.assertEqual(my_cart.get_price(),4.0)
        my_cart.add('strawberries', 1)
        offers.product_b2g3rdf(my_cart, 'strawberries')
        self.assertEqual(my_cart.contents['strawberries'], 3)
        self.assertEqual(my_cart.get_price(),4.0)
        my_cart.add('strawberries', 1)
        offers.product_b2g3rdf(my_cart, 'strawberries')
        self.assertEqual(my_cart.contents['strawberries'], 4)
        self.assertEqual(my_cart.get_price(),6.0)
        my_cart.add('strawberries', 1)
        offers.product_b2g3rdf(my_cart, 'strawberries')
        self.assertEqual(my_cart.contents['strawberries'], 5)
        self.assertEqual(my_cart.get_price(),8.0)
        my_cart.add('strawberries', 1)
        offers.product_b2g3rdf(my_cart, 'strawberries')
        self.assertEqual(my_cart.contents['strawberries'], 6)
        self.assertEqual(my_cart.get_price(),8.0)
        my_cart.add('strawberries', 1)
        offers.product_b2g3rdf(my_cart, 'strawberries')
        self.assertEqual(my_cart.contents['strawberries'], 7)
        self.assertEqual(my_cart.get_price(),10.0)

    def test_20pc_off_snickers_4_mars(self):
        # changed the price of snickers to 1.0
        products =  {'snickers': 1.0, 'strawberries': 2.0,
                    'apple': 0.15, 'ice cream': 3.49, 'mars': 0.5}
        my_cart = cart.Cart(products)
        self.assertEqual(my_cart.get_price(),0)
        offers.p1_p2_off(my_cart, 'mars', 'snickers', 0.2)
        self.assertEqual(my_cart.get_price(),0)
        my_cart.add('mars', 1)
        offers.p1_p2_off(my_cart, 'mars', 'snickers', 0.2)
        self.assertEqual(my_cart.contents['mars'], 1)
        self.assertEqual(my_cart.get_price(),0.5)
        my_cart.add('snickers', 1)
        offers.p1_p2_off(my_cart, 'mars', 'snickers', 0.2)
        self.assertEqual(my_cart.contents['mars'], 1)
        self.assertEqual(my_cart.contents['snickers'], 1)
        self.assertEqual(my_cart.get_price(),1.8)
        my_cart.add('snickers', 1)
        offers.p1_p2_off(my_cart, 'mars', 'snickers', 0.2)
        self.assertEqual(my_cart.contents['mars'], 1)
        self.assertEqual(my_cart.contents['snickers'], 2)
        self.assertEqual(my_cart.get_price(),1.3)



def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ProductLoadTestCase))
    suite.addTest(unittest.makeSuite(BasicCartTestCase))
    suite.addTest(unittest.makeSuite(DiscountTestCase))
    return suite

if __name__ == '__main__':
    unittest.main()
