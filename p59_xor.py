import itertools

file_url = open(r'G:\\test_c\\projectEuler\\p059_cipher.txt')
cipher_text = map(int,file_url.read().split(','))

def decode(cipher_text, key_length, key_set, morsel):
    for key in itertools.product(key_set, repeat=key_length):
        msg =  [x^y for x, y in zip(cipher_text, itertools.cycle(key))]
        if morsel in ''.join(map(chr, msg)):
            return sum(msg)
    return "No solution"

print "Project Euler 59 Solution =", decode(cipher_text, 3, range(97, 123),' the ')