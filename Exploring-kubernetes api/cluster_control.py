import subprocess
from kubernetes import client, config
from generate_deployment import generate_deployment_yaml
from generate_service import generate_service_yaml
from apply_yaml_files import apply_yaml
def start_cluster():
    try:
        subprocess.run(["minikube","start"])
    except:
        print("Minikube may be not installed")
def delete_cluster():
    try:
        subprocess.run(["minikube","delete"])
    except:
        print("Minikube is not installed")

def take_deployment_file_inputs():
    image = input("Enter image name: ")
    port = input("Enter container port: ")
    metadata_name = input("Enter metadata name: ")
    label = input("Enter label: ")
    selector_matchlabel_app = input("Enter selector matchLabel app: ")
    template_metadata_labels_app = input("Enter template metadata labels app: ")
    container_name = input("Enter container name: ")
    resources_limit_cpu = input("Enter resources limit cpu: ")
    resources_requests_cpu = input("Enter resources requests cpu: ")

    deployment_yaml = generate_deployment_yaml(image, port, metadata_name, label, selector_matchlabel_app, template_metadata_labels_app, container_name,resources_limit_cpu,resources_requests_cpu)
    
    with open('manifests_file/deployment.yml', 'w') as file:
        file.write(deployment_yaml)

    print("Deployment YAML written to deployment.yml")

def take_service_file_inputs():
    metadata_name = input("Enter metadata name: ")
    type = input("Enter type of service: ")
    selector_app = input("Enter selector app: ")
    port = input("Enter container port: ")
    targetPort = input("Enter target port: ")
    portForward = input("Enter portForward: ")

    service_yaml = generate_service_yaml(metadata_name,type,selector_app,port,targetPort,portForward)
    with open("manifests_file/service.yml","w") as file:
        file.write(service_yaml)
    print("Service.yml is created successfully..")

def main():
    while True:
        user_input = input("What do you want start a cluster or delete a cluster or nothing(yes/no/delete): ")
        if user_input.lower()=="yes":
            start_cluster()
            config.load_kube_config() 
            v1 = client.CoreV1Api()
            print("Fill these lines for creating a deployment..")
            print()
            take_deployment_file_inputs()
            print("Fill these lines for creating a service..")
            print()
            take_service_file_inputs()
            apply_input = input("Do you want to apply the yaml files you have created: ")
            if apply_input.lower()=="yes":
                num_of_yaml_files = int(input("How many yaml files you need to apply?: "))
                i = num_of_yaml_files
                while i!=0:
                    apply_yaml()
                    i= i-1
        elif user_input.lower()=="delete":
            delete_cluster()
        elif user_input.lower()=="no":
            print("There is no action!")
            break
        else:
            print("Enter valid input!!!")
if __name__=="__main__":
    main()