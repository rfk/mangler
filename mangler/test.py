
import os
import unittest

import mangler


class TestManglerDocstring(unittest.TestCase):

    def test_readme_matches_docstring(self):
        """Ensure that the README is in sync with the docstring.

        This test should always pass; if the README is out of sync it just
        updates it with the contents of mangler.__doc__.
        """
        dirname = os.path.dirname
        readme = os.path.join(dirname(dirname(__file__)),"README.rst")
        if not os.path.isfile(readme):
            f = open(readme,"wb")
            f.write(mangler.__doc__.encode())
            f.close()
        else:
            f = open(readme,"rb")
            if f.read() != mangler.__doc__:
                f.close()
                f = open(readme,"wb")
                f.write(mangler.__doc__.encode())
                f.close()

