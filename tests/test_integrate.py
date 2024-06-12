import unittest
from integrate import integrand
from math import pi


class Test_integrate(unittest.TestCase):

    def test_integrate(x,self):
        self.assertEqual(integrand(x),0.3465735902799727)
        self.assertEqual(integrand(x),3.847739796558311e-15)