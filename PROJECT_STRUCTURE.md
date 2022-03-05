# How this project is organized

```
📦root
 ┣ 📂.vscode
 ┃ ┗ 📜tasks.json
 ┣ 📂age
 ┃ ┣ 📜bot.py
 ┃ ┣ 📜components.py
 ┃ ┣ 📜entity.py
 ┃ ┗ 📜__init__.py
 ┣ 📂bot
 ┃ ┣ 📂commands
 ┃ ┃ ┣ 📜duel.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂components
 ┃ ┃ ┗ 📜duel.py
 ┃ ┗ 📂entities
 ┃ ┃ ┣ 📜classes.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┣ 📜.env
 ┣ 📜.env.example
 ┣ 📜.gitignore
 ┣ 📜main.py
 ┣ 📜PROJECT_STRUCTURE.md
 ┣ 📜refresh.bat
 ┗ 📜setup.py
```

## 📂.vscode

Folder where the VS Code settings are located.

### 📂tasks.json
Contains a task called "sr", that runs "refresh.bat" and executes the file in the current tab that is editing the code

To run it in vscode, Terminal > Run Task > sr

If it asks you to scan something, choose the option to ignore this scan

## 📂age

Folder where I abstracted the discord lib (interactions.py)

## 📂bot

Folder where are the files related to all bot content

    📂commands          # bot commands
        📜duel.py
    📂components        # bot interface components
        📜duel.py
    📂entities          # bot entities (classes, races, etc)
        📜classes.py


## 📜.env.example

Rename to .env and add the bot token, dev server id

## 📜main.py

File where the bot runs

## 📜refresh.bat

Run the setup.py

## 📜setup.py

Installs the lib

Allows you to import the files as

```py
from age import bot
```

Instead of

```py
from ..bot import *
```

Solves the `ImportError: attempted relative import with no known parent package` error

This error occurs when you try to import fileA.py into fileB.py, with ``from ..dirA import fileA`

    📂dirA
        📜fileA.py
    📂dirB
        📜fileB.py
