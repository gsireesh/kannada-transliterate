from unittest import TestCase

from character_mappings import CONSONANT_CHAR_CLASS, kn_iast_mappings, kn_iast_classes
from transliterate import transliterate_kn_iast


class TestTransliteration(TestCase):
    def test_single_chars(self):
        # test a collection of single characters
        for original, expected_trans in kn_iast_mappings.items():
            actual_trans = transliterate_kn_iast(original)
            if kn_iast_classes.get(original) == CONSONANT_CHAR_CLASS:
                expected_trans = expected_trans + "a"
            self.assertEqual(expected_trans, actual_trans)

    def test_multicharacter_strings(self):
        pairs = [("ಕನ್ನಡ", "kannaḍa"), ("ಬರಹ", "baraha"), ("ಕೇನ್ದ್ರದಿನ್ದ", "kēndradinda")]

        for original, expected_trans in pairs:
            actual_trans = transliterate_kn_iast(original)
            self.assertEqual(expected_trans, actual_trans)
