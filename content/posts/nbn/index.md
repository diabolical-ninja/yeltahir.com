---
title: "Introducing NBN-Py"
date: 2022-06-11T00:00:00+11:00
draft: false

resources:
- name: featured-image
  src: nasa-Q1p7bh3SHj8-unsplash.jpg

toc:
  auto: false

---

For avid readers of this blog (there is one...right?) you’ll remember my quest to find a house and the [app built](https://www.yeltahir.com/posts/smart_property_search/) to help out. While building that I stumbled across a few references to an unofficial NBN API that could be used to determine the technology type present for a given address. I presume a nifty nelly reverse engineered one or some of the nbn [check your address](https://www.nbnco.com.au/connect-home-or-business/check-your-address) sites to figure them out.

These APIs proved incredibly useful and so it only seemed right to package them up and make it easier for the next hacker to grab them and use them in their project.

Introducing [nbnpy](https://nbnpy.readthedocs.io), a python library that wraps up these unofficial NBN API’s to help you better understand the NBN connection details for a given address.

{{< admonition type=success title="View the source" open=false >}}
NBN-Py is all open source: [NBN-Py](https://github.com/diabolical-ninja/nbnpy)
{{< /admonition >}}


{{< admonition type=warning title="Please Note" open=true >}}
This is an unofficial wrapper and thus not affiliated with the NBN.
{{< /admonition >}}



# So, what can it do?

First off we need to install the package:
```python
pip install nbnpy
```

There are two steps involved when using the NBN API; first we must identify the unique ID for a location and second we can look up the connection information using that ID.

Two methods are provided for retrieving the location ID:    
* via the address (`get_location_ids_from_address`)    
* via the longitude and latitude (`get_location_ids_from_lat_long`)
    
Lets do it:

```python
from nbnpy.nbn import NBN

nbn_client = NBN()
location_ids = nbn_client.get_location_ids_from_address("1 Flinders Street, Melbourne VIC")
```
    
Printing out `location_ids` we get:
```json
{
   "timestamp": 1654868885090,
   "source": "lapi",
   "suggestions": [
       {
           "id": "LOC000175010671",
           "formattedAddress": "Unit 1 32 Flinders St, Melbourne, VIC",
           "latitude": -37.81540657,
           "longitude": 144.97344433
       },
       {
           "id": "LOC000174955905",
           "formattedAddress": "Offc 1 52 Flinders St, Melbourne, VIC",
           "latitude": -37.81534233,
           "longitude": 144.97267563
       },
       {
           "id": "LOC000080310563",
           "formattedAddress": "Se 1 G 80 Flinders St, Melbourne, VIC",
           "latitude": -37.8158619,
           "longitude": 144.97204103
       },
       {
           "id": "LOC000175871974",
           "formattedAddress": "Shop 1 G 84 Flinders St, Melbourne, VIC",
           "latitude": -37.81589333,
           "longitude": 144.97177103
       },
       {
           "id": "LOC000122845440",
           "formattedAddress": "Unit 1 100 Flinders St, Melbourne, VIC",
           "latitude": -37.81610389,
           "longitude": 144.97143233
       }
   ]
}
```

After choosing the desired location ID we can then lookup the associated NBN connection information.

```python
location_info = nbn_client.location_information("LOC000175010671")
```

Which gives us:
```json
{
   "timestamp": 1654869030505,
   "servingArea": {
       "csaId": "CSA300000010316",
       "techType": "FTTC",
       "serviceType": "Fixed line",
       "serviceStatus": "available",
       "serviceCategory": "brownfields",
       "rfsMessage": "Sep 2018",
       "description": "Exhibition"
   },
   "addressDetail": {
       "id": "LOC000175010671",
       "latitude": -37.81540657,
       "longitude": 144.97344433,
       "reasonCode": "FTTC_SA",
       "altReasonCode": "NULL_NA",
       "techFlip": "",
       "serviceType": "Fixed line",
       "serviceStatus": "available",
       "disconnectionStatus": "PAST",
       "disconnectionDate": "Sep 2020",
       "techType": "FTTC",
       "formattedAddress": "UNIT 1 32 FLINDERS ST MELBOURNE VIC 3000 Australia",
       "address1": "Unit 1 32 Flinders St",
       "address2": "Melbourne VIC 3000 Australia",
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
       "coatChangeReason": "",
       "cbdpricing": true,
       "ee": true,
       "TC2SME": true
   }
}
```

We can see this place has a fibre to the curb (FTTC) connection. Great!


## Frustrated?
Keen observers may have noticed the key `frustrated`, a boolean field, in the response. While I have no idea what that refers to, thus far I’ve been unable to find a property where `frustrated == TRUE`...


# Happy Hacking
Hopefully this package makes life a little easier for the next person curious about their NBN connection.

If you run into any bugs or usability problems please [raise an issue](https://github.com/diabolical-ninja/nbnpy/issues) on the github repository. 

NBN-Py:
* Repository: https://github.com/diabolical-ninja/nbnpy
* Documentation: https://nbnpy.readthedocs.io
* Package on PyPi: https://pypi.org/project/nbnpy/

