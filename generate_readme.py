import os

DIR_PATH: str = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "mouse",
)
FILE_NAME: str = "simulate_mouse.py"

DEST_PATH: str = "test.md"

INTRO: str = f"""# Python Functions - [{FILE_NAME}]({FILE_NAME})

Standardized functions to save up repetitive work and keep code clean within Python scripting.
These all have basic formats and uses, but they can be customized relatively easily to achieve tailored functionalities.

## Content

"""


def main() -> None:
    data: list[str] = read_python_script(os.path.join(DIR_PATH, FILE_NAME))
    functions: list[PythonFunction] = get_functions(data)
    readme: ReadMe = create_readme(functions)
    write_readme(readme, DEST_PATH)


class PythonFunction:
    def __init__(self) -> None:
        self.name: str = ""
        self.content: str = ""
        self.en_content: bool = False
        self.summary: str = ""
        self.args: list[str] = []
        self.en_args: bool = False
        self.returns: list[str] = []
        self.en_returns: bool = False

    def add_line(self, line: str) -> None:
        if line.startswith("def "):
            self._set_name(line)
            self._add_content(line)
        elif line.strip().startswith('"""'):
            if self.summary == "":
                self._set_summary(line)
        elif line.strip() == "Args:":
            self.en_args = True
        elif line.strip() == "Returns:":
            self.en_returns = True
        elif self.en_content:
            self._add_content(line)
        if (self.en_returns or self.en_args) and line.strip() == '"""':
            self.en_content, self.en_args, self.en_returns = True, False, False
        elif self.en_args:
            if line.strip():
                self._add_argument(line)
            else:
                self.en_args = False
        elif self.en_returns:
            self._add_return(line)

    def _set_name(self, line: str) -> None:
        self.name = line[line.index("def ") + 4 : line.index("(")] + "()"

    def _add_content(self, line: str) -> None:
        self.content += line

    def _set_summary(self, line: str) -> None:
        self.summary = line.strip()[3:]

    def _add_argument(self, line: str) -> None:
        self.args.append(line.strip())

    def _add_return(self, line: str) -> None:
        self.returns.append(line.strip())


class ReadMe:
    def __init__(self) -> None:
        self.intro: str = INTRO
        self.content: list[str] = []
        self.functions: list[str] = []

    def add_function(self, func: PythonFunction) -> None:
        self.content.append(f"-   [{func.name}](#{func.name[:-2]})")
        func_str: str = ""
        func_str += f"### {func.name}\n\n"
        func_str += f"{func.summary}\n\n"
        for idx, arg in enumerate(func.args):
            if idx == 0:
                func_str += f"-   {arg}\n\n"
            else:
                func_str += f"    -   {arg}\n"
        else:
            func_str += "\n"
        for idx, ret in enumerate(func.returns):
            if idx == 0:
                func_str += f"-   {ret}\n\n"
            else:
                func_str += f"    -   {ret}\n"
        else:
            func_str += "\n"
        func_str += f"```python\n{func.content.strip()}\n```\n"
        self.functions.append(func_str)


def read_python_script(filepath: str) -> list[str]:
    data: list[str] = []
    with open(filepath, "r") as f:
        for line in f:
            data.append(line)
    return data


def get_functions(data: list[str]) -> list[PythonFunction]:
    functions: list[PythonFunction] = []
    func = PythonFunction()
    start: bool = False
    for line in data:
        if line.startswith("def "):
            if func.name:
                functions.append(func)
            func = PythonFunction()
        func.add_line(line)
        # if line.startswith("def "):
        #     if func.name:
        #         functions.append(func)
        #     func = PythonFunction()
        #     func.set_name(line)
        #     func.add_content(line)
        # elif line.strip().startswith('"""'):
        #     if func.summary == "":
        #         func.set_summary(line)
        # elif line.strip() == "Args:":
        #     func.en_args = True
        # elif line.strip() == "Returns:":
        #     func.en_returns = True
        # elif func.en_content:
        #     func.add_content(line)
        # if func.en_returns and line.strip() == '"""':
        #     func.en_content, func.en_args, func.en_returns = True, False, False
        # elif func.en_args:
        #     if line.strip():
        #         func.add_argument(line)
        #     else:
        #         func.en_args = False
        # elif func.en_returns:
        #     func.add_return(line)
    functions.append(func)
    return functions


def create_readme(functions: list[PythonFunction]) -> ReadMe:
    result = ReadMe()
    for func in functions:
        result.add_function(func)
    return result


def write_readme(readme: ReadMe, file_path: str) -> str:
    with open(file_path, "w") as f:
        f.write(readme.intro)
        f.write("\n".join(readme.content))
        f.write("\n\n## Functions\n\n")
        f.write("\n".join(readme.functions))
    return file_path


if __name__ == "__main__":
    main()
