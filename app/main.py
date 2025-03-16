import sys
all_command=["exit","echo","type"]

def type_command(user_input):
    command = user_input.strip().rstrip("type").strip().split(" ")[0]
    if command in all_command:
        print(f"{command} is a shell builtin")
    else:
        print(f"{command}: not found")

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
