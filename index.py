#Author Jan "zemler" Zemla

#Edit file hosts.txt with your hosts :)

import os

def main():
    with open("hosts.txt","r") as data:
            d = data.readline().strip()
            while len(d) != 0:
                os.system("echo ===================================== >> test")
                os.system("echo [+] HOST >> test")
                os.system(f"nslookup {d} >> test")
                os.system("echo ===================================== >> test")
                d = data.readline().strip()

if __name__ == "__main__":
    main()