import unicodedata
import re

def normalize_text(text: str) -> str:
    text = str(text).lower().strip()
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('utf-8')
    return text

sheng_dict = {
    "broo": "bro",
    "bruh": "bro",
    "brathe": "bro",
    "brathee": "bro",
    "radha": "rada",
    "radaa": "rada",
    "radaaa": "rada",
    "mse": "msee",
    "mseeh": "msee",
    "mseee": "msee",
    "fity": "fiti",
    "fitii": "fiti",
    "mbokaa": "mboka",
    "mbokaaa": "mboka",
    "lukuu": "luku",
    "lukuuu": "luku",
    "dobaa": "doba",
    "riengg": "rieng",
    "thiangg": "thiang",
    "mnetii": "mneti",
    "boiiz": "boiz",
    "boizz": "boiz",
    "nomaa": "noma",
    "chwanii": "chwani",
    "teii": "tei",
    "u": "you",
    "ur": "your"
}

def normalize_text(text):
    text = str(text).lower().strip()
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('utf-8')

    return text

def normalize_repetitions(word):
    return re.sub(r'(.)\1{2,}', r'\1', word)

def normalize_sheng_text(text):
    words = text.split()
    normalized_words = [sheng_dict.get(normalize_repetitions(w), w) for w in words]

    return " ".join(normalized_words)

def preprocess(text: str) -> str:
    text = normalize_text(text)
    text = normalize_sheng_text(text)

    return text


