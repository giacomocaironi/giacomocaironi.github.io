---
title: Why I built my own static site generator
date: 2020-05-14
author: Giacomo Caironi
tags:
  - python
draft: False
description: The majority of the time you down't want to reinvent the wheel. It is time consuming and often there are people out there who have already built something better. However when I started looking to static site generators to build my personal site, I found out that getting exactly what I wanted wasn't a trivial task. Using one generator would have required me to write a custom plugin to have the urls properly set, to use another I would have to write custom code just for having something other than a blog. The last one, who had almost anything I wanted (but anyway had all the features I really needed) used a templating language I absolutely didn't like. So instead of using one of these tools I decided to build my own.  
---
The majority of the time you down't want to reinvent the wheel. It is time consuming and often there are people out there who have already built something better. However when I started looking to static site generators to build my personal site, I found out that getting exactly what I wanted wasn't a trivial task. Using one generator would have required me to write a custom plugin to have the urls properly set, to use another I would have to write custom code just for having something other than a blog. The last one, who had almost anything I wanted (but anyway had all the features I really needed) used a templating language I absolutely didn't like. So instead of using one of these tools I decided to build my own.

## Some background

I first thought about building my own site when I started looking to python web frameworks, in particular Flask. For the ones who don't know it, Flask is a very flexible web micro-framework. I preferred it over Django, another very popular python web framework, because it gives you much control over the way the site was built. I really enjoyed it and built a little project using it. But I found out that using Flask to build an apparently simple blog was not as easy as it may seems. I later found out some cool packages that let you render Markdown directly in the browser, so you could have a WYSIWYG (What you see is what you get) editor. However in the meantime I learned about static site generators.

I first learned about them when I discovered Github Pages. It seemed a fantastic thing, a place where I could host my site for free. I know that there are some services, like Heroku, which can host a python web app for free (with restrictions). However the idea of doing everything in the same platform I use for version control seemed fascinating. So I started using it.

## A brief look at some static site generators

At first I tried out Pelican, a static site generator written in python, which was very appealing because I could use the Jinja2 templates, that I had learned using Flask. However I thought it hadn't enough flexibility, I wasn't able to understand how to make something that was not only a blog. I wanted to create custom collections.

Then I switched to Jeckyll, because of the ability to create custom collections and the fact that had integration with github pages. And I started writing this site.However when I tried to introduce pagination in the index page of the blog, I found that first of all it wasn't supported natively by Github Pages. I learned to circumvent this using CI tools, but that not having to use them was one of the reason I wanted to use jeckyll. But then I realized that the Jeckyll plugin that managed pagination was a little broken, as it couldn't create the custom urls I wanted. I managed to create something manageable, but it was a very ugly hack. As I don't know Ruby, the language Jeckyll is written in, I couldn't fix it, and I didn't want to learn a new language just for writing my site.

I then looked at Hugo, another popular static site generator which had most of what I wanted, but used a templating engine which I didn't know. Hugo is the most complete one out of the three but the fact that, unlike the other two, it written in Go and then compiled means that if you want a custom logic, it is very hard to do. Still I think that if you are eager to learn his very strange template language, it is the best out of the three. It is also very fast.

## How it works

So I was unsure. All of the three had something I wanted: the templates of Pelican, the ease of use of Jeckyll, the abilty to create custom collections, that both Jeckyll an Hugo have, and the power and speed of Hugo. So I started thinking if I could write something that was exactly what I wanted: it had to be very simple to use to create something standard, like a blog, but that could still be used to create more complex sites enough easily; it had to let the user define the urls they want in a simple way; it had to use as default the Jinja2 template engine; it had to be fast enough.

I thought about the structure for a while and then started thinkering. I literally built the basic skeleton in three days. I created it as a python library and put it on PyPi. I called it Kart, because i like the letter K and because it seemed appropriate, something fast enough and very funny to use.

Kart is build around the concept of flexibility and pluggability. The main class is responsible only for serving the files, building the folder structure and calling the other part of the library. But the cool part is that, apart from this, you dont' need to use the code I have written. You can simply create a custom python class responsible for you precise use case, and then make it callable by the main class. It works as long as the class has the same methods as the default classes but is difficult to do. My idea for doing this is that no static site generator is tailored for each user. I thought having a solid base, but letting people insert custom code easily, could help people in my situation.

The structure of Kart resembles is some way that of Pelican (maybe because when I started writing Kart I had in mind its functioning which I had read a few months back). There are type of classes, each one responsible for one particular use case. However Kart brings this idea a step further than Pelican, so it has more classes each responsible for a more little scope. In this way you don't have to reuse or rewrite code if you want to modify only a little part of the library. Anyway I hope to explain this in more detail in a future post.

## Comparisons

So after what I have said, how does it compare to the alternatives I have mentioned? Let's start by Pelican. Kart uses the same language and it is structured in a similar way; if you are willing to dive deep you can achieve the same thing with both, but with Kart it is way easier and faster to do. In respect to Jeckyll it has the same ease of use, but has out of the box some features that if you want to have in Jeckyll you have to write a custom Plugin(this area it is similar to Pelican). Talking about Hugo Kart has two little advantages and one disadvantage. Kart is slower, so if you really need that speed Kart is not suitable, but I don't think that this is a problem for the majority of people. On the other hand Kart uses a simpler templating language and because it is written in python is a little more flexible.

## Conclusion

So this is the story of Kart. Could have I just forked another static site generator instead of building my own? Of course. But is has been a very funny and teaching experience. I had to think about the architecture of a software maybe for the first time, and now I have something I am very proud to show.

If you want to learn more about Kart I started writing the documentation as [this link](https://giacomocaironi.github.io/Kart). If you want to help the development of Kart, I would be very thankful!
