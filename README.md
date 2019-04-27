# rasa-latest(v 0.11.3) - please note the repository is old and not maintained, so it is not the latest version anymore
Simple demo to demonstrate the rasa core's version 0.11.3 

The steps are very simple. make sure you have docker installed

```
docker-compose up --build

```

You have to add your credentials file that should look like this

```
rest:
facebook:
  verify: "rasa-bot"
  secret: "yoursecret"
  page-access-token: "yourpageaccesstoken"
```
follow this guide to know how to setup channels using Rasa
https://rasa.com/docs/core/connectors/ 

Brief Information about the stack

You have three folders here

- actions -- this contains the actions.py and docker container that spins up the action server. I have used rasa_core_sdk to bootstrap the custom action development
- nlg -- this contains the templating engine and docker container that starts the nlg server. You can use your own NLG engine here
- data -- contains the training data and trained models. 
