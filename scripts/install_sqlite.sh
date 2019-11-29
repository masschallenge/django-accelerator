#!/usr/bin/env bash


remove_older_version(){
    echo "======= sqlite version current ======="
    sqlite3 --version
    sudo apt-get purge --auto-remove sqlite3
}

install_sqlite(){
    # install sqlite 3.29.0
    wget https://www3.sqlite.org/cgi/src/tarball/fc82b73eaa/SQLite-fc82b73eaa.tar.gz
    tar -zxvf SQLite-fc82b73eaa.tar.gz
    cd SQLite-fc82b73eaa
    ./configure && make && sudo make install
    sudo cp sqlite3 /usr/bin/sqlite3
    echo 'export LD_LIBRARY_PATH="/usr/local/lib"' >> ~/.bashrc
    . ~/.bashrc
    echo "======= sqlite version updated ======="
    sqlite3 --version
}