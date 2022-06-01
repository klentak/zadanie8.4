import random
import rsa

number = int(input("Podaj długość bitów: "))

random.seed(1)

public_key, private_key = rsa.generate_keys(number).values()

print("Wygenerowane klucze publiczne", public_key)
print("Wygenerowane klucze prywatne", private_key)

message = input("Podaj wiadomość do zaszyfrowania: ")
blockSize = int(input("Podaj wielkość bloku: "))

f = open("encrypted.txt", "w")
f.write('%s; %s\n' % (public_key[0], public_key[1]))
encryptedMessageInBlocks = rsa.encryption(message, blockSize, public_key)
f.write(';'.join(map(str, encryptedMessageInBlocks)))

print('zaszyfrowana wiadomość', encryptedMessageInBlocks)
decrypted = rsa.decryption(encryptedMessageInBlocks, private_key)


print('odszyfrowoana wiadomość', decrypted)
print('odszyfrowoana wiadomość w ascii: "%s"' % rsa.block_to_text(decrypted))