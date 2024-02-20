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
# jobs = server.get_jobs()
def get_jobs():
    jobs = server.get_jobs()
    return jobs

val=0
while(val!=4):
    val = int(input("""What do you want to do?
        1.Create a Job
        2.Delete a job
        3.Get Pluggins Details
        4.EXIT     
        """))
    jobs = get_jobs()
    all_jobs = [job['name'] for job in jobs]
    if val==1:
        job_name = input("Write a job name you want to create: ")
        
        if job_name not in all_jobs:
            print("Creating job... ")
            server.create_job(job_name, jenkins.EMPTY_CONFIG_XML)
        else:
            print('Job is already present')
    elif val==2:
        job_name = input("Write a job name you want to delete: ")
     
        if job_name in all_jobs:
            server.delete_job(job_name)
            print('Job deleted successfully!!!')
        else:
            print('Job is not present,please write a valid job name!!!')
    elif val==3:
        plugins = server.get_plugins_info()
        needsUpdate = []
        noNeedUpdate = []
        for plugin in plugins:
            if plugin['hasUpdate']:
                needsUpdate.append(plugin['longName'])
            else:
                noNeedUpdate.append(plugin['longName'])
        print("Plugins need Update : ")
        for i in needsUpdate:
            print(i)
        print(" ")
        print(" ")
        print("Plugins with no new update : ")
        for i in noNeedUpdate:
            print(i)
    elif val==4:
        print("Exit")
        exit(1)