---
title: Astro 585 Discussion 9
layout: post
published: false
image1: /img/<+imagename+>
image1title: <+title+>
image1subtitle: <+title+>
tags:
- astro585 
---

##What if 

##


##Example: N-body integration and parallize

Integrate each system either for a 



Integrate for 


##Working with a lot of initial condidions
When you have a lot of initial conditions and 

####SIMD
**Single Instruction Multiple Data**
This literally means that at every clock cycle all of the processors are doing the same operation.

####SPMD
A little looser: e.g. one processor has this branch of an if statement, and another took the other branch.
They have the same program, but the exact set of detailed instructions that they actually perform might be slightly different.


##Cores, threads, processes
GPUs are sort of designed to accommodate rapidly changing amount of threads - this can be on a millisecond timescale
The amount of physical cores stays the same, but the hardware adapts to the changing 



##To handle rapid changes in 
A spike in one product, then Amazon, and Google can adaptively expand 

Instead to buy a computer cluster that accommodates the most traffic you ever need

Fast increases in utilization - needed for the cloud 

Effective usage model

##
Sometimes you do have a variable number of processors - cloud computing

##Open source and cloud computing
Cloud computing works pretty well if you are using open source software on the cloud.

But initiating a 1000 IDL or Matlab boxes on the cloud might not be practical unless you have some insane alternate renew stream 

##Scaling and communication effects
Be aware of bottlenecks 

The problem with synchronization is that it says: _wait for the slowest one_

Sync statements are particularly dangerous if you have a big number of cores.

In GPUs, they tackle this by grouping different cores together.

Would you really want to wait for the processors that is busy cleaning out its temp-file?


First try to parallelize your program in the simplest way possible, and then expand.

There are not really good profiling tools when you are making a program that should run on a 1000 cores.
- more guess-work is involved. Then it is good to have the analytics scaling very useful, and then just looking at how it is actually performing in real life.
So some combination of analytical deriving, and actual benchmarking on smaller scale problems is the best way to see where you should be spending your time parallelizing.

To give you a framework how to think about things in the future.

Streaming multi processors
Smaller 





