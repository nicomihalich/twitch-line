#!/usr/bin/env python

import settings
import requests
import json
from subprocess import call

URL = "https://api.twitch.tv/kraken/users/"+settings.TWITCH_USERNAME+"/follows/channels"

def get_streams():
  return requests.get(URL).json()['follows']

def load_stream(url,quality="best"):
  call(["livestreamer", url, quality])

def print_help():
  print "r - get streams , l## - load steam number ##, q - quit"

def main():
  while (True):
      raw = raw_input('twitch-line: ')
      if (raw == '?' or raw == 'h'):
        print_help()
      if (raw == 'r'):
        r = get_streams()
        for i in range(0,len(r)):
          channel = r[i]['channel']
          print str(i) + '. ' + channel['display_name'] + " : " + channel['status']
      if (raw.find('l') == 0):
        load_stream(get_streams()[int(raw[1:])]['channel']['url'])
      if (raw == 'q'):
        break


if __name__ == '__main__':
  main()
