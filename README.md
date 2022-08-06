# Twitter Covid Vaccine Sentiment Anylasis

The ability to quickly retrive thousands of tweets and perform sentiment anylasis on them has intrigued researchers on the possibility of using twitter to measure public opinion. In this project, I try to determine whether using Twitter is an accurate form of measuring public opinion on a given topic. 

Managed a team of 3 using NLTK to run sentiment analysis on tweets related to receiving the COVID vaccine.

## About this project
This was the first data-science  project that I had worked on. Orginally, it was for my public opinion communications class; the expectation was something not techinal at all. However, as I was getting interested in the field, I wanted to see what I could do. 

## Workflow
The idea behind the project was simple. Scrape a bunch of tweets, perform sentiment anylasis on them, and then compare to polling data. 

## Scraping the tweets
I had multiple methods of scraping tweets. 
1. Creating my own webscraping using Selimun webdriver
2. Using Twitter's API 
3. Using Twint library

Though having looked into (and doing) all of these options - for the project I decided to go with using the Twint library. I decided to focus on covid vaccines because not only is there a lot of polling data (important to measure tweets) - but there is a plethora of tweets out there.

Other criteria: The tweets had to be between Jan 2021 and Dec 2021. They had to have more than 5,000 likes. Had to be a verified user. 

## Workflow

