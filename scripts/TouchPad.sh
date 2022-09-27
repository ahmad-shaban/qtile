#!/bin/bash 

touchpad_dev_id=$(xinput list | grep Touchpad | awk '{print $6}' | cut -c 4-)

tap_prop_id=$(xinput list-props $touchpad_dev_id | grep 'Tapping Enabled (' | awk '{print $4}' | awk -F '(' '{print $2}' | awk -F ')' '{print $1}')

natural_scroll_prop_id=$(xinput list-props $touchpad_dev_id | grep 'Natural Scrolling Enabled (' | awk '{print $5}' | awk -F '(' '{print $2}' | awk -F ')' '{print $1}')

# Enable tap to click
xinput set-prop $touchpad_dev_id $tap_prop_id 1

# Enable Natural Scrolling
xinput set-prop $touchpad_dev_id $natural_scroll_prop_id 1
