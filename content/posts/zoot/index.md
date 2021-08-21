---
title: "Zoot"
date: 2021-08-21T00:00:00+11:00
draft: true

resources:
- name: featured-image
  src: batman_jazz.jpg

toc:
  auto: false

mermaid: true
---

Outside of data, a huge passion of mine is music, in particular jazz. In Melbourne we're fortunate to have quite a establishments that support live music and offer amazing shows every night of the week. But this raises a problem; who to see? Where to go? What's on?!

As friends and I constanstly returned to the same sites, the venues over and over every time we wanted to figure who to see the same thought popped up any time I see a repetitive task; "you know who's great at doing the same thing over and over again? Computers!" So without further ado I'd like to introduce you to [Zoot](https://m.me/rootytootyzooty), you're friendly neighbourhood jazzbot.

{{< admonition type=success title="View the source" open=true >}}
If you'd like to look under the cover it's all open source: [Zooty Tooty](https://github.com/zootytooty)
{{< /admonition >}}


Also, a bit shout out to [Trent](https://github.com/trent-howard) & [Pete](https://github.com/petergreco), who without there would not be a Zoot!

# Say Hi Zoot 👋🏽

Before we get into all the nitty gritty lets have some fun & give Zoot a whirl. You can chat with zoot on facebook at {{< link "https://m.me/rootytootyzooty" >}}. 


## What's On?
The simplest way to get started is to ask `What's on?` for the shows available today. For example:

![alt text](zoot_whats_on.png)

If you want to get a little fancy you can even specify a venue or a day (or both!) such as:

![alt text](zoot_venue_date.png)

## Where to go?

You can also find where the zool joints are around town. How? Just ask zoot!

![alt text](zoot_venues.png)


{{< admonition type=tip title="Zoot Help" open=false >}}
Full help and how-to details are available on [Zoot's hompage](https://zootytooty.github.io/zoothome/)
{{< /admonition >}}


# So, What's a Zoot?

At heart of it there are three core parts that make up Zoot; getting the gig info, the chat interface and some smarts to figure out what's going on and what was asked.

## Scrape, Scrape, Scrape

[View Source](https://github.com/zootytooty/ScrapeFromTheApe)

Quite possibly the main prompt for building Zoot was that a database or calendar of gigs around Melbourne doesn't exist. This meant that before we could really do anything we needed to build that database and that meant a whole lot of web scraping. For anyone who's been down this path before you'll be accutately aware of the challenges this brings but for those that haven't here are couple of hurdles we ran into that you surely will too.

### Everything is Different

No one site is the same as any other site and this means the code you wrote for one almost certainly doesn't work on the rest. Developers love to spruik the benefits of generalised code and reusability but unfortunately when it comes to webscraping those words barely make the dictionary. 

### Everything Changes

Just when you think all your scrapers have been built and everything's finally working, someone will come and change their site just enough to render everything you've built completely useless!


## Lets Have a Chat

[View Source](https://github.com/zootytooty/BeBot)


## Machine Learning to the Rescue...Sort of

[View Source](https://github.com/zootytooty/WitTrane)

Quite a few chatbots look for keywords or phases to try and understand what the user is asking for. For example, you might say "if hi, hello or hey" are in the message then return your welcome message. Unfortunately this approach can be quite inaccurate as message content and length grow in complexity, such as when the users says "hey, I want paella for dinner". What would be ideal is rather than looking for specific words or phrasing we could generate a general understanding of the intent or meaning of the users request and use that to determine how to respond. This is where machine learning, in particular Natural Language Understanding (NLU) can help us out.

Rather than building our own model from scratch we used a service from Facebook called [Wit.ai](https://wit.ai/), which allows us to provide sample phrases and tag them with particular attributes present in the phrase. 


# Putting It All Together

When we glue all those bits and pieces together we get something that looks like this.



### Key Note

An overarching consideration when making our technology and infrastructure choices was "is it easy?" and "is it free?"