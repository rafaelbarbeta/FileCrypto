import base64

def byte_to_b64(byte): #converts an image to base64 encoding and returns an list with the ASCII values for the image
    text_base64 = list(base64.b64encode(byte))
    return text_base64

def b64_to_byte(text_list): #converts an list with ASCII values into the machine readable bytes
    for i in range(len(text_list)) :
        text_list[i] = chr(text_list[i])
    text_string = "".join(text_list)
    bytes_decoded = base64.b64decode(bytes(text_string,"ascii"))
    return bytes_decoded




