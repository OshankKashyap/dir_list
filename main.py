# Main module for the directory listing program

import os
import sys


class Main:
    def check_hidden(self, file: str) -> bool:
        # Check if the provided file is hidden or not
        # check if the operating system is nt or posix
        if os.name == "nt":
            return True
        elif os.name == "posix":
            if file[0] == ".":
                return False
            else:
                return True

    def show_files(self, path: str) -> None:
        # Show all the content present in current path
        number = 1
        contents = os.listdir(path)

        # perform a check for hidden files and only show the un-hidden files and directories
        for content in contents:
            content = os.path.join(path, content)
            # if sys.platform == "win32":

            if (
                os.path.isfile(content) or os.path.isdir(content)
            ) and self.check_hidden(os.path.basename(content)):
                print(f"[{number}] {os.path.basename(content)}")
                number += 1


# get the path and check if it is valid or not
try:
    path = sys.argv[1]
except IndexError:
    print("Path was not provided.")
    sys.exit()

if not os.path.exists(path):
    print(f"PATH: {path}; does not exist")
    sys.exit()

main = Main()
main.show_files(path)
