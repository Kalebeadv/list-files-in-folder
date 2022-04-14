from os import walk

def list_files_in(path,files):
    
    for (dirpath, dirnames, filenames) in walk(path):
      files.extend(filenames)
      break
    
def show_files(files):
    
    for numero,arquivo in enumerate(files):
        print(arquivo)

def menu():

    print("---------------- MENU ----------------")
    print("\n\n1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("--------------------------------------")


def choose_your_destiny():
    
    while(True):
        destiny = int(input("Qual opção deseja(1,2,3,4 ou 5):"))
        if(destiny == 1):
            
            path = ""
            files = []
            list_files_in(path,files)
            show_files(files)
            menu()
            continue;
            
        elif(destiny == 2):
            
            path = []
            count = 0
            while(count != 6):
                files = []
                list_files_in(path[count],files)
                show_files(files)
                count += 1
            menu()
            continue
        
        elif(destiny == 3):
            
            path = ""
            files = []
            list_files_in(path,files)
            show_files(files)
            menu()
            continue;

        elif(destiny == 4):
            
            path = ""
            files = []
            list_files_in(path,files)
            show_files(files)
            menu()
            continue;
        
        elif(destiny == 5):
            break

        else:
            menu()
            continue           

menu()
choose_your_destiny()

