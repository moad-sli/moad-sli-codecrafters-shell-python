import sys

def command_not_found(user_input):
    if user_input == "exit 0":
        return 0
    elif user_input.startswith("echo "):
        print(user_input.removeprefix("echo ").strip())
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
