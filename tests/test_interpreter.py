import unittest
from io import StringIO
import sys
from mjlang import MJLangInterpreter

class TestMJLang(unittest.TestCase):
    def setUp(self):
        self.interpreter = MJLangInterpreter()
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_hello_annie(self):
        code = """
        OW!
        JAM "Annie, are you ok?"
        HEE-HEE!
        """
        self.interpreter.run(code)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Annie, are you ok?")

    def test_addition(self):
        code = """
        OW!
        SHAMONE result BILLIE JEAN 5 THRILLER 5 AOW
        JAM result
        HEE-HEE!
        """
        self.interpreter.run(code)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "10")

if __name__ == "__main__":
    unittest.main()
