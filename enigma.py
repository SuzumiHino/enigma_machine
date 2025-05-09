alphabet = "1234567890abcdefghijklmnopqrstuvwxyz "
alphabet.split()
enigma_code = ['1','2','3','4','5','6','7','8','9','0','c','d','a','b',
               'w','i','p','m','f','k','j','n','h','l','q','g','o','z',
               'u','v','s','t','e','y','x','r',' ']
enigma_dict = {k: v for k, v in zip(alphabet, enigma_code)}

def crypt(input_text):
    text_list = list()
    for char in input_text:
        text_list.append(char)
    text = []
    for num in (text_list):
        text.append(enigma_dict[num])
    return "".join(text)

input_text = input('Enter a text:').lower()
print(crypt(input_text))

