# Frequently Asked Questions #

## What is p14p? ##

"p14p" is shorthand for Python-on-a-chip  (fourteen characters between the first and last "p".

## What processors are supported? ##

Look in `src/platform/` to see the list of platforms that are supported.

## How much RAM is necessary? ##

At least 5 KB to initalize, 8 KB to do something small and more KB if your goals are lofty.

## I just built the latest release, why does it fail? ##

Please use the latest code from the repository rather than the releases.  The release is showing its age and many bugs have been fixed in the repository.

## Why does this simple for-loop fail? ##

```
for i in range(1, 10000): 
  print i 
```

The `range()` function creates a List with the given number of integers inside it.  That list and its contents are consuming all the available RAM.  Use `xrange()` or `while()` with a counter instead.

## Does p14p have an interactive prompt? ##

Yes, we call it "interactive pymite" or `ipm` for short.

## What modules are available? ##

The modules that are available are the .py files in `src/lib/`.  The modules that get compiled into the binary are defined by the variable `PMSTDLIB_SOURCES` in `src/vm/Makefile`([r09](https://code.google.com/p/python-on-a-chip/source/detail?r=09)) or `src/vm/SConscript` (v10).

## How do I access C libraries? Ho do I write native functions? ##

Hints:
  1. Follow examples in `src/lib/__bi.py`
  1. Use `NATIVE_` macros to access function parameters.
  1. Set the Python return value as the top-of-stack using `NATIVE_SET_TOS()`
  1. Your C function should return a `PM_RET_EX_` if an exception occurs or `PM_RET_OK` if everything was good.

Here are the macros used inside native functions to access the things that are useful:
```
/** pushes an obj in the only stack slot of the native frame */ 
#define NATIVE_SET_TOS(pobj) (gVmGlobal.nativeframe.nf_stack = (pobj)) 
/** gets the nth local var from the native frame locals */ 
#define NATIVE_GET_LOCAL(n) (gVmGlobal.nativeframe.nf_locals[n]) 
/** gets a pointer to the frame that called this native fxn */ 
#define NATIVE_GET_PFRAME()   (*ppframe) 
/** gets the number of args passed to the native fxn */ 
#define NATIVE_GET_NUM_ARGS() (gVmGlobal.nativeframe.nf_numlocals) 
```

## Does the PyMite VM have a GIL? ##

No.