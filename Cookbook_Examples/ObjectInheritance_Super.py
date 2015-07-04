import unittest
""" Add functions to the existing unittest.TestCase object
"""
class TestCase(unittest.TestCase):
56
57	def assertEqual(self, obj1, obj2):
58	    if obj1 != obj2:
        59	print('')
        60	print(repr(obj1))
        61	print(repr(obj2))
        62	print(obj1)
        63	print(obj2)
64	super(TestCase, self).assertEqual(obj1, obj2)
65
66	# Python 2.3 does not have unittest.TestCase.assertTrue:
67	def assertTrue(self, expr, msg=None):
68	if not expr:
69	msg = self._formatMessage(msg, "%s is not True" % safe_repr(expr))
70	raise self.failureException(msg)

class TestFileTypeRepr(TestCase):
1449
1450	def test_r(self):
1451	type = argparse.FileType('r')
1452	self.assertEqual("FileType('r')", repr(type))