import jenkins
import json
import os
import api_token

host = "http://localhost:8083"
username = "admin"
password = api_token.password

server = jenkins.Jenkins(host,username=username,password=password)
user = server.get_whoami()
print("Hello",user['fullName'])

