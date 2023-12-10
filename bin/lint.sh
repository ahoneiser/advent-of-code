#!/bin/bash

PATHS=(src)

for P in ${PATHS[@]}; do
  isort $P
  black $P
done
