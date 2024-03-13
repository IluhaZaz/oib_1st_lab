class LangError(Exception):
    def __init__(self, msg, lang: str = "rus") -> None:
        self.message = msg
        self.lang = lang.lower()
    

    def __str__(self):
        match self.lang:
            case "eng":
                from lexicon.lexicon_eng import LEXICON_ENG as LEXICON
            case _:
                from lexicon.lexicon_ru import LEXICON_RU as LEXICON
        return f'{self.message}: {LEXICON["lang_err"]}'
