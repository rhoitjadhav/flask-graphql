#!/bin/bash
set -e

exec gunicorn -b 0.0.0.0 "src:create_app()" &
PID=$!

inotifywait -r -m /app -e modify,move,create,delete,attrib |
  while read path action file; do
    # restart the python app if any python changes are detected
    if [[ "$file" =~ .*py$ ]]; then
      # if the PID exists, kill it
      kill -s 0 $PID > /dev/null && kill $PID
      sleep 1
      exec gunicorn -b 0.0.0.0 "src:create_app()" &
      PID=$!
    fi
  done