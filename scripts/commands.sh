#!/usr/bin/env bash

ls -l
sqlite3 --version
which sqlite3
LD_LIBRARY_PATH=/usr/local/lib make coverage-run
