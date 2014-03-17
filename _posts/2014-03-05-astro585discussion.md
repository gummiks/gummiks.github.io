---
title: Astro 585 Discussion 11
published: false
layout: post
tags:
- astro585 
---

##Scientific computing, openMP, and MPI

Reduction

map, and mapreduce

##openMP
A very small number of reduction operations

You can set the number of chunk size

Overhead of starting and stopping, penalty of waiting for synchronization


##nowait
Putting a nowait doesn't help you always. In only matters if there is some useful work to be done.
Usually you would want to combine this with <code>dynamic scheduling</code>.

When you set a dynamic scheduler you are saying: "I need to get this work done; who is available?"
The compiler doesn't know which worker will finish first - so it can't set a static schedule that 

####Sparse matrix
You only store the values that are non-zero.
The time operations on the matrix will take will heavily depend on the number of values that are non-zero. 


##When should you parallelize?
Only parallelize code if investing that time will be likely to pay off.

##100 single processor jobs vs 1 job with 100 processors in parallel
I have parallelized the work in the courses way possible, and now it is actually much much faster in the scheduling.
Write scripts to scedule the jobs, and check how they are doing.


##Race conditions
You have multiple processors trying to read, and write to the same place in memory.
When you are so used to serial coding, it takes a while to be awere of these types of issues.


####Locks
With every variable you can associate another variable which tells you if somebody is modifying the former variable or not.

Rather than you implementing yourself, it is better to use <code>atomic</code>.

Atomic types are very useful, as they prevent you from having to use barriers.

##Prefix sums
You actually don't want this that often in scientific computation.

PREFIX-sum operations can be parallelized this way
The last element in the array is the  


##Parallizing dependencies 
If you have 

Reduce the number of dependencies, and try to implement the algorithms that take advantage of caches, and removes the dependencies

##Nested loops
openMP will give you correct results for this, but it might not parallize well.
You might have to give it guidance on how to parallelize it.


##Prototype
Go with the one that works best


##
If you recognize that you have a variable of the parallelization like _chunksize_, and you don't know what 

<code>It was more complicated to explain what to do, rather than actually performing the work.</code>





