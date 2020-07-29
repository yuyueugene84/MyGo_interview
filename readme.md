# MyGo Interview Answer

### Purpose:
This project is my answer to the following question:
[Link](https://pastebin.com/p63ha0CE). Which asked the interviewer to create a function that can reverse a nested dictionary, for example, given follow nested dictionary:

```python
{
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}
```

the function should return:

```python
{
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
}
```

### Run the function

To see how it works, please open your terminal app and enter the following command under this project's root directory: 

`python main.py`

### Test Case

To check out the test case for the function I built, please refer to `reverse_dic_test.py`. To run it, please open your terminal app and enter the following command under this project's root directory:

`python -m unittest reverse_dic_test.py`