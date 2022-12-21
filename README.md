# TwitterScraper
a Twitter post scraping bot that collects posts and dumps them to a database for later data analysis

to use first create a directory to clone the repository into
```
mkdir twitter_scraper_directory
```
navigate to the new directory you just created and clone the repo into it with 
```
cd twitter_scraper_directory
git clone https://github.com/SeanRogan/TwitterScraper
```
create a private.py file with ```touch private.py``` to store sensitive information. then use the ```pip install requirements.txt``` command to install required packages

# Sensitive Information
this scraper requires several sensitive pieces of information to be use in the code. API keys and secrets, and a database connection string with the username and password visible. To keep things separate, the application calls these strings from a private.py file. the file should look like this:
```
# the following value are fake placeholders, make sure you replace them with your real API and DB credentials
# API key and secret
TWITTER_API_KEY = "V232tVWWrhberbbreRDvvfdbtneBFFDBvvvw"
TWITTER_API_SECRET = "SGW$V#2f32vwv3VW#@#V#@@V@Gu"
# App Access token and secret
TWITTER_APP_KEY = "32fjocuuhuSGWFhc3g8bSWFEW8b326888fg1"
TWITTER_APP_SECRET = "Ndfsjdlkfj3ipfjc0208uf32j000"
# twitter bearer token
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAAKsdhasdqwo3u0u0EFJeeJJF#@Fhfhqi3fhoqh3ofCAHFEhc3qihcqihiohaiohcaoihoih2oqhcqo"
# Db connection string
CONNECTION_STRING = 'postgresql://name:pass@scraperstorage.blahblah23912.us-east-1.rds.amazonaws.com:5432/data'
```
# Twitter API Credentials
To use the scraper youll need to sign up for a twitter developer account here https://developer.twitter.com , to get an API key and secret, an Application token and token secret, and a bearer token. These all go into the private.py file. the api key and secret belong in the TWITTER_API_* variables, the application token and secret belong in the TWITTER_APP_* variables.

# Data Storage
The scraper is made to work with a postgresql database. If you have a database simply add your connection string in the private.py file. the database connection string format for postgresql is as follows:  
## postgresql://username:password@hostname:port/dbname 



