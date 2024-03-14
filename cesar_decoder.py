from collections import Counter

from utils.alphabet import alphabet
from utils.custom_exception import LangError

def decode(input_file, output_file, shift: int, lang = "RU"):
    if lang not in alphabet.keys():
        raise LangError(lang)
    
    alf = alphabet[lang]

    res = ""

    with open(input_file, mode = "r", encoding = "utf-8") as f:
        s: str = f.read()
        s = s.upper()

    c = Counter(s)

    shift: int = ord(c.most_common()[0][0]) - ord("О")

    decoded_alf = alf[shift:-1] + alf[:shift] + " "



    decoded_dict = dict()

    for i, j in zip(decoded_alf, alf):
        decoded_dict[i] = j
    
    res = ""

    for i in s:
        res += decoded_dict.get(i, i)
    with open(output_file, mode = "w", encoding = "utf-8") as f:
        f.write(res)


if __name__ == "__main__":
    decode("files\\ex.txt", "files\\output.txt", 3)