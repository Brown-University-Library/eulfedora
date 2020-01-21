#!/usr/bin/env bash

# shell script to start up continuous integration fedora instance
cd /opt/eulfedora_ci
nohup ./fedora_ci/tomcat/bin/startup.sh &
sleep 60
cat nohup.out
curl http://127.0.0.1:8080/fedora
