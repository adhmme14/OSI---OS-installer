import os

os.system("clear")

def main():
    while True:
        print("""
1 - apline
2 - archlinux
3 - artix
4 - debian
5 - deepin
6 - fedora
7 - manjaro
8 - opensuse
9 - pardus
10 - ubuntu
11 - void
""")

        cmd = input("select distributions: ")

        if cmd == "1" or cmd == "alpine":
            os.system("proot-distro install alpine")

        elif cmd == 2 or cmd == "archlinux":
            os.system("proot-distro install archlinux")

        elif cmd == "3" or cmd == "artix":
            os.system("proot-distro install artix")

        elif cmd == "4" or cmd == "debian":
            os.system("proot-distro install debian")

        elif cmd == "5" or cmd == "deepin":
            os.system("proot-distro install deepin")

        elif cmd == "6" or cmd == "fedora":
            os.system("proot-distro install fedora")

        elif cmd == "7" or cmd == "manjaro":
            os.system("proot-distro install manjaro")

        elif cmd == "8" or cmd == "opensuse":
            os.system("proot-distro install opensuse")

        elif cmd == "9" or cmd == "pardus":
            os.system("proot-distro install pardus")

        elif cmd == "10" or cmd == "ubuntu":
            os.system("proot-distro install ubuntu")

        elif cmd == "11" or cmd == "void":
            os.system("proot-distro install void")

def setup():
    while True:
        print("[1] install distributions")
        print("[2] setup")
        print("[3] about")
        print("[0] exit")

        cmd = input("\nselect option: ")

        if cmd == "1":
            main()

        elif cmd == "2":
            os.system("pkg install proot-distro")
            print("[*] done")

        elif cmf == "3":
            print("""
OSI - OS Installer
version: 1.0
made by IAM_ALONE (adhmme14)""")

        elif cmd == "0":
            break

        else:
            print("[*] unavailable command")

setup()
