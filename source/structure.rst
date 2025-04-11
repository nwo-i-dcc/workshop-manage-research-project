.. _sec:structure:

Project directory structure
===========================

Creating a general projects directory
-------------------------------------

Now that we know where to create our project directory, it is time to create the directory itself.
In this tutorial, we assume that you create the project directory in your home directory (``/home/<user>``
or ``/Users/<user>``, where ``<user>`` is your user name).

To keep the top of your home directory clean, it is best to create a main directory for all projects.
This is a bit subjective, but if you do that, it clearly separates your science project files from
downloads, pictures, etc. We create the directory ``Projects`` for this purpose, but of course you can
give it a different name if you like.

On Linux and Mac, you can create the folder in the terminal like this::

    user@terminal:~> mkdir ~/Projects

This will be the place for all your future projects.

Creating a project directory using cookiecutter
-----------------------------------------------

So, how do we create a directory structure for our next research project? Of course, there are other people
who have thought of this before. They were even so kind to share their experiences and came up with a good
structure to start with. There is even a python package that gives you access to a lot of possible project
templates: `Cookiecutter <https://cookiecutter.readthedocs.io/en/stable/>`_.

The template that we use in this tutorial is the `NWO Cookiecutter
<https://github.com/nwo-i-dcc/nwo-cookiecutter>`_. To use this template, we
first need to make sure that conda is running and the cookiecutter package is installed.

To create a new project directory, we first change to our ``Projects`` directory::

    (base) user@terminal:~> cd Projects
    (base) user@terminal:~/Projects>

In this directory, we can now create a new project directory. Do you already have a good name for your project?
A short and unique name helps a lot. You create the new directory using the ``cookiecutter`` program::

    (base) user@terminal:~/Projects> cookiecutter https://github.com/nwo-i-dcc/nwo-cookiecutter

When you execute the above, you need to answer a couple of questions.
Give a name to your project. This is going to be the name of the project
directory, so make sure it is easy enough (one word)::

    [1/5] project_name (What is the name of your project?): hubble

A Python package directory is automatically created. You can give this package
a unique name. Do not give it the same or similar name as existing Python packages::

    [2/5] repo_name (Give a name to the Python package of your project (one word)): hubble

If you add your name and email address to the project, it will appear in
the Python package and the README::

    [3/5] author_name (Your name (or your organization/company/team)): Jane Doe (NWO)
    [4/5] email (Your email address): jdoe@nwo-i.nl

Finally, you provide a short description of the project. This will also
be added to the Python package and the top-level README file::

    [5/5] description (A short description of the project): Hubble project

The created directory structure
-------------------------------

The NWO cookiecutter creates the following directory structure::

    ├── README.md          <- The top-level README.md file for information about the project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── intermediate   <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data set.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── references         <- Related papers, manuals, and all other explanatory materials.
    │   ├── manuals        <- Directory for manuals.
    │   ├── papers         <- Directory for related papers.
    │   └── other          <- Other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   ├── presentations  <- Presentations given about the project.
    │   ├── meetings       <- Updates presented in group meetings, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting.
    │
    ├── env.sh             <- A bash file to contain all the environment variables
    │                         and software sources to run the project.
    │
    ├── src                <- Source code for use in this project (* Git).
    │   │
    │   ├── docs           <- Documentation for the source code.
    │   │
    │   ├── notebooks      <- Jupyter notebooks.
    │   │
    │   ├── <repo_name>    <- Python module for project.
    │   │   │
    │   │   ├── __init__.py   <- Make this directory a python module.
    │   │   ├── scripts       <- Directory to add python scripts.
    │   │   └── functions.py  <- Add your python functions here.
    │   │
    │   └── pyproject.toml <- Python project definition file used to build a python package.
    │
    └── paper              <- Directory to write your paper (* Git/Overleaf).


Data
~~~~

Now that the directory structure is created, we can discuss the contents.
In the data directory you can store your data. These data can be in various
stages of analysis. There can be raw data from an instrument or data
from an external source, from which you derive intermediate data and
end results.

It is usually a good idea to separate the original data (raw or external)
from the processed data. You usually do not want to alter the raw or external
files in any way, so saving them in separate directories avoids accidentally
changing these files.

Subdirectories
''''''''''''''

The data directory contains the following subdirectories:

- external: To store external data,
- raw: To store raw data from the instrument,
- intermediate: To store intermediate data products while processing,
- processed: To store the end results of the processing.

Link to large file storage
''''''''''''''''''''''''''

If your datasets are large, it is best to store them on a disk with high
capacity. You can still include them in this directory structure by creating
a symbolic link. It is best to replace the current directory. For example,
the ``external`` directory needs to be removed before we can make a link to
an existing directory elsewhere. Be careful with the ``rm`` command!

First check whether the external directory is empty::

    user@linux:~/Projects/hubble/data> ls external/

If the directory does not contain anything that you want to keep, then remove it::

    user@linux:~/Projects/hubble/data> rm -rf external/

If we have the external data stored in ``/path/to/storage/external``, then
we can create the new link with the command::

    user@linux:~/Projects/hubble/data> ln -s /path/to/storage/external external

The data will still be available at ``data/external``, but the files will be
physically stored in ``/path/to/storage/external``.

The env.sh file
~~~~~~~~~~~~~~~

Since you probably use a number of external software packages in this
project, it may be a good idea to use ``env.sh`` as a source file to
set all the software packages and environment variables that you need.

In the file, you can source software packages to make them available
in your environment. In addition, you can set project specific variables.
For example, you can set a variable containing the absolute path to
your project directory. You can then read this variable in your Python
programs and use it to find your files relative to this path. This
way, you can move your directory to another system and all you need
to change is the path contained in the environment variable.

For an example, see ``PROJECT_DATA_DIR`` set in ``env.sh``. In
``src/<repo_name>/functions.py`` you can find the ``get_data_dir`` function
which reads and checks the path from ``PROJECT_DATA_DIR``. This
way, you can use the path throughout your package.

Please make sure that your ``env.sh`` file does not end up in
a git repository, or at least make sure that the environment
does not contain sensitive information.

.. admonition:: EXERCISE

   Uncomment the ``PROJECT_DIR`` and ``PROJECT_DATA_DIR`` environment
   variables in ``env.sh`` and change the directory path to your hubble
   project location.

Once you have saved the ``env.sh`` file, you can load the variables into
your environment using the source command::

    (base) user@terminal:~/Projects/hubble> source env.sh

References
~~~~~~~~~~

You can use this directory to save any explanatory materials related
to your project. These can be papers, manuals, and other documents
that are useful to have around.

Reports
~~~~~~~

The reports directory can be used to store all kinds of (intermediate)
reports about the project. From figures that you presented at group
meetings to presentations given at conferences.

Tip for the meeting directory: If you create a subdirectory for each
meeting with the date in ``YYYY-MM-DD`` format (the ISO-8601 standard),
they will be nicely ordered by time in your directory listing.

Source directory (src)
~~~~~~~~~~~~~~~~~~~~~~

In this directory, you can put your Python source code.
It is usually very helpful to create functions or classes
for operations that you use often.

It is very useful to keep this directory under git version
control. This will be discussed in the next section.

The directory is set up in a way such that you can easily
create a Python package. It contains the ``docs`` and
``notebooks`` directories to document the code and provide
examples as jupyter notebooks.

There is a lot to say about structuring a Python project.
If you want to learn more about the dos and don'ts of
structuring Python, you can read this part of the
`Hitchhiker's guide to Python
<https://docs.python-guide.org/writing/structure/>`_,
for example.

Docs
''''

You can use this directory to create source code documentation.
A way to do that is to use the python ``sphinx`` package.

If you are interested, then look at the `Sphinx Quickstart
guide <https://www.sphinx-doc.org/en/master/usage/quickstart.html>`_.

Notebooks
'''''''''

In this directory, you can store jupyter notebooks that you use
to explore the data and visualize it.

Pyproject.toml
''''''''''''''

The ``pyproject.toml`` file describes the properties of your python
package, what packages it depends on and how it is installed. You
can find more information about this file here:
`Write your own pyproject.toml
<https://packaging.python.org/en/latest/guides/writing-pyproject-toml/>`_.

Paper
~~~~~

In the paper directory, you can write your (LaTeX) paper. Many people
use Overleaf these days and it is possible to use git version control
to sync your paper files with Overleaf.

Please see the `Git integration <https://www.overleaf.com/learn/how-to/Git_integration>`_
manual of Overleaf to get your Overleaf project into this directory.

README
------

.. admonition:: EXERCISE
              
   Rename the standard README.md file in the top directory and
   download the template README.md file from `this Github page
   <https://github.com/jdeplaa/open-data-template/blob/main/template/README.md?plain=1>`_.
   This will become our README file for the reproduction package at the end.

File formats
------------

When you store your data or text in files, it is very important that
you do this in `open file formats <https://en.wikipedia.org/wiki/Open_file_format>`_.
There are many ways to encode data
in files, and for the computer to read them, you usually need a special
library or module. For the file format you choose, it is best that that
format has publicly available read and write software. Large tables with numbers
are usually most efficiently stored in binary files, like `FITS
<https://en.wikipedia.org/wiki/FITS>`_, or `HDF5
<https://en.wikipedia.org/wiki/Hierarchical_Data_Format>`_.
Text that needs to be human readable, like READMEs or source code
are stored in `ASCII format <https://en.wikipedia.org/wiki/ASCII>`_.
In all cases, make sure that the files you create are easy to read
by others.

Naming files
------------

Next to a good directory structure, giving your files consistent names
is also very helpful. Checkout the checklist below from `The Turing way
handbook <https://book.the-turing-way.org/project-design/filenaming>`_:

- Name your files consistently
- Keep it short but descriptive
- Avoid special characters or spaces to keep it machine-compatible
- Use capitals, dashes, or underscores to keep it human-readable
- Use consistent date formatting, for example ISO 8601: YYYY-MM-DD to maintain default order
- Include a version number when applicable
- Share/establish a naming convention when working with collaborators
- Record a naming convention in your data management plan (if you have one)
