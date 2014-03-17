---
title: Astro 585 Discussion 6
layout: post
published: false
image1: /img/coursework/astro585/bandwith.png
image1title: Latency-Bandwith diagram
image1subtitle: Image gotten from IHPCfSE by G Hager, and G Wellein
tags:
- astro585
---

_Now we are getting to the most interesting part of the curse._

##How are matrices stored?
It really helps knowing to know how matrices are stored in memory. Are they **colum-major**, or **row-major**?

- _Julia_ is like _Fortran_, storing matrices as _column-major_ data structures; while _C_ uses _row-major_ data structures.

So then in your implementation of the simulation of _Life, the Universe, and Everything_, then might need to have **big matrices**; and you might save a lot of Big-Thought's computing time by knowing if it is faster to traverse your Big-Matrix by the columns-first, or by rows-first.  

##Are your matrices sparse?
If you have a lot of 0 entries in your matrix, then instead of allocating a big rectangular block of memory for it, then rather store it as a list of non-zero entries instead.

For example, if you had a diagonal-matrix you really would only need one vector to store the data, right? And similarily, a tri-diagonal one would need 3.

##Is the data already cached?
The main philosophy here is: _How do we reuse data that is already in the cache?_

##The power of _views_
A powerful example: _What's a clever algorithm to transpose a matrix?_

Just flip the indices!

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


##Cache associativity?
When you have data in the big memory and you want it in the cache - what do you do? Where can it be?

####Non-associative cache?
It might go something like this:

- Byte-1 of main memory can only go to Byte-1 in the cache

- Byte-2 of main memory can only go to Byte-2 in the cache

...

- Byte-1024 of main memory can only go to Byte-1024 in the cache

- Byte-1025 of main memory can only go to Byte-1 in the cache

Reading a cache like this is _very fast_, as you don't have to search for the data too long - every byte has a fixed and known location.
But the main downside is: _you rarely use the whole cache!_

Solution to this is called _padding_.
