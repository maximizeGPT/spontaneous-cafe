#!/bin/sh
# Transcode generated clips from tools/out/<shot>.raw.mp4 into src/assets/video/<shot>.mp4
# as a seamless ping-pong loop (forward then reverse), 1280 wide, H.264, muted, and cut a poster from frame 0.
set -e
cd "$(dirname "$0")/.."
for raw in tools/out/*.raw.mp4; do
  shot=$(basename "$raw" .raw.mp4)
  ffmpeg -v error -y -i "$raw" -an -filter_complex "[0:v]scale=1280:-2,fps=25,split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1:a=0[v]" -map "[v]" \
    -c:v libx264 -preset slow -crf 25 -pix_fmt yuv420p -movflags +faststart "src/assets/video/$shot.mp4"
  case $shot in
    home-pan) poster=home-poster;; foraging-moss) poster=foraging-poster;; chef-plating) poster=chef-poster;;
    catering-table) poster=catering-poster;; classes-knife) poster=classes-poster;; *) poster=$shot;;
  esac
  ffmpeg -v error -y -i "src/assets/video/$shot.mp4" -frames:v 1 -q:v 3 "src/assets/img/$poster.jpg"
  printf '%-16s %8s bytes  %s\n' "$shot" "$(stat -f%z "src/assets/video/$shot.mp4")" "$(ffprobe -v error -show_entries format=duration -of csv=p=0 "src/assets/video/$shot.mp4")s"
done
