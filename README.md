# What is Quick IQ

Quick IQ is a mobile application project aimed at increasing the cognition level of children in the developmental age. It achieves this through games. At the same time, with the help of the voice assistant in the application, our child can consult and chat with the assistant while navigating the application.

## Quick IQ Bot Server Application

There is 3 part of Quick IQ application. The first one is frontend written with Flutter, second one is rest-api server connected to a sql database (mysql) written with nodejs, and lastly this project, bot server. 

1. [Quick IQ Flutter Application](https://github.com/DogukanTopcu/quick_iq_flutter)
2. [Quick IQ Nodejs MySQL Server](https://github.com/DogukanTopcu/quick_iq_server)
3. [Quick IQ Flask Bot Server](https://github.com/DogukanTopcu/quick_iq_bot_server)

Bot server allows the bot in the application interface to respond according to the user's actions and answers.


## How to run?

This is a flask project. You can find necessary information about flask in this link [here](https://flask.palletsprojects.com/en/3.0.x/quickstart/). 

`flask --app app run`
Running on http://127.0.0.1:5000
