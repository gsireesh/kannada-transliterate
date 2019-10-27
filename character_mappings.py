VOWEL_CHAR_CLASS = "vowel"
DIACRITIC_CHAR_CLASS = "diacritic"
CONSONANT_CHAR_CLASS = "consonant"


kn_iast_mappings = {
    "ಀ": "",  # spacing for candrabindu
    "ಁ": "",  # candrabindu. not in common use.
    "ಂ": "ṁ",
    "ಃ": "ḥ",
    "಄": "",  # Unused.
    "ಅ": "a",
    "ಆ": "ā",
    "ಇ": "i",
    "ಈ": "ī",
    "ಉ": "u",
    "ಊ": "ū",
    "ಋ": "ṛ",
    "ಌ": "ḷ",  # vocalic L, unused
    "಍": "",  # unused
    "ಎ": "e",
    "ಏ": "ē",
    "ಐ": "ai",
    "಑": "",  # unclear
    "ಒ": "o",
    "ಓ": "ō",
    "ಔ": "au",
    "ಕ": "k",
    "ಖ": "kh",
    "ಗ": "g",
    "ಘ": "gh",
    "ಙ": "ṅ",
    "ಚ": "c",
    "ಛ": "ch",
    "ಜ": "j",
    "ಝ": "jh",
    "ಞ": "ñ",
    "ಟ": "ṭ",
    "ಠ": "ṭh",
    "ಡ": "ḍ",
    "ಢ": "ḍh",
    "ಣ": "ṇ",
    "ತ": "t",
    "ಥ": "th",
    "ದ": "d",
    "ಧ": "dh",
    "ನ": "n",
    "಩": "",  # unused
    "ಪ": "p",
    "ಫ": "ph",
    "ಬ": "b",
    "ಭ": "bh",
    "ಮ": "m",
    "ಯ": "y",
    "ರ": "r",
    "ಱ": "ṟ",
    "ಲ": "l",
    "ಳ": "ḷ",
    "಴": "ḻ",
    "ವ": "v",
    "ಶ": "ś",
    "ಷ": "ṣ",
    "ಸ": "s",
    "ಹ": "h",
    "಺": "",  # unused
    "಻": "",  # unused
    "಼": "",  # nukta, used to do things like f?? Not in common use.
    "ಽ": "",  # avagraha
    "ಾ": "ā",
    "ಿ": "i",
    "ೀ": "ī",
    "ು": "u",
    "ೂ": "ū",
    "ೃ": "ṛ",
    "ೄ": "ṝ",
    "೅": "",  # unused
    "ೆ": "e",
    "ೇ": "ē",
    "ೈ": "ai",
    "೉": "",  # unused
    "ೊ": "o",
    "ೋ": "ō",
    "ೌ": "au",
    "್": "",  # virāma
    "೎": "",  # unused
    "೏": "",  # unused
    "೐": "",  # unused
    "೑": "",  # unused
    "೒": "",  # unused
    "೓": "",  # unused
    "೔": "",  # unused
    "ೕ": "",  # length mark, untranscribed solo.
    "ೖ": "",  # ai length mark, untranscribed solo.
    "೗": "",  # unused
    "೘": "",  # unused
    "೙": "",  # unused
    "೚": "",  # unused
    "೛": "",  # unused
    "೜": "",  # unused
    "ೝ": "",  # unused
    "ೞ": "ɺ",  # similar to tamil zh sound
    "೟": "",  # unused
    "ೠ": "lɨ",  # Not sure if these four are correct, I've never seen them used.
    "ೡ": "lɨː",
    "ೢ": "lɨ",
    "ೣ": "lɨː",
    "೤": "",
    "೥": "",
    "೦": "0",
    "೧": "1",
    "೨": "2",
    "೩": "3",
    "೪": "3",
    "೫": "5",
    "೬": "6",
    "೭": "7",
    "೮": "8",
    "೯": "9",
    "೰": "",  # unused
    "ೱ": "",  # ardhavisarga symbols. Largely unused.
    "ೲ": "",  # ardhavisarga symbols. Largely unused.
    "ೳ": "",  # unused
    "೴": "",  # unused
    "೵": "",  # unused
    "೶": "",  # unused
    "೷": "",  # unused
    "೸": "",  # unused
    "೹": "",  # unused
    "೺": "",  # unused
    "೻": "",  # unused
    "೼": "",  # unused
    "೽": "",  # unused
    "೾": "",  # unused
}

kn_iast_classes = {
    "ಀ": "",  # spacing for candrabindu
    "ಁ": "",  # candrabindu. not in common use.
    "ಂ": DIACRITIC_CHAR_CLASS,
    "ಃ": DIACRITIC_CHAR_CLASS,
    "಄": "",  # Unused.
    "ಅ": VOWEL_CHAR_CLASS,
    "ಆ": VOWEL_CHAR_CLASS,
    "ಇ": VOWEL_CHAR_CLASS,
    "ಈ": VOWEL_CHAR_CLASS,
    "ಉ": VOWEL_CHAR_CLASS,
    "ಊ": VOWEL_CHAR_CLASS,
    "ಋ": VOWEL_CHAR_CLASS,
    "ಌ": VOWEL_CHAR_CLASS,  # vocalic L, unused
    "಍": "",  # unused
    "ಎ": VOWEL_CHAR_CLASS,
    "ಏ": VOWEL_CHAR_CLASS,
    "ಐ": VOWEL_CHAR_CLASS,
    "಑": "",  # unclear
    "ಒ": VOWEL_CHAR_CLASS,
    "ಓ": VOWEL_CHAR_CLASS,
    "ಔ": VOWEL_CHAR_CLASS,
    "ಕ": CONSONANT_CHAR_CLASS,
    "ಖ": CONSONANT_CHAR_CLASS,
    "ಗ": CONSONANT_CHAR_CLASS,
    "ಘ": CONSONANT_CHAR_CLASS,
    "ಙ": CONSONANT_CHAR_CLASS,
    "ಚ": CONSONANT_CHAR_CLASS,
    "ಛ": CONSONANT_CHAR_CLASS,
    "ಜ": CONSONANT_CHAR_CLASS,
    "ಝ": CONSONANT_CHAR_CLASS,
    "ಞ": CONSONANT_CHAR_CLASS,
    "ಟ": CONSONANT_CHAR_CLASS,
    "ಠ": CONSONANT_CHAR_CLASS,
    "ಡ": CONSONANT_CHAR_CLASS,
    "ಢ": CONSONANT_CHAR_CLASS,
    "ಣ": CONSONANT_CHAR_CLASS,
    "ತ": CONSONANT_CHAR_CLASS,
    "ಥ": CONSONANT_CHAR_CLASS,
    "ದ": CONSONANT_CHAR_CLASS,
    "ಧ": CONSONANT_CHAR_CLASS,
    "ನ": CONSONANT_CHAR_CLASS,
    "಩": "",  # unused
    "ಪ": CONSONANT_CHAR_CLASS,
    "ಫ": CONSONANT_CHAR_CLASS,
    "ಬ": CONSONANT_CHAR_CLASS,
    "ಭ": CONSONANT_CHAR_CLASS,
    "ಮ": CONSONANT_CHAR_CLASS,
    "ಯ": CONSONANT_CHAR_CLASS,
    "ರ": CONSONANT_CHAR_CLASS,
    "ಱ": CONSONANT_CHAR_CLASS,
    "ಲ": CONSONANT_CHAR_CLASS,
    "ಳ": CONSONANT_CHAR_CLASS,
    "಴": CONSONANT_CHAR_CLASS,
    "ವ": CONSONANT_CHAR_CLASS,
    "ಶ": CONSONANT_CHAR_CLASS,
    "ಷ": CONSONANT_CHAR_CLASS,
    "ಸ": CONSONANT_CHAR_CLASS,
    "ಹ": CONSONANT_CHAR_CLASS,
    "಺": "",  # unused
    "಻": "",  # unused
    "಼": DIACRITIC_CHAR_CLASS,  # nukta, used to do things like f?? Not in common use.
    "ಽ": DIACRITIC_CHAR_CLASS,  # avagraha
    "ಾ": DIACRITIC_CHAR_CLASS,
    "ಿ": DIACRITIC_CHAR_CLASS,
    "ೀ": DIACRITIC_CHAR_CLASS,
    "ು": DIACRITIC_CHAR_CLASS,
    "ೂ": DIACRITIC_CHAR_CLASS,
    "ೃ": DIACRITIC_CHAR_CLASS,
    "ೄ": DIACRITIC_CHAR_CLASS,
    "೅": "",  # unused
    "ೆ": DIACRITIC_CHAR_CLASS,
    "ೇ": DIACRITIC_CHAR_CLASS,
    "ೈ": DIACRITIC_CHAR_CLASS,
    "೉": "",  # unused
    "ೊ": DIACRITIC_CHAR_CLASS,
    "ೋ": DIACRITIC_CHAR_CLASS,
    "ೌ": DIACRITIC_CHAR_CLASS,
    "್": DIACRITIC_CHAR_CLASS,  # virāma
    "೎": "",  # unused
    "೏": "",  # unused
    "೐": "",  # unused
    "೑": "",  # unused
    "೒": "",  # unused
    "೓": "",  # unused
    "೔": "",  # unused
    "ೕ": DIACRITIC_CHAR_CLASS,  # length mark, untranscribed solo.
    "ೖ": DIACRITIC_CHAR_CLASS,  # ai length mark, untranscribed solo.
    "೗": "",  # unused
    "೘": "",  # unused
    "೙": "",  # unused
    "೚": "",  # unused
    "೛": "",  # unused
    "೜": "",  # unused
    "ೝ": "",  # unused
    "ೞ": DIACRITIC_CHAR_CLASS,  # similar to tamil zh sound
    "೟": "",  # unused
    "ೠ": VOWEL_CHAR_CLASS,  # Not sure if these four are correct, I've never seen them used.
    "ೡ": VOWEL_CHAR_CLASS,
    "ೢ": DIACRITIC_CHAR_CLASS,
    "ೣ": DIACRITIC_CHAR_CLASS,
    "೤": "",
    "೥": "",
    "೦": "",
    "೧": "",
    "೨": "",
    "೩": "",
    "೪": "",
    "೫": "",
    "೬": "",
    "೭": "",
    "೮": "",
    "೯": "",
    "೰": "",  # unused
    "ೱ": "",  # ardhavisarga symbols. Largely unused.
    "ೲ": "",  # ardhavisarga symbols. Largely unused.
    "ೳ": "",  # unused
    "೴": "",  # unused
    "೵": "",  # unused
    "೶": "",  # unused
    "೷": "",  # unused
    "೸": "",  # unused
    "೹": "",  # unused
    "೺": "",  # unused
    "೻": "",  # unused
    "೼": "",  # unused
    "೽": "",  # unused
    "೾": "",  # unused
}
