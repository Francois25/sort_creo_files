# trier un dossier et ne garder que
# la dernière version de chaque fichier.

import os

choose_folder = ''
list_files = ''
lasts_files = ''
list_file_delete = ''

def new_folder():
    try:
        choose_folder = input("Quel dossier traiter ? : ")
        os.chdir(choose_folder)
        return choose_folder

    except:
        #exit()
        choice = input("Dossier incorrect, voulez vous abandonner ?\n  Y - N : ")
        if choice.upper() == 'Y':
            exit()
        elif choice.upper() == 'N':
            new_folder()
        else:
            print("Vous devez entrer un choix entre Y et N")
            exit()

def order_files(list_files): 
    extension_max = '0'
    last_name_file = ''
    latest_file = ''
    list_latest_file=[]

    for file in list_files:
        name_file = file.rsplit('.', 1)[0]   
        extension = file.rsplit('.', 1)[1]
        if not extension.isdigit():
            print(f"Ce type de fichier n'est pas exploitable : {file}")

        # modification de l'extension sur 2 chiffres
        if len(extension) == 1:
            extension = "0" + extension    
        
        # Nom de fichier hors extension identique au dernier traité
        if name_file == last_name_file:
            if extension > extension_max:
                extension_max = extension
                latest_file = file

        # Nom de fichier hors extension différent du dernier traité                        
        elif name_file != last_name_file:
            if last_name_file != '':
                list_latest_file.append(latest_file)
            last_name_file = name_file
            latest_file = file
            if extension < extension_max:
                extension_max = extension
    
    # liste des dernières versions
    list_latest_file.append(latest_file)
    return list_latest_file


def file_to_delete(list_files, lasts_files):
    list_file_delete = []
    for file in list_files:
        if not file in lasts_files:
            list_file_delete.append(file)
    return list_file_delete


def delete_file(list_file_delete):
    if len(list_file_delete) == 0:
        print("\nAucuns fichiers à supprimer\n")
        return
    print(f"\nEtes vous sûr de vouloir supprimer le(s) {len(list_file_delete)} fichier(s) suivant(s) du dossier {choose_folder} ?")
    for i in list_file_delete:
        print(i)
    choice = input("\nY - N : ")
    if choice.upper() == 'N':
        pass
    else:
        print("\n!!! Cette action est irréversible, appuyer ENTER !!!")
        input("")
        for file in list_files:
            if not file in lasts_files:
                os.chdir(choose_folder)
                #os.remove(file)
        print(f"{len(list_file_delete)} fichiers supprimés, dossier traité.")
        choose_folder = ''
        return choose_folder


def start():
    choose_folder = new_folder()
    os.chdir(choose_folder)
    list_files = os.listdir()
    lasts_files = order_files(list_files)
    list_file_delete = file_to_delete(list_files, lasts_files)
    delete_file(list_file_delete)
    another_folder()


def another_folder():
    choice = input("voulez vous traiter un autre dossier ?\n Y - N : ")
    if choice.upper() == 'Y':
        start()
    else:
        exit()


start()
#delete_file(list_files, lasts_files, list_file_delete, choose_folder)
#choose_folder = ''
#another_folder()