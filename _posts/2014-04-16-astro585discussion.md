---
title: Astro585 discussion
layout: post
tags:
- astro585 
---

Goals to try to achieve

- <code>Zen with Git</code>

##The "I'm embarrassed about my code mentality"
"My code isn't perfect, I'll be embarrassed if I put it out there for everybody to see. What if there are bugs in it?"_
- Making code public accelerates the finding of bugs. Its better to find them, rather than letting them fest.

##Philosophical debate
Science should be reproducible: do we have an ethical responsibility to share our code? 

Throwing out stuff out there with little documentation might end up giving you headaches later in life; you might end up getting a lot of emails from users that want to use the code, but they didn't understand it properly. 
Solution: <code>documentation</code>, <code>examples</code>, <code>short tutorials</code> - people will appreciate it!

##Code sharing in grant proposals
Reviewers rarely comment on: _"Oh, this person is going to make their code public"_, with a bad connotations.
Sharing code is actually getting much more hip these days - which is a good thing!

##If your goal is to be useful
Make tutorial style examples. People are more likely to use the code if those are provided.

##Should we publish our source code with the paper?
That would be lovely actually. 
There are already some journals out there that make you submit source code with your paper.
It might make more sense to have a source code repository though (for example on <code>Github</code> or <code>Bitbucket</code>), and just link to it.
That way you can also make smaller updates without have to resubmit your whole code when you fix that one tiny bug; less headache for the world.

##Finding bugs when code reviewing
If you make it your purpose it life to find bugs, you will find them. 
But they might be stupid bugs; like _"this was actually a tab, not 4 spaces"._
Common, friend, at the end of the day, this is supposed to be useful!

#Questions to think about for writeup

- What did you get out of the project?

- What did you do?

- What were your parallelization strategies?

- How did things scale when you parallelized them?

- Did you use a profiler?

- How did the tests go? What did you test? Did they pass? 
