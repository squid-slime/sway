#!/bin/bash

DEVICE_IDENTIFIER="1118:2496:Microsoft_Surface_Type_Cover_Tablet_Mode_Switch"
APP_NAME="wvkbd-mobintl"

while true; do
    # Get the PID of the target application
    APP_PID=$(pidof "$APP_NAME")

    # Check if the device exists
    if swaymsg -t GET_INPUTS | grep -q "$DEVICE_IDENTIFIER"; then
        echo "Typecover connected"
        if [[ -n "$APP_PID" ]]; then
            echo "Sending SIGUSR1 to PID: $APP_PID"
            kill -USR1 "$APP_PID"
        fi
    else
        echo "Typecover disconnected"
        if [[ -n "$APP_PID" ]]; then
            echo "Sending SIGUSR2 to PID: $APP_PID"
            kill -USR2 "$APP_PID"
        fi
    fi

    sleep 1
done
