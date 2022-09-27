#!/bin/bash

rx_usage=$(ifconfig wlp3s0 | grep RX | grep byte | awk -F '(' '{print $2}' | awk -F ')' '{print $1}')

tx_usage=$(ifconfig wlp3s0 | grep TX | grep byte | awk -F '(' '{print $2}' | awk -F ')' '{print $1}')

echo -e "\n$tx_usage ⇡⇣ $rx_usage"
