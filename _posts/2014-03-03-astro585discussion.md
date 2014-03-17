---
title: Astro 585 Discussion 10
layout: post
published: false
image1: /img/<+imagename+>
image1title: <+title+>
image1subtitle: <+title+>
tags:
- astro585 
---

##Programming with openMP

##In Julia
You can add <code>@parallel</code> but it will give different answers.

If you are timing such for loops you have to add <code>sync</code> statements.

In openMP there is an implicing _barrier_ function.

Some things compilers are good at, but don't trust it to be smart about everything. 

##Threads, jobs, tasks and other jargon
The operating system is using what would be known as non-cooperative schedulers. - "I don't know what these processes are doing; I'll give you this, and this, and this.

When you parallize something by using many threads, each thread has a stack, and a set of pointers

####Light-weight threads
The created stacks for threads tend to linger on in the memory, i.e. the stacks aren't destroyed immediately, when the thread is finished.
"I happen to have a stack in memory, here, take it" 

allocate a stack for each thread

####Threads
Almost like a mini-program

####Tasks
A sort of like a queue, they don't necessarily be assigned to one thread
Do not have stacks.

A task-system 

For co

MCMC package is Julia


