#!/bin/bash

# Launch rtorrent
swaymsg exec 'foot -a "rtorrent" rtorrent'
sleep 0.5

# Launch gomuks
swaymsg exec 'foot -a "gomuks" gomuks'
sleep 0.5

