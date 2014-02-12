---
title: Astro 585 - Profilers
layout: post
tags:
- astro585 
---

<code>Bottom lines:</code>

* Try to find the thing that takes the longest - **and do something about it!**

*  Every bit of code that you write, _write it as you were trying to convince somebody else to use it_.
Make it public (push on Github), and sure enough the person that is going to be reusing your code is,_ well, most likely yourself!_

##Profiling
A profiler is a program to see where a program is spending most of its time (examples: <code>prof</code>, and <code>gprof</code>). Early profiling tools were mostly based on counting; monitoring how often, and how long calling a function takes.

####Downsides
You are adding more instructions to your program! In a way you are interrupting the whole enterprise every time you call a function. If you are limited by caches, and writing in registers running a profiler on it makes the program run slower - so in fact you are timing a slower version of your program with the additional overhead the profiler inserts.


+ **Perks** You get information about where the program is spending most of its time - then you can see what places you might want to speed up! Some hardware actually offer **hardware profiling** where the hardware has special registers only used for profiling - not interfering with the main program too much (however, you are still disrupting things - you need to unwind the pipeline, creating additional overhead, etc.)


##Timed profiler
You can **interfere less**: instead of checking every line with a statistical profiler - you can check the program at a fixed interval, asking the program: _"Where are you now?"_ in a fixed time interval.
Note: you can have _resonance_ in for-loops - which gives a bad representation of how the program is actually running.

This is how the <code>Julia</code> profiler works.

If you are trying to figure out something about _branching_, then statistical profiling is better.


##Overloaded functions, profiling and _name manging_
C++ supports overloaded functions i.e. functions that have the same names.
Then if you are profiling C++ code the profiler puts extra identifiers to distinguish the different versions of the overloaded functions. The identifiers have sometimes something to do with the variables that the functions use, or sometimes _just complete random gibberish_ - this is called: **name mangling**.

##Astronomers and code writing
Most of what astronomers do isn't so complicated that we really need to talk to a computer scientist about our code.

However, if you are gonna ask <code>NSF</code> about of a lot of computer resources - then it really helps to have collaborated a bit with a computer scientist, or at least _had conversations over lunch with a computer scientist._ And if you _really, really care_ then you would write the proposal with one. 

Still, computer scientists are expensive (compare 1 month of a computer scientist's time vs funding 2 grad students for a semester).
And yet, sometimes you are required to write the proposal with one. 

In an ideal world these things would be well matched; _but sometimes a bit of bending is needed_.

The world of writing code between CS students, and astronomy students are different.
In astronomy we don't really care if you solve a problem cleverly, just that you solve it.
The typical scenario is that an _astronomy graduate student is thrown into a pond to solve a problem, hopefully to reach shore with the solution in hand_.


Taking people into lunch - can be very productive.
Then you can get hints into what 
Per unit time, and per unit dollar collaboration. 
Are there proposals that we want to work together on?
Don't spend too much of your time to reinvent the wheel - when somebody else has already done it.

##Some things that we should do more of
####Code reviews 
Make somebody else review your code. It doesn't need to be too formal - the bottom line is: _getting feedback can be beneficial!_

It can be good for spotting coding standards, and other small bugs - but doesn't necessarily catch the _Big-Picture_ things.


##How do you organize your code into files and folders?
Not a single magic answer. 

What usually works: Do a bottom up approach (_i.e. the start-without-a-plan plan_), starting with 1 file, and then expand it to a few files, grouping similar ones together, and then from there branching into dividing the code into subdirectories, again grouping similar-purpose code together.

There are tools that can be used to automate complex work flow issues - like _make-files_.
This can lead to a multi-step process: even before you type make - then you might need to _configure_ the code, and then you have to _make_ it, and then to _make install it_ etc.

####Cmake
If you have a complex thing that is not related to operating system issues, then _cmake_ might be useful.
It makes a lot easier to have logic in your build system - you can have if and loops, and variables - to do _logic!_. 


####Processor-directives 
**Preprocessor** If this system currently has this variable set then compile this, otherwise this piece of code. 
Very useful for running code on different platforms; Windows, Mac, Linux.

_I need to take a better look at this._

####Lacking permissions
**If you are dealing with setups** Try to place them in their default install locations: _Your time will be saved!_
Sometimes you don't have the permissions to install things where you want them - then you have to deal with what the system admins tell you to do! 

##Git tags
If you cloned an ever changing code to use for a project, and then when you update it something doesn't work as it did, then in principle you can revert to an earlier point in time.
However, it might not be obvious to what point in time to revert to!
Then, <code>tags</code> can come in handy: you can tag your version that you used, making it much easier to find that specific version later.

<code>Tag-example:</code> _Final-version-that-was-used-for-my-paper_


##Libraries vs packages
In the old days people compiled code into libraries and then linked other code to those libraries.
Programming languages like Python now offer you to manage your code in packages - which is much more convenient (you don't have to spend time with linking issues - usually you are just an addPackage() away from using somebody else's packaged code!)

This has saved many a person a lot of time.

##Good advice
If you can make your code easy to use and reuse, then you yourself are likely to benefit; your group is likely to benefit; and maybe somebody else is also likely to benefit. And there is also that chance of a chance that that person which benefited will also benefit you in some way later! 



