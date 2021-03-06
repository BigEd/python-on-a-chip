# This file is Copyright 2003 Dean Hall.
#
# This file is part of the Python-on-a-Chip program.
# Python-on-a-Chip is free software: you can redistribute it and/or modify
# it under the terms of the GNU LESSER GENERAL PUBLIC LICENSE Version 2.1.
#
# Python-on-a-Chip is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# A copy of the GNU LESSER GENERAL PUBLIC LICENSE Version 2.1
# is seen in the file COPYING up one directory from this.

#
# System Test 119
# Print Python traceback on exception
#

def divzero(n):
    print "In divzero"
    a = n/0

def foo():
    divzero(42)

def bar():
    foo()
    
def baz():
    bar()

if ismain():
    print "calling baz()"
    print "Expecting a ZeroDiv exception and traceback to print"
    baz()  # expect exception and traceback
