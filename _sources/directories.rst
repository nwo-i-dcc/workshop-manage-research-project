.. _sec:directories:

Project directory
=================

Choosing a place for your project directory
-------------------------------------------

One of the first choices that you need to make is where you create your project directory. There can be several
factors that you need to take into account here:

- At which location will I work mostly?
- Will I need a lot of computation resources later?
- How are back-ups arranged for the location where I store my files?
- Does the IT department of my institute have preferences where I store my files?
- How much disk space will my project need?

These are all important questions, but you may not have all the answers when you start a project. We will discuss
these questions below, but if you are still unsure what to do, feel free to ask your supervisor or one of the data
stewards for advice.

General recommendations
~~~~~~~~~~~~~~~~~~~~~~~

We strongly recommend to store important files, such as your project directory, on institute servers
(more about these later). These servers are protected against hardware failure and some are also backed-up daily.
By storing data on institute servers the chance that you loose your data is smaller.

If storing your data on institute servers is not an option for you, then please make sure that you have a
backup hard drive that you use to back up your files regularly. You can ask ICT or the data stewards for advice.

.. note:: Apple Time machine can be a good backup solution, but keep in mind that your backup is stored on disk
          with permissions that only allow your user account to access them. In case your laptop breaks down,
          you need to load your entire user account on a different laptop to have access to your data again.

Working remotely
~~~~~~~~~~~~~~~~

The place where you work mostly probably depends on where you live and at which institute you are based.
If you live nearby and you have a desk at the institute to work on, you may do most of your work there.
If you live further away, chances are higher that you do most of your research on a laptop.
A mix of the two is also possible.

What are the tools that can help you to work remotely? And what are their advantages and disadvantages?

- **Owncloud/SURF drive**: Owncloud and SURF drive are a cloud service similar to Dropbox or Google Drive.
  You can download an app that synchronises your local owncloud directory with the one on the
  server. This way you can work locally in a folder, but have the same files available on multiple machines. Take care,
  however, that when you delete something, it is also deleted automatically on your other devices.

- **Remote desktop**: Institutes usually offer remote desktop solutions for Windows and Linux. These allow you to open a screen
  of a Windows or Linux machine at the institute on your own laptop and work on it. You need a VPN connection for this.
  The remote desktop app allows you to use the institute machine remotely, which means all the files are stored at the
  institute and process will also run there. Your laptop is just used as a way to connect to the remote machine.

- **SSH login**: Similarly, it is possible to connect to Linux machines through a terminal and even start graphical
  programs through SSH. This also requires you to have a VPN connection. Since this does not transfer the whole
  desktop of the remote machine, this usually works faster on slow connections. Knowledge about the Linux terminal
  is required though.

Computational resources
~~~~~~~~~~~~~~~~~~~~~~~

If you expect to need a lot of computational power to do your analysis, it is probably better to store your data
files in a place on the institute network where it is accessible from all computers. In that case, it is also
helpful if your software and/or scripts are also available on the network. Please ask your colleague or 
data steward which disk is best for you.

Storage space
~~~~~~~~~~~~~

The local harddrives of desktops and laptops usually have space for >100 GB of data and sometimes even a couple of TB.
Many institutes have large shared storage on the network available. For most applications, this is enough. If you think 
that you need more, then please ask your local data steward or ICT support contact.

Please ask your data steward or your ICT department as well about the backup policy if you want to use a network disk. 
You want your data to be safe, but on the other hand, making a backup of large datasets is costly and time consuming. 
The ICT department may have preferences where you store large datasets, so please follow them. There is a trick to 
have your data in the project directory tree and on another disk at the same time. To do this, you can create a symbolic 
link. This will be explained in the next section.

Conclusion
~~~~~~~~~~

- The best place for your project directory is your home directory. However, depending on the setup at your institute
  it may not be the best place to store large datasets. Please follow the instructions of your local ICT department.
- If you need to have your project directory available on your laptop, then you can consider creating this directory
  on an owncloud or SURF drive folder. This way you can share your project files between devices and benefit from a 
  backup. Note that your owncloud or SURF drive folder is limited in size and may not be suitable for very large datasets. 
  Also, keep in mind that if you delete something, the automatic synchronisation will also delete it on all your other 
  copies. 



