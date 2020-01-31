#!/bin/bash

for fileName in "test/images"/*
do
  testFileName="${fileName/.jpg/.md}"
  testFileName="${testFileName///images/}"
  python3 thememe $fileName > $testFileName
done
