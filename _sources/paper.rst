.. _sec:paper:

Paper preparation
=================

In the ``paper`` directory, you can write your (LaTeX) paper. Many people
use Overleaf these days and it is possible to use git version control
to sync your paper files with Overleaf.

Please see the `Git integration <https://www.overleaf.com/learn/how-to/Git_integration>`_
manual of Overleaf to get your Overleaf project into this directory.

During this workshop, you can either use overleaf to write the LaTeX paper
(log in with your ORCID), or use a local installation of LaTeX.

We have prepared a very short paper that you can finish in the last
sections of this workshop. Please download :download:`hubble.tex </_static/hubble.tex>`
and :download:`hubble.bib </_static/hubble.bib>` and copy them to your
``paper`` directory. If you use Overleaf, you can use git to commit these
files to the Overleaf server.

The ``hubble.tex`` file contains the main text of the paper and the
statements for the typesetting. The ``hubble.bib`` file contains a list
of publications (with all the metadata) that BibTeX can use to generate
a bibliograpy. BibTeX is a very useful tool to manage your citations.


.. admonition:: EXERCISE

  Once both files are in place, try to build the LaTeX files.
  In the terminal, you need to give the following commands::

    latex hubble.tex
    bibtex hubble
    latex hubble.tex
    latex hubble.tex
    dvipdf hubble.dvi

  The commands above will generate a ``hubble.pdf`` file.

Adding your results to the paper
--------------------------------

As you can see, the results and conclusion sections are not yet complete.
We can start with the results section.

.. admonition:: EXERCISE

  Add the following to the results section:

  - Add the Hubble constant and the age of the universe that you derived to the text.
  - Complete the table with the used objects, distances and velocities. For this you can
    add a line to the ``hubblequery.py`` script to write the ``newtable`` with ``format='latex'``
    instead of ``format='fits'``. Also change the file name.
    (see `Astropy Table IO <https://docs.astropy.org/en/stable/table/io.html#getting-started>`_).
  - Add the plot as a figure. Depending on the type of LaTeX that you run, you may
    need to convert or save the plot as postscript (see also matplotlib.pyplot.savefig).

.. admonition:: EXERCISE (OPTIONAL)

  Write a couple of sentences about your result in the conclusion section. Is the Hubble
  constant that you find consistent with what modern dedicated observatories, like Planck, find?

When everything is added, check if your updated LaTeX file still produces a nice PDF
by building it with the commands above or using the Overleaf build function.

