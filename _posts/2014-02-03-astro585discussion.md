---
title: Astro 585 discussion 2
layout: post
published: false
image1: /img/coursework/astro585/performance.png
image1title: Performance curve
image1subtitle: 
tags:
- astro585
---


One of the general themes of this course (and perhaps in real life as well?);

<code><i>Try not to do work that you don't need to do</i></code>

_RISC_-y chips, and _CISC_-y chips

#Comments about <i>Homework 2</i>

####Coding habits in <code>Julia</code>
Put an exclamation mark at the end of a function if your function modifies some of the input arguments.

####Performance checking

People who did memory allocation in the for loop:

1. <code>asserts</code> didn't really make any difference in time

2. making generic function calls didn't really make a difference either

People who <b>didn't</b> do memory allocation in the for loop:

1. <code>asserts</code> didn't really make any difference in time

2.  making generic function calls did really make a difference 

##Explaining performance curves in homework 2

Check the following code:

<pre>
	using PyPlot
	n_list = [ 2^i for i=1:24 ] #Increasing i from 1:10 to 1:24 to see further
	elapsed_list = map(calc_time_log_likelihood,n_list)
	plot(log10(n_list), log10(elapsed_list), color="red", linewidth=2, marker="+", markersize=12);
	xlabel("log N"); ylabel("log (Time/s)");	
</pre>

<i>Note that we are using <code>map</code> - next it might be cool to check out <code>pmap</code>.</i>
This gives the following result on my computer:

<div id="myCarousel" class="carousel slide">
  <!-- Carousel items -->
	<div class="carousel-inner">
		<div class="active item">
			<img class="carouselImage" src=" {{ page.image1 }}"> 
			<div class="container">
				<div class="carousel-caption">
					<p class="lead"> {{ page.image1title }}</p>
					<p class="muted"> {{ page.image1subtitle }}</p>
				</div>
			</div>
		</div>
	</div>
</div>

Sometimes things that you think should take longer don't: look at the first part from 0.5 to around 2 - the curve is almost flat. There we are probably making good use of the <i>caches</i>.
Then as we keep using bigger and bigger arrays, we see a linear increase in time: we are starting to use the main memory.

<b>Note:</b> <i>Some people saw strange bumps/spikes in their curves; probably due to memory-cache interactions, where the computer is trying to be smart, but pays a price in performance for it</i>.

##What are caches though?
Caches, are a small amount of memory that is better accessible to the CPU; the memory access is much, much faster, than accessing the main memory.
Accessing the memory is slow, and expensive. 
Smaller caches are relatively fast, while bigger ones are slower.

<hr></hr>

#Discussion on chapter 6: Computer Organization

##When do we need ques, and when do we need stacks?
If you wanna get a Starbucks - you stand in line and get your coffee the last.
However, if you are the last one to check in your flight-luggage, then there is a good chance that you are the first to get it back (bags are usually stacked on top of each other).

**Ques:** - Well if you need to do things that require you to do them in a particular fixed order.

**Stacks:** - Function calls for small variables. They are not efficient when you have dynamic memory allocation. Moreover, you have to be careful with using stacks and recursive functions - can lead to <code>stack overflows!</code>

<i>
Check out <code>tail recursion</code> though: The ability to implement neat recursive algorithms without doing terrible things.
</i>

##Registers, stacks, and heaps
**Registers**  
Registers are a <i>property of the hardware</i>, while the stacks, and heaps are <i>software constructs</i>.
And accessing the registers is basically free - this is what you would like to do in an ideal world. 

**_stack_ vs _heap_**   
If its dynamically allocated, it is almost certain that the compiler will put it into the <code>heap</code> - its safer, and a reasonable thing to do. Still however, it costs time and performance.

A function can return data types that are small, on the stack, or return a pointer to a memory location on the heap (if the return data is big).



##Language choices
Some languages were written a long time ago. Ideas like <code>"I would like to access the web"</code> were non-existent when the people were developing the initial versions of <code>Fortran</code>.
If you are doing text processing - then it makes sense to use Python or Perl - don't really try to do it in Fortran or C; you have to do some real acrobatics.

In general if you use a higher level language - then hopefully you need a fewer lines of code; and hopefully you have less bugs, and are quicker to get things done.
However using an interpreted language you have to live with the overhead it has to go through when interpreting.

One of the nice things about <code>Julia</code> - is that it combines some of the best of the ides of high-level language, as high performance, but its syntax is similar to Python's.

##Higher level language parallelism
**Macro-use-framework** Sometimes referred to as _embarrassingly parallel_  - still, this is often the best parallelization you can come up with. Why? A) its easy for you, and B) its easy for the computer to do.

