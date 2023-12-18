#!/usr/bin/env bash

ffmpeg -i "$1" -vn -ar 16000 -ac 1 -c:a pcm_s16le output.wav
