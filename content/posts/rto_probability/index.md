---
title: "Flexible RTO has a Maths Problem"
date: 2025-11-05T00:00:00+11:00
draft: false

resources:
  - name: featured-image
    src: office_overlap_cover.png

toc:
  auto: false

math:
  enable: true
---

There's been a lot of talk of late about work from home (WFH) vs return to office (RTO) policies with companies siding hardline with one, the other or hedging their bets half way. 

One of the points often raised in favour of more office time is an opportunity to collaborate more. In-person meetings, social collisions and the famed “water cooler chat”. Some companies are mandating the in office days, which to an extent guarantees these outcomes, but many companies are mandating the number of days, leaving which days to the employees' discretion. This got me wondering: what's the likelihood that two people would be in the office on the same day?

Scratching this quizzical itch we can calculate the probability of in office overlaps!


{{< admonition type=success title="View the source" open=true >}}
Analysis available on [Github](https://github.com/diabolical-ninja/rto-probability)
{{< /admonition >}}


# Our Scenarios

There are two scenarios we'll model. But first, a constraint!

## Constraints
We're going to assume that each person/team is free to choose the day/s of the week to attend the office. Thus, day of the week selection in our model is random.

Now for our scenarios:

## Scenario 1: At least one collision

What is the probability that across a 5 day week **all** people are in the office on the same day for at least **one** of their required in office days.

For example Peter & Benjamin are required to be in the office two days a week. What is the probability that at least one of their days overlaps?

<iframe width="800" height="600" name="all-days-overlap" src="heatmap_at_least_1_day_teams_vs_days.html" style="border:none;" ></iframe>


## Scenario 2: Collisions everyday

What is the probability that across a 5 day week **all** people are in the office on the same day for **all** of their required in office days.

For example, Peter & Benjamin are required in the office two days a week. What is the probability that they are both in on the same two days?

<iframe width="800" height="600" name="all-days-overlap" src="heatmap_all_days_teams_vs_days.html" style="border:none;" ></iframe>


# So, what did we learn?

There are many reasons for an in-office policy but if the objective of an RTO policy is for increased face to face collaboration then the maths is pretty clear; companies should be specifying which days to come in (or requiring 4 to 5 in office days)! Leaving it to random selection all but guarantees each day will be a hybrid with some people at home others at the office and lots and lots of Zoom calls! As the team size grows office overlap quickly hits zero...

So, if the goal is in-person collaboration then mandate the days else bin the RTO policy and come up with another way.
