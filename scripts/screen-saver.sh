#!/bin/bash

# set display time of inactivity to 10 mins
xset dpms 0 0 600 &

# trigger i3lock
xss-lock -- i3lock -c 000000 &

