def position(matrix, x):
    for i in range(0, 6):
        for j in range(0, 6):
            if matrix[i][j] == x:
                return [i, j]


def encrypt(matrix, plain_text):
    trend = 'rlud'
    k = 1
    ans = ""
    for i in range(0, len(plain_text)):
        if k == 5:
            k = 1
        if k == 1:
            pos = position(matrix, plain_text[i])
            ans = ans + matrix[pos[0]][(pos[1] + int(new_key[i])) % 6]
        elif k == 2:
            pos = position(matrix, plain_text[i])
            ans = ans + matrix[pos[0]][(pos[1] - int(new_key[i]) + 6) % 6]
        elif k == 3:
            pos = position(matrix, plain_text[i])
            ans = ans + matrix[(pos[0] - int(new_key[i]) + 6) % 6][pos[1]]
        elif k == 4:
            pos = position(matrix, plain_text[i])
            ans = ans + matrix[(pos[0] + int(new_key[i])) % 6][pos[1]]
        k = k + 1
    return ans


def decrypt(matrix, cipher_text):
    trend = 'lrdu'
    k = 1
    ans = ""
    for i in range(0, len(cipher_text)):
        if k == 5:
            k = 1
        if k == 2:
            pos = position(matrix, cipher_text[i])
            ans = ans + matrix[pos[0]][(pos[1] + int(new_key[i])) % 6]
        elif k == 1:
            pos = position(matrix, cipher_text[i])
            ans = ans + matrix[pos[0]][(pos[1] - int(new_key[i]) + 6) % 6]
        elif k == 4:
            pos = position(matrix, cipher_text[i])
            ans = ans + matrix[(pos[0] - int(new_key[i]) + 6) % 6][pos[1]]
        elif k == 3:
            pos = position(matrix, cipher_text[i])
            ans = ans + matrix[(pos[0] + int(new_key[i])) % 6][pos[1]]
        k = k + 1
    return ans


matrix = [['a', 'b', 'c', 'd', 'e', 'f'],
          ['g', 'h', 'i', 'j', 'j', 'l'],
          ['m', 'n', 'o', 'p', 'q', 'r'],
          ['s', 't', 'u', 'v', 'w', 'x'],
          ['y', 'z', '!', '@', '#', '$'],
          ['%', '^', '&', '*', '(', ')']]

plain_text = input("Enter the Plain Text : ")

Key = input("Enter the Key (Key should be numeric) (The Length of the key should be <= Length of plain Text) : ")

key_arr = [char for char in Key]

for i in range(len(key_arr)):
    if key_arr[i] == '6':
        key_arr[i] = '7'

Key = ''.join(key_arr)

new_key = ''.join(key_arr)
ctr = 0

while len(plain_text) != len(new_key):
    new_key += Key[ctr]
    ctr += 1
    if ctr == len(Key):
        ctr = 0

print("New Key : ", new_key)
Cipher_Text = encrypt(matrix, plain_text)
print("Cipher Text : ", Cipher_Text)
print("Cipher_Text : ", decrypt(matrix, Cipher_Text))