#!/usr/bin/env bash

install_sqlite(){
    # install sqlite 3.29.0
    wget https://www3.sqlite.org/cgi/src/tarball/fc82b73eaa/SQLite-fc82b73eaa.tar.gz
    tar -zxvf SQLite-fc82b73eaa.tar.gz
    cd SQLite-fc82b73eaa
    ./configure && make && make install
    mv /usr/bin/sqlite3 /usr/bin/sqlite3.bak
    cp sqlite3 /usr/bin/sqlite3
    export LD_LIBRARY_PATH="/usr/local/lib" >> ~/.bashrc
    echo "======= sqlite version updated ======="
    sqlite3 --version
}