# not finished
# a class to find all the functions in a file and give comments and dependencies in a structured manner
class FileAnalyzer:
    class CFunction:
        def __init__(self, function_name: str, function_comment: str, dependencies: str, line):
            self.function_name: str = function_name
            self.function_comment: str = function_comment
            self.dependencies: str = dependencies
            self.line: int = line

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_content = None
        with open(self.file_path, 'r') as file:
            self.file_content = file.read()

        # a list of all the functions defined in there with their dependencies and comments
        self.function_list: dict[str, FileAnalyzer.CFunction] = {}
        # the contents will look like this
        # {
        # "function_name" : ["function_comment" , dependencies]
        # }

    def analyze(self):
        def find_functions(file_name: str):
            with open(file_name, 'r') as file:
                contents: list[str] = file.read().split(';')

