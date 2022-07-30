#!/bin/bash

/usr/bin/ffmpeg -hide_banner \
    -ignore_unknown \
    -hwaccel cuvid \
    -r 24\
    -i $1 \
    -c:v hevc_nvenc \
    -pix_fmt yuv420p \
    -rc constqp \
    -qp 17 \
    -an \
    -sn \
    $2

