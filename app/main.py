import glob
import sys
import os

all_command=["exit","echo","type"]
command_path=os.getenv("PATH").split(os.pathsep)

def type_command(user_input):
    list_of_paths=os.getenv("PATH").split(os.pathsep)
    command = user_input.strip().removeprefix("type").strip().split(" ")[0]
    if os.getenv("PATH"):
        for path in list_of_paths:
            command_path = path + "/" + command
            if command_path in glob.glob(path + "/*"):
                print(f"{command} is {command_path}")
                return 1
        else:
            print(f"{command}: not found")

    else:
        if command in all_command:
            print(f"{command} is a shell builtin")
        else:
            print(f"{command} invalid_command")
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
