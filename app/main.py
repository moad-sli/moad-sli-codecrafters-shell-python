import glob
import sys
import os

all_command=["exit","echo","type"]
command_path=os.getenv("PATH").split(os.pathsep)
list_of_paths=os.getenv("PATH").split(os.pathsep)


def command_in_path(command):
    for path in list_of_paths:
        command_path = path + "/" + command
        if command_path in glob.glob(path + "/*"):
            return command_path
    return False

def type_command(user_input):

    command = user_input.strip().removeprefix("type").strip().split(" ")[0]
    if command in all_command:
        print(f"{command} is a shell builtin")
    else:
        command_path=command_in_path(command)
        if command_path:
                print(f"{command} is {command_path}")
                return 1
        else:
            print(f"{command}: not found")
    return 1

def run_command(user_input):
    command=user_input.strip().split(" ")[0]
    command_path=command_in_path(command)
    if command_path:
        args=user_input.strip().removeprefix(command).strip()
        return os.system(user_input)
    else:
        return 1

def command_not_found(user_input):
    if user_input == "exit 0":
        return 0
    elif user_input.startswith("echo "):
        print(user_input.removeprefix("echo ").strip())
        return 1
    elif user_input.startswith("type"):
        type_command(user_input)
        return 1
    else:
        if run_command(user_input)==0:
            return 1
        else:
            print(f"{user_input}: command not found")
            return 1

def take_input():
    sys.stdout.write("$ ")
    return input()

def main():

    # Wait for user input
    command=take_input()
    while command_not_found(command):
        command=take_input()

if __name__ == "__main__":
    main()
