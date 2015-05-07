#!/bin/sh

(conda install --yes --file requirements.txt; return 0)
pip install -qr requirements.txt
