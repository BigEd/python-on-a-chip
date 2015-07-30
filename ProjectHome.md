Welcome!  Python-on-a-Chip (p14p) is a project to develop a reduced Python virtual machine (codenamed PyMite) that runs a significant subset of the Python language on microcontrollers without an OS.  The other parts of p14p are the device drivers, high-level libraries and other tools.  Please join the [python-on-a-chip google group](http://groups.google.com/group/python-on-a-chip) to discuss this project.

Latest news:

  * 2011/09/26 Mentioned on [Leaf Labs blog](http://leaflabs.com/2011/09/pymite/) and then [Hack-a-day](http://hackaday.com/2011/09/26/python-on-a-microcontroller/)
  * 2011/03/24 [Maillist](http://groups.google.com/group/python-on-a-chip) membership surpasses 256.
  * 2011/03/12 [PyCon 2011 Lightning Talk](http://pycon.blip.tv/file/4884752/) (begins at 3:45 in the video) and [the slides](https://docs.google.com/present/edit?id=0AeQVZstbmezwZGd2dDZ3czhfMDhuZ3E3d2Ri&hl=en)
  * 2010/12/26 ([716cef81d103](http://code.google.com/p/python-on-a-chip/source/detail?r=716cef81d103)) Added support for iterating over a dict "for _keys_ in _dict_", summing the keys of a dict, unpacking a dict's keys, summing a bytearray.
  * 2010/10/20 SCM transitioned from subversion (svn) to mercurial (hg).
  * 2010/10/18 ([8ae4b86461c9](http://code.google.com/p/python-on-a-chip/source/detail?r=8ae4b86461c9)) P14p Release 09
  * 2010/09/29 ([8fa5983193ae](http://code.google.com/p/python-on-a-chip/source/detail?r=8fa5983193ae)) New platform: [MoSync](http://www.mosync.com/).
  * 2010/09/01 ([1bdb8d31f27b](http://code.google.com/p/python-on-a-chip/source/detail?r=1bdb8d31f27b)) New platform: [Arduino Mega](http://arduino.cc/en/Main/ArduinoBoardMega).
  * 2010/08/24 ([1266c8fc40ff](http://code.google.com/p/python-on-a-chip/source/detail?r=1266c8fc40ff)) New platform: [RedBee EconoTAG](http://redwirellc.com/store/index.php?route=product/product&product_id=56) 802.15.4 wireless module.
  * 2010/08/11 ([85b9a8ccf5d6](http://code.google.com/p/python-on-a-chip/source/detail?r=85b9a8ccf5d6)) New platform: [Teensy++ 2.0](http://www.pjrc.com/teensy/)
  * 2010/07/23 ([7caf29a7c370](http://code.google.com/p/python-on-a-chip/source/detail?r=7caf29a7c370)) New platform: [Microchip PIC24/dsPIC](http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&nodeId=2629&param=en533465)
  * 2010/06/24 ([ec4034b23bff](http://code.google.com/p/python-on-a-chip/source/detail?r=ec4034b23bff)) New feature: Bytearray: packet = bytearray(128); b = bytearray(b"abc")
> (looking for [older news?](http://code.google.com/p/python-on-a-chip/wiki/OldNews))

Features of the PyMite VM:

  * Requires roughly 55 KB program memory
  * Initializes in 4KB RAM; print "hello world" needs 5KB; 8KB is the minimum recommended RAM.
  * Supports integers, floats, tuples, lists, dicts, functions, modules, classes, generators, decorators and closures
  * Supports 25 of 29 keywords and 89 of 112 bytecodes from Python 2.6
  * Can run multiple stackless green threads (round-robin)
  * Has a mark-sweep garbage collector
  * Has a hosted interactive prompt for live coding
  * Licensed under the GNU GPL ver. 2

The PyMite VM DOES NOT HAVE:

  * A built-in compiler
  * Any of Python's libraries (no batteries included)
  * A ready-to-go solution for the beginner (you need to know C and how to work with microcontrollers)

The [release](http://python-on-a-chip.googlecode.com/files/pymite-09.tar.gz) can be downloaded from the **Downloads** tab above.  However, we recommend checking out the head of the mercurial repository.
