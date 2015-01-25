#! /bin/bash

watchmedo shell-command \
    --patterns="*.sas" \
    --recursive \
    --command='python sas2rst.py sas_source/ snd_attempt/ && make -C snd_attempt/ html' \
    sas_source
