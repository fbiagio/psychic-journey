#!/bin/bash

## declare an array variable
declare -a VMS=("VMworker1" "VMworker2" "VMloader" "VMflower")

## now loop through the above array
for i in "${VMS[@]}"
do
    echo "$i"
    rm -fr /vagrant/${i}/proj/*
    cp -fr /vagrant/proj_source/* /vagrant/${i}/proj/
done