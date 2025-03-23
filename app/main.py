import glob
import sys
import os
import shlex
import readline



all_command=["exit","echo","type","pwd","cd"]
command_path=os.getenv("PATH").split(os.pathsep)
list_of_paths=os.getenv("PATH").split(os.pathsep)
options = [command.split("/")[-1] for path in list_of_paths for command in glob.glob(path+"/*") ]+all_command

def complete(text,state):
    matches = [option for option in options if option.startswith(text)]
    if state < len(matches):
        return matches[state]+" "
    return None
def display_matches(input,matches,state):
    print()
    if matches:
        print(" ".join(matches))
    print("$ " + input, end="")

readline.set_completer(complete)
readline.parse_and_bind('tab: complete')
readline.set_completion_display_matches_hook(display_matches)

def command_in_path(command):
    for path in list_of_paths:
        command_path = path + "/" + command
        if command_path in glob.glob(path + "/*"):
            return command_path
    return False

def type_command(user_input,file_object=None):

    command = user_input.strip().removeprefix("type").strip().split(" ")[0]
    if command in all_command:
        print(f"{command} is a shell builtin",file=file_object)
    else:
        command_path=command_in_path(command)
        if command_path:
                print(f"{command} is {command_path}",file=file_object)
                return 1
        else:
            print(f"{command}: not found")
    return 1

def run_command(user_input):
    command=shlex.split(user_input)[0]
    command_path=command_in_path(command)
    if command_path:
        #args=user_input.strip().removeprefix(command).strip()
        return os.system(user_input)
    else:
        return 1

def cd_command(user_input):
    path=user_input.removeprefix("cd").strip()
    if path == "~":
        path=os.getenv("HOME")
    try:
        os.chdir(path)
    except:
        print(f"cd: {path}: No such file or directory")
def std_redirection(user_input):
    if "2>>" in user_input:
        error_file=open(user_input.split("2>>")[1].strip(),"a")
        command = user_input.split("2>>")[0]
        file_object=None
    elif "2>" in user_input:
        error_file=open(user_input.split("2>")[1].strip(),"w")
        command = user_input.split("2>")[0]
        file_object=None
    elif "1>>" in user_input or ">>" in user_input:
        user_input = user_input.replace("1>>", ">>")
        file_name = user_input.split(">>")[1].strip()
        file_object = open(file_name, "a")
        command = user_input.split(">")[0]
    elif "1>" in user_input or '>' in user_input:
        user_input=user_input.replace("1>",">")
        file_name=user_input.split(">")[1].strip()
        file_object=open(file_name,"w")
        command=user_input.split(">")[0]
    else:
        command=user_input
        file_object=None
    return command,file_object

def exec_command(user_input):
    command,file_object = std_redirection(user_input)

    if command == "exit 0":
        return 0
    elif command.startswith("echo "):
        print(' '.join(shlex.split(command.removeprefix("echo ").strip())),file=file_object)
    elif command.startswith("type"):
        type_command(command,file_object)
    elif user_input.startswith("cd"):
       cd_command(user_input)
    elif command.strip()=="pwd":
        print(os.path.abspath(os.getcwd()),file=file_object)
    else:
        if run_command(user_input) in [0,256]:
            pass
        else:
            print(f"{user_input}: command not found")
    return 1

def take_input():
    sys.stdout.write("$ ")
    command = input()
    if command.startswith("ech\t"):
        command="echo"
    elif command.startswith("exi\t"):
        command="exit"
    return command


def main():

    # Wait for user input
    command=take_input()
    while exec_command(command):
        command=take_input()

if __name__ == "__main__":
    main()
