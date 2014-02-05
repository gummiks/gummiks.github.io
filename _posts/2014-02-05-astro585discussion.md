---
title: Astro 585 discussion
layout: post
tags:
- astro585 
---

<code>Bottom lines:</code>

* **Profile your code!**
* If you are going to be running a code a lot - **benchmark it.**

##Worrying about hardware?
Not so much. The thing is: in a few years you will be running your code on a different chip on a different system, maybe somewhere on the cloud. So at this point, don't worry too much about the low level hardware side of the coding. Moreover, ignore _RISCs_ and _CISCs_ - except if you are planning on buying a supercomputer!

##When should we use vector processors?
The most common vector processors today are graphics chips. 
If you are doing the same operations on the same data again, and again, and again, then you might be better off using a graphics card, letting it perform these operations. It is not uncommon to get around 2x performance or more that way, with little effort.

Make your compiler optimize for your computer? 
Can get around 10x performance.

##Jobs on a supercomputer
**If the supercomputer is homogeneous**, i.e. has the same type of chips as computing nodes, then it might be very advisable to compile your code for that exact chip. It might just be worth your while to spend those 5 minutes reading that <code>man</code> page to check what flags you need to use in order to optimize the code, to get that performance increase you are looking for!

**If your supercomputer is heterogeneous**, i.e. has different types of chips as computing nodes, some AMD over here, and some Intel chips over there. Then you have to two choices:

1. _You compiled it and optimized it for one particular chip._ Then it won't run on the other types (it will probably crash!). The code might run faster, but you might just be spending your time waiting in the que line!

2. _You compiled it more generally, not optimizing for a particular chip._ Then the code will probably run slower, but you'll be quicker out of the queue line!


##Real world testing vs micro-benchmarking
_Where you are blazingly fast at multiplying a bunch of numbers, but Microsoft Word performs differently._








##More about caches
In practice a computer has multiple cache levels.
Normally what you do is specify the L2 cache size, as the L1 is usually more constrained in size, and sometimes you see the effect of the computer moving data around in these different levels.

####Can cache sometimes be too big - so that it might actually slow you down?
Yes, this applies to L1 caches. For a larger cache it is harder to have a fast clock speed; it takes longer to move electrons over a bigger distance, than a smaller distance.

####Is there an optimal ratio of processor clock speed, and cache size?
**_Yes, the fastest, and the biggest L2 cache size!_** Well, still its not exactly that simple. The chip manufacturers are kind of trying to figure this out for you - they want to make chips that people buy. 

**Example (see graph in last class)**:
If I were to go from 2mb to 8mb in L2 cache size, the range of which it took the same amount of time while still increasing the data size steadily, would probably be around 4 times as big (see graph in last class).


##Using SSD drives - does it mean performance increase vs. using magnetic disks?
**It depends on what you want to do.** 

<b>For sequential reading, and sequential writing</b> the old magnetic disk actually perform quite well with respect to the SSD drives (the platter is reading of a very fast spinning disk), and the old fashioned ones are still a cheaper option if you are working with huge amount of data.

<b>However, for random reading</b> the old fashioned disks are much slower, while SSD are much better - physically moving things like the platter needle in the old hard drives is much slower than moving electrons around in an SSD.

##Are there hybrid systems, that combine a normal processor, and a vector processor?
Yes, there are; usually it is a CPU processor, bundled with a graphics co-processor.

##Two different parallelisms
####Structure-level-parallelism
When you can have your code such that is making use of __structure-level-parallelism__; you can get the benefit of the hardware doing different instructions at the same time - meaning performance increase via pipelining.

####Data-level-parallelism
Write your code so that is easy for the compiler to find ways to do **data-level-parallelism.**
Modern compilers, have instruction level cache, and are constantly trying to figure out how they can use its computation units effectively. They break the instructions into smaller chunks, and try to order them in a smart way.

Write the working set data small enough so that it can fit into the cache - this way you can potentially get an increase the performance several times.

##When optimizing - optimize the slowest part!
Still you have to be aware that the total execution time will still depend on all the parts of the program. _For example:_

* You have a program that is 10 parts, each of which takes 10% of the time to run. You choose one part to optimize, making it effectively free to perform. - _This way, you only make the program 10% faster._

* You have a program that is 10 parts, where one of the part takes 90% of the time to run. You choose this part to optimize, making it effectively free to perform. - _This way, you make the program 10x faster!_

##Branch predictions
Pretty cool way to make your compiler to work for you - <code>Need to look better into this!</code>
You can speed things up by reducing the instructions performed on your branch.
Still sometimes the only thing to do is: _compile, and compile, and hope!_
