import base64

def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode("utf-8")
    except Exception:
        return False

#change the file to what you want to use to encode/decode. I used a simple txt document named "secret_message.txt" to do this function.    
with open("secret_message.txt") as file:
    text = file.read()
    isb64 = isBase64(text)
    #if the text comes back as Base64 then it will decode it.
    if isb64:
        print("true")
        base = text.encode("utf-8")
        decoded_base = base64.decodebytes(base)
        print(decoded_base)
    #if the text in the documnet comes back to anything but Base64 it will encode it and print the encoded text.  
    else:
        print("false")
        base = text.encode("utf-8")
        encoded_base = base64.encodebytes(base)
        encoded_base = encoded_base.decode("utf-8")
        print(encoded_base)
        