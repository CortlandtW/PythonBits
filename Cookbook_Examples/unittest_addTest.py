import unittest
import helpspot

class TestHelpSpot(unittest.TestCase):
    "A few simple tests for HelpSpot"

    def __init__(self, testname, path, user, pword):
        super(TestHelpSpot, self).__init__(testname)
        self.hs = helpspot.HelpSpot(path, user, pword)

    def test_version(self):
        a = self.hs.version()
        b = self.hs.private_version()
        self.assertEqual(a, b)

    def test_get_with_param(self):
        a = self.hs.filter_get(xFilter=1)

    def test_unknown_method(self):
        self.assertRaises(helpspot.HelpSpotError, self.hs.private_wuggienorple)

if __name__ == '__main__':
    import sys
    user = sys.argv[1]
    pword = sys.argv[2]
    path = sys.argv[3]

    suite = unittest.TestSuite()
    suite.addTest(TestHelpSpot("test_version", path, user, pword))
    suite.addTest(TestHelpSpot("test_get_with_param", path, user, pword))
    suite.addTest(TestHelpSpot("test_unknown_method", path, user, pword))

    unittest.TextTestRunner().run(suite)


