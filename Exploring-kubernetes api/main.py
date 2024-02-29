from kubernetes import client, config

config.load_kube_config() #checks whether the any kubernetes cluster is there or not 

v1 = client.CoreV1Api()  #select version
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)  #list out the pods in all namespaces

for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

