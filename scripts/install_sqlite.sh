#!/usr/bin/env bash


remove_older_version(){
    echo "======= sqlite version current ======="
    sqlite3 --version
    sudo apt-get purge --auto-remove sqlite3
}

install_sqlite(){
    # install sqlite 3.29.0
    sudo add-apt-repository ppa:jonathonf/backports -y && \
    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 6B05F25D762E3157
    sudo apt-get -y update && sudo apt-get install -y sqlite3 && \
    echo 'export LD_LIBRARY_PATH="/usr/local/lib"' >> ~/.bashrc
    . ~/.bashrc
    echo "======= sqlite version updated ======="
    sqlite3 --version
}
