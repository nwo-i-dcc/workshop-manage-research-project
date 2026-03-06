.. _sec:repro:

Reproduction package
====================

Now that we have fitted the data and wrote down the results and conclusions
in the paper, we can start creating a reproduction package to help others
check our results or benefit from the work that we have done.

A reproduction package is a collection of relevant data files, scripts
and documentation that accompanies a scientific paper. This package should
be published in a trusted repository, like Zenodo.org.

In this workshop, we will use the `Zenodo sandbox <https://sandbox.zenodo.org/>`_
where we can do uploads without contaminating the repository. The Zenodo
sandbox works exactly the same as the real Zenodo, but the uploads are regularly
deleted.

A template for a reproduction package (including a checklist) can be found
`on Github <https://github.com/jdeplaa/open-data-template>`_. It is not compulsory
to use this. The important thing is that the package contains well documented
and useful data.

FAIR principles
---------------

When creating and publishing data, it is good to think about the FAIR data
principles. FAIR stands for:

- Findable
- Accessible
- Interoperable
- Reusable

The first two, findable and accessible, mean that you need to put the data in
a place where people can find and access it. This is why we pick a public
repository like Zenodo.

The last two mean that we should use programming languages and data formats that
are easy to run for others. Python is an open source language and it is not
necessary, for example, to buy a license. The FITS format is an open format
that is well described by NASA and has good library support. This makes sure that
other people can reuse the data.

Creating the package
--------------------

To reproduce our Hubble result, other people would need our data and scripts.
We have the following list:

- ``data/hubble_data.fits``
- ``src/hubble``, including hubblequery.py, hubblefit.py, etc.

In the :ref:`sec:structure`, we have already created a new README.md file in the
top level directory of our project. It should already contain some information
about how to run the scripts.

.. admonition:: EXERCISE

  Fill out the remaining relevant sections of the README.md file.
  The most important items are the software dependencies, a description of the
  scripts and how to run them, and a short description of the data. Do not forget
  that people need to set the PROJECT_DIR and PROJECT_DATA_DIR variables.

When the README.md file is updated, put the data file and scripts in a tar.gz file.
This is a really small project, and we will make only one file. If your project
is larger, you can also decide to create separate packages for the data, scripts,
and figures.

Next, we create the tar.gz file and it is important to leave out the README.md::

    user@terminal:~/Projects/hubble> tar cvfz hubble.tar.gz data/hubble_data.fits src/hubble


Upload to Zenodo
----------------

Go to `sandbox.zenodo.org <https://sandbox.zenodo.org>`_ and log in with your
sandbox account. On the top right of the page you can now click the `+` symbol
and choose 'New upload' from the drop-down menu. This will open a new upload form.

.. note:: If you are doing a real upload, please add the community of your institute
          to the form. The button for this is all the way at the TOP of the form!


Upload the files
''''''''''''''''

In the files section, you can upload the ``hubble.tar.gz`` file and the ``README.md``.
The reason that we upload the README.md separately, is that Zenodo will show the README.md
file as a preview for the package. This way, people will see the README.md already on screen 
before they download the package.

Basic information
'''''''''''''''''

The basic information section is rather straightforward. In almost all circumstances it
is the best to reserve a `DOI <https://en.wikipedia.org/wiki/Digital_object_identifier>`_. 
Only if the journal provided you with a specific DOI for 
the dataset (not the paper!), you need to provide that one instead. So, choose 'No' and
click to reserve a DOI.

Choose the resource type 'Dataset' and fill out the title of the paper. If you want,
you can copy a relevant paragraph from the paper as description. 

The license can remain 'Creative-Commons Attribution 4.0 International', it is usually
a good standard choice. If you have a lot of code, it may be better to apply a `software
license <https://choosealicense.com/>`_ to that part of the package. Also, it is
important to respect the licenses of other codes if you use external packages. This
can be complicated in certain cases, so if you are in doubt, please discuss it
with your data steward.

Other information
'''''''''''''''''

As you can see there is a lot of other information that you can add. For this workshop,
most are irrelevant, but once you do this for real it is good to provide as much
additional data as you can. These metadata can also be added to the upload later, so
do not worry if something needs to be added later. Only the datafiles cannot be altered
after the upload is finished. When your data files change, it is possible to upload a 
new version of the publication.

The more relevant metadata that you can add, the easier it will be for people to find
your data and reuse it. So, try to be as complete as you can.

Go back to the top-right of the form where you can 'save', and if you are finished 'publish'
the package.

Additional options
''''''''''''''''''

By default, your new upload is visible to everyone. However, there could be circumstances 
where you want to release the data later. In those cases, you can either set the upload to
'Restricted' instead of private, or apply an embargo date.


The data availability section
-----------------------------

Now that we have a Zenodo upload, including DOI, we can go back to our paper and fill out
the data availability section. 

A good data availability section contains the following information:

- A brief description of the raw data and software used and where they can be found (ESA/NASA archive?). 
  Please also include the version number of the software.
    
- A brief description of the final data products (images, spectra, lightcurves, etc.), the scripts 
  that were used to generate them, and where they can be found. Preferably, these should be in a 
  reproduction package that has been uploaded to a repository (Zenodo) and has a DOI. 
    
- Do not forget to cite the reproduction package (with DOI) in the references section! 
  If the DOI is available in the references, then it is machine readable and it will appear, 
  for example, also as a publication in ADS.
    
- If there are access conditions for your data and scripts, explain why they are there and 
  how to get access. This also holds for embargo's.
    
- Mention the license which applies to your reproduction package.
    
- If you use separate software packages, describe them briefly and cite them using either 
  a DOI, ASCL reference or paper. Citing the Github page is nice, but may not be available 
  on the long term. It is anyway good scientific conduct to cite the work of others, also software work.
  

For our package, we can at least write a sentence that the data is available at Zenodo.
We can even make a citation! If you go to your upload at Zenodo and scroll down to the
'Export' block on the right side. There you can select 'BibTeX' from the drop-down menu
and download the citation directly in BibTeX format! You can copy the citation to
the ``hubble.bib`` file and cite the Zenodo upload in the data availability section.


Congratulations!
----------------

You have gone through a small research project and shared your data and scripts!
Your real research projects will be significantly larger, but hopefully the 
suggestions in this workshop will help you to keep things organised. 

If you want to learn more about project design and how to work in a
reproducible way, take a look at `The Turing way handbook
<https://book.the-turing-way.org/>`_.

Good luck with your own research project!!! 
