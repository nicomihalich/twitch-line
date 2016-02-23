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

## License
The MIT License (MIT)

Copyright (c) 2013 Nico Mihalich

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
