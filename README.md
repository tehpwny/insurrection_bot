Insurrection bot
=====================

Insurection bot speaks rants from a running automatic_insurrection server (https://github.com/johm/automatic_insurrection) using espeak

License
=====================
This project is licensed under GNU GENERAL PUBLIC LICENSE v3

Installation
=====================

Debian
----------------------
For example into a dedicated directory:

```
git clone https://github.com/tehpwny/insurrection_bot --recursive
cd insurrection_bot/

sudo pip install bs4 
sudo apt install espeak
sudo apt install ruby ruby-haml ruby-sinatra
ruby automatic_insurrection/insurrect.rb&
python insurrection_bot.py
```


Usage
======================
Parameters:

  - *--pretty*: Adds some pretty ASCII shiet
  - *--beat*: Tries to play any file named beat in CWD with mplayer (find some trap beat for more thug style!) 
  - *--fortune*: Displays just one rant
