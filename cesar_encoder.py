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
        s = s.upper()

    encoded_alf: str = alf[shift:] + alf[:shift]

    encoded_dict = dict()

    for i, j in zip(encoded_alf, alf):
        encoded_dict[j] = i
    
    
    for i in s:
        res += encoded_dict.get(i, i)

    with open(output_file, mode = "w", encoding = "utf-8") as f:
        f.write(res)

if __name__ == "__main__":
    encode("files\\input.txt", "files\\output.txt", 3)