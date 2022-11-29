import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

again = True


def caesar(text, shift, direction):
    end_text = ""
    for i in range(len(text)):
        if text[i] in alphabet:
            ind = alphabet.index(text[i])
            if direction == "encode":
                ind = (ind + shift) % 26
            else:
                ind = (ind - shift % 26 + 26) % 26
            end_text += alphabet[ind]
        else:
            end_text += text[i]
    print(f"The {direction}d result is : {end_text}")


while again:
    direction = input("Type encode to encrypt, type decode to decrypt :\n").lower()
    text = input("Type your message : \n").lower()
    shift = int(input("Type the shift number :\n"))
    caesar(text, shift, direction)
    choice = input("Type 'yes if you want to go again. Otherwise type 'no'./n").lower()
    if choice == "no":
        again = False


