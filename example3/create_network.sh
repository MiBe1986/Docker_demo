#!/bin/bash

docker network create -d bridge --ip-range=192.168.100.0/29 --subnet=192.168.100.0/28 test_network