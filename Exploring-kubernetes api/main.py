from kubernetes import client, config

config.load_kube_config() #checks whether the any kubernetes cluster is there or not 

v1 = client.CoreV1Api()  #select version
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)  #list out the pods in all namespaces

for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

# import os
# def find_file(document_name):
#     current_dir = os.getcwd()
#     for root, dirs, files in os.walk(current_dir):
#         if document_name in files:
#             file_path = os.path.join(root, document_name)
#             return file_path
#     return None

# if __name__ == "__main__":
#     document_name = input("Enter the document name to search for: ")
#     file_path = find_file(document_name)
#     if file_path:
#         print("File found at:", file_path)
#     else:
#         print("File not found in the current directory or its subdirectories.Enter correct filename.")