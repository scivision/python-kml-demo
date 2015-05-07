#!/bin/sh

(conda install --yes --file requirements.txt; return 0)
(pip install -r requirements.txt; return 0)
echo "done with conda pip"
