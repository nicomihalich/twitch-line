twitch-line
============
A cli based [Twitch](http://twitch.tv) live stream browser and viewer.  Pulls your followed (live) streams from the Twitch API and lets you load them in [VLC](https://videolan.org/vlc/) via [Livestreamer](https://github.com/chrippa/livestreamer).  Why? Because it uses less resources than watching in the browser.

### Installation

0. Install [Python](http://www.python.org/) and [pip](http://www.pip-installer.org/en/latest/)
    - [For windows users](http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows)
1. Install the [Python Requests library](https://github.com/kennethreitz/requests)
2. Install [Livestreamer](https://github.com/chrippa/livestreamer)
3. Install [VLC](https://videolan.org/vlc/)
4. Change the value of TWITCH_USERNAME to your Twitch.tv username in `twitch-line.py`
5. Run `/path/to/twitch-line.py` or alias it or add it to your path or some combination of all 3

#### Notes
- You can't see chat
- If stream crashes you have to reopen from the cli
- If you follow over 100 people and they are all live, you will only see 100
- No commercials (streamers don't get revenue.  Only use if you sub or donate in other ways)
- Kappa

##### Future plans
- Background the livestreamer call
- Live updating streams
