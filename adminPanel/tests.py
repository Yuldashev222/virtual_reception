from django.test import TestCase


import time
date = input('Date (dd/mm/yyyy): ')
try:
  valid_date = time.strptime(date, '%d/%m/%Y')
  print(valid_date)
except ValueError:
  print('Invalid date!')