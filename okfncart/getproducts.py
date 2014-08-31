# -*- coding: utf-8 -*-
# Copyright (C) 2014  Christian Ledermann
#

import csv
import os

def loadproducts(file_name):
    """ In our system, we'll represent products as simple strings
    like "apple" or "donut". Assume that the prices of the different
    products are provided in a simple CSV file mapping a product to a price
    (in some unspecified currency)
    """
    products = {}
    with open(file_name, 'rb') as csvfile:
        prodreader = csv.reader(csvfile)
        for row in prodreader:
            products[row[0]] = float(row[1])
    return products
