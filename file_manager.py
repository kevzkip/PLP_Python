def read_and_modify_file():
    try:
        with open('original.txt', 'r') as infile:
            content = infile.read()

        modified_content = content.upper()

        with open('modified.txt', 'w') as outfile:
            outfile.write("MODIFIED CONTENT:\n")
            outfile.write(modified_content)

        print("✅ Modified content has been written to 'modified.txt'.")

    except FileNotFoundError:
        print("❌ 'original.txt' not found. Please make sure the file exists.")
    except Exception as e:
        print(f"⚠️ An error occurred while reading/writing files: {e}")

def user_file_reader():
    filename = input("📎 Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            print("\n📄 File Content:\n")
            print(file.read())

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("🚫 Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    print("🔧 Running File Read & Modify Operation...\n")
    read_and_modify_file()

    print("\n📘 Running Error Handling Lab...\n")
    user_file_reader()
