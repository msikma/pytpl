Python Template
===============

This is a minimalist template for writing Python applications. It's designed
so you can quickly start developing, with the intent to eventually publish on
[PyPI](https://pypi.python.org/pypi). It uses `setuptools` to facilitate
installation and dependency resolution.

Compatible with Python 3.4 and up.


Usage
-----

To get started, you'll need two things. First, make sure you've got `pip`
installed (it's included in a standard Python install from the [official website](http://python.org/)).
Also, make sure you've got a *[virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)*
set up.

When developing a `setup.py` application, run the following to get started:

    $ ./setup.py develop

If you're installing this package for *production* instead, run the following:

    $ ./setup.py install

These commands will download all dependencies and make your application
usable within your current virtual environment. The only difference that
`develop` has is that it symlinks to your actual code so you can modify it
on the fly, whereas `install` actually installs a copy into your Python
packages directory.


Example
-------

This template itself contains an example command line script, just to show
how installing via `setup.py` is the easiest way to deploy Python packages.
After installation is complete, run the following script:

    $ pytpl

If you properly installed the package using `setup.py`, it should be globally
available from any working directory, as long as your virtual environment
is activated.


Copyright
---------

Copyright © 2016, Michiel Sikma

MIT licensed. See `copyright.md` for more information. Feel free to copy
this template for your own purposes.
