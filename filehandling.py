class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def write_file(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)
        print(f"Content written to {self.filename}")

    def read_file(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        print(f"Content of {self.filename}:")
        print(content)
        return content

    def append_file(self, content):
        with open(self.filename, 'a') as file:
            file.write(content)
        print(f"Content appended to {self.filename}")

    def read_in_binary(self):
        with open(self.filename, 'rb') as file:
            content = file.read()
        print(f"Binary content of {self.filename}:")
        print(content)
        return content

    def write_in_binary(self, content):
        with open(self.filename, 'wb') as file:
            file.write(content)
        print(f"Binary content written to {self.filename}")

# Main program
def main():
    print("File Handling Activity:")
    filename = input("Enter the filename to work with: ")
    file_handler = FileHandler(filename)

    while True:
        print("\nChoose an operation:")
        print("1. Write to the file")
        print("2. Read the file")
        print("3. Append to the file")
        print("4. Read the file in binary mode")
        print("5. Write to the file in binary mode")
        print("6. Exit")

        choice = int(input("Enter your choice (1/2/3/4/5/6): "))

        if choice == 1:
            content = input("Enter content to write to the file: ")
            file_handler.write_file(content)

        elif choice == 2:
            file_handler.read_file()

        elif choice == 3:
            content = input("Enter content to append to the file: ")
            file_handler.append_file(content)

        elif choice == 4:
            file_handler.read_in_binary()

        elif choice == 5:
            content = input("Enter content to write in binary (will be encoded as UTF-8): ").encode('utf-8')
            file_handler.write_in_binary(content)

        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
