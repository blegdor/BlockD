# test_blockd.py
"""
Tests for BlockD module.
"""

import unittest
from blockd import BlockD

class TestBlockD(unittest.TestCase):
    """Test cases for BlockD class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockD()
        self.assertIsInstance(instance, BlockD)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockD()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
