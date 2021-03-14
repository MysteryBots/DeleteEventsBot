# Delete Events Bot
> A star ⭐ from you means a lot to us! 

<p align="center"><a href="https://www.github.com/MysteryBots/DeleteEventsBot"><img src="https://telegra.ph/file/b171755f0b48b67de0e56.jpg" width="5000"></a></p>


Telegram bot to delete service messages in groups.

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

<details open="open">
  <summary> Table of Contents</summary>
  <ol>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#deploy-to-heroku">Deploy To Heroku</a></li>
        <li><a href="#local-deploying">Local Deploying</a></li>
      </ul>
    </li>
    <li>
      <a href="#environment-variables">Environment Variables</a>
      <ul>
        <li><a href="#mandatory-vars">Mandatory Vars</a></li>
        <li><a href="#optional-vars">Optional Vars</a></li>
      </ul>
    </li>
    <li><a href="#functions">Functions</a></li>
    <li><a href="#to-do">To-Do</a></li>
    <li><a href="#stats">Stats</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#credits">Credits</a></li>
    <li><a href="#support">Support</a></li>
  </ol>
</details>


## Usage

### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/MysteryBots/DeleteEventsBot)

1) Tap on above button and fill `API_ID`, `API_HASH`, `BOT_TOKEN`. Alternatively fill `OWNER_ID` and `OWNER_NAME`. 
Note : Fill both or leave both unless bot won't work.
2) Then tap "Deploy App" below it. Wait till deploying is complete (will take atmost 2 minutes). 
3) After deploying is complete, tap on "Manage App"
4) Check the logs to see if your bot is ready! 

### Local Deploying
1) Clone the repo
   ```markdown
   git clone https://github.com/MysteryBots/DeleteEventsBot
   ```
2) Edit `Config.py` and fill the needed variables by following [this](https://github.com/MysteryBots/DeleteEventsBot/blob/master/Config.py#L11) 

3) Enter the directory
   ```markdown
   cd DeleteEventsBot
   ```
4) Run the file
   ```markdown
   python3 delevents.py
   ```

## Environment Variables
#### Mandatory Vars
- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth) or [@TgOrgBot](https://t.me/TgOrgBot) 
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth) or [@TgOrgBot](https://t.me/TgOrgBot) 
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather) 
#### Optional Vars 
> (fill both or neither)
- `OWNER_ID` - Get it from [@MissMiley_bot](https://t.me/MissMiley_bot) by sending /id to it.
- `OWNER_NAME` - Your Name (to be shown as owner in bot)


## Functions
> More features soon, this is an minimal example :) 
1) Delete Telegram Service Messages like "joined", "left", "pinned", etc.
2) Specify owner's account to get help or something.

## To-Do
> That's on you mainly...
1) Add DB to specify what to delete and what not to.
2) Show owner his/her bot's stats.

## Stats
[![GitHub forks](https://img.shields.io/github/forks/MysteryBots/DeleteEventsBot.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/MysteryBots/DeleteEventsBot/network/) [![GitHub stars](https://img.shields.io/github/stars/MysteryBots/DeleteEventsBot.svg?style=social&label=Star&maxAge=2592000)](https://github.com/MysteryBots/DeleteEventsBot/stargazers/) [![GitHub watchers](https://img.shields.io/github/watchers/MysteryBots/DeleteEventsBot.js.svg?style=social&label=Watch&maxAge=2592000)](https://github.com/MysteryBots/DeleteEventsBot/watchers/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/MysteryBots/DeleteEventsBot/graphs/commit-activity)



## License
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)


## Contributing
[![GitHub contributors](https://img.shields.io/github/contributors/MysteryBots/DeleteEventsBot.svg)](https://github.com/MysteryBots/DeleteEventsBot/graphs/contributors/)
> Contributions are heartily accepted. 

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Credits
- [Dan Tès](https://github.com/delivrance) for his [Pyrogram](https://docs.pyrogram.org) Library

## Support
Channel :- [@MysteryBots](https://t.me/MysteryBots)

Group Chat :- [@MysteryBotsChat](https://t.me/MysteryBotsChat)

## :) 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/MysteryBots) 

[![ForTheBadge makes-people-smile](http://ForTheBadge.com/images/badges/makes-people-smile.svg)](https://github.com/MysteryBots)


