![GitHub last commit](https://img.shields.io/github/last-commit/PiShock-Inc/TransforMate)
[![CodeQL](https://github.com/PiShock-Inc/TransforMate/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/dorythecat/TransforMate/actions/workflows/github-code-scanning/codeql)

# TransforMate
> A bot to Transform your Mates

## Who's this bot for?
Ever felt like Tupperbox and PluralKit weren't enough for your RPs? Ever felt
like you needed to spice them up, transforming your friends and family? Well,
look no further! With TransforMate, this task is made much simpler!

## Current Features
### For users:
- Transform yourself and others
- Go back and forth with a single command
- Highly customizable and modular
- Straightforward to use and understand
- Well-documented, open-source, and in active development and support
- Friendly, helpful, and active community
- Free to use
- No ads, no tracking, no selling of data
- Cohesive, easily understandable documentation, with tutorials
- [Free webpage to generate your own TSF files with more control](https://www.transformate.live/tsf_editor.html)

### For server staff:
- Little to none setup and configuration
- Easily configurable for all kinds of servers
- Block users from using the bot, on a per-user or per-server basis
- Global ban system that helps you keep your server safe from known bad actors
- A big (and growing) community for support
- Easy to use documentation with tutorials
- Avoid cluttering your logs if you're using Dyno

### For developers:
- Open-source, with a permissive license
- Well-documented, with a clear and easy-to-understand codebase
- Easy to contribute to, with a friendly and welcoming community
- Active development and support
- Fully open source data formats
- Fully documented expected behaviours

## Upcoming Features
- More customization options, both for users AND server staff
- Plugins and custom scripting language
- And much more fun stuff!!!

## Inviting TransforMate
To invite TransforMate to your server, you can use [this link](https://discord.com/oauth2/authorize?client_id=1522230400959643688&permissions=4504029862685760&integration_type=0&scope=bot).
You can either use it as is, or, if you have any security concerns with giving the bot the Administrator permission, you
can also disable it and just keep the other permissions active, though this may need additional setup, and may be prone
to unusual behaviours.

By adding TransforMate to your server, you agree to our
[Terms of Service](https://pishock-inc.github.io/TransforMate/legal/tos/), and to our
[Privacy Policy](https://pishock-inc.github.io/TransforMate/legal/privacy_policy/).

## Hosting TransforMate
To host your own TransforMate instance, you'll just need to clone this repo,
install the requirements, and create a `.env` file with the following contents:
```
# General bot configuration
BOT_TOKEN= # Your Discord Bot token
WEBHOOK_NAME= # The name of the Discord Webhooks your bot will create
BLOCKED_USERS="[user_id1, user_id2, ...]" # List of globally blocked users
USER_REPORTS_CHANNEL_ID= # Discord Channel ID to send user reports to
CACHE_PATH="cache" # Path for cache files, especifically TMUD data and server settings
MAX_REGEN_USERS=100 # Maximum number of users in a server allowed for /regen_server_tfs
```

If all of these contents aren't present, an error will be thrown by the program
automatically.

You should also install all the requirements from `requirements.txt` and create the
cache directory and a `people` directory inside it, with, for example,
`mkdir cache/people`.

For more information or help, don't hesitate to ask in our Discord server!

## Collaborating with the project
If you've had a cool idea, found a bug, or wanted to add some of your own code, 
feel free to open an issue or to do a pull request! You can also contact us in
our Discord server, where we have channels and forums specifically for this stuff!

## More info
[Discord Server](https://discord.gg/uGjWk2SRf6)

Inspired by the awesome BPTBot, made by Leroco.
