from unittest import TestCase

from character_mappings import kn_iast
from transliterate import transliterate_kn_iast


class TestTransliteration(TestCase):

	def test_single_chars(self):
		# test a collection of single characters
		for original, expected_trans in kn_iast.items():
			actual_trans = transliterate_kn_iast(original)
			self.assertEqual(expected_trans, actual_trans)

	def test_multicharacter_strings(self):
		pairs = [
			('ಕನ್ನ ಡ', 'kannaḍa'),
			('ಬರಹ', 'baraha'),
			('ಕೇನ್ದ್ರದಿನ್ದ', 'kēndradinda')
		]

		for original, expected_trans in pairs:
			actual_trans = transliterate_kn_iast(original)
			self.assertEqual(expected_trans, actual_trans)
