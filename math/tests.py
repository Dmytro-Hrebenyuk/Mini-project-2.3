import unittest
from my_code import read_file, review_brackets, write_correct_lines

class TestBracketCorrection(unittest.TestCase):

    def test_read_file(self):
        input_filename1 = "test1.txt"
        input_filename2="test2.txt"

        expected_lines1 = ['(<{}>)', ')<{}>)', '(<{}>', '(<{}>]']
        expected_lines2 = ['[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(', '{([(<{}[<>[]}>{[]{[(<()>', '(((({<>}<{<{<>}{[]{[]{}', '[[<[([]))<([[{}[[()]]]', '[{[{({}]{}}([{[{{{}}([]', '{<[[]]>}<{[{[{[]{()[[[]', '[<(<(<(<{}))><([]([]()', '<{([([[(<>()){}]>(<<{{', '<{([{{}}[<[[[<>{}]]]>[]]', '){[{{}}[<[[[<>{}]]]>[]]', '[<(<(<(<{}>)>)>)>][]()']

        lines1 = read_file(input_filename1)
        lines2 = read_file(input_filename2)

        self.assertEqual(lines1, expected_lines1)
        self.assertEqual(lines2,expected_lines2)

    def test_review_brackets(self):
        input_lines = ['(<{}>)', ')<{}>)', '(<{}>', '(<{}>]']
        expected_compensation = 5
        expected_corrected_lines = ['(<{}>)', '(()<{}>)', '(<{}>)', '(<{}>)']

        compensation, corrected_lines = review_brackets(input_lines)

        self.assertEqual(compensation, expected_compensation)
        self.assertEqual(corrected_lines, expected_corrected_lines)

    def test_review_brackets_test2(self):
        input_lines = ['[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(', '{([(<{}[<>[]}>{[]{[(<()>', '(((({<>}<{<{<>}{[]{[]{}', '[[<[([]))<([[{}[[()]]]', '[{[{({}]{}}([{[{{{}}([]', '{<[[]]>}<{[{[{[]{()[[[]', '[<(<(<(<{}))><([]([]()', '<{([([[(<>()){}]>(<<{{', '<{([{{}}[<[[[<>{}]]]>[]]', '){[{{}}[<[[[<>{}]]]>[]]', '[<(<(<(<{}>)>)>)>][]()']
        expected_compensation = 5581
        expected_corrected_lines = ["[({(<(())[]>[[{[]{<()<>}]})", "[(()[<>])]({[<{<<[]>}]})", "{([(<{}[<>[]>{[]{[(<()>)]})", "(((({<>}<{<{<>}{[]{[]{}]]}})", "[[<[([]))<([[{}[[()]]]]]", "[{[{({}]{}}([{[{{{}}([}]]]]", "{<[[]]>}<{[{[{[]{()[[[[]}]]]]]]}>", "[<(<(<(<{}))><([]([]())>)>)]", "<{([([[(<>()){}]>(<<{}))])}>", "<{([{{}}[<[[[<>{}]>[]]]]>[])}>", "){[{{}}[<[[[<>{}]>[]]]]>[]}", "[<(<(<(<{}>)>)>)>][]()]()"]

        compensation, corrected_lines = review_brackets(input_lines)

        self.assertEqual(compensation, expected_compensation)
        self.assertEqual(corrected_lines, expected_corrected_lines)

    def test_write_correct_lines(self):
        input_lines = ['(<{}>)', '(()<{}>)', '(<{}>)', '(<{}>)']
        expected_filename = 'test_output.txt'

        write_correct_lines(input_lines, expected_filename)

        written_lines = read_file(expected_filename)

        self.assertEqual(input_lines, written_lines)

    def test_write_correct_lines_test2(self):
        input_lines = ["[({(<(())[]>[[{[]{<()<>}]})", "[(()[<>])]({[<{<<[]>}]})", "{([(<{}[<>[]>{[]{[(<()>)]})", "(((({<>}<{<{<>}{[]{[]{}]]}})", "[[<[([]))<([[{}[[()]]]]]", "[{[{({}]{}}([{[{{{}}([}]]]]", "{<[[]]>}<{[{[{[]{()[[[[]}]]]]]]}>", "[<(<(<(<{}))><([]([]())>)>)]", "<{([([[(<>()){}]>(<<{}))])}>", "<{([{{}}[<[[[<>{}]>[]]]]>[])}>", "){[{{}}[<[[[<>{}]>[]]]]>[]}", "[<(<(<(<{}>)>)>)>][]()]()"]
        expected_filename = 'test2_output.txt'

        write_correct_lines(input_lines, expected_filename)

        written_lines = read_file(expected_filename)

        self.assertEqual(input_lines, written_lines)
if __name__ == '__main__':
    unittest.main()
