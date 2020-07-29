from reverse_dic import *

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

print(reverse_dic(input_value))