import sys

def command_not_found(user_input):
    print(f"{user_input}: command not found")
def main():
    sys.stdout.write("$ ")

    # Wait for user input
    command=input()
    command_not_found(command)

if __name__ == "__main__":
    main()
