Python Template
===============

|PyPI version|

.. |PyPI version| image:: https://badge.fury.io/py/pytpl.svg
   :target: https://pypi.python.org/pypi/pytpl

This is a minimalist template for writing Python applications. It’s
designed so you can quickly start developing, with the intent to
eventually publish on `PyPI`_. It uses ``setuptools`` to facilitate
installation and dependency resolution.

Compatible with Python 3.4 and up.

Usage
-----

To get started, you’ll need two things. First, make sure you’ve got
``pip`` installed (it’s included in a standard Python install from the
`official website`_). Also, make sure you’ve got a `virtual environment`_
set up.

When developing a ``setup.py`` application, run the following to get
started:

::

    $ ./setup.py develop

If you’re installing this package for *production* instead, run the
following:

::

    $ ./setup.py install

These commands will download all dependencies and make your application
usable within your current virtual environment. The only difference that
``develop`` has is that it symlinks to your actual code so you can
modify it on the fly, whereas ``install`` actually installs a copy into
your Python packages directory.

Example
-------

This template itself contains an example command line script, just to
show how installing via ``setup.py`` is the easiest way to deploy Python
packages. After installation is complete, run the following script:

::

    $ pytpl

If you properly installed the package using ``setup.py``, it should be
globally available from any working directory, as long as your virtual
environment is activated.

Unit tests
----------

Every good package should have unit tests. An example is included. The
``setup.py`` file contains a reference to the test suite, which has module
name ``pytpl.tests``. There are two ways to run the unit tests—either via
``setup.py``:

::

    $ ./setup.py test

Or manually by invoking Python:

::

    $ python -m unittest discover -v pytpl/tests

Publishing to PyPI
------------------

`PyPI`_ is the standard Python module repository. As a general rule of
thumb, if what you’re making could be useful to other people, you should
publish it there.

To learn how to publish to PyPI, you need to set up an account there.
Read `the tutorial by Peter Downs`_ for more information.

When you’re set up, you first need to register the package name with the
following command:

::

    $ ./setup.py register

Then you can publish whenever you have a new version:

::

    $ ./setup.py sdist upload

Make sure to bump the version properly. Strictly speaking, the version
number needs to comply with `PEP386`_, but it’s strongly recommended
that you follow `semver`_ conventions.

Just to show how useful PyPI is, we’re including one external module in
our dependencies list—see ``setup.py``. This module is automatically
downloaded and activated inside our virtual environment when we run
``./setup.py develop``.

Copyright
---------

Copyright © 2016, Michiel Sikma

MIT licensed. See ``copyright.rst`` for more information. Feel free to
copy this template for your own purposes.

.. _PyPI: https://pypi.python.org/pypi
.. _official website: http://python.org/
.. _virtual environment: http://docs.python-guide.org/en/latest/dev/virtualenvs/
.. _the tutorial by Peter Downs: http://peterdowns.com/posts/first-time-with-pypi.html
.. _PEP386: https://www.python.org/dev/peps/pep-0386/
.. _semver: http://semver-ftw.org/
