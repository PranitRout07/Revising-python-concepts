def generate_deployment_yaml(image, port, metadata_name, label, selector_matchlabel_app, template_metadata_labels_app, container_name,resources_limit_cpu,resources_requests_cpu):
    yaml_template = f"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: {metadata_name}
  labels:
    app: {label}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {selector_matchlabel_app}
  template:
    metadata:
      labels:
        app: {template_metadata_labels_app}
    spec:
      containers:
      - name: {container_name}
        image: {image}
        ports:
        - containerPort: {port}
        resources:
          limits:
            cpu: {resources_limit_cpu}
          requests:
            cpu: {resources_requests_cpu}"""
    return yaml_template

def main():
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

if __name__ == "__main__":
    main()
