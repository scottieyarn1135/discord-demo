# Discord bot

I have been working on a discord bot I have done this to get some experience around working on a python framework and dockerizing my applications. 

The current features of the bot:
```
/random_quote -> Makes an enbeded message with a random quote from quote api
```

```
/quote_of_the_day -> gets the quote of the day from quote api
```
```
/space_picture_of_the_day -> This will give a small description from the nasa api and it will provide the link to the image or youtube video (This would also show the image but I removed it while I work on a fix incase nasa include a youtube link instead which is an edge case)
```
```
/pokepicker <pokemon name> <Shiny or you would leave it blank>
If you wanted a normal pikachu it would be the following commands: /pokepicker pikachu
If you wanted a shiny pikachu it would be the following commands: /pokepicker pikachu shiny
```

# Deployment

This was made with docker in mind I am assuming you are used to docker as a tool

you have also set up both a discord bot and you have the api key and you have a nasa api key
<a href="https://www.freecodecamp.org/news/create-a-discord-bot-with-python/">Follow the start of this page to learn how to make an api key for the discord</a>
<a href="https://api.nasa.gov/">Link to request a nasa api key</a>
To run on a local server or testing locally
```
Make sure you are in the directory.
docker build -t discord-bot .
docker run -e DISCORD_TOKEN=<discord-api-key> -e NASA_KEY=<nasa-api-key> discord-bot
```

the second option or if you do not want to host it locally you can host it on a cloud provider such as AWS, GCP or Azure just make sure you set the environment variables when deploying.
