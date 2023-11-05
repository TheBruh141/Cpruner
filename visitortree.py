import os
import logging


# this is the class to generate a map of the files inside a folder.
class VisitorTree:

    def __init__(self):
        self.crawl_root: str = "NOT SET YET"
        self.files: dict = {}

    def initializeVisitorTree(self, file_location: str):
        # Crawl through the entire file tree and find .c and .h associated files
        # and store them, so that they can be accessed later

        # Reset the existing data if needed
        self.files = {}
        self.crawl_root = file_location

        # Walk through the directory tree starting from the provided file_location
        for root, dirs, files in os.walk(file_location):
            for filename in files:
                if filename.endswith(".c") or filename.endswith(".h"):
                    file_path = os.path.join(root, filename)

                    # Extract the base name (without extension) and extension of the file
                    base_name, extension = os.path.splitext(filename)

                    # Check if the file is a .c or .h file
                    if extension in [".c", ".h"]:
                        # Create a unique key for the file based on its base name
                        key = os.path.join(root, base_name)

                        # If the key does not exist in self.files, create a new entry
                        if key not in self.files:
                            self.files[key] = []

                        # Append the file to the list associated with the key
                        self.files[key].append(filename)

    def getMap(self):
        # Return the generated map
        return self.files
