
import sys
setup_kwds = {}


#  Use setuptools if available.
#  We need it for 2to3 integration on python3.
#  Otherwise, fall back to plain old distutils.
try:
    from setuptools import setup
except ImportError:
    if sys.version_info > (3,):
        raise RuntimeError("python3 support requires setuptools")
    from distutils.core import setup
else:
    if sys.version_info > (3,):
        setup_kwds["use_2to3"] = True


#  Extract the docstring and version declaration from the module.
#  To avoid errors due to missing dependencies or bad python versions,
#  we explicitly read the file contents up to the end of the version
#  delcaration, then exec it ourselves.
info = {}
src = open("mangler/__init__.py")
lines = []
for ln in src:
    lines.append(ln)
    if "__version__" in ln:
        for ln in src:
            if "__version__" not in ln:
                break
            lines.append(ln)
        break
exec("".join(lines),info)


NAME = "mangler"
VERSION = info["__version__"]
DESCRIPTION = "bytecode mangler for frozen python apps"
LONG_DESC = info["__doc__"]
AUTHOR = "Ryan Kelly"
AUTHOR_EMAIL = "ryan@rfk.id.au"
URL="http://github.com/rfk/mangler"
LICENSE = "MIT"
KEYWORDS = "freeze frozen py2exe bytecode obfuscate"
CLASSIFIERS = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved",
    "License :: OSI Approved :: MIT License",
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
]

setup(name=NAME,
      version=VERSION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      description=DESCRIPTION,
      long_description=LONG_DESC,
      license=LICENSE,
      keywords=KEYWORDS,
      packages=["mangler"],
      classifiers=CLASSIFIERS,
      **setup_kwds
     )

