from collections import Counter

from utils.alphabet import alphabet
from utils.custom_exception import LangError

def decode(input_file, output_file, shift: int = None, lang = "RU"):
    if lang not in alphabet.keys():
        raise LangError(lang)
    
    alf = alphabet[lang]

    res = ""

    with open(input_file, mode = "r", encoding = "utf-8") as f:
        s: str = f.read()
        s = s.upper()

    if not shift:
        c = Counter(s)

        shift: int = ord(c.most_common()[0][0]) - ord("О")

    encoded_alf: str = alf[shift:] + alf[:shift]

    decoded_dict = dict()

    for i, j in zip(encoded_alf, alf):
        decoded_dict[i] = j
    
    res = ""

    for i in s:
        res += decoded_dict.get(i, i)
    with open(output_file, mode = "w", encoding = "utf-8") as f:
        f.write(res)


if __name__ == "__main__":
    decode("files\\output.txt", "files\\ex.txt", 3)