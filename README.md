ipgettercarlos
=========

About
=========
Still has no Python 3 support.
This module is designed to fetch your external IP address from the internet.
It is used mostly when behind a NAT.
It picks your IP randomly from a serverlist to minimize request overhead on a single server

If you want to add or remove your server from the list contact me on github

Copyright © 2014 phoemur@gmail.com
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.

Im not Sam Hocevar but I edited it a bit to make it work universally i think or just for my set up.

API Usage

    >>> import ipgetter
    >>> myip = ipgetter.myip()
    >>> myip
       '8.8.8.8'
    >>> myip = ipgetter.myiptest()
    	#will print out a lot of things that tests serverlist


SHELL Usage
=========

no support lol

Installation
=========

	# pip install ipgettercarlos

Or download the tarball:
	
	#python setup.py install

Changelog
=========

0.1 (2014-09-29)
 * changed urllib dependancy to request
