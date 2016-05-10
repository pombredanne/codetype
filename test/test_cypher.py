import os
import sys
import unittest

from cypher.cypher import identify

sys.path.insert(0, os.path.abspath("."))
LANG_DIR = os.path.join("test", "lang")


class identifyTestCase(unittest.TestCase):
    """
    """
    def test_identify(self):
        """
        """
        for subdir, dirs, files in os.walk(LANG_DIR):
            known = os.path.basename(subdir)
            if known != "lang":
                print("Testing {} ...".format(known))
            for f in files:
                if f.endswith(".txt"):
                    computed = identify(os.path.join(subdir, f), is_file=1)
                    self.assertEqual(known, computed)


if __name__ == "__main__":
    unittest.main()