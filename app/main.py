import sys

def command_not_found(user_input):
    sys.stdout.write("$ ")
    if user_input == "exit 0":
        return 0
    else:
        print(f"{user_input}: command not found")
        return 1
def main():

    # Wait for user input
    command=input()
    while command_not_found(command):
        command=input()

if __name__ == "__main__":
    main()
