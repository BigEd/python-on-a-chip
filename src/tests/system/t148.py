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
# System Test 148
# Create configurable Float datatype
#

print "0.0 + 3.0 == ", 0.0 + 3.0
assert 0.0 + 3.0 == 3.0
assert 1.0 + 3.0 == 4.0
assert 3.0 + 1.0 == 4.0

print "0.0 - 3.0 == ", 0.0 - 3.0
assert 0.0 - 3.0 == -3.0
assert 1.0 - 3.0 == -2.0
assert 3.0 - 1.0 == 2.0

print "0.0 * 3.0 == ", 0.0 * 3.0
assert 0.0 * 3.0 == 0.0
assert 1.0 * 3.0 == 3.0
assert 3.0 * 1.0 == 3.0

print "0.0 / 3.0 == ", 0.0 / 3.0
assert 0.0 / 3.0 == 0.0
assert 3.0 / 1.0 == 3.0
assert 3.0 / 3.0 == 1.0
assert 256.0 / 16.0 == 16.0

print "0.0 % 3.0 == ", 0.0 % 3.0
assert 0.0 % 3.0 == 0.0
assert 3.0 % 1.0 == 0.0
assert 3.0 % 3.0 == 0.0
assert 256.0 % 16.0 == 0.0

print "3.0 ** 3.0 == ", 3.0 ** 3.0
assert 2.0 ** 8.0 == 256.0
assert 3.0 ** 0.0 == 1.0
assert 3.0 ** -0.0 == 1.0
assert 3.0 ** 1.0 == 3.0
assert 1.0 ** 3.0 == 1.0
assert 2.0 ** -1.0 == 0.5

print "0.0 and 3.0 == ", 0.0 and 3.0
assert (0.0 and 3.0) == 0.0
assert (3.0 and 0.0) == 0.0
assert (3.0 and 5.0) == 5.0
assert (5.0 and 3.0) == 3.0

print "0.0 or 3.0 == ", 0.0 or 3.0
assert (0.0 or 3.0) == 3.0
assert (3.0 or 0.0) == 3.0
assert (3.0 or 5.0) == 3.0
assert (5.0 or 3.0) == 5.0

print "not 1.0 == ", not 1.0
assert (not -1.0) == False
assert (not 1.0) == False
assert (not 0.0) == True
assert 0.0 == False
assert -0.0 == False
assert 1.0 == True
assert 3.0 == True

pi = 3.141592654
print "pi < 3.0 == ", pi < 3.0
assert (pi < 3.0) == False
assert (pi <= 3.0) == False
assert (pi == 3.0) == False
assert (pi != 3.0) == True
assert (pi > 3.0) == True
assert (pi >= 3.0) == True
assert (3.0 is 3.0) == True
assert (3.0 is 1.0) == False
assert (1.0 is not 3.0) == True
assert (1.0 is not 1.0) == False

print
print "Mixing number types"
print
print "3.0 + 3 == ", 3.0 + 3
assert (3.0 + 3) == 6.0
assert (3 + 3.0) == 6.0

print "3.0 - 3 == ", 3.0 - 3
assert (3.0 - 3) == 0.0
assert (3 - 3.0) == 0.0

print "3.0 * 3 == ", 3.0 * 3
assert (3.0 * 3) == 9.0
assert (3 * 3.0) == 9.0

print "3.0 / 3 == ", 3.0 / 3
assert (3.0 / 3) == 1.0
assert (3 / 3.0) == 1.0

print "3.0 % 3 == ", 3.0 % 3
assert (3.0 % 3) == 0.0
assert (3 % 3.0) == 0.0

print "3.0 ** 3 == ", 3.0 ** 3
assert (3.0 ** 3) == 27.0
assert (3 ** 3.0) == 27.0

assert (3 < 3.0) == False
assert (3 <= 3.0) == True
assert (3 == 3.0) == True
assert (3 != 3.0) == False
assert (3 > 3.0) == False
assert (3 >= 3.0) == True
assert (3 is 3.0) == False
assert (3 is not 3.0) == True

assert 3.0 / 0.0 == 999.0 # Expect ZeroDivisionError (0xE3)
#assert 3.0 % 0.0 == 999.0 # Expect ZeroDivisionError (0xE3)
