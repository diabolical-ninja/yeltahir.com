---
title: "Smarter Property Search"
date: 2021-04-11T00:00:00+11:00
draft: true

toc:
  auto: false

mermaid: true
---

In 2020 I decided it was time to fulfil the great Australian dream and buy a house. After not long on the classic property listing portals it became readily apparent that they could not answer the questions I wanted answered. Which homes have proper internet? Can I get to work within 10min? 30min? This led to the only solution a technologist knows; to throw my hands in the air and say “welp, guess I’ll have to build it myself!”. 

I setout to build a simple API that, given a collection of search parameters, would return the house of my dreams! Here's what a build!


{{< admonition type=success title="View the source" open=true >}}
If you'd like to give this project a whirl it's all open source: [Smart Property Search](https://github.com/diabolical-ninja/smart-property-search)
{{< /admonition >}}

### Just before we get started

The obvious question upfront is "why don't the big players build this?"

These sites provide a nice example of the difference between a user and a customer or the now classic saying "if you're not paying for it you are the product". People looking to buy, sell or rent may be the primary site users but it’s the folk making, and paying for, the listing that are the real customers as they bring in the revenue. If you as a user could craft the perfect query and they then returned your perfect home first try there’d be little desire to spend time on the site and thus little desire for the agents to list. These 


# Cutting to the chase....

### Did it work?

Yes indeed. The house I bought was one of only a few left after all the filters did their business.

### Did it save time?
Also yes. Setting aside the initial development effort it enabled me to spend considerably less time trawling through listings on property sites, cross referencing against google maps and so on. 

### Will it get used again?
While I’m in no rush to move (or buy) again, whenever that happens this app will absolutely get a whirl. Being open source I hope others also use it, abuse it and get value out of it’s utility as well.



# What Was Built?

While there was a long list of desired attributes an overwhelming requirement was “can I get this via an API?”. With that I compiled features to start building out.

## What’s Available?
Before any fancy filtering can be made I had to first know what properties were available. Thankfully the Domain Group have a fantastic [public API](https://developer.domain.com.au/) to retrieve and filter property listings. Together with their generous enough free tier and very handy swagger documentation, this would form the basis of the application.

## Filter, filter, filter



### Travel Time
I hate the commute, the less time on it the better. I’d much rather spend that time doing anything else; going for a walk, snoozing, working, anything really. This meant that travel time, rather than distance, was key. Being near a train station a couple of suburbs out is more important to the commute than being in an inner city suburb with no public transport insight. 

To simplify and semi-standardise the calculation, a couple of assumptions were made:
1. Public transport was the assumed mode of transport, in particular train and tram only. Also, the fewer changes the better.
2. The desired arrival time is always 9am the next business day.

With those criteria in place, travel time is calculated for each property using the google maps API, in particular the [distance matrix API](https://developers.google.com/maps/documentation/distance-matrix/overview) which allows for calculating the travel time for a matrix of origins and destinations rather than one by one.


### Property Attributes

On most of the major property listing sites you’ll see options to filter by attributes such as whether or not it has air conditioning or a pool but so often they fail as those submitting the listing choose not to assign those attributes and instead spell it out in the description. 

This filter simply compares both the tagged property attributes and runs a keyword search across the detailed description to determine whether that attribute is present. This is represented by the [filter_parameter.yml](https://github.com/diabolical-ninja/smart-property-search/blob/master/src/filter_parameters.yml) that allows for arbitrary addition of search terms to filter against.

```yaml
features:
  AirConditioning:
    domain: 
      - AirConditioning
    desc: 
      - air conditioning
      - a/c
      - aircon
      - cooling
      - airconditioning
  Feature2:
    domain:
        - something
        - ...
    desc:
        - term1
        - term2
        - ...
```


### NBN

[View Source](https://github.com/diabolical-ninja/smart-property-search/blob/master/src/nbn.py)

Unfortunately for Australia our broadband infrastructure was turned into a political football and kicked around at the whim of different governments. This has resulted in a patchwork of technologies across the country and thus a bit of a lucky dip as to how future proof your NBN technology will be. The ideal home would have fibre to the premise (FTTP).

There is an unofficial API available from the NBN that can help with this search. For any given address two calls are required:
1. **Get Location ID**
    Each property has a unique NBN location ID used to retrieve the technology type. This ID can be requested using either the street address or latitude + longitude coordinates. 
2. **Get Location Details**
    With the location ID we can now request the location details which include information about the connection date, status and most importantly the connection type which can then be used to filter on. 

{{< admonition type=info title="The Frustrated NBN" open=false >}}
Amongst the keys returned by the location API there is one called `frustrated`, a Boolean field. Thus far I’ve been unable to find a property where `frustrated == TRUE`...

```json
{
    "timestamp": 1618113620795,
    "servingArea": {
        "csaId": "CSA300000010316",
        "techType": "FTTB",
        "serviceType": "Fixed line",
        "serviceStatus": "available",
        "serviceCategory": "brownfields",
        "rfsMessage": "Sep 2018",
        "description": "51 SPRING ST MELBOURNE, VIC 3000"
    },
    "addressDetail": {
        "id": "LOC000057978100",
        "latitude": -37.81394807,
        "longitude": 144.9738317,
        "reasonCode": "FTTB_CT",
        "techFlip": "",
        "serviceType": "Fixed line",
        "serviceStatus": "available",
        "disconnectionStatus": "PAST",
        "disconnectionDate": "Sep 2020",
        "techType": "FTTB",
        "formattedAddress": "UNIT 81 51 SPRING ST MELBOURNE VIC 3000 Australia",
        "address1": "Unit 81 51 Spring St",
        "address2": "Melbourne VIC 3000 Australia",
        "statusMessage": "connected-true",
        "frustrated": false,
        "zeroBuildCost": true,
        "wp1DisconnectionDate": "11 September 2020",
        "wp1DisconnectionStatus": "PAST",
        "wp2DisconnectionDate": "11 September 2020",
        "wp2DisconnectionStatus": "PAST",
        "wp3DisconnectionDate": "11 September 2020",
        "wp3DisconnectionStatus": "PAST",
        "wp4DisconnectionDate": "11 September 2020",
        "wp4DisconnectionStatus": "PAST",
        "speedTierAvailability": true,
        "eec": 1,
        "cbdpricing": true,
        "ee": true,
        "TC2SME": true
    }
}
```

{{< /admonition >}}



### Walkability 

[View Source](https://github.com/diabolical-ninja/smart-property-search/blob/master/src/walkscore.py)

For me, the way local residents interact with their surrounds really helps to shape the feel of a community. The local cafes or artisan produce stores, spending time in the local parks, walking from place to place rather than driving. These all combine to give a community an energy and an identity.

Building out an accurate representation of these features into a single, filterable score is a difficult task. Fortunately the folks over at [Walk Score](https://www.walkscore.com/) have condensed attributes such as the availability of restaurants, public transport, schools and the like into a single walkability score. For this application the walkability score will be a sufficiently good proxy for those features to filter against.


## Sticking it all together

Putting it all together we get the following sequence of events.

{{< mermaid >}}

sequenceDiagram
    participant App
    participant Domain
    participant gm as Google Maps
    participant NBN
    participant ws as Walk Score

    %% All Listings
    App->>Domain: Request All Listings
    Domain-->>App: 

    %% Travel Time
    App->>gm: Request Travel Time
    gm-->>App: 

    activate App
        App->>App: Filter by travel time
    deactivate App

    %% Enriched Listings
    loop Request Full Listing Details
        App->>Domain: 
        Domain-->>App: 
    end

    activate App
        App->>App: Filter by desired attributes
    deactivate App

    %% NBN
    loop Request NBN Type
        App->>NBN: 
        NBN-->>App: 
    end

    activate App
        App->>App: Filter by NBN Technology Type
    deactivate App


    %% Walkscore
    loop Request Walkscore
        App->>ws: 
        ws-->>App: 
    end

    activate App
        App->>App: Filter by desired attributes
    deactivate App

{{< /mermaid >}}


# What does it look like in action?

Let’s say we’re a high roller, have a bunch of money to spend and want a penthouse in the heart of Melbourne. We start by collecting our request parameters:

```json
{
    "domain": {
        "listingType": "Sale",
        "propertyTypes": [
            "Penthouse",
            "ApartmentUnitFlat"
        ],
        "minBedrooms": 4,
        "minBathrooms": 3,
        "minPrice": 2000000,
        "locations": [
            {
                "state": "VIC",
                "postcode": "3000"
            }
        ]
    },
    "filters": {
        "travelTime": {
            "destinationAddress": "Spring St, East Melbourne VIC 3002",
            "maxTravelTime": 30
        },
        "features": [
            "Outside"
        ],
        "nbn": [
            "FTTP",
            "FTTB"
        ],
        "walkscore": 90
    }
}
```

Sending this off to the API, we then get:
```json
[
    {
        "listing": {
            "id": 2016620490,
            "listing_slug": "7306-228-la-trobe-st-melbourne-vic-3000-2016620490",
            "price": "$2,700,000",
            "address": {
                "displayable_address": "7306/228 La Trobe St, Melbourne",
                "postcode": "3000",
                "state": "VIC"
            },
            "property_details": {
                "property_type": "ApartmentUnitFlat",
                "features": [
                    "AirConditioning",
                    "BuiltInWardrobes",
                    "Ensuite",
                    "Floorboards",
                    "InternalLaundry",
                    "SecureParking",
                    "SwimmingPool",
                    "CityViews",
                    "Intercom",
                    "BroadbandInternetAccess",
                    "Bath",
                    "Dishwasher",
                    "Study"
                ],
                "bathrooms": 4.0,
                "bedrooms": 4.0,
                "carspaces": 2
            }
        },
        "travel_details": {
            "distance": "1.42km",
            "travel_time": "4.83mins"
        },
        "nbn": "FTTP",
        "walkscore": {
            "walkscore": 99,
            "summary": "Walker's Paradise",
            "transit": {
                "score": 100,
                "description": "Rider's Paradise",
                "summary": "105 nearby routes: 49 bus, 56 rail, 0 other"
            }
        }
    },
    {
        "listing": {
            "id": 2016212479,
            "listing_slug": "7206-228-la-trobe-street-melbourne-vic-3000-2016212479",
            "price": "$2,500,000",
            "address": {
                "displayable_address": "7206/228 La Trobe Street, Melbourne",
                "postcode": "3000",
                "state": "VIC"
            },
            "property_details": {
                "property_type": "ApartmentUnitFlat",
                "features": [
                    "AirConditioning",
                    "BuiltInWardrobes",
                    "Floorboards",
                    "SwimmingPool",
                    "CityViews",
                    "Gym",
                    "Bath",
                    "Dishwasher",
                    "OutdoorSpa"
                ],
                "bathrooms": 4.0,
                "bedrooms": 4.0,
                "carspaces": 2
            }
        },
        "travel_details": {
            "distance": "1.42km",
            "travel_time": "4.83mins"
        },
        "nbn": "FTTP",
        "walkscore": {
            "walkscore": 99,
            "summary": "Walker's Paradise",
            "transit": {
                "score": 100,
                "description": "Rider's Paradise",
                "summary": "105 nearby routes: 49 bus, 56 rail, 0 other"
            }
        }
    }
]
```

Fantastic! Only two places we need to inspect...and $2m to find!

{{< admonition type=note title="What’s the URL?" open=true >}}
The domain API is limited to 500 calls a day under the free tier, and given the chatty nature of the app these get chewed up quite quickly. If you’d like to give it a try you'll need the following items to get up & running:
* An AWS account
* A Domain Developer Portal Account
* Google Maps API token
* Walkscore API Token

{{< /admonition >}}


# Upgrades

## So Chatty
You’ll notice the app is quite chatty. In order to get the full listing details, NBN info and Walk Score the app currently sends each request one by one, adding up to hundreds of requests if there are many properties to be considered. Ideally the API providers would offer a mechanism to bulk request the information, significantly reducing the number of calls required. In the absence of that parallelising the calls could provide meaningful speed ups albeit at the risk of abusing their services.


## New Features
Beyond making the app more efficient there are a number of additional data points that would be great additions. The ones at the top of the queue are:
* Filter on school zone
* Support for multiple destinations & way to optimise the acceptable time and distance between them
* Market performance such as capital growth, rental yield, etc