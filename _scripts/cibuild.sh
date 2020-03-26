#!/bin/bash

# skip if build is triggered by pull request
if [ $TRAVIS_PULL_REQUEST == "true" ]; then
  echo "this is PR, exiting"
  exit 0
fi

# enable error reporting to the console
set -e

# cleanup "_site"
rm -rf _site
mkdir _site

# build with Jekyll into "_site"
python3 main.py build

# push
cd _site
git config user.email "giacomo.caironi@gmail.com"
git config user.name "Giacomo Caironi"
git add --all
git commit -m "Travis #$TRAVIS_BUILD_NUMBER"
git push --force origin master
