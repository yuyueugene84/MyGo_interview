from reverse_dic import *
import unittest

# Input:
input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}
# Output:
output_value = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
}
# input empty dictionary
input_empty = {}
# output empty dictionary
output_empty = {}
# input with wrong data type
input_wrong_type = []

class TestReverseDic(unittest.TestCase):
    def test_value(self):
        self.assertEqual(reverse_dic(input_value),output_value)
    def test_input_empty_dic(self):
        self.assertEqual(reverse_dic(input_empty),output_empty)
    def test_input_is_dic(self):
        with self.assertRaises(AttributeError): reverse_dic(input_wrong_type)