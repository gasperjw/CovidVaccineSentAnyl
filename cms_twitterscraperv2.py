#AhmedSameer CMS Project
import twint

c = twint.Config()

c.Search = ['Vaccine']       # topic
c.Limit = 1000      # number of Tweets to scrape
c.Since = '2021-01-01' #tweets since
c.Until = '2021-12-31' #tweets until
c.Lang = 'eng' #gives english
c.Verified = 'True' # verified users
c.Min_likes = 5000
c.Store_csv = True       # store tweets in a csv file
c.Output = "famoustweets.csv"     # path to csv file


twint.run.Search(c)




