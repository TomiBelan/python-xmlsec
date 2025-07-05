#!/bin/bash

exec >&2

echo "==== uatest.sh BEGIN ===="

curl -v -H 'User-Agent: https://github.com/xmlsec/python-xmlsec' 'https://www.aleksey.com/xmlsec/download/'

for p in 3.8 3.9 3.10 3.11; do
  echo "==== $p ===="
  python$p uatest.py
  echo "status $?"
done

echo "==== uatest.sh END ===="
