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

CrystalFeel is Multidimensional Emotion Intensity Analysis from Natural Language. It uses a collection of machine learning-based emotion analysis algorithms for analyzing the emotional-level content from natural language. CrystalFeel produces multiple psychologically meaningful analytic outputs based on a multi-theoretic conceptual ground in emotion type, emotion dimension, and emotion intensity. It is developed by researchers studying affective and social intelligence from A*STAR's Institute of High Performance Computing.

Their online platform has a "Try Your Text" option - so I created a web bot that would automatically take the tweets I had scraped entered it and take the results. Here is an example: 
![Screen Shot 2022-08-09 at 6 10 13 PM](https://user-images.githubusercontent.com/94769763/183777200-4c657c9a-22d6-4944-afd1-2b35c9ae8f8e.png)

While this is not good to determine public opinion of whether people are PRO Vaccine or NEG vaccine(I cannot tell if the tweet is PRO or NEG vaccine based off sentiment score), it does tell how the public feels overall towards vaccines in general. Are people mostly optimistic when talking about vaccines, or are they angry? This is the type of question that can be answered through this method, however, it was not the main focus of the project so we scrapped the idea. 

## Anylasis 
We decided to then to just hand rate whether a tweet was pro or neg vaccine for the top 100 tweets with the most likes. We did this because  popular tweets because, instead of just 100 tweets with one or two likes, we had about 1.4million interactions on twitter on this topic.

Based off just counts:
![Screen Shot 2022-08-09 at 6 16 46 PM](https://user-images.githubusercontent.com/94769763/183777918-a04693c0-ad73-4a4b-800d-554ecac12ad5.png)

When Adding Likes as Weight: 
![Screen Shot 2022-08-09 at 6 16 40 PM](https://user-images.githubusercontent.com/94769763/183777957-ed3b2ede-1bf0-4b1e-a34e-a8910f35aa37.png)

![Screen Shot 2022-08-09 at 6 18 38 PM](https://user-images.githubusercontent.com/94769763/183778000-daa1d09f-e9b1-429f-9eb6-be1380ca2bb5.png)

We found that in count NEG vaccine tweets heavily dominate, however, when adding likes they are almost 50/50. This probably has to do with the concept in Public Opinion of "who shares their opinion" and what it means to like a tweet vs to actually tweet something yourself. 

## Comparasion to Public Polling Data 
Kaiser Family Foundation 2021 Monthly Vaccine Monitor 
Question we focused on: “Have you personally received the COVID-19 vaccine or not?”
Chosen because sample size is consistent, source is credible and the method measures actions regarding subject
![Screen Shot 2022-08-09 at 6 23 38 PM](https://user-images.githubusercontent.com/94769763/183778436-ba1ad52d-7b41-40b0-b310-ba301fe11e5f.png)

Public polling data tells us that people against the vaccine are in the minority, however Twitter data with weight tells us that it’s closer to a 50/50 split. Twitter data without weight tells us a majority are against. 

## Other Research 

Policy Change and Public Opinion: Measuring Shifting Political Sentiment With Social Media Data

Nicholas Adams did a research study in 2020 using Twitter data and machine-learning methods to analyze the causal impact of the Supreme Court’s legalization of same-sex marriage at the federal level in the United States on political sentiment and discourse toward gay rights.Throughout this research study, the individuals analyzed the public opinion after the Supreme Court’s decision to legalize same-sex marriage across the fifty states. 

https://journals.sagepub.com/doi/abs/10.1177/1532673X20920263


