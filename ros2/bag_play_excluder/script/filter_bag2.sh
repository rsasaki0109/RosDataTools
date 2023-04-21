#!/bin/bash

BAG_PATH=$1
shift

if [ -z "$BAG_PATH" ]; then
  echo "Usage: $0 <path_to_bag> <excluded_topic1> <excluded_topic2> ..."
  exit 1
fi

EXCLUDED_TOPICS=""
for topic in "$@"
do
  EXCLUDED_TOPICS+="|$topic"
done

INCLUDED_TOPICS=$(ros2 bag info $BAG_PATH | grep -P "Topic: (?!(${EXCLUDED_TOPICS:1}))" | awk '{print $2}')

if [ -z "$INCLUDED_TOPICS" ]; then
  echo "No topics to play. Check your excluded topics list."
  exit 1
fi

ros2 bag play $BAG_PATH --topics ${INCLUDED_TOPICS[@]}