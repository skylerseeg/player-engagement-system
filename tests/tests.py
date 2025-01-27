import unittest
from app.recommender import recommend

class TestRecommender(unittest.TestCase):
    def test_recommend_valid_player(self):
        result = recommend(12345)
        self.assertTrue("recommended_items" in result)

if __name__ == "__main__":
    unittest.main()
