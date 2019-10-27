from character_mappings import (
    CONSONANT_CHAR_CLASS,
    DIACRITIC_CHAR_CLASS,
    kn_iast_mappings,
    kn_iast_classes,
)


def transliterate_kn_iast(kannada_string: str) -> str:
    output_list = []
    prev_char = None
    if not kannada_string:
        return kannada_string

    for char in kannada_string:
        trans_char = kn_iast_mappings.get(char, char)
        # impute the presence of as
        if kn_iast_classes.get(prev_char) == CONSONANT_CHAR_CLASS and (
            kn_iast_classes.get(char) == CONSONANT_CHAR_CLASS or char in "ಂಃ "
        ):
            output_list.append("a")
        output_list.append(trans_char)
        prev_char = char
    last_char = kannada_string[-1]

    if kn_iast_classes.get(last_char) == CONSONANT_CHAR_CLASS:
        output_list.append("a")

    return "".join(output_list)
