#!/bin/bash

exec < /dev/tty 

hooktipper $@ > /dev/tty

exec <&-
