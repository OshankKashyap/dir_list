# Main module for the directory listing program

import os
import sys


class Main:
    def check_hidden(self, file: str) -> bool:
        # Check if the provided file is hidden or not
        # only for UNIX systems

        if file[0] == ".":
            return False
        else:
            return True

    def show_files(self, path) -> None:
        # Show all the content present in current path
        number = 1
        contents = os.listdir(path)

        # perform a check for hidden files and only show the un-hidden files and directories
        for content in contents:
            content = os.path.join(path, content)
            if (
                os.path.isfile(content) or os.path.isdir(content)
            ) and self.check_hidden(os.path.basename(content)):
                print(f"[{number}] {os.path.basename(content)}")
                number += 1


# get the path and check if it is valid or not
path = input("Enter Path -> ")
if not os.path.exists(path):
    print(f"{path}: does not exist")
    sys.exit()

main = Main()
main.show_files(path)
