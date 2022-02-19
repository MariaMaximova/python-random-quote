import random

last = 16
rnd = random.randint(0, last)
rnd_two = random.randint(0, last)

def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(f"{quotes[rnd]}{quotes[rnd_two]}".strip())

if __name__== "__main__":
  primary()
