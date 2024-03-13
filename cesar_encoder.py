from utils.alphabet import alphabet
from utils.custom_exception import LangError

def encode(input_file, output_file, shift: int, lang = "RU"):
    if lang not in alphabet.keys():
        raise LangError(lang)
    
    alf = alphabet[lang]

    res = ""

    with open(input_file, mode = "r", encoding = "utf-8") as f:
        s: str = f.readlines()
        s = "".join(s)
        s = s.lower()

    encoded_dict = dict.fromkeys(alf)

    for i in alf[:-shift]:
        encoded_dict[i] = chr(ord(i) + shift)
    for i in alf[-shift:]:
        encoded_dict[i] = chr(ord(alf[0]) - (ord(alf[-1]) - ord(i) - shift + 1))
    
    
    for i in s:
        res += encoded_dict.get(i, i)

    with open(output_file, mode = "w", encoding = "utf-8") as f:
        f.write(res)

if __name__ == "__main__":
    encode("files\\input.txt", "files\\output.txt", 3)
    
    
    

