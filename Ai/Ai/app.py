
"""
import requests as rq

a = rq.get("https://www.google.com/")

print(a.json())

h = a.json()
print(h[''][''])
"""






import requests as rq
import sys


while True:

  que = input("question = ")

  if que != "end chat":
    GPT =  "https://one-api.ir/chatgpt/?token=843530:657815b9d8c49&action=gpt3.5-turbo&q=" + que
    a = rq.get(GPT)
    j = a.json()
    j = j['result'][0]

    print('robot : ' + j)
  else :
    sys.exit()