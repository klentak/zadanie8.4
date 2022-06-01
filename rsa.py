from randomPrimeNumber import random_prime_number


def mod_inverse(a: int, m: int):
  for x in range(1, m):
    if (((a % m) * (x % m)) % m == 1):
      return x
  return -1


def generate_keys(s: int):
  # Wybieramy losowo dwie duże liczby pierwsze
  p = random_prime_number(2 ** (s - 1), 2 ** (s))
  q = random_prime_number(2 ** (s - 1), 2 ** (s))

  # Obliczamy wartość n = p * q
  n = p * q

  # Obliczamy wartość funkcji Eulera dla n: (n)=(p-1)(q-1)
  eulerFunctionResultFromN = (p - 1) * (q - 1)

  # Wybieramy liczbę e, (1 < e < φ(n)) względnie pierwszą z φ(n).
  e = random_prime_number(2, eulerFunctionResultFromN)

  d = mod_inverse(e, eulerFunctionResultFromN)

  return {
    'public': (e, n),
    'private': (d, n),
  }


def divide_into_blocks(message: str, blockSize: int):
  i = 0
  result = []
  while i < len(message):
    tempResult = 0
    for j in range(blockSize):
      if i >= len(message):
        break
      tempResult += ord(message[i]) * (8 ** j)
      i += 1
    result.append(tempResult)

  return result


def encryption(message: str, blockSize: int, key):
  blocks = divide_into_blocks(message, blockSize)
  result = []
  for block in blocks:
    result.append(
      block_cryption(block, key)
    )

  return result


def decryption(message, key):
  result = []
  for block in message:
    result.append(
      block_cryption(block, key)
    )

  return result


def block_cryption(m, key):
  return (m ** key[0]) % key[1]


def block_to_text(block):
  result = ''
  for element in block:
    result += chr(element)

  return result
