#!/usr/bin/env python

import settings
import requests
import json
from subprocess import call

URL_PREFIX = "https://api.twitch.tv/kraken/"
URL = URL_PREFIX + "users/" + settings.TWITCH_USERNAME + "/follows/channels?limit=100"
ALL_URL = URL_PREFIX + "streams"

class Stream:
  def __init__(self, url, num, name, game, status):
    self.url = url
    self.num = num
    self.name = name
    self.game = game
    self.status = status

def get_streams():
  stre = ""
  for s in requests.get(URL).json()['follows']:
    stre += s['channel']['name']+","
  streams = []
  i = 0
  for s in requests.get(ALL_URL+"?channel="+stre[:-1]+'&limit=100').json()['streams']:
    i += 1
    stream = s['channel']
    streams.append(Stream(stream['url'],str(i),stream['display_name'],stream['game'],stream['status']))
  return streams

def load_stream(url,quality="best"):
  call(["livestreamer", url, quality])

def print_help():
  print "r - get streams , l## - load steam number ##, q - quit"

def print_welcome():
  print "Welcome to twitch-line."
  print_help()

def print_stream(stream):
    print stream.num + '. ' + stream.name + ", playing " + stream.game + " : " + stream.status

def print_streams(streamlist):
  for stream in streamlist:
    print_stream(stream)

def main():
  streamlist = get_streams()
  print_welcome()
  print_streams(streamlist)
  while (True):
    raw = raw_input('twitch-line: ')
    if (raw == '?' or raw == 'h'):
      print_help()
    if (raw == 'r'):
      streamlist = get_streams()
      print_streams(streamlist)
    if (raw.find('l') == 0):
      n = raw[1:]
      if not n.isdigit() or int(n) >= len(streamlist):
        print "not a stream number"
        continue
      load_stream(streamlist[int(n)].url)
    if (raw == 'q'):
      break

if __name__ == '__main__':
  main()
