# bike_hud
A mobile web app for tracking real time information on a bike. Flask backend, angular front end. Strava API.

## API

###routes:

#### / 
- get - index.html

#### /ride
- post - new ride posted to strava

#### /login
- post - login to existing account

#### /register
- post - create a new account

#### /strava
- post - login to strava to sync ride data
- put - update strava credentials

#### /spotify ? (may handle this all on front end through a widget - need to research)
- post - login to spotify?

## UI

### Views

#### Desktop 

The desktop view will consist of a simple landing page with info about the tech and the app. Possible include some 
information on further development goals. It will direct users to open the same page from their mobile devices. App 
will only run on mobile device in correct orientation.

#### mobile vertical

This will be where users log in. There is a simple message to the user that if they turn the device sideways that it 
will turn on the hud.

#### Mobile Horizontal

This will be the actual hud that responds live to the user. There will be a full screen speedometer, strava start 
button to begin tracking a ride, widget for listening to music possibly?