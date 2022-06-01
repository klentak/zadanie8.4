import random

def miller_rabin(n):
  if n == 2:
    return True

  if n % 2 == 0:
    return False

  r, s = 0, n - 1
  while s % 2 == 0:
    r += 1
    s //= 2
  for _ in range(5):
    a = random.randrange(2, n - 1)
    x = pow(a, s, n)
    if x == 1 or x == n - 1:
      continue
    for _ in range(r - 1):
      x = pow(x, 2, n)
      if x == n - 1:
        break
    else:
      return False
  return True


def random_prime_number(x, y):
  while True:
    random_number = random.randint(x, y)
    if miller_rabin(random_number):
      return random_number
