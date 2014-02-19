---
title: Astro 585 discussion
layout: post
tags:
- astro585 
---

##What is TLB?
_The translation-look-aside-buffer_ (TLB) is a cache that memory management hardware uses to improve virtual address translation speed.

Issues:

- But then what happens if this buffer isn't big enough?

- The way the TLB works is likely different between different processors.


##_Virtual memory space_ or _Virtual address space_
In the old days when you had only say 2MB of RAM, then you could use a feature called 'Virtual memory space' to simulate that you might actually have 4MB of data. This was came in handy when you were running windows, and running both Word, and Excel at the same time, and both were hogging your memory. So when you alt-tabbed you could actually save the memory on the window that was not being used to disk.

##Using higher level interfaces vs knowing the minute details
_Higher level interfaces:_ **You don't really know what you are doing, but the good thing is, you are much quicker at it!**

##Why are micro commands reordered by the compiler/assembler?
Lets say we are doing the computation: A*B + C
Once you have translated the high-level language to micro-commands; like move this byte over here, and that one over there, you can figure out which ones depend on one another.
And once you have done then the idea is to try to make the hardware try to perform as many operations that it can concurrently, while not breaking any of the dependencies.

<code>
Use the hardware better = performance gains.
</code>

##Memory issues and garbage collection
If you say: _get me this memory_ and your computer gives it to you, you also have the responsibility to _de-allocate it_. 

**Remember:**
- <code>with great memory allocation comes great memory de-allocation</code>

Surprisingly, **a lot of people forget to do the second part** (those people fall in the group of _B-programmers_ or _Bad-programmers_ - a curious lot.

Its probably fine to be sloppy about memory issues if your program only runs for _a fifth of a second_. 
But what if you are running a web-server that you want to run for months without crashing - then memory leaks _really are a bad thing_.

At some point, someone got the idea to take this responsibility away from _bad_-programmers; this was the dawn of _garbage collection_ - then the computer is responsible for de-allocating dynamically allocated memory. 

##Garbage collectors
They do make life easier, but you pay the price of slowing things down. So: <code>you can be sloppy, and not worry about it. </code>

Don't be sloppy though - then you will need to collect less of it!
The bottom line is <code>There is no perfect garbage collector, but some are more equal than others.</code>

In Julia you can disable the garbage collector when you want.
To turn it on: <code>gc()</code>

You can even specify your own memory manager.

##Electric fence
Checkout using <code>efence</code> within <code>gcc</code> to check for memory leaks.

Static variables exist once it is allocated until the program ends.

##Smart pointers
Pointers that contain  information of how many other pointers are currently pointing to that place in memory.

####Bad side:
- Overhead of changing the increment/decrement information

- Can be hard to deal with those if you have a circular linked list. _Solution:_ even smarter pointers??  --> more overhead.




##Constant pointers
In C, C++, Fortran you can define constant pointers. Its a way to tell the compiler that this specific variable will not change over the course of the program.

The reason Fortran used to be much faster than C was due to <code>aliasing</code>.

##Static vs Dynamic memory allocation
####Static
- Then you know up front the size of the memory you want to allocate.

- If you only use this, you are probably very unlikely to run into memory leaks.

- The memory can be allocated to the stack if it is small enough, but a reasonable compiler would allocate it on the heap if it is realatively big. Only small enough statically allocated variables are allocated on the stack, but can the stack dynamically grow?

- Garbage collectors do not work on the stack.

####Dynamic 
- Then you don't know up front the size of the memory you want to allocate.


