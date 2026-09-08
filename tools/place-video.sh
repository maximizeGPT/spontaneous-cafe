#!/bin/sh
# Transcode generated clips from tools/out/<shot>.raw.mp4 into src/assets/video/<shot>.mp4 (1280 wide, ~1.2 Mbps)
# and <shot>-720.mp4 (720 wide, ~0.6 Mbps), both seamless ping-pong loops, muted, faststart. Poster from frame 0.
set -e
cd "$(dirname "$0")/.."
for raw in tools/out/*.raw.mp4; do
  shot=$(basename "$raw" .raw.mp4)
  for w in 1280 720; do
    if [ "$w" = 1280 ]; then out="src/assets/video/$shot.mp4"; br=1200k; else out="src/assets/video/$shot-720.mp4"; br=600k; fi
    ffmpeg -v error -y -i "$raw" -an -filter_complex "[0:v]scale=$w:-2,fps=24,split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1:a=0[v]" -map "[v]" \
      -c:v libx264 -preset slow -b:v $br -maxrate $br -bufsize $(( ${br%k} * 2 ))k -pix_fmt yuv420p -movflags +faststart "$out"
  done
  case $shot in
    home-pan) poster=home-poster;; foraging-moss) poster=foraging-poster;; chef-plating) poster=chef-poster;;
    catering-table) poster=catering-poster;; classes-knife) poster=classes-poster;; *) poster=$shot;;
  esac
  ffmpeg -v error -y -i "src/assets/video/$shot.mp4" -frames:v 1 -q:v 4 "src/assets/img/$poster.jpg"
  printf '%-16s 1280: %7s bytes   720: %7s bytes\n' "$shot" "$(stat -f%z "src/assets/video/$shot.mp4")" "$(stat -f%z "src/assets/video/$shot-720.mp4")"
done
