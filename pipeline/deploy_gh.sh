#!/bin/bash
# Usage: deploy_gh.sh <lease_id> <repo_dir> <local_dir> <new|edit> file1 [file2 ...]
# Commits text files into github.com/raj-28/gripx-previews (branch trunk) using the GitHub web editor in the cloud browser.
# (Binary uploads fail in the cloud browser, so photos are inlined into img.js by build_modern.js.)
L=$1; DIR=$2; SRC=$3; MODE=$4; shift 4
for f in "$@"; do
  if [ "$MODE" = new ]; then URL="https://github.com/raj-28/gripx-previews/new/trunk?filename=$DIR/$f"; else URL="https://github.com/raj-28/gripx-previews/edit/trunk/$DIR/$f"; fi
  tools cloud_browser navigate --lease-id $L --tab-id 1 --url "$URL" >/dev/null; sleep 3
  R=$(tools cloud_browser find --lease-id $L --tab-id 1 --query 'file contents editor textbox' --json | jq -r '[.[]|select(.role=="textbox" and (.text|test("Editing")))][0].ref')
  tools cloud_browser form-input --lease-id $L --ref $R --value-stdin < "$SRC/$f" >/dev/null; sleep 2
  C=$(tools cloud_browser find --lease-id $L --tab-id 1 --query 'Commit changes... button' --json | jq -r '[.[]|select(.text|test("^Commit changes"))][0].ref')
  tools cloud_browser click --lease-id $L --ref $C >/dev/null; sleep 1
  D=$(tools cloud_browser find --lease-id $L --tab-id 1 --query 'Commit changes confirm button in dialog' --json | jq -r '[.[]|select(.text=="Commit changes")][0].ref')
  tools cloud_browser click --lease-id $L --ref $D >/dev/null; sleep 6
  echo "committed $DIR/$f"
done
