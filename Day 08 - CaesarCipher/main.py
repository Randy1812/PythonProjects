from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)
ans = "yes"
while ans == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(text, shift, direction):
        if shift > 26:
            shift %= 26
        if direction == "decode":
            shift *= -1
        final_text = [" " for i in range(len(text))]
        for i in range(len(text)):
            if text[i].isalpha():
                pos = alphabet.index(text[i])
                pos += shift
                if pos > 25:
                    pos -= 26
                final_text[i] = alphabet[pos]
            else:
                final_text[i] = text[i]
        print(f"The encrypted text is : {''.join(final_text)}")

    caesar(text, shift, direction)
    ans = input("Continue ? (yes / no) ").lower()
