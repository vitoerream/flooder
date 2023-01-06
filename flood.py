import requests
import random 
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Testo a cazzo: ", length, "is:", result_str)
    
def peppe(num):
    numero = num
    print(numero)
    
link = 'https://shraidar.org/new_login.php'
for x in range(1000):
  peppe(x)
  payload = {'email': get_random_string(10), 
        'pass': get_random_string(8),
        'submit': ''
          }
  run = requests.post(url=link, data=payload)
  
  print(run.status_code)
  print(run.text)
