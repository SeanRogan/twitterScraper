# Twitter Scraper
a Twitter post scraping service that collects posts and dumps them to a database for later data analysis. 

# Pre-Requisites
The service is built with python 3.10, and uses a PostgreSQL database of the latest stable version. It also requires several python packages as dependencies, they will be installed upon using the run_script.sh or you can install manually following the instructions below.

#Install
to install and use the service, first create a directory to clone the repository into
```
mkdir twitter_scraper_directory
```
navigate to the new directory you just created and clone the repo into it with 
```
cd twitter_scraper_directory
git clone https://github.com/SeanRogan/twitterScraper
```
create a private.py file with ```touch private.py``` to store sensitive information. then use the ```pip install requirements.txt``` command to install required packages. Then you can open private.py in the text editor of your choice, and add your information as instructed below.

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
### postgresql://username:password@hostname:port/dbname 

# How to set up for your first scrape

Once you have your scripts all in the same directory and a database is running and ready to connect to your machine, all you have to do is edit the settings.py file to add or change the search terms you want to use. Up to 5 search "rules" are allowed with the basic free usage plan twitter offers. Rules can be simple search terms, or special strings that perform filter based on hashtags, presence of media or images, or other criteria, with examples like ```"cat has:media -grumpy"``` or ```"#nowplaying (happy OR exciting OR excited OR favorite OR fav OR amazing OR lovely OR incredible) (place_country:US OR place_country:MX OR place_country:CA) -horrible -worst -sucks -bad -disappointing"```
See the twitter api documentation on creating rules to filter the stream of tweets here https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule.
Rules should be entered into the settings.py STREAM_FILTER_RULES list as a string. Once your settings and private files are filled in with your information, just run the start script to start the scraper, which will save the table as a csv file every night at midnight. You can adjust the time and frequency that happens by changing the chron job settings in start_script.sh. you can also just run the script standalone with ```python scraper.py```
# Happy Scraping 🎅🏻
