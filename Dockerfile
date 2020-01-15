FROM accelerator_tests:latest

WORKDIR /srv/www/mc/current

COPY . /srv/www/mc/current

CMD ["make", "coverage"]