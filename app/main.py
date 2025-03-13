import sys

def command_not_found(user_input):
    print(f"{user_input}: command not found")
    return 1
def main():
    sys.stdout.write("$ ")

    # Wait for user input
    command=input()
    while command_not_found(command):
        sys.stdout.write("$ ")
        command=input()

if __name__ == "__main__":
    main()
