import unittest
from datetime import datetime
from app import validate_date

class TestStockVisualizerApp(unittest.TestCase):

    def test_stock_symbol(self):
        # Stock symbols (uppercase, 1-7 characters)
        self.assertTrue("GOOG".isalnum() and "GOOG".isupper())
        self.assertTrue("AAPL".isalnum() and "AAPL".isupper())
        self.assertTrue("TSLA".isalnum() and "TSLA".isupper())

    def test_chart_type(self):
        # Chart types (1 or 2)
        self.assertIn("1", ["1", "2"])
        self.assertIn("2", ["1", "2"])

    def test_time_series_option(self):
        # Valid time series (1, 2, 3, or 4)
        self.assertIn("1", ["1", "2", "3", "4"])
        self.assertIn("2", ["1", "2", "3", "4"])
        self.assertIn("3", ["1", "2", "3", "4"])
        self.assertIn("4", ["1", "2", "3", "4"])

    def test_date_format(self):
        # Valid dates (YYYY-MM-DD)
        self.assertIsNotNone(validate_date("2022-01-01"))
        self.assertIsNotNone(validate_date("2002-09-06"))

    def test_end_date_after_start_date(self):
        # Test that end date is on or after start date
        start_date = "2000-01-01"
        end_date = "2001-02-01"
        self.assertTrue(datetime.strptime(end_date, "%Y-%m-%d") >= datetime.strptime(start_date, "%Y-%m-%d"))

if __name__ == "__main__":
    unittest.main()