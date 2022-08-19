#Author Jan "zemler" Zemla
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