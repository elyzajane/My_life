def write_to_file():
    try:
       # Open a writing file
       with open("mylife.txt", "w") as file: 
            # Ask the user to input and write to file
            while True:
                # Ask the user to input a line of text
                line = input("Enter line: ")

                # Write the line to the file
                file.write(line + "\n")

                # Ask the user if there are more lines to enter
                more_lines = input("Are there more lines y/n? ")
                if more_lines.lower() == "n":
                    break

        # Print a message indicating the file has been written successfully
            print("The file mylife.txt has been written successfully.")
    except IOError:
        # If an error occurs while writing to the file, print an error message
        print("An error occurred while writing to the file.")

write_to_file()