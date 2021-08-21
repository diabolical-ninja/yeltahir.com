---
title: "Zoot, Your Friendly Neighourhood Jazzbot"
date: 2021-08-21T00:00:00+11:00
draft: true

resources:
- name: featured-image
  src: batman_jazz.jpg

toc:
  auto: false

mermaid: true
---

Outside of data, a huge passion of mine is music, in particular jazz. In Melbourne we're fortunate to have quite a few establishments that support live music and offer amazing shows every night of the week. But this raises a problem; who to see? Where to go? What's on?!

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

Quite possibly the main prompt for building Zoot was that a database or calendar of gigs around Melbourne doesn't exist. This meant that before we could really do anything we needed to build that database and that meant a whole lot of web scraping. Picking out our favourite venues across town, a scraper was written to extract and clean the data needed into something we could build Zoot around. Each show, after scraping would look like:

```json
{
        "title": "ANITA WARDELL",
        "venue": "paris_cat",
        "description": "Paris Cat serves up London based Anita Wardell, recipient of the BBC's Best of Jazz award for a night of high stakes singing. Jazz standards, vocalise, swinging bebop, and more. Anita is regarded as a master of her art.  She will be joined by the fabulous trio of Dave McEvoy on piano, Frank DiSario on bass and Ronny Ferella on drums. A night not to miss! Dave McEvoy (piano),  Frank DiSario (bass) and  Ronny Ferella (drums). http://www.anitawardell.com/https://soundcloud.com/anitawardell Genre - Jazz/Swing/Bebop Performance Room - Basement",
        "performance_date": "2020-08-21",
        "doors_open": "21:00",
        "music_starts": "21:30",
        "price": 40.0,
        "url": "https://roller.app/pariscat/product/506177?date=20210821",
        "image_url": "https://cdn.rollerdigital.com/image/7TYsiH4Owk-_Iy8vgq9-0g.jpg"
    }
```

Maybe in future versions it would be fantastic to also collect the genre, musician names, the instrumentation and a whole host of other details to create tailored recommendations of what and who to see.


##

In order to store, save and access any of this gig information we needed databse and a way of interacting with it. In the spirit of KISS, when went 

## Lets Have a Chat

[View Source](https://github.com/zootytooty/BeBot)

In order for any of this to work we needed a way for users to chat with Zoot. Would it be SMS? Do we build an app? Our choice was to use Facebook Messenger because of the incredibly large existing userbase, the existing support they have for chatbots and that it simplified our solution. It meant we didn't have to write or manage any new services that would directly face users. It's plug and play, and that's great!


## Machine Learning to the Rescue...Sort of

[View Source](https://github.com/zootytooty/WitTrane)

Whenever someone sends Zoot a message we need to figure out what they're asking and whether there are any special words or context they're providing. If someone says "Yo Zoot, who's playing tomorrow at jazzlab?" we need to know they're interested in `Whats On`, specifically tomorrow and at the venue Jazzlab.

Often this done by looking for keywords or phases, for example assuming if `hi, hello or hey` are present then respond with your welcoming message. Unfortunately this approach can quickly fall down because of multiple keywords or typos from users. Using example above, is the user saying Hi or asking what's on? What if they a "z" in _"jazlab"_? It's easy for us to see the intent, see the similarity but it's much harder for computers. What would be ideal is if rather than looking for specific keywords we could build a general understanding of the message intent and what it's asking.

Fortunately a bunch of smart folk in the machine learning community have thought of this and developed something called Natural Language Understanding (NLU). For us there were two tools in the NLU toolkit of particular interest.

### Intent Classifcation

The goal here is to be able to tag a sentance or user message with the general intent of the request. A single intent, for example "What's On?" could be phrased multiple ways and we want to learn that they all have the same meaning. If someone says "what's on", "who's playing tonight" or "what's crackalackin'" we want to learn they all share the same intent. For Zoot we have four intents:

* `whats_on`: For messages asking what's on, where and when
* `venues`: When people what to know all venues around town
* `help`: To return a link to our [help page](https://zootytooty.github.io/zoothome/)
* `hello`: Just being a friendly little Zoot 😃 


### Named Entity Recognition (NER)

Within each message there are attributes (or entities) we want to extract that let us know the finer details of the users request. Again going back to our example above there are two important entities we want to be aware of.

Yo Zoot, who's playing `tomorrow` at `jazzlab`?
* `Date`: We want to understand the date context of a message. Tomorrow, today, next week, on Thursday, etc. The it's a date entity but
* `Venue`: By knowing the venue the user is interested in we can refine what Zoot returns


### Wit.AI

Rather than building our own model we used a service from Facebook called [Wit.ai](https://wit.ai/), which allowed us to provide sample user messages and tag them with the appropriate intent and entity/s. With those it was able learn a more general understanding of what users were asking for and allowed us to respond a little smarter than if we stuck with only keywords.

We trained Wit by sending many, many samples and built templates that allowed us to iterate across every possible combination of intent and entity. For example, one template for the `whats_on` intent was "Are there any gigs {entities_wit$datetime:datetime} at {traits_venue}", which generated samples such as:
* Are there any gigs `tomorrow` at `Jazzlab`
* Are there any gigs `next wednesday` at `Moldy Fig`
* Are there any gigs `tonight` at `Paris Cat`

Once trained, we could call Wit's API with user messages and it would provide a breakdown of what the intents, entities and their respective confidences. For example
```json
{
    "text": "Who's playing at birds basement tomorrow",
    "intents": [
        {
            "id": "240179067977375",
            "name": "whats_on",
            "confidence": 1
        }
    ],
    "entities": {
        "wit$datetime:datetime": [
            {
                "id": "871058740461194",
                "name": "wit$datetime",
                "role": "datetime",
                "start": 32,
                "end": 40,
                "body": "tomorrow",
                "confidence": 0.9666,
                "entities": [],
                "type": "value",
                "grain": "day",
                "value": "2021-08-22T00:00:00.000+10:00",
                "values": [
                    {
                        "type": "value",
                        "grain": "day",
                        "value": "2021-08-22T00:00:00.000+10:00"
                    }
                ]
            }
        ]
    },
    "traits": {
        "venue": [
            {
                "id": "516705612770815",
                "value": "birds_basement",
                "confidence": 0.9993
            }
        ]
    }
}
```



We used a service from Facebook called [Wit.ai](https://wit.ai/), which allows us to provide sample phrases and tag them with particular attributes. From these samples Wit can learn a more general knowledge of the message, hopefully make it 

Rather than building our own model from scratch we used a service from Facebook called [Wit.ai](https://wit.ai/), which allows us to provide sample phrases and tag them with particular attributes present in the phrase. 


# Putting It All Together

When we glue all those bits and pieces together we get something that looks like this.

![Zoot Architecture](Zoot_Architecture.png)



### Key Note

An overarching consideration when making our technology and infrastructure choices was "is it easy?" and "is it free?". You'll notice everything is serverless and this meant we could focus on building Zoot & its functionality rather than building infrastructure. It also meant we could say:

* Why MongoDB Atlas? Because their free tier is fanstastic
* Why Heroku to host Zoot? Because their free tier is fanstastic
* Why AWS Lambda to host the API? Because the free tier is fanstastic
* Why Wit.AI? Because it's 100% free
* Why Facebook Messenger? Because it's 100% free

Notice a pattern here?