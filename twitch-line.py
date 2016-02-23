#!/usr/bin/env python

import requests
import json
from subprocess import call

TWITCH_USERNAME = "clickMixup"

URL_PREFIX = "https://api.twitch.tv/kraken/"
URL = URL_PREFIX + "users/" + TWITCH_USERNAME + "/follows/channels?limit=100"
ALL_URL = URL_PREFIX + "streams"

class Stream:
  def __init__(self, url, name, game, status):
    self.url = url
    self.name = name
    self.game = game
    self.status = status

def get_streams():
  stre = ""
  for s in requests.get(URL).json()['follows']:
    stre += s['channel']['name']+","
  streams = []
  for s in requests.get(ALL_URL+"?channel="+stre[:-1]+'&limit=100').json()['streams']:
    stream = s['channel']
    streams.append(Stream(stream['url'],stream['display_name'],stream['game'],stream['status']))
  return streams

def load_stream(url,quality="source"):
  call(["livestreamer", url, quality])

def print_help():
  print "r - get streams , l## - load steam number ##, q - quit"

def print_welcome():
  print "Welcome to twitch-line."
  print_help()

def print_stream(i,stream):
  name = stream.name or ''
  game = stream.game or ''
  status = stream.status or ''
  print str(i) + '. ' + name + ", playing " + game + " : " + status

def print_streams(streamlist):
  for i, stream in enumerate(streamlist):
    print_stream(i,stream)

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
    else:
      print "not a command"

if __name__ == '__main__':
  main()
