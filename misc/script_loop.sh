#!/bin/bash
#Simple bash script to reboot python script in case of crash
#leg5@nyu.edu

#Execute by running "bash script_loop.sh <your_script.py>" in Terminal

# run the script, re-spawn if it crashes
# note that the $1 just refers to the first argument passed to the function -
# this is a shell script thing.
until python $1; do
    # tell the user why it crashed
    echo "Script crashed with exit code $?.  Respawning.." >&2
    sleep 1  # wait for 1 second before reboot to allow memory to clear
done
