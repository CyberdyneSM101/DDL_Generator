from colorama import init, Fore, Back, Style
import random
import Your_Font

def Generate_GoogleDrive_Direct_link(x):
    Link = x.split("/file/d/")
    Main_Link = Link[0]
    Initializer = "/u/0/uc?id="
    Link = Link[1].split("/view?usp=sharing")
    Link = Link[0]
    Download_Command = "&export=download"
    return Main_Link+Initializer+Link+Download_Command

def Generate_OneDrive_Direct_Link(x):
    x = x.split("\"")
    x = x[1].split("embed")
    x.insert(1,"download")
    return "".join(x)

def Generate_FileTransfer_Direct_Link(x):
    Link = x+"?do=download"
    return Link

def Banner():
    B1 = ['\n    ____  _                __     __    _       __      ______                           __            \n   / __ \\(_)_______  _____/ /_   / /   (_)___  / /__   / ____/__  ____  ___  _________ _/ /_____  _____\n  / / / / / ___/ _ \\/ ___/ __/  / /   / / __ \\/ //_/  / / __/ _ \\/ __ \\/ _ \\/ ___/ __ `/ __/ __ \\/ ___/\n / /_/ / / /  /  __/ /__/ /_   / /___/ / / / / ,<    / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    \n/_____/_/_/   \\___/\\___/\\__/  /_____/_/_/ /_/_/|_|   \\____/\\___/_/ /_/\\___/_/   \\__,_/\\__/\\____/_/     \n\n                                                            To Generate Direct Link for:\n                                                                1- Google Drive\n                                                                2- OneDrive [all files without pictures]\n                                                                3- filetransfer.io']
    B2 = ['\n___  _ ____ ____ ____ ___    _    _ _  _ _  _    ____ ____ _  _ ____ ____ ____ ___ ____ ____ \n|  \\ | |__/ |___ |     |     |    | |\\ | |_/     | __ |___ |\\ | |___ |__/ |__|  |  |  | |__/ \n|__/ | |  \\ |___ |___  |     |___ | | \\| | \\_    |__] |___ | \\| |___ |  \\ |  |  |  |__| |  \\ \n\n                                                            To Generate Direct Link for:\n                                                                1- Google Drive\n                                                                2- OneDrive [all files without pictures]\n                                                                3- filetransfer.io']
    return random.choice([B1[0],B2[0]])

def Help():
    H1 = ['\n|=======================================================================|\n|  Commands Menu                                                        | \n|  =============                                                        |    \n|                                                                       |\n|  Command                 Description                                  |                                    \n|  -------                 -----------                                  |                                    \n|     1                    Generate Direct Link for Google Drive        |                                    \n|                          [*] Your Google Drive Shareable Link         |\n|                                                                       |                                \n|     2                    Generate Direct Link for OneDrive            |                            \n|                          [*] Your OneDrive Embed Link                 |\n|                                                                       |\n|     3                    Generate Direct Link for filetransfer.io     |                                                            \n|                                                                       |\n|    help                  print Help Menu                              |    \n|                                                                       |    \n|    back                  exit the tool                                |\n|=======================================================================|\n']
    return H1[0]



def Main():
    Your_Font.Your_Font()
    init(autoreset=True)
    print(Fore.GREEN+Banner())
    print(Fore.GREEN+"\n[*] For Uasge type: help")
    print(Fore.GREEN+"[+] Coded by Cyberdyne")
    print(Fore.GREEN+"[+] Discord: Cyberdyne#9233 "+"\n")
    while True:
        try:
            main = input("[*]Generator: ")
            if main == "1":
                try: 
                    m1 = input("\n[*]Shareable Link: ")
                    init(autoreset=True)
                    print(Fore.GREEN+ "\n[+]Your Direct Link: \n"+ Generate_GoogleDrive_Direct_link(m1)+ "\n")
                    pass
                except KeyboardInterrupt:
                    init(autoreset=True)
                    print(Fore.RED+"[-]Keyboard Interrupt Blocked")
                    pass
                except:
                    init(autoreset=True)
                    print(Fore.RED+"[-]Link Is Incorrect")
                    pass

            elif main == "2":
                try: 
                    m2 = input("\n[*]Embed Link: ")
                    init(autoreset=True)
                    print(Fore.GREEN+ "\n[+]Your Direct Link: \n"+ Generate_OneDrive_Direct_Link(m2)+ "\n")
                    pass
                except KeyboardInterrupt:
                    init(autoreset=True)
                    print(Fore.RED+"[-]Keyboard Interrupt Blocked")
                    pass
                except:
                    init(autoreset=True)
                    print(Fore.RED+"[-]Link Is Incorrect")
                    pass
            elif main == "3":
                try:
                    m2 = input("\n[*]Link: ")
                    init(autoreset=True)
                    print(Fore.GREEN+ "\n[+]Your Link: \n"+ Generate_FileTransfer_Direct_Link(m2)+ "\n")
                    pass
                except KeyboardInterrupt:
                    init(autoreset=True)
                    print(Fore.RED+"[-]Keyboard Interrupt Blocked")
                    pass
                except:
                    init(autoreset=True)
                    print(Fore.RED+"[-]Link Is Incorrect")
                    pass

            elif main == "help":
                print(Help())
            elif main == "exit":
                break
            
        except KeyboardInterrupt:
            init(autoreset=True)
            print(Fore.RED+"[-]Keyboard Interrupt Blocked")
        finally:
            pass

if __name__ == "__main__":
    Main()
















