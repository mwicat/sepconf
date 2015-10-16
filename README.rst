Sepconf
=======

Sepconf is little script that can help you if you want to automatically generate 
a PBX configuration file for a number of devices e.g. for testing purposes.

Currently supported configuration formats are Freeswitch and Asterisk, so you can feed the
script with either `freeswitch.tmpl` or `asterisk.tmpl`. Template will be first searched in your
current working directory and then in package's `data/templates` directory.

Installation
------------

To install using `pip`::

	sudo pip install -e git+https://github.com/mwicat/sepconf.git#egg=sepconf

Getting started
---------------

To generate 2x Cisco 7940 devices and render configuration file in one step::

	sepconf generate 2 --phone=7940 --render=freeswitch.tmpl

Output::

	[SEP000000000000](7940)
	description = User 1
	button = line, 1001
	
	[1001](defaultline)
	label = 1001
	cid_name = User 1
	cid_num = 1001
	
	
	[SEP000000000001](7940)
	description = User 2
	button = line, 1002
	
	[1002](defaultline)
	label = 1002
	cid_name = User 2
	cid_num = 1002

To generate 2x Cisco 7940 devices and save them to CSV file::

	sepconf generate 2 --phone=7940 > phones.csv

Contents of `phones.csv`::

	SEP000000000000,User 1,7940,1001
	SEP000000000001,User 2,7940,1002

To render devices from CSV file::

	sepconf render freeswitch.tmpl < phones.csv
