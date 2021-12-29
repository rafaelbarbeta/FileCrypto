import base64


class Vigenere64():
    
    ascii_values_list = [] #defines a list were the ascii values representing the base64 characters are going to be stored

    def __init__(self, bytes_image): #the bytes of the file open is stored in the "bytes_image" instance variable
        self.bytes_image = bytes_image

    def byte_to_b64(self): #converts an image to base64 encoding and returns an list with the ASCII values for the image
        self.ascii_values_list = list(base64.b64encode(self.bytes_image))

    def b64_to_byte(self): #converts an list with ASCII values into the machine readable bytes
        for i in range(len(self.ascii_values_list)) :
            self.ascii_values_list[i] = chr(self.ascii_values_list[i])
        text_string = "".join(self.ascii_values_list)
        bytes_decoded = base64.b64decode(bytes(text_string,"ascii"))
        return bytes_decoded




