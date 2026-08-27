# test_fusevault.py
"""
Tests for FuseVault module.
"""

import unittest
from fusevault import FuseVault

class TestFuseVault(unittest.TestCase):
    """Test cases for FuseVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FuseVault()
        self.assertIsInstance(instance, FuseVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FuseVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
