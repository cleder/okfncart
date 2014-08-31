Specification
===============

We're going to be selling food products through an online store,
and we'd like you to write the code that's going to power the user's
shopping cart. In our system, we'll represent products as simple strings
like "apple" or "donut". Assume that the prices of the different
products are provided in a simple CSV file mapping a product to a price
(in some unspecified currency):

::

    apple,0.15
    ice cream,3.49
    strawberries,2.00
    snickers bar,0.70
    ...

Our shopping cart should support the following operations:

* add some quantity of a product to the cart
* calculate the total cost of the cart
* NB: don't worry about handling the situation in which someone tries
to add a product to the cart for which the price hasn't been provided.
Assume that's been validated elsewhere.

Of course, there's a twist, which is as follows. We'd like to be able
to configure certain kinds of "offer" which can be applied to the cart,
affecting the resulting cost. Examples of the kind of offer might be as follows:

* "buy one get one free" on ice cream
* buy two punnets of strawberries, and get the third free
* get 20% off a Snickers bar if you buy a Mars bar at the same time

We'd like you to implement each of these example offers, but structure
your program in such a way that adding other common retail offer types is easy.

