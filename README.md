# The Backend Application for Helios
This project is the backend service for the helios writing app.


## Running the flask app locally
This microservice uses Python 3 and the Flask framework at its core. Prerequisites to running it locally are to have Python 3 installed along with the Flask package. Python uses virtual environments to manage the packages in different projects, so you'll want to make sure you have your environment(s) setup before running this project locally as well. You can use standard python environments in the terminal or Anaconda for environment management (I like Anaconda but this is personal preference).

### Linux/MacOS
1. Open up the project and go to the project's root directory ("helios_flask_app").
2. Use the command `EXPORT FLASK_APP=helios-app` to set the root app directory environment variable.
3. Use the command `EXPORT FLASK_ENV=development` to set the environment to development and allow for debugging mode.
4. Now you can run the app with the command `flask run`

***NOTE:*** If you're having trouble setting the flask environment variables as described above, you can use the Windows instructions below to run the project locally and it should still work ok.

### Windows
I'm still figuring out how to do this elegantly on Windows but the below method works for now:

1. Open up the project and go to the project's root directory ("helios_flask_app").
2. Run the command `flask --app helios-app run` to run the flask app locally.
    * This will run the app locally but not in Debug mode.