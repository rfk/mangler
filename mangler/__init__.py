"""

mangler:  bytecode mangler for frozen python apps
=================================================

Mangler is a tool to obfuscate the bytecode of your frozen python applications.
It makes it (slightly) harder for someone to take code from your app and use
it for their own evil ends.

Mangler works with the output of py2exe, py2app and cxfreeze.  Support for
bbfreeze and pyinstaller will be added eventually; if you desparately need
such support you can slip me a fifty and I'll get right on it...


Is it secure?
-------------

It's as secure as possible.  Which is to say: no, it's not.  A determined
attacker will be able to obtain the unobfuscated bytecode of your program,
decompile it to an approximation of your source code, and have his/her wicked
way with the result.

But remember:  such reverse engineering is possible to some degree with *any*
application, written in any language.  Anyone who says differently is selling
you snake oil.

What mangler can do is make it harder.  A standard frozen python application
basically ships with a big zipfile of all your code in an easily decompiled
form.  Mangler applies some simple byte-level mangling to the contents of this
zipfile, meaning extra work for someone who wants to get at its contents.

There is plenty more that could be done to make the attacker's work even
harder.  But it would require compiling a C extension or, even better,
compiling a custom python interpreter.  If you think you'd like to go down that
road, I provide distributing-pyton-apps consulting and for a modest fee
I'll be happy to (a) talk you out of it, or (b) implement something for you.


Sounds awesome, how do I use it?
--------------------------------

If you're just using py2exe, py2app or cxfreeze in their basic form, you
can just call the "mangler" script with the path to your frozen app:

    mangler /path/to/frozen/application


This will generate a new mangling key, mangle the frozen bytecode using it,
and patch the executables to correctly load the mangled bytecode.  Easy.

For more complicated scenarios, well, I haven't for around to fixing the API
yet.  Bear with me.


"""

__ver_major__ = 0
__ver_minor__ = 1
__ver_patch__ = 0
__ver_sub__ = ""
__version__ = "%d.%d.%d%s" % (__ver_major__,__ver_minor__,__ver_patch__,__ver_sub__)


import sys
import os


def mangle(appdir):
    """Mangle the bytecode for a frozen python application."""
    pass


def main(argv=None):
    if argv is None:
        argv = sys.argv


if __name__ == "__main__":
    main()


