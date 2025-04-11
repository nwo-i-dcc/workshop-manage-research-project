.. _sec:git:

Git version control
===================

Git is a program to track changes in text files, and is therefore very
useful in source code development. It saves intermediate versions with
comments, allowing you to go back to an older version of your code,
without saving several copies of it.

In the NWO cookiecutter template, there are two directories that
can benefit from version control: ``src`` and ``paper``. The ``src``
directory contains your Python source code and notebooks. The ``paper``
directory can be used to host your LaTeX paper project. In this Section,
we concentrate on the ``src`` directory.

How git works is explained in the `Carpentries version control
<https://swcarpentry.github.io/git-novice/>`_ workshop.

Initialize Git for the src directory
------------------------------------

To start using version control for this directory, you can give the
commands below. Make sure that you are in the ``src/`` directory
before you give these commands::

    git init
    git add .
    git commit -m "Initialise git for the project"

From now on, the source directory is under version control.

Upload your local repository (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the main advantages of git is that you can upload your repository
to a server. This is helpful as backup, but it also allows you to collaborate
with others. We will assume here that we just upload to Github for
backup purposes and personal note taking.

Since you have an existing ``src`` directory already, you need to create
an empty project on `github.com <https://github.com>`_. If you do not want to share your
software with others (yet), then make sure that you create a private
repository. **Uncheck** the option to create a README file when you create a new
project. Once your Github project is created, you can add
the URL to your local git repository::

    git remote add origin git@github.com:/your_project.git
    git push -u origin main

Github have certain security measures in place to protect
against unauthorized uploads. For SSH access, an `SSH key should be created
<https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?tool=webui>`_
and added to your account. If you want to connect through HTTPS, then
you need to `create special access tokens
<https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>`_
You can ask your data steward if you have trouble pushing your changes to
the online repository.

Setting up the Github project
-----------------------------

Although we do not go into this further in this workshop,
you can read more about setting up a Github project
in "The Turing way handbook" in the section `version control
<https://book.the-turing-way.org/reproducible-research/vcs#>`_
and `Creating project repositories
<https://book.the-turing-way.org/project-design/project-repo>`_.
The last section is especially helpful if you are going to
work on the software with collaborators.

