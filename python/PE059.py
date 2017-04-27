encrypted = open("PE059.txt", "r")
encrypted = [int(x) for x in encrypted.read().split(',')]
set_1 = [encrypted[i] for i in range(0, len(encrypted), 3)]
set_2 = [encrypted[i] for i in range(1, len(encrypted), 3)]
set_3 = [encrypted[i] for i in range(2, len(encrypted), 3)]

from collections import Counter

key_1 = Counter(set_1).most_common(1)[0][0]
key_2 = Counter(set_2).most_common(1)[0][0]
key_3 = Counter(set_3).most_common(1)[0][0]
key = (key_1 ^ ord(' '), key_2 ^ ord(' '), key_3 ^ ord(' '))

decrypted = [encrypted[i] ^ key[i%3] for i in range(0, len(encrypted))]
answer = sum(decrypted)
text = ''.join([chr(x) for x in decrypted])
print(text)
print(answer)