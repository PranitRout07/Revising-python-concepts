import subprocess

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
def main():
    while True:
        user_input = input("What do you want start a cluster or delete a cluster or nothing(yes/no/delete): ")
        if user_input.lower()=="yes":
            start_cluster()
        elif user_input.lower()=="delete":
            delete_cluster()
        elif user_input.lower()=="no":
            print("There is no action!")
            break
        else:
            print("Enter valid input!!!")
if __name__=="__main__":
    main()