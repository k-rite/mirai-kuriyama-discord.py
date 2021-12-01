
# Discord.py Reaction Bot
# MIRAI KURIYAMA
A multipurpose, semi-modular Discord bot written in Python with the new [discord.py](https://github.com/Rapptz/discord.py) module.

[![Discord.py](https://img.shields.io/pypi/v/discord.py.svg)](https://pypi.python.org/pypi/discord.py/)
[![Python](https://img.shields.io/badge/Python-3.5%2C%203.6%2C%203.7-blue.svg)](https://python.org/)

# Installing dependencies
The following packages are required to run (as well as [Python](https://python.org) 3.5 or over):

```
python -m pip install discord
```

**To easily setup Mirai and change tokens, you should use the `config.py` script.**

> Not working? Try replacing `python` with `py` or `python3`.

# Downloading the source code
To download with Git, type this command into a terminal:
```
git clone k-rite/mirai-kuriyama-discord.py 
```
Alternatively, you can use the [GitHub Desktop Client](https://desktop.github.com/) to download it.

You can also download the repository as a ZIP or TAR file.

To run the script on Windows with [Git Bash](https://git-scm.com/downloads), delete `sudo` from the first line and it should run.

# Setting up and config
MIrai comes with a `config.py` file. Here you will add your Discord App token, and add startup extensions. You can generate a token at *https://discordapp.com/developers/applications/me.*

Find the string `"token here"` in the config file and replace it with your token.

In the `config.py` file, you can also customise insults, error messages, bot prefix, bot description and the file you want the bot to log events to. (MORE WILL BE ADDED IN FUTURE VERSIONS)


# Creating an extension (cog)
Inside the `misc` folder, you will find templates for commands and cogs.


You can refer to [this documentation](https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html?highlight=cogs) for how to create a cog.


# Loading/Unloading an extension (cog)
Use the command `load` to load commands from `startup_extensions` in config.py. You can unload them separately with the `unload` command.

You can also load cogs from a folder, by using the format: `folder.filename`

Mirai's plugins are found in the `cogs` folder.

# Starting the bot
You can start the bot by launching `main.py` directly, or using a Python IDE such as Thonny.


# Inviting to servers
Use the [Discord Permissions Calculator](https://discordapi.com/permissions.html) to invite the bot to your server using the ID printed to the console, and make sure that it has admin permissions.

If you want to invite your bot to other people's servers, make sure to tick "Public bot" on the Apps page.


# Tips
Make sure to always update Mirai. You can create [GitHub Webhooks for Discord](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks) to get notified whenever a repo is updated.

When you do this, always keep a backup! It's also useful to write down your token, but **NEVER** give this to anyone you don't trust, or publish it to your GitHub. Don't worry though - you can generate a new token whenever you want on the Discord developer portal.

To read and edit this document properly offline, [Atom](https://atom.io/) and [VS Code](https://code.visualstudio.com/) both have a built-in Markdown Previewer that you can open by hitting <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>v</kbd> on a PC or <kbd>cmd</kbd> + <kbd>shift</kbd> + <kbd>v</kbd> on a Mac.

# See Also
See the discord.py repo for more information on the API: https://github.com/Rapptz/discord.py
