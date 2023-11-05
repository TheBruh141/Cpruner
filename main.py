import os
import argparse
import logging
import sys
from datetime import datetime
import visitortree as vt


# validates a location
# return values:
# 0 : file or folder does not exist
# 1 : file exists
# 2 : folder exits
# 3 : file exists but not c file
# 4 : folder exists but is empty
# -1 : None
def validate_location(location: str) -> int:
    # Check if the path exists
    if not os.path.exists(location):
        return 0  # File or folder does not exist

    # Check if it's a file
    if os.path.isfile(location):
        if location.endswith('.c'):
            return 1  # File exists and is a C file
        else:
            return 3  # File exists but is not a C file

    # Check if it's a folder
    if os.path.isdir(location):
        contents = os.listdir(location)
        if not contents:
            return 4  # The Folder exists but is empty
        return 2  # Folder exists

    return -1  # Default case (should not be reached)


def set_logger(level: int) -> bool:
    log_level = logging.ERROR  # Default to ERROR
    if level == 1:
        log_level = logging.WARNING
    elif level == 2:
        log_level = logging.INFO
    elif level >= 3:
        log_level = logging.DEBUG

    user_logger = logging.getLogger()
    user_logger.setLevel(log_level)

    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(3)

    # Create a file handler for the log file
    log_file = "Cprune.log"
    with open(log_file, "a") as f:
        f.write(f"\n |-----------<[{str(datetime.now())}]>-----------| \n")
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    user_logger.addHandler(logging.StreamHandler(sys.stdout))

    return True


def main(args):
    # Set the logger verbosity level
    set_logger(args.verbose)

    # Validate the input file or folder
    location = args.filename
    result = validate_location(location)

    # if only we had switch statements in this language
    if result == 0:
        logging.error(f"File or folder '{location}' does not exist.")
    elif result == 1:
        logging.info(f"File '{location}' exists and is a C file.")
    elif result == 2:
        logging.info(f"Folder '{location}' exists.")
    elif result == 3:
        logging.error(f"File '{location}' exists but is not a C file.")
    elif result == 4:
        logging.warning(f"Folder '{location}' exists but is empty.")
    else:
        logging.error("Invalid validation result.")

    tree: vt.VisitorTree = vt.VisitorTree()
    tree.initializeVisitorTree(location)


if __name__ == "__main__":
    # argument parsing
    parser = argparse.ArgumentParser(
        prog='SML-Cprune',
        description='This program is used to analyze dependencies of C code and tree shake (prune) them to become '
                    'more compacted. It removes unnecessary code for compilation.',
        epilog='For more information, go to https://sml-lib-documentation.vercel.app/'
    )

    parser.add_argument("-i", "--input", dest="filename", required=True,
                        help="input file or folder", metavar="FILE/FOLDER")
    parser.add_argument("-v", "--verbose", dest="verbose", type=int, default=0,
                        help="set verbosity level (0=ERROR, 1=WARNING, 2=INFO, 3=DEBUG)", metavar="LEVEL")
    global_args = parser.parse_args()

    # Call the main function to start the program
    main(global_args)
