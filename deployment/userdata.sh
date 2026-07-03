#!/bin/bash

yum update -y

yum install python3 git nginx -y

pip3 install flask

pip3 install flask-cors

pip3 install pymysql

systemctl enable nginx

systemctl start nginx
