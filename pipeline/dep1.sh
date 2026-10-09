#!/bin/bash
# dep1.sh slug folder files...   (MODE=edit for existing files; lease id in /tmp/lease)
cd ~/gripx-lead-demos; s=${1}; f=${2}; shift 2
./deploy_gh.sh "$(cat /tmp/lease)" "$f" "out/$s" "${MODE:-new}" "$@" 2>&1 | tail -2
