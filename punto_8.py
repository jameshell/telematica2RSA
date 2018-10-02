
def decrypt(key, n, ciphertext):
    print("Clave publica -> ")
    print(key)
    print("Valor de N ->")
    print(n)
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)

llave = int(input("Inserte la llave: "))
n = int(input("Inserte N: "))
# Put the cipher text here...
texto = [11501, 13347, 1706, 10418, 8943, 2041, 10418, 38, 7031, 10418, 2823, 2433, 5402, 7104, 2011, 11708, 9065, 15862, 7104, 10418, 6397, 8943, 10418, 15389, 11708, 9591, 2011, 2823, 6397, 7104, 10418, 3447, 10418, 6397, 8943, 2041, 15389, 11708, 9591, 2011, 2823, 6397, 7104, 10418, 15389, 2011, 8943, 2823, 6397, 7104, 10418, 2471, 7104, 2011, 10418, 11501,   7104,   7031,   2823,   2433,   6397,   10418,   11501,   11708,   7975,   8943,   2041,   9065]

print("Su mensaje original es:")
print(decrypt(llave, n, texto))

