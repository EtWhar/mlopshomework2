import unittest
from src.app import hash_feature

class TestFeatureEngineering(unittest.TestCase):
    def test_hash_feature_consistency(self):
        # Ensure same input gives same output
        self.assertEqual(hash_feature("test_user"), hash_feature("test_user"))
    
    def test_hash_feature_range(self):
        # Ensure output is within bucket range
        num_buckets = 50
        result = hash_feature("another_user", num_buckets=num_buckets)
        self.assertTrue(0 <= result < num_buckets)
    
    def test_hash_feature_invalid_input(self):
        # Ensure it raises error for non-string input
        with self.assertRaises(ValueError):
            hash_feature(123)

if __name__ == '__main__':
    unittest.main()
