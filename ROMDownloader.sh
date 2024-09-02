#!/bin/bash

. /mnt/mod/ctrl/configs/functions &>/dev/null 2>&1
progdir=$(cd $(dirname "$0"); pwd)

program="python3 ${progdir}/ROMDownloader/main.py"
log_file="${progdir}/ROMDownloader/log.txt"

$program > "$log_file" 2>&1
