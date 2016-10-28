import unittest
from diamond import Diamond

"""
    a
   b b
  c   c
 d     d
e       e
 d      d
  c    c
   b  b
    a
"""


class DiamondSeparatorTest(unittest.TestCase):

    def test_when_a_given_it_returns_empty_string(self):
        res = Diamond().separator('a')

        self.assertEqual(res, '')

    def test_when_b_given_it_returns_one_spaces(self):
        res = Diamond().separator('b')

        self.assertEqual(res, ' ')

    def test_when_c_given_it_returns_three_spaces(self):
        res = Diamond().separator('c')

        self.assertEqual(res, '   ')


class DiamondIndentTest(unittest.TestCase):

    def test_when_a_given_it_returns_empty_string(self):
        res = Diamond().indent(current='a', limit='a')

        self.assertEqual(res, '')

    def test_when_b_given_it_returns_empty_string(self):
        res = Diamond().indent(current='b', limit='b')

        self.assertEqual(res, '')

    def test_when_b_given_and_current_is_a_it_returns_one_space(self):
        res = Diamond().indent(current='a', limit='b')

        self.assertEqual(res, ' ')

    def test_when_c_given_and_current_is_a_it_returns_two_spaces(self):
        res = Diamond().indent(current='a', limit='c')

        self.assertEqual(res, '  ')


class DiamondGetLettersFromTest(unittest.TestCase):

    def test_when_a_given_it_returns_expected_list(self):
        res = Diamond().get_letters_from(limit='a')

        self.assertEqual([c for c in res], ['a'])

    def test_when_b_given_it_returns_expected_list(self):
        res = Diamond().get_letters_from(limit='b')

        self.assertEqual([c for c in res], ['a', 'b', 'a'])

    def test_when_c_given_it_returns_expected_list(self):
        res = Diamond().get_letters_from(limit='c')

        self.assertEqual([c for c in res], ['a', 'b', 'c', 'b', 'a'])


class DiamondGetCharListTest(unittest.TestCase):

    def test_when_a_given_it_returns_a(self):
        expected = ['a', '\n']

        res = Diamond().get_chars_list('a')

        self.assertEqual(res, expected)

    def test_when_b_given_it_returns_expected_list(self):
        expected = [
            ' ', 'a', '\n',
            'b', ' ', 'b', '\n',
            ' ', 'a', '\n'
        ]

        res = Diamond().get_chars_list('b')

        self.assertListEqual(res, expected)

    def test_when_c_given_it_returns_expected_list(self):
        expected = [
            '  ', 'a', '\n',
            ' ', 'b', ' ', 'b', '\n',
            'c', '   ', 'c', '\n',
            ' ', 'b', ' ', 'b', '\n',
            '  ', 'a', '\n'
        ]

        res = Diamond().get_chars_list('c')

        self.assertListEqual(res, expected)


class DiamondCreateTest(unittest.TestCase):

    def test_when_a_given_it_returns_expected_diamond(self):
        expected = 'a\n'

        res = Diamond().create('a')

        self.assertEqual(res, expected)

    def test_when_b_given_it_returns_expected_diamond(self):
        expected = ' a\nb b\n a\n'

        res = Diamond().create('b')

        self.assertEqual(res, expected)

    def test_when_c_given_it_returns_expected_diamond(self):
        expected = '  a\n b b\nc   c\n b b\n  a\n'

        res = Diamond().create('c')

        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
