""" test """
import unittest

class TestMysite(unittest.TestCase):
    """Test for my sitetest method"""
    def test_upper(self):
        """ Test for my site. This will be error. """
        self.assertEqual('foo'.upper(), 'foo')

if __name__ == '__main__':
    unittest.main()
