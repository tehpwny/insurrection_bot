Insurrection bot
=====================

Insurection bot speaks or rap rants from a running automatic_insurrection server (https://github.com/johm/automatic_insurrection) using espeak and mplayer

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

sudo pip install bs4 request
sudo apt install eapeak ruby ruby-haml ruby-sinatra
ruby automatic_insurrection/insurrect.rb > /dev/null 2>&1 &
python insurrection_bot.py --trap
```


Usage
======================
Parameters:

  - *--pretty*: Adds some pretty ASCII shiet
  - *--trap*: adds trap music as background sound
  - *--fortune*: Displays just one rant


Credits
======================

Inspiration
-------------
Automatic insurrection - https://github.com/johm/automatic_insurrection/tree/7c9ffca0c9accea3c56ab5af0a7f9ecaca6658eb
```
The purpose of this little program is to expose the seductions of
rhetoric, not to criticize actions taken.  Despite my admiration for
many of the actions taken in the name of insurrection, I'm suspicious
of how easy it is to substitute style for substance in the communiques
describing these actions.  And this is not to say that all
"insurrectionist" texts are meaningless, despite its difficulty, I
found the Coming Insurrection to be, with all its excesses, a serious
(if contentious) contribution to revolutionary thought.  And, to point
out just one other exemplar, the recent "Communique from an Absent
Future: The Terminus of Student Life" is by and large an excellent
piece of analysis.  This program is intended only to demonstrate the
pitfalls of language which sounds too good to be meaningful.
```

Beats: 
------
  * Banlieue Nord By CyberSDF -- Creative Commons -- https://www.youtube.com/watch?v=9cxrECw3yOA
