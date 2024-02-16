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

#creating a job 
jobs = server.get_jobs()
job_names = []

for job in jobs:
    job_names.append(job['name'])

if 'Job1' not in job_names:
    server.create_job('Job1', jenkins.EMPTY_CONFIG_XML)
    print("Created a job!!!")    

for i in jobs:
    if i['name']=='Job1':
        print(i)
#deleting a particular job

for job in jobs:
    if job['name']=='Job1':
        server.delete_job('Job1')
        print('Job deleted successfully!!!')
