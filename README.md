# [TravelByBaking](https://travelbybaking.com)
Online presence maintenance and upgrades


Project DashBoard
https://rcastillo-team.atlassian.net/jira/software/projects/TBB/boards/4

Exploratory and work in pogress Data Model 

https://dbdiagram.io/d/TbyB-Data-Model-6697d49a8b4bb5230e99e08a



TravelByBaking/scrapTBB.py  : 
==========================
 Scraps the website
 Extracts all the links
 If the link is whitin the same site goes a level deep
 Compares all the links in the current run with the previous
 If the recently extracted link is new (is not in the old file), appends it into the new links to convert to .json.

 TravelByBaking/html2json.py
 ===========================
 Reads as an input a file containning links (normally the new ones from (scrapTBB.py)
 Based on Xpath, or classes maps the html content to .json objects.


TravelByBaking/updateindex.py
=============================

Manipulates an exitent .json files
Supports 3 ways to update a .json file:
    
    1 Reads a .json file containing a list (array) of objects (Dict) with changes
            taking the recipe to modify as a part of the input 
            and then the key and value to change
    2 Reads a .json file containing a Dict (Object) or Arrays to directly
            change existents key , value , these might be Arrays (Lists) or Objects (Dicts)
    3 Reads a .json file containing  a new Object or Array to append to all the existents recipes
    

    Examples:



