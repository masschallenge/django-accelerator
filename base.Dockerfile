FROM ubuntu:14.04

WORKDIR /srv/www/mc/current
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections &&  \
    useradd -s /bin/bash -u 3000 -m accelerate_user && \
    chown -R accelerate_user /home/accelerate_user && \
    chown -R accelerate_user /srv/www/mc/current

RUN apt-get update -y && apt-get install sudo software-properties-common python-software-properties -y  && \
    add-apt-repository ppa:saiarcot895/myppa && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y apt-fast && \
    apt-fast -y install git openssh-server build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev libffi-dev && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y build-essential checkinstall apt-utils wget curl python3.6 python3.6-dev && \
    apt-get install -y aria2 --no-install-recommends && \
    curl https://bootstrap.pypa.io/get-pip.py | python3.6 && \
    apt-get install -y cachefilesd && \
    echo "RUN=yes" > /etc/default/cachefilesd && \
    chown -R accelerate_user /var/lib/ && \
    sed -i  '/requiretty/s/^/#/'  /etc/sudoers && \
    echo "accelerate_user ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers && \
    echo "accelerate_user -  nofile 65535" >> /etc/security/limits.conf && \
    apt-fast -y install python-setuptools python-dev emacs24 libjpeg8-dev

RUN sudo apt-get install python-apt && \
    ln -s /usr/lib/python3/dist-packages/apt_pkg.cpython-{35m,34m}-x86_64-linux-gnu.so && \
    add-apt-repository ppa:jonathonf/backports && \
    apt-get -y update && sudo apt-get install -y sqlite3 && \
    echo 'export LD_LIBRARY_PATH="/usr/local/lib"' >> ~/.bashrc

RUN sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1 && \
    sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2 && \
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 3