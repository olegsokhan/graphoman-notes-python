from utils import WordUtils
import unittest


class TestWordUtils(unittest.TestCase):

    def test_with_filters_off_0(self):
        note = "a b c"
        result = WordUtils().get_unique_words_with_filters_off(note)
        self.assertEqual(['a','b', 'c'], result)

    def test_with_filters_off_1(self):
        note = "a b c a b c a b c a b c"
        result = WordUtils().get_unique_words_with_filters_off(note)
        self.assertEqual(['a','b', 'c'], result)

    def test_with_filters_off_2(self):
        note = "a, b, c, 'wow'"
        result = WordUtils().get_unique_words_with_filters_off(note)
        self.assertEqual(['a,', 'b,', 'c,', "'wow'"], result)

    def test_with_filters_off_3(self):
        note = "[one] <one> [one] one!"
        result = WordUtils().get_unique_words_with_filters_off(note)
        self.assertEqual(['[one]','<one>','one!'], result)

    def test_with_filters_on_0(self):
        note = "a b c"
        result = WordUtils().get_unique_words_with_filters_on(note)
        self.assertEqual(['a','b', 'c'], result)

    def test_with_filters_on_1(self):
        note = "a, b, c, a, b? (c) [a] 'b' <c> a! b. c"
        result = WordUtils().get_unique_words_with_filters_on(note)
        self.assertEqual(['a','b', 'c'], result)

    def test_with_filters_on_2(self):
        note = "a, b, c, 'wow' b c a"
        result = WordUtils().get_unique_words_with_filters_on(note)
        self.assertEqual(['a', 'b', 'c', "wow"], result)

    def test_with_filters_on_3(self):
        note = "[one] <one> [one] one!"
        result = WordUtils().get_unique_words_with_filters_on(note)
        self.assertEqual(['one'], result)


if __name__ == '__main__':
    unittest.main()