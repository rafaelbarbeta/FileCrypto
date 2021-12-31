from funcs import Vigenere64
from os.path import isfile

print("\033[32mFileCrypto - Python3 script to encrypt files with the Vigenère Cipher\033[0m")


file_to_convert = False
key = ""
while isfile(file_to_convert) == False:
    file_to_convert = input("Please, select an file from your local folder: ") #Open a file in binary mode for reading 
while key == "":
    key = input("Please, type the key you want to use to encrypt/decrypt: ")
with open(file_to_convert,"rb") as bin_to_convert:
    bytes_like = bin_to_convert.read() #bytes_like variable contains the binary data of the chosen file
ving = Vigenere64(bytes_like,key)


option = 0
options = {"1", "2", "encrypt", "decrypt"} #available options
print("Options available: ") # Menu
print("1) Encrypt ")
print("2) Decrypt")
while option not in options: #If option is not in available options, the script does not continue
    option = input("Option (number or word): ")
    option = option.lower()


if option == "1" or option == "encrypt":
    ving.byte_to_b64() # encode file in base64
    ving.encrypt() # encrypt file with vigenère cipher
    final_output = ving.b64_to_byte()  #decode base64 into a bytes object
elif option == "2" or option == "decrypt":
    ving.byte_to_b64() # encode file in base64
    ving.decrypt() # decrypt file with vigenère cipher
    final_output = ving.b64_to_byte() #decode base64 into a bytes object


with open(file_to_convert,"wb") as bin_converted: # writes the bytes from the encrypted/decrypted file to "file_to_convert"
   bin_converted.write(final_output)