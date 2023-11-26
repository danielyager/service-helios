# The Backend Application for Helios
This project is the backend service for the helios writing app.


## Running the flask app locally
This microservice uses Python 3 and the Flask framework at its core. Prerequisites to running it locally are to have Python 3 installed along with the Flask package. Python uses virtual environments to manage the packages in different projects, so you'll want to make sure you have your environment(s) setup before running this project locally as well. You can use standard python environments in the terminal or Anaconda for environment management (I like Anaconda but this is personal preference).

### Linux/MacOS
1. Open up the project and go to the project's root directory ("helios_flask_app").
2. Use the command `EXPORT FLASK_APP=helios_app` to set the root app directory environment variable.
3. Use the command `EXPORT FLASK_ENV=development` to set the environment to development and allow for debugging mode.
4. Use the command `EXPORT DATABASE_URI=`*DATABASE_URI_VALUE*  where *DATABASE_URI_VALUE* is listed in the Google Drive for you to use.
5. Now you can run the app with the command `flask run`


### Windows
1. Open up the project and go to the project's root directory ("helios_flask_app").
2. Use the command `$env:FLASK_APP="helios_app"` to set the root app directory environment variable.
3. Use the command `$env:FLASK_ENV="development"` to set the environment to development and allow for debugging mode.
4. Use the command `$env:DATABASE_URI=`*DATABASE_URI_VALUE*  where *DATABASE_URI_VALUE* is listed in the Google Drive for you to use.
5. Now you can run the app with the command `flask run`