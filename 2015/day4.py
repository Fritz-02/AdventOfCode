from get_input import get_input
import hashlib

puzzle_input = get_input(2015, 4)


n = 1
p1 = None
p2 = None
while True:
    hash_input = f"{puzzle_input}{n}".encode()
    hash_output = hashlib.md5(hash_input).hexdigest()
    if p1 is None and hash_output[:5] == "00000":
        p1 = n
    if p1 and hash_output[:6] == "000000":
        p2 = n
    if p1 and p2:
        break
    n += 1

print(p1)
print(p2)
