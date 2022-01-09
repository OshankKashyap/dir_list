# Main module for the directory listing program

import os


class Main:
    def __init__(self):
        self.get_curr_path()

    def get_curr_path(self) -> None:
        # Method to get the current path and store it in self.curr_path
        # self.path = os.getcwd()
        self.path = os.getcwd()

    def check_hidden(self, file: str) -> bool:
        # Check if the provided file is hidden or not
        # only for UNIX systems

        if file[0] == ".":
            return False
        else:
            return True

    def show_content(self) -> None:
        # Show all the content present in the current path

        number = 1
        contents = os.listdir(self.path)
        # perform a check for hidden files and only show the un-hidden files and directories
        for content in contents:
            content = os.path.join(self.path, content)
            if (
                os.path.isfile(content) or os.path.isdir(content)
            ) and self.check_hidden(os.path.basename(content)):
                print(f"[{number}] {os.path.basename(content)}")
                number += 1


main = Main()
main.show_content()
