![The Jersey Bulletin](https://i.imgur.com/6orq2qv.png)
*CS490, Group 8 Final Project*

---
[Click here for a live deployment of the Jersey Bulletin!](https://jersey-bulletin.herokuapp.com/) -- **Please note:** You may have to wait a minute or two as well as refresh the page for the app to start up. This is due to the web server turning on via Heroku Dynos. After the initial start up, the web app will load normally!

The Jersey Bulletin is an open forum for New Jersey residents while also acting as a one stop shop for information you may need as a New Jersey resident. This web app will feature different tabs containing different information relating to different aspects of life in the Garden state. Some of the information we hope to relay to the user include weather, politics, traffic, and news. Along with this information, all tabs will also feature their own bulletin board. In order to add any messages to the bulletin board, you must sign in with your Google account via OAuth.

This Project allows you to post to launch a website that acts as a hub for NJ residents. To launch the app run the command `npm run build` to update your script.js and then run `python app.py` in order to run the app. If running `npm run build` asks you if you want to install `webpack-CLI` respond 'yes'.

# Installations and Technologies.
Before running this app, make sure you have all of the dependencies installed. All the dependencies are in the `requirements.txt` file, but all of these packages are not necessary.
1. Use the command `pip install` to install flask, coverage, pylint, pytz, black, tweepy, pyopenstates, and flask-socketio.
2. Use `npm` to install the heroku package, `npm install -g heroku`
3. It's recommended that you use the `Git CLI` in order to keep your code up to date.

## Database Setup
This web application uses `psql` as the database to provide persistence with the bulletin boards. In order to get psql to work with python, run the following commands:
1. `sudo yum update`, say yes for all the prompts.
2. `sudo pip install --upgrade pip`
3. `sudo pip install psycopg2-binary`
4. `sudo pip install Flask-SQLAlchemy==2.1`

If you have not already created a psql database, follow these steps in order to initialize one.

1. `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`, Enter yes to all prompts.    
2. `sudo service postgresql initdb`  
3. `sudo service postgresql start`    
4. Make a new superuser: `sudo -u postgres createuser --superuser $USER` 
5. Make a new database: `sudo -u postgres createdb $USER`   
6. Make sure your user shows up and make a new one:    
	1. `psql`    
	2. `\du` look for yourself as a user    
	3. `\l` look for yourself as a database 
	4. `create user [some_username_here] superuser password '[password]';` 
	5. Make sure you remember the quotes around password and the semicolon. 
		1. Check `\du` to ensure it worked.
	6. `\q` to quit out of psql

## API Keys
In order to get the modules to work correctly, you will need to register and obtain a few API Keys.
1. [OpenWeather API](https://openweathermap.org/) - This is used for the weather module, used for retrieval of up-to-date weather information.
2. [Geocodio API](https://www.geocod.io/) - This is used to retrieve the latitude and longitude for use with the OpenWeather API.
3. [GNews API](https://www.gnews.io/) - This is used to retrieve relevant New Jersey news.
4. [Google Maps API](https://developers.google.com/maps/documentation) - This is used to retrieve traffic related data from Google Maps.
5. [Twitter API](https://developer.twitter.com/en/apply-for-access) - This is used to retrieve tweets from New Jersey political figures.
	1. Go to https://developer.twitter.com/en/apply-for-access and apply for access.
	2. When you are approved, create a project and save your consumer key, consumer secret, access token, and access token secret.
6. [OpenStates API](https://v3.openstates.org/docs) - This is used for the modules for politician information and bill information.
	1. Go to the link above and click on "Register for an account".
	2. Follow the steps and click "Activate API Key"
7. [National Park Service](https://www.nps.gov/subjects/developer/get-started.htm) - used to retrieve NJ natinal parks information.
	1. Go to the link above and sign up by filling out your information.
	2. You will recieve an email containing your API key so this email safe and secure for your use

Create a file named `.env` and set it up as the following:
```
OPEN_WEATHER_API_KEY=<Open weather API Key Here>
GEOCODIO_API_KEY=<Geocodio API Key Here>
FREE_NEWS_API_KEY=<Gnews API Key Here>
DATABASE_URL=<URL to your psql database>
TWITTER_CONSUMER_KEY = "<Twitter consumer key>"
TWITTER_CONSUMER_SECRET = "<Twitter consumer secret>"
TWITTER_ACCESS_TOKEN = "<Twitter access token>"
TWITTER_ACCESS_TOKEN_SECRET = "<Twitter access token secret>"
GOOGLE_MAP_API_KEY=<Google map API Key Here>
POLITICS_API_KEY=<OpenStates API key Here>
NPS_API_KEY=<NPS API Key Here>
```

Note: Do not include quotes or the `<>` characters in the `.env` file.\
Optional, but you can run the command `source .env` to ensure the system has read the API Key variables.

## Setting up the clientside
There are a few commands you must run in order to ensure that the clientside will run properly.
1. `npm install`
2. `npm i nanoid`
3. `npm install -g webpack`
3. `npm i @material-ui/core`
4. `npm install webpack@next --dev`
4. `npm install --save-dev webpack`
5. `npm install --save google-map-react`



## Setting up testcases
If you wish to utilize test cases, enter the following commands to ensure you have the correct modules:
1. `pip install unittest`
2. `pip install requests_mock`

In order to run these tests, run `python unmocked_unit_tests.py` and `python mocked_unit_tests.py` to test the test cases in those files.

In order to view the code coverage, run the following commands in the directory:
1. `coverage run -m --source=. unittest tests/*.py`
2. `coverage html`
3. In the future, you can simply run ``coverage run -m --source=. unittest tests/*.py && coverage html`` to run both of these commands at the same time.

### Linting
If you wish to check the linting on this project, execute the following commands.
1. `pip install pylint`
2. `pip install black`
3. `npm install -g eslint`
4. `eslint --init`, select the following options.
	1. "To check syntax, find problems, and enforce code style"
	2. "Javascript modules (import/export)"
	3. "React"
	4. "No"
	5. "Browser"
	6. "Use a popular style guide"
	7. "Airbnb"
	8. "Javascript"
	9. When asked if you want to install dependencies with npm, say "Yes"
5. Run `eslint scripts/[FILE]` on any of the `.js/.jsx`  files in the scripts directory.
	1.  Run `eslint --fix scripts/[FILE]` in order to automatically fix some of the linting errors
6. Run `pylint [FILE]` on any of the python files.

### Heroku Deployment
   If you wish to deploy to heroku, log into heroku on your command line and run the 
      following commands to move your database over:
        0. If you do not already have a heroku project: `heroku create` and add your 
          keys to the config variables.
        1. `heroku addons:create heroku-postgresql:hobby-dev`
        2. `heroku pg:wait`
        3. `heroku pg:push postgres DATABASE_URL`
        4. `git push heroku master`

## Work Completed by Each Group Member
1. Ameer Hassan
	1. Create the weather widget and its functionality.
	2. Establish Google OAuth.
	3. Set up the Heroku deployment for the MVP deployment.
	4. Set up zipcode/city authorization for the weather.
	5. Create a list of city/zipcode pairs for authorization of NJ municipalities within the app.
	6. Create the personal tab and user account persistence for the personal tabs.
2. Joseph Fiore
	1. Create the Comment section and have it be different for every tab.
	2. Create the widget displaying tweets from political figures.
	3. Create widget displaying info on political figures.
	4. Create widget displaying bills up for vote.
	5. Allow for users to like and unlike comments.
	6. Show user's profile pictures when they log in.
3. Akash Patel
	1. Create the Traffic Widget so it shows a map of NJ and the traffic within.
	2. Create the page's landing page and set up that page's CSS.
	3. Create NJ National Park Widget and all the necessary features to make it usefull
	4. Combined both OAuth login button into one login modal
	5. Worked on storing use input in DB from the weather search bar for convenient 
	6. All of the my above features were tested and linted before launching
4. Karan Patoliya
	1. Add tab switching and the functionality therein.
	2. Give users the option of using FaceBook OAuth.
	3. Add search to traffic widget & make it responsive concurrent to weather search.
	4. Create the sports module with info on NJ sports team.
	5. Redesigning and setting up landing page.
5. Bishoy Kamel
	1. Create a widget to display local news stories using cache.
	2. Create news unit testing. 
	3. Create background gear feature to change colors and save to database. 
	4. Create header that appears when user scrolls up but will disappear when user scrolls down.
	5. Create footer to display information about us and usefull links for New Jersey Residents. 
6. Group Work
	1. Edit Proposal
	2. Establish and continuously update Kanban Board
	3. Work on the style of the site.
	4. Add content to the landing page.
	5. Find bugs and report them to the person who's work it applies to.
	6. Lint and test one anothers code.

## Technical Issues and Solutions
The comment section was having an issue where each tab was not recognizing different comment sections as different.
  This was solved by utilizing hooks to keep the comment sections as the same element that
  simply updates on a switched tab.
API Requests are incredibly frequent, making it likely we run out of requests often.
	This was solved by caching the results of API requests so a minimal amount of them occur.
The background button was by default set to the left where it was overlapping on the discussion tab.
	The solution was adjusting and moving the positions in multiple css files.
The news very rarley displayed the same articles multiple times, due to the api sending over that infomation.
	The solution for this was adding an if else statment that check if whats being added to cache is already there or not.
The comment section was having issues where they were getting the comments sent to all tabs.
  This was solved by utilizing rooms in the backend to ensure that comments were only sent 
  to users in one tab.

