---
name: Kart
description: A very flexible static site generator written in python
date: 2020-03-21
---
Kart is a static site generator written in python. It was designed with flexibility in mind, because I felt like I wasn't able to get exactly what I wanted from the preveious static site generators I had tried.

Its flexibility comes from its modularity. The kart class is composed of three components: the miners which are responsible for getting the data from text files; the mappers, which generate the urls for the site and the renderers, which generate the site based on the information from the mappers.

The strength of Kart is that it comes with very powerful defaults but at the same time is very easy to create your own miners, mappers or renderers.
