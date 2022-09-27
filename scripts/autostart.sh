#!/usr/bin/env bash

# Enable this to change screeb resolution in virtual machines
#xrandr -s 1920x1080

# wallpaper
feh --bg-fill ~/.config/qtile/wallpapers/space.jpg &

# compositor
picom --config ~/.config/qtile/picom/picom.conf &

# touchpad
~/.config/qtile/scripts/TouchPad.sh

# power management
#xfce4-power-manager &
#xfce4-screensaver &

# Authentication
gnome-keyring-daemon --start &
shopt -s globstar
/usr/lib*/**/polkit-gnome-authentication-agent-1 &

# Disable beep
xset b off
