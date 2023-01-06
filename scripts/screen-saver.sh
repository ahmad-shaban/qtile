#!/bin/bash

# set display time of inactivity to 10 mins
xset dpms 0 0 600 &

# trigger i3lock
xss-lock -- $HOME/.config/qtile/scripts/lock-screen.sh &

