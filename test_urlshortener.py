# test_urlshortener.py
"""
Tests for UrlShortener module.
"""

import unittest
from urlshortener import UrlShortener

class TestUrlShortener(unittest.TestCase):
    """Test cases for UrlShortener class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = UrlShortener()
        self.assertIsInstance(instance, UrlShortener)
        
    def test_run_method(self):
        """Test the run method."""
        instance = UrlShortener()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
