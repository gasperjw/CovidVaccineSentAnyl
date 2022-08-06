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

![Screen Shot 2022-08-06 at 8 01 54 AM](https://user-images.githubusercontent.com/94769763/183249977-744e8755-7c33-4273-a745-eb26b2007e23.png)

## Sentiment Anyalsis
For sentiment Anyalsis, I tried multiple things. 

I used TextBlob's natural language kit in order to try to calculate a sentiment score, however, I felt like it was unreliable. So after I tried using Vaders, however, was not a keen fan of it either. Because of that, I created my own model using Tensorflow. 

![Screen Shot 2022-08-06 at 8 01 30 AM](https://user-images.githubusercontent.com/94769763/183249984-0104463b-9d88-4121-9673-a2022f08bcb5.png)

However, as you can see here, the model's prediction on the test was pretty terrible. The big problem was my dataset. Text anylasis takes a lot of data in order to become accurate, and I did not want to go through thousands of tweets and hand classify them to get a good training data set. So I opted for _Crystalfeel _.

CrystalFeel is Multidimensional Emotion Intensity Analysis from Natural Language. CrystalFeel is a collection of machine learning-based emotion analysis algorithms for analyzing the emotional-level content from natural language. CrystalFeel produces multiple psychologically meaningful analytic outputs based on a multi-theoretic conceptual ground in emotion type, emotion dimension, and emotion intensity. It is developed by researchers studying affective and social intelligence from A*STAR's Institute of High Performance Computing.

Their online platform has 

