from kubernetes import client, config, utils
from search_yaml_files import find_file

def main():
    config.load_kube_config()
    k8s_client = client.ApiClient()
    yaml_file = input("Enter the yaml file name: ")
    yaml_file_path = find_file(yaml_file)
    utils.create_from_yaml(k8s_client,yaml_file_path,verbose=True)
    

if __name__ == "__main__":
    num_of_times = int(input("Enter how many yaml files you have to apply: "))
    i = num_of_times
    while i!=0:
        main()
        i= i-1