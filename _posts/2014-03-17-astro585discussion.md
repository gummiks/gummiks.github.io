---
title: Astro 585 discussion
layout: post
image1: /img/<+imagename+>
image1title: <+title+>
image1subtitle: <+title+>
tags:
- astro585 
---

<code>Bottom lines:</code>

- MPI is like the Fortran of parallel programming.

- MPI has grown pretty big, as people have added a lot of Functionalities to it - so now it is sort of a monstrosity if you try out the documentation.

##MPI
If your advisor's advisor's advisor wrote code in MPI, it might be a bit confusing.

If you are doing things where you don't really need MPI parallelization, using openMP might be less error prone.

##Debating between MPI, openMP, or Julia
<b>Keep this in mind:</b>

- Even for old timers with MPI, they will probably be more error prone using that, rather than going with openMP, or Julia.

##MPI analogs in Julia
The <code>@spawn</code>, and <code>fetch</code> functions in Julia, are kind of analogous to <code>send</code>, and <code>receive</code> in MPI - still the former two are much higher level (the latter only send data).


##Adaptive scheduling algorithms

Example of integrating a function:

1. _Would you divide the interval into 10 different intervals, distributing each interval to integrate to 10 processors?_ - But what if you have a tolerance parameter, and a singularity in one interval? Then you might be waiting a long time for that one processor

2. _Would you adaptively integrate?_ - This will probably be the best way, but then do you really understand every possible outcome of that adaptation?
