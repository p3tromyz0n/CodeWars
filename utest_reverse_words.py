import unittest
import reverse_words


class ReverseWordsTest(unittest.TestCase):

    def test_reverse_words(self):

        self.assertEqual(reverse_words.reverse_words('Sweet dreams are made of this'), 'teewS smaerd era edam fo siht')
        self.assertEqual(reverse_words.reverse_words('Antidisestablishmentarianism'), 'msinairatnemhsilbatsesiditnA')
        self.assertEqual(reverse_words.reverse_words('r u n'), 'r u n')
        self.assertEqual(reverse_words.reverse_words('Who am I to disagree?'), 'ohW ma I ot ?eergasid')

    def test_reverse_words_short(self):

        self.assertEqual(reverse_words.reverse_words_short('Sweet dreams are made of this'), 'teewS smaerd era edam fo siht')
        self.assertEqual(reverse_words.reverse_words_short('Antidisestablishmentarianism'), 'msinairatnemhsilbatsesiditnA')
        self.assertEqual(reverse_words.reverse_words_short('r u n'), 'r u n')
        self.assertEqual(reverse_words.reverse_words_short('Who am I to disagree?'), 'ohW ma I ot ?eergasid')


if __name__ == '__main__':
    unittest.main()
