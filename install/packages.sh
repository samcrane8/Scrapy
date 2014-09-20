#!/bin/bash


PACKAGES="mysql-server libmysqlclient-dev python-pip python-dev ssh build-essential libssl-dev libffi-dev python-dev python-lxml  libxml2-dev libxslt1-dev"
setup()
{
    echo " *** Following packages will be attempted to be installed: "
    echo " *** $PACKAGES ***"
    install_packages

}


install_packages()
{

    echo " *** Install Global Packages ***"

    for package in $PACKAGES
       do
        echo "Attempting to install $package ... "

            INSTALLED=$(dpkg -l | grep ${package})

            if [ "" == "${INSTALLED}" ]
                then
                echo "${package} does not exist, starting installation."
                set +e
                RESULTS=$(sudo apt-get install ${package} -y)
                echo "${RESULTS}"
                set -e
                else
                echo "$package already exists..."
            fi
        done



}

setup
