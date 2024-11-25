#!/bin/bash
gpio -g mode 17 out
gpio -g mode 22 out
gpio -g mode 27 out
while true
do
  gpio -g write 17 1
  gpio -g write 22 1
  gpio -g write 27 1
  sleep 1
  gpio -g write 17 0
  gpio -g write 22 0
  gpio -g write 27 0
  sleep 1
done
