import unittest 
from main import bmi, label

class valid(unittest.TestCase):
    def test_item(self):
        self.assertEqual(bmi(160,100), 39.0624999999999, "Hasilnya 39.0624999999999")
        self.assertEqual(bmi(160,60), 23.437499999999996, "Hasilnya 3.906249999999999")
        self.assertEqual(bmi(160,10), 39.0624999999999, "Hasilnya 3.906249999999999")

    def label(self):
        self.assertEqual(label,(bmi(160, 100)), "Overweight","Hasilnya Overweight")
        self.assertEqual(label,(bmi(160, 60)), "Normal" ,"Hasilnya Normal")
        self.assertEqual(label,(bmi(160, 10)), "Underweight","Hasilnya Underweight")
        
