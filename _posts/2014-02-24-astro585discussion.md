---
title: Astro 585 Discussion 8
published: false
layout: post
tags:
- astro585 
---

**Bottom lines**

- Write your parallel code as if the machine doesn't have a shared memory system (more distributed), and then if it has, spend time to optimize it for shared memory. 

- If there is a doubt in your mind that you need a sync statement - <code>use it!</code>. Also, help yourself (and potentially others) out by commenting on how confident you are on this sync statement.

- _Optimize later_ is a good motto to keep in mind when parallelizing code.

##Interactive vs batch machines

####Interactive
They usually have very short walltimes (maybe something like 5 minutes or so)
Good for rapidly debugging your code, but they might have very short walltimes - (like 5 minutes!).

Examples of such clusters here at _Penn State:_

- **Tesla** - has GPUs 

- **Hammer** 

####Batch
More queue oriented. Has a _scheduler,_ and a _load-balancer_



##Infiniband vs Gigabit
<code>Gigabit</code> has very low latency vs Infiniband.
Moreover, Infiniband has more bandwidth.

##Scheduling jobs

When you are starting out it might get good get the cluster to send you an email when your program *starts*, *ends*, and/or *aborts*. It can be done _per-core_ or _per-node_.

##False sharing
Too frequent updates on caches between different processors.
Can severly hurt application performance.

**Common strategies to reduce this traffice:**

You can intentionally group all your writes at once. 

##Julia's three datastructures that are good for parallel 

####Normal arrays

####Distributed arrays
Can be spread across many processors. 
Each processor owns a chunk of the array.
Other processors can ask for other chunks of it - costs communication time though.

As slow as the network is, it is still faster than a hard-disk, if you really need a lot of memory using distributed arrays might be a good choice.

####Shared arrays
**Warning:** <code>labeled as experimental</code>

This is ment for for arrays multiple cores at a workstation.

With a shared array, there is one copy of the array in the shared memory, and the multiple cores have access to it.

**Downside:** You have to be careful if you have multiple processes that are reading and writing simultaneously to the shared array. You can use <code>sync</code> or other types of <code>barriers</code> to prevent running into unvanted troubles, but if you have a lot of synchronization statements then the parallization might not work to well for you.

Advice: If there is a doubt in your mind that you need a sync statement - <code>use it!</code>. 
Also, help yourself (and others) out by commenting on how confident you are on this sync statement.


##Virtualizing
Very good for debugging parallel code, and stress test it.
_People who work in cloud computing really love this._

However, for performance benchmarking it does not really do it - at the end of the day you are gonna have to benchmark it on a similar system to the one that you are going to use.

##Hardware
**Fiber optics:** probably best for backbones, but within one cluster you would need a probably pretty good case to buy it.

**Copper:** Much slower, but cheaper.
