# MODULE INSTALLER BASE |FROM MC LANG REPOSITIORY| v0.1 | ORIGINAL CODE
# edit here:
module_file = "./core.mclangmodule"
install_file = "core.mclangmodule"
version_file = "./versioninfo"
#OPTIONAL: repository link:
repo_link = "https://github.com/Patric-k-k/minecraftprogramminglang"
repo_type = "github repository"
# Code:
import os
try:
    module_path = os.path.join(os.getenv("APPDATA"), "mclang", "modules", install_file)
    with open(module_path, "r") as f:
        lines = f.readlines()
    with open(version_file, "r") as f:
        version = f.readlines()[3]
    if lines[0].replace("#","").strip() == version.strip():
        print("VERSION IS UP TO DATE")
        print(f"YOU CAN CHECK IF THERE IS A MORE UP TO DATE VERSION THEN {version.strip()} AT THE {repo_type.upper()}. {f'({repo_link})' if repo_link != '' else ''}")
        from time import sleep
        sleep(2)
        exit(0)
    else:
        print(f"!!CORE MODULE OUT OF DATA!! Installed version: {lines[0].replace('#','')}. Installer version: {version}")
except FileNotFoundError:
    ...
print("!!WARNING!! This file does not check for any new versions.")
print("!!WARNING!! It only uses the one in this directory, and")
print("!!WARNING!! doesn't access the internet.")
print("this file is EXPERIMENTAL and is NOT REQUIRED yet.")
print("you don't need to run this file UNLESS you want to use")
print("the programming language in a different directory.")
print("do you want to continue? (y/n)", end=" ")
i = input()
if i.lower() == "y":
    print("Installing core module...")
    with open(module_file, "r") as f:
        lines = f.readlines()
    module_path = os.path.join(os.getenv("APPDATA"), "mclang", "modules", install_file)
    os.makedirs(os.path.dirname(module_path), exist_ok=True)
    with open(module_path, "w+") as f:
        f.writelines(lines)