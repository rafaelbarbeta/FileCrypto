from funcs import Vigenere64

print("\033[31mImgCrypto - Python3 script to encrypt images with the Vigenère Cipher\033[0m")

img_to_convert = input("Please, select an image from your local folder: ") #Opena a iamge in binary mode for reading
with open(img_to_convert,"rb") as bin_to_convert:
    bytes_like = bin_to_convert.read() #bytes_like variable contains the binary data of the chosen image

ving = Vigenere64(bytes_like)

print("Options available: ") # Menu
print("1) Encrypt ")
print("2) Decrypt")
option = input("Option (number or word): ")

option = option.lower()
if option == "1" or option == "encrypt":
    ving.byte_to_b64() # encode image in base64
    test_variable = ving.b64_to_byte() #just for debugging reasons

elif option == "2" or option == "decrypt":
    ving.byte_to_b64()
    test_variable = ving.b64_to_byte()


with open("output.png","wb") as bin_converted: # writrs the bytes from the encrypted/decrypted file in "output.png"
    bin_converted.write(test_variable)