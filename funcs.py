import base64

class Vigenere64():
    
    ascii_values_list = [] #defines a list were the ascii values representing the base64 characters are going to be stored
    key_decomposed = [] #like the assci_values_list, this class variable will be used to stored the key broken down into pieces
    base64_symbols = [i for i in range(48,123) if i not in range(58,65) and i not in range(91,97)] #all alfanumeric e alphabetci characters
    base64_symbols.append(43) # append +
    base64_symbols.append(47) # append /
    bse64_symbols_values = [i for i in range(64)] # this list will be used to create a dictionary with the "base64_symbols" to use the vigenère cipher

    def __init__(self, bytes_file,key): #the bytes of the file open is stored in the "bytes_file" instance variable
        self.bytes_file = bytes_file
        self.ascii_remaped = dict(zip(self.base64_symbols,self.bse64_symbols_values))
        self.key_len = len(key)
        for i in range(self.key_len): #split the key in characters, the get it's ascii corresponding number
            self.key_decomposed.append(ord(key[i]))
            self.key_decomposed[i] = self.ascii_remaped.get(self.key_decomposed[i]) #remaps the number according with the dictionary "ascci_remaped"

    def get_key(self, val): # Not the best approach to get the keys from values. To be changed in further commits
        for key, value in self.ascii_remaped.items():
             if val == value:
                  return key

    def byte_to_b64(self): #converts an image to base64 encoding and returns an list with the ASCII values for the image
        self.ascii_values_list = list(base64.b64encode(self.bytes_file))

    def b64_to_byte(self): #converts an list with ASCII values into the machine readable bytes
        for i in range(len(self.ascii_values_list)) :
            self.ascii_values_list[i] = chr(self.ascii_values_list[i])
        text_string = "".join(self.ascii_values_list)
        bytes_decoded = base64.b64decode(bytes(text_string,"ascii"))
        return bytes_decoded

    def encrypt(self):
        for i in range(len(self.ascii_values_list)):
            mapped_value = self.ascii_remaped.get(self.ascii_values_list[i])
            if mapped_value == None: #if the mapped value is None, that means the padding "=" has been reached, and therefore the encrypt function has fineshed it's job
                break
            encrypted_mapped_value = (mapped_value + self.key_decomposed[i % self.key_len]) % 64
            encrypted_ascii_value = self.get_key(encrypted_mapped_value)
            self.ascii_values_list[i] = encrypted_ascii_value

    def decrypt(self):
        for i in range(len(self.ascii_values_list)):
            mapped_value = self.ascii_remaped.get(self.ascii_values_list[i])
            if mapped_value == None: #if the mapped value is None, that means the padding "=" has been reached, and therefore the encrypt function has fineshed it's job
                break
            encrypted_mapped_value = (mapped_value - self.key_decomposed[i % self.key_len]) % 64
            encrypted_ascii_value = self.get_key(encrypted_mapped_value)
            self.ascii_values_list[i] = encrypted_ascii_value