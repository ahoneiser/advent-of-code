#!/bin/bash

PATHS=(src tests)

for P in ${PATHS[@]}; do
  isort $P
  black $P
done
