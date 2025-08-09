from urllib import request
from time import sleep

while True:
   sleep(2)
   x = 1
   form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdesE9dt_Cqx27z3GGWikpXdOPIridqwQVlFsqmV7G5NH-nyg/formResponse?usp=pp_url&entry.185091517={}".format(x)
   request.urlopen(form_url)
   print("check your google form")
