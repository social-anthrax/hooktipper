#! /usr/bin/env bash -e

exec < /dev/tty 

python3 ./hooktipper/main.py $@ > /dev/tty

exec <&-