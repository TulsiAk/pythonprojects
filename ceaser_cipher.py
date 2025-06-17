alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encode(text,shift):
    new_text=""
    for i in text:
        modified_index=alphabet.index(i)+shift
        new_text+=alphabet[modified_index]
    return new_text
def decode(text,shift):
    new_text=""
    for i in text:
        modified_index=alphabet.index(i)-shift
        new_text+=alphabet[modified_index]
    return new_text
if direction=='encode':
    result=decode(text,shift)
elif direction=='decode':
    result=decode(text,shift)
else:
    print("INVALID DIRECTION")
print(f"This is the encrypted or decrypted result  based on your coice = {result}")   