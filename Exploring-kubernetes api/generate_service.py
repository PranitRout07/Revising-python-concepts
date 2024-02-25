def generate_service_yaml(metadata_name,type,selector_app,port,targetport,portForward):
    service_yaml = f"""apiVersion: v1
kind: Service
metadata:
  name: {metadata_name}
spec:
  type: {type}
  selector:
    app: {selector_app}
  ports:
    - port: {port}
      targetPort: {targetport}
      {type}: {portForward}"""
    
    return service_yaml
def main():
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
if __name__=="__main__":
    main()