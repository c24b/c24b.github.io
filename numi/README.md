# Webscrapping and datamining Genomics Wiki

Introduces: requests, beautifulsoup, regex.

Author(s): @c24b

This exercice will introduce you a want to constitue datasets over the web.
 
During this exercices you will create datasets to mine and query based on a specific website called www.openwetware.org.
It will be an introduction to web scrapping and datamining techniques using:
* Requests to get webpages
* BeautifulSoup /lxml to extract interesting data
* Json or csv to store and manipulate data
* Pyplot to visualize the data

You will have to extract collect and manipulate the data from this website in order to answer a few questions: 
First you will have to build a little program that go for page to page colecting the data and be able to answer such questions as:
* How many user in this wiki?
* How many groups?
* How many labs?
* Which group is the more active on this wiki?
* Which lab is the more active on this wiki?
* What are the interactions between user, groups and labs?

We will use 3 different entry points in the website in order to mine user activity on the website:
- http://www.openwetware.org/index.php?title=Special:ListUsers&limit=5000
- http://www.openwetware.org/wiki/Groups
- http://www.openwetware.org/wiki/Labs



