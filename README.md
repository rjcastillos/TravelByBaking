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

        Step 1 
        #python3 scrapTBB.py
              CLI  output
                        at the end shows the new pages discovered
                        https://travelbybaking.com/converting-oven-temperatures/
                                New page found  https://travelbybaking.com/how-to-make-puff-pastry/

                                New page found  https://travelbybaking.com/delicious-and-easy-cottage-cheese-pancake-recipe/

                                New page found  https://travelbybaking.com/easy-and-tasty-cabbage-pie/

                                New page found  https://travelbybaking.com/homemade-cottage-cheese/

                                New page found  https://travelbybaking.com/leek-tart-with-puff-pastry/
                Leaving the new entries in the file
                linkstoupdate.txt
        Step 2
                #python3 html2json.py
                Input is the file created in step 1 linkstoupdate.txt
                creates a new .json file "newallRecipesData.json" 
                also could append the new objects to the existent .json
                
        Step 3
                make sure the ThumbNails exist
                If the new recipes were not appended using the script in Step 2 , these have to be appended manually in "allRecipesData.json"
        
        To update the recipes by categories we need to run the JS in the Web location

        
        





