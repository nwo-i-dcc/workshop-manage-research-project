.. _sec:intro:

Introduction
============

Motivation
----------

When you start up a research project, you do not always think a lot about how to organise it on your computer.
Especially when it is your first time, you start with an empty project directory somewhere. During the course
of the project, this directory grows organically. While you are exploring side steps, you also tend to create
(temporary) directories elsewhere as well. Sometimes these sidesteps turn out to be useful, but often they turn
out to be failed experiments.

As the project moves along, you may feel several times that the structure that you chose in the beginning
was not so practical after all. It becomes harder to keep an overview of everything you have done, and what
part of it is useful. By the time you are writing the paper, finding back which versions of your result files
and scripts produce the right results can be a challenge. This will also make it time consuming to create a
reproduction package.

If you recognise yourself in the text above, do not worry. You are not alone! This happens to everybody.

This workshop is intended to help you structure your research project, and teach you tools and tricks
that can help you to keep an overview of what you have done.

How you work and how you like to organise things is very personal. Just think about how differently people
organise the stuff in their kitchen. There is no right or wrong here. This workshop is all about offering
you tools and methods that can help you find the organisational structure that works for you.

What will we do during the workshop?
------------------------------------

We will repeat the analysis of Edwin Hubble when he discovered the expansion of the universe in 1929.
For this project, we will create a new project directory structured following
a cookiecutter template and go through the process of a research project, from collecting the data
to publishing a reproduction package. The focus is not so much on programming, but more on learning
tips and tricks to organise your project in a practical way. 

Sections and timing
-------------------

Based on practical experience, we estimate the following times needed to teach each section:

===================== ===============
Section               Time (min)
===================== ===============
Introduction          5
Project directory     15
Directory structure   70
Git version control*  10
Data analysis         60
Producing a paper*    TBD
Reproduction package  30
**Total**             **190** (3:10)
===================== ===============

\* These sections can be skipped/shortend to save time

What do you need before you start?
----------------------------------

Computer/laptop with Python
'''''''''''''''''''''''''''

You will need a laptop with Python installed, including a couple of Python packages:

- astropy
- astroquery
- build
- matplotlib
- cookiecutter

You can either use the native Python installation of your operating system and install these packages
with ``pip``::

    pip install astropy astroquery build matplotlib cookiecutter
    
or install these packages in anaconda::

    conda install astropy astroquery build matplotlib cookiecutter

LaTeX (optional)
~~~~~~~~~~~~~~~~

A LaTeX installation would be very helpful. On Linux systems you can install LaTeX through the package manager
of the distribution. On Mac, you can either install `MacTeX <https://www.tug.org/mactex/mactex-download.html>`_
or install latex through homebrew or macports.

If you do not want to install LaTeX, you can alternatively create an account on `Overleaf <https://www.overleaf.com/>`_
and/or log in to Overleaf using ORCID (see below in the section 'Useful accounts').

Jupyter (optional)
~~~~~~~~~~~~~~~~~~

The exercises in this workshop can be done without jupyter. Only a terminal window is necessary. However, if
you like programming in a jupyter notebook, then you can use it.

Git (optional)
~~~~~~~~~~~~~~

We will briefly touch upon using version control for your software and paper. The most
popular version control system is git. This program is usually installed by default
on Mac and Linux, but on `Windows it needs to be installed <https://gitforwindows.org/>`_.

Useful accounts
'''''''''''''''

The workshop recommends a couple of web services. If you are planning to publish a paper or any other relevant materials,
having an ORCID would be great, but not strictly necessary. Using ORCID you can also log into Zenodo and Overleaf. 


ORCID (Optional)
~~~~~~~~~~~~~~~~

`ORCID <https://orcid.org/>`_ originated as a method to identify individual scientists with a numeric identifier, 
to avoid confusion with names. Once you have an account, you can add information about your publications and career, 
like a CV. This information is (partially) public. In addition, an ORCID account provides access to a lot of 
other scientific web services. 

Please only create an account there if you are or intend to be a publishing scientist not
to pollute the ORCID database with unused accounts.

ORCID is especially helpful if you want to log in to Overleaf or the real Zenodo.


Zenodo sandbox account
~~~~~~~~~~~~~~~~~~~~~~

The `Zenodo Sandbox <https://sandbox.zenodo.org/>`_ is a copy of the official Zenodo website that can be used for
testing. It is best not to connect your ORCID to this one and create a seperate account. This account will also be 
deleted after a while, just like all the uploads. Create this account just before the workshop starts.


Overleaf
~~~~~~~~

`Overleaf <https://www.overleaf.com/>`_ is an online LaTeX editor to prepare papers and collaboratively work with
other scientists. With this webservice, it is not necessary to install LaTeX on your local machine. You can get a 
limited free account, which can be linked to your ORCID. Git access requires a paper created by a paid account.
