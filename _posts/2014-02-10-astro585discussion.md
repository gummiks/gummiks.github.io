---
title: Astro 585 Discussion 4
layout: post
published: false
tags:
- astro585
---

<code>Bottom lines:</code>

##Homework notes

####Git 

+  Went well - some people had 40 commits!

####HDF - IO

+ The overhead associated with it can be significant for small file sizes, but for bigger file sizes, it starts to get negligible.

+ If anyone finds that it is faster to print out to STDOUT rather than to a file - let me know!

<pre>
	function df_hdf_load(N::Int)
</pre>


##Difference between unit tests and regression tests

####Unit tests
- Making sure that one function works

####Regression tests
- Combine writing and reading; making sure that they are inverses of each other


###Using try - catch
An _IF_ statement can also work if you know how it can fail

What _Try and Catch_ is throwing an exception. Its a way to see if the program says: _"Hey! There is a problem here!"_ - Then if you don't have a _Try-Catch_ clause your program will crash.

The advantage of Try-Catch is that you can catch some errors that are buried deep down maybe. However, its a much more expensive way to deal with a problem, rather than using an IF statement.

Its for things that don't have a clear order. It doesn't really happen too often in scientific programming.
Good places to use would be in I/O, and networks.

Still, with an IF statement, then you can 

###Project Proposals
_Don't choose anything obnoxious._ Spend time up front to make your life a lot easier.

Do a small project well, rather than a lot of stuff quick and dirty.
Still, not trivially annoying.

Dealing with inevitable weirdness. 


#Basic optimization techniques for serial code

###Ideas for simple optimizations

+ Don't call your functions too often

+ Pass pointers rather than by reference

++ Know what your computer is doing - don't accidentally 

+ Providing types at compile-time

+ If using an interpreted language: Vectorize!

+ Reduce branching



###Loops
Compilers can be smart, and can speed up one-dimensional loops.
They have a harder time to figure out of how to make nested loops faster.


Sometimes 


##Should we optimize serial code first, before parallelize it?
It kind of depends on your problem.

They key is to think about: "How are you gonna parallelize it"

If its embarrassingly parallel - basically distributing the serial code to a lot of workers. Then it might be better to 

Then you can also go into the idea of parallelizing  at multiple levels.

Not a simple answer to it really but. 

###Defining Custom Types
Linear Transit Ephemeris
