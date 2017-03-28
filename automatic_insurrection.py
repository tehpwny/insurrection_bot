import sys

from random import choice
from time import sleep
import urllib.request
from urllib.error import URLError

from bs4 import BeautifulSoup
from subprocess import call, Popen
import os
import sys
from bs4.element import Tag


RAND = '--more-rant' in sys.argv
PRETTY = '--pretty' in sys.argv

INSURRECTIOM_SERVER = 'http://localhost:4567'
def get_sock():
    try:
        sock = urllib.request.urlopen(INSURRECTIOM_SERVER).read().decode("utf-8")
    except urllib.error.URLError:
        raise RuntimeError("automatic_insurection server should be running on localhost:4567 (https://github.com/johm/automatic_insurrection)")
    else:
        return sock

def get_rants():
    url = 'http://localhost:4567'
    sock = get_sock()

    soup = BeautifulSoup(sock, "html.parser")

    rant_text = soup.find('div', id='rant').text
    return rant_text.split('. ')

def get_rant():

    sock = get_sock()

    soup = BeautifulSoup(sock, "html.parser")
    div_rant = soup.find('div', id='rant').find('div', id='pull_quote')
    rant = div_rant.contents

    rant_msg = ['*{}*'.format(element.contents[0]) if isinstance(element, Tag) else element for element in rant]

    div_morerant = soup.find('div', id='morerant')
    morerant = div_morerant.contents
    morerant_msg = ['*{}*'.format(element.contents[0]) if isinstance(element, Tag) else element for element in morerant]
    msg = choice((' '.join(rant_msg), ' '.join(morerant_msg))) if RAND else ' '.join(rant_msg)
    return msg.replace('*', '')


if '--fortune' in sys.argv:
    if PRETTY:
        print('\n*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n\n{}\n'.format(get_rant()))
        print('\n*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n')
    else:
        print(get_rant())
    sys.exit()

if '--beat' in sys.argv:
    beat = Popen(["mplayer", "-loop", "0", "-really-quiet", "./beat"])


while True:
    print('\n*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n\n\n')
    for message in get_rants():
        print(message + '\n')
        cmd = 'espeak -p 45 -s 172 "{}"'.format(message)
        sleep(choice((0.75, 1)))
        os.system(cmd)
