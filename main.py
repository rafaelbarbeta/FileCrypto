from funcs import Vigenere64

print("\033[31mImgCrypto - Python3 script to encrypt images with the Vigenère Cipher\033[0m")

img_to_convert = input("Please, select an image from your local folder: ") #Opena a iamge in binary mode for reading
key = input("Please, type the key you want to use to encrypt/decrypt: ")
with open(img_to_convert,"rb") as bin_to_convert:
    bytes_like = bin_to_convert.read() #bytes_like variable contains the binary data of the chosen image

ving = Vigenere64(b'HelloWorld',key)

print("Options available: ") # Menu
print("1) Encrypt ")
print("2) Decrypt")
option = input("Option (number or word): ")

option = option.lower()
if option == "1" or option == "encrypt":
    ving.byte_to_b64() # encode image in base64
    ving.encrypt()
    test_variable = ving.b64_to_byte() #just for debugging reasons

elif option == "2" or option == "decrypt":
    ving.byte_to_b64()
    ving.decrypt()
    test_variable = ving.b64_to_byte()

with open("textoplano","wb") as bin_converted: # writes the bytes from the encrypted/decrypted file in "output.png"
   bin_converted.write(test_variable)