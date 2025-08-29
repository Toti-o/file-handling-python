# File Handling + Error Handling Assignment
# Author: Your Name
# Date: YYYY-MM-DD

def main():
    # Ask the user for the file to read
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content (e.g., uppercase version)
        modified_content = content.upper()

        # Save to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ File processed successfully! Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don't have permission to access this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
