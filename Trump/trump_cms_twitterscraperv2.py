import twint

c = twint.Config()

c.Search = ['vaccine']       # topic
c.Limit = 100     # number of Tweets to scrape
c.Since = '2020-01-01'
c.Min_likes = 5000
c.Lang = 'en'
c.Store_csv = True       # store tweets in a csv file
c.Output = "vaccine.csv"     # path to csv file


twint.run.Search(c)
