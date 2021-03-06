#!/usr/bin/env bash

# set colors for text
BOLD='\e[1m'
BLUE='\e[34m'
RED='\e[31m'
YELLOW='\e[33m'
GREEN='\e[92m'
NC='\e[0m'

# set text formats
info() {
    printf "\n${BOLD}${BLUE}====> $(echo $@ ) ${NC}\n"
}

warning () {
    printf "\n${BOLD}${YELLOW}====> $(echo $@ )  ${NC}\n"
}

error() {
    printf "\n${BOLD}${RED}====> $(echo $@ )  ${NC}\n"
    bash -c "exit 1"
}

success () {
    printf "\n${BOLD}${GREEN}====> $(echo $@ ) ${NC}\n"
}

# restrict and set expected make commands in django-accelerator
set_expected_commands (){
    VARIABLES+=(
        help
        package
        clean
        code-check
        coverage
        coverage-run
        coverage-report
        coverage-html-report
        coverage-xml-report
        install
        uninstall
        data-migration
        migrations
        test
    )
}


set_expected_commands
for variable in ${VARIABLES[@]}; do
    if [[ $1 == $variable ]]; then
        echo "---running--"
        make $1
        success "Done..."
        exit 0
    fi
done

warning "[ make run command=<command> ] does not support \"$1\" command"
