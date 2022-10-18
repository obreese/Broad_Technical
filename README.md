# Broad_Technical

Environment:
I'm not going to include the requirements.txt for my workspace, because it's one I've used for many projects so there's too many unessary packages there. The relevant information for our purposes is the following:

- python version 3.9.2
- requests version 2.25.1

Firstly, Python may seem like a strange choice for a postion which requires Java and React. I'm actually in 2 classes using typescript this semester and none using Python, so it's even more surprising. I find for interviews using Python is a good idea for a couple reasons. First: it reads like pseudocode. In terms of explaining algorithms, and getting a working solution at a small scale, I think it's hard to find a better option. The other important reason, especially for take-home assessments like this one, is that I've never had a problem with an interviewer running my code. Pip is an easy package installer, and environments are generally simple to set up and relatively bug-free.

Question 1 requests I document my decision to rely on the server API to filter results rather than doing my own processing, so I'll explain that here. It's always my preference to rely on the server to filter for again two reasons. The most important one is that we can treat APIs like a black-box implementation. With a relatively reliable organization like the MBTA (never thought I'd say those words), we can assume they've thoroughly tested their code for edge cases: at least better than a single developer can during an interview. Performance is the second reason. Sure, there may be a throttling issue with the server not allowing tons of requests, but it seems to work well enough for my purposes here, and whenever possible it's usually good practice to push work onto a scalable resource rather than a local one.

Edge case implementation:
I'm certainly aware of edge cases that might exist, such as a route_id not being valid, subway_route_ids getting passed in as empty, or invalid input for "stop 1" and "stop 2". I don't gracefully handle these errors in the code not for lack of noticing but for lack of time. Since the instructions specifically downplay the importance of catching edge cases, I feel that making assumptions that the user will enter valid data is reasonable for the purposes of this assessment.
