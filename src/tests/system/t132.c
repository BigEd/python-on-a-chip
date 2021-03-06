/*
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
*/

/**
 * Test for Issue #132
 *
 * VM doesn't throw TypeError 
 * when function has wrong number of arguments
 *
 */


#include "pm.h"

#define HEAP_SIZE 0x2000

extern unsigned char usrlib_img[];


int main(void)
{
    uint8_t heap[HEAP_SIZE];
    PmReturn_t retval;
    
    retval = pm_init(heap, HEAP_SIZE, MEMSPACE_PROG, usrlib_img);
    PM_RETURN_IF_ERROR(retval);

    retval = pm_run((uint8_t *)"t132");
    C_ASSERT((int)retval == PM_RET_EX_TYPE);
    if (retval == PM_RET_EX_TYPE) return (int)PM_RET_OK;
    return (int)retval;
}
