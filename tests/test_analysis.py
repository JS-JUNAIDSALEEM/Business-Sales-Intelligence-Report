
# Automated Tests

import unittest
import runpy
from pathlib import Path


class TestSalesAnalysis(unittest.TestCase):

    @classmethod

    def setUpClass(cls):
        # Run main.py and get its cleaned dataset
        project_path = Path(__file__).resolve().parent.parent
        main_file = project_path / "main.py"

        cls.results = runpy.run_path(str(main_file))
        cls.df = cls.results["df"]


# Test 1: Duplicate OrderID Removal

    def test_duplicate_order_id_removal(self):
        self.assertFalse(self.df["OrderID"].duplicated().any())


# Test 2: Positive Quantities and Prices

    def test_positive_quantity_and_price(self):
        self.assertTrue((self.df["Quantity"] > 0).all())
        self.assertTrue((self.df["UnitPrice"] > 0).all())


# Test 3: Discount Values Between 0 and 1

    def test_discount_values(self):
        self.assertTrue(self.df["Discount"].between(0, 1).all())


# Test 4: Correct Revenue Calculations

    def test_revenue_calculations(self):
        expected_gross = (self.df["Quantity"] * self.df["UnitPrice"])
        expected_net = (expected_gross * (1 - self.df["Discount"]))

        self.assertTrue((self.df["GrossRevenue"] == expected_gross).all())
        self.assertTrue((self.df["NetRevenue"] == expected_net).all())


# Test 5: Correct Number of Cleaned Records

    def test_cleaned_records_count(self):
        self.assertEqual(len(self.df), 28)

if __name__ == "__main__":
    unittest.main()
