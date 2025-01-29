import os

DIR_PATH: str = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "parse_functions",
)
FILE_NAME: str = "parse_functions.py"

DEST_PATH: str = "test.md"

INTRO: str = f"""# Python Functions - [{FILE_NAME}]({FILE_NAME})

Standardized functions to save up repetitive work and keep code clean within Python scripting.
These all have basic formats and uses, but they can be customized relatively easily to achieve tailored functionalities.

## Content
"""


def main() -> None:
    data: list[str] = read_python_script(os.path.join(DIR_PATH, FILE_NAME))
    functions: list[PythonFunction] = []
    classes: list[PythonClass] = []
    functions, classes = get_content(data)
    readme = ReadMe()
    readme.generate(functions, classes)
    readme.write(DEST_PATH)


class PythonFunction:
    def __init__(self) -> None:
        self.name: str = ""
        self.content: str = ""
        self.en_content: bool = False
        self.summaries: list[str] = []
        self.en_summaries: bool = False
        self.args: list[str] = []
        self.en_args: bool = False
        self.returns: list[str] = []
        self.en_returns: bool = False

    def add_line(self, line: str) -> None:
        if self.en_summaries or line.strip().startswith('"""'):
            self._add_summary(line)
        if self.en_args:
            self._add_argument(line)
        elif self.en_returns:
            self._add_return(line)
        if self.en_content and not self.en_summaries:
            self._add_content(line)

    def set_name(self, line: str) -> None:
        self.name = line[line.index("def ") + 4 : line.index("(")] + "()"
        self.en_content = True

    def _add_content(self, line: str) -> None:
        if line.strip() != '"""':
            self.content += line

    def _add_summary(self, line: str) -> None:
        self.en_summaries = True
        if line.strip() == "":
            pass
        elif len(self.summaries) == 0:
            self.summaries.append(line.strip()[3:])
        elif line.strip() == '"""':
            self.en_summaries = False
            self.en_args = False
            self.en_returns = False
        elif line.strip() == "Args:":
            self.en_args = True
            self.en_returns = False
        elif line.strip() == "Returns:":
            self.en_args = False
            self.en_returns = True
        elif not self.en_args and not self.en_returns:
            self.summaries.append(f"\n{line}")

    def _add_argument(self, line: str) -> None:
        if line.strip():
            self.args.append(line.strip())

    def _add_return(self, line: str) -> None:
        if line.strip():
            self.returns.append(line.strip())


class PythonClass:
    def __init__(self) -> None:
        self.name: str = ""
        self.content: str = ""
        self.en_content: bool = False
        self.summaries: list[str] = []
        self.en_summaries: bool = False

    def add_line(self, line: str) -> None:
        if self.en_summaries or line.strip().startswith('"""'):
            self._add_summary(line)
        if self.en_content and not self.en_summaries:
            self._add_content(line)

    def set_name(self, line: str) -> None:
        self.name = line[line.index("class ") + 6 : line.index("(")] + "()"
        self.en_content = True

    def _add_content(self, line: str) -> None:
        if line.strip() != '"""':
            self.content += line

    def _add_summary(self, line: str) -> None:
        self.en_summaries = True
        if line.strip() == "":
            pass
        elif len(self.summaries) == 0:
            self.summaries.append(line.strip()[3:])
        elif line.strip() == '"""':
            self.en_summaries = False
        else:
            self.summaries.append(line.strip())


class ReadMe:
    def __init__(self) -> None:
        self.intro: str = INTRO
        self.func_content: list[str] = []
        self.functions: list[str] = []
        self.class_content: list[str] = []
        self.classes: list[str] = []

    def generate(
        self, functions: list[PythonFunction], classes: list[PythonClass]
    ) -> None:
        for func in functions:
            self._add_function(func)
        for cls in classes:
            self._add_class(cls)

    def _add_function(self, func: PythonFunction) -> None:
        self.func_content.append(f"    -   [{func.name}](#{func.name[:-2].lower()})")
        func_str: str = ""
        func_str += f"## {func.name}\n\n"
        for sum in func.summaries:
            func_str += f"{sum}\n"
        func_str += "\n"
        for idx, arg in enumerate(func.args):
            if idx == 0:
                func_str += f"-   {arg}\n\n"
            else:
                func_str += f"    {arg}\n"
        else:
            func_str += "\n"
        for idx, ret in enumerate(func.returns):
            if idx == 0:
                func_str += f"-   {ret}\n\n"
            else:
                func_str += f"    {ret}\n"
        else:
            func_str += "\n"
        func_str += f"```python\n{func.content.strip()}\n```\n"
        self.functions.append(func_str)

    def _add_class(self, cls: PythonClass) -> None:
        self.class_content.append(f"    -   [{cls.name}](#{cls.name[:-2].lower()})")
        cls_str: str = ""
        cls_str += f"## {cls.name}\n\n"
        for sum in cls.summaries:
            cls_str += f"{sum}\n"
        cls_str += "\n"
        cls_str += f"```python\n{cls.content.strip()}\n```\n"
        self.classes.append(cls_str)

    def write(self, file_path: str) -> str:
        with open(file_path, "w") as f:
            f.write(self.intro)
            if len(self.functions) > 0:
                f.write("\n-   [Functions](#functions):\n\n")
                f.write("\n".join(self.func_content))
            if len(self.classes) > 0:
                f.write("\n-   [Classes](#classes):\n\n")
                f.write("\n".join(self.class_content))
            if len(self.functions) > 0:
                f.write("\n\n# Functions\n\n")
                f.write("\n".join(self.functions))
            if len(self.classes) > 0:
                f.write("\n\n# Classes\n\n")
                f.write("\n".join(self.classes))
        return file_path


def read_python_script(filepath: str) -> list[str]:
    data: list[str] = []
    with open(filepath, "r") as f:
        for line in f:
            data.append(line)
    return data


def get_content(data: list[str]) -> tuple[list[PythonFunction], list[PythonClass]]:
    functions: list[PythonFunction] = []
    func = PythonFunction()
    en_func: bool = False
    classes: list[PythonClass] = []
    cls = PythonClass()
    en_cls: bool = False
    for line in data:
        if line.startswith("def "):
            en_func = True
            en_cls = False
            if func.name:
                functions.append(func)
            func = PythonFunction()
            func.set_name(line)
        if en_func:
            func.add_line(line)
        if line.startswith("class "):
            en_cls = True
            en_func = False
            if cls.name:
                classes.append(cls)
            cls = PythonClass()
            cls.set_name(line)
        if en_cls:
            cls.add_line(line)
    if func.name:
        functions.append(func)
    if cls.name:
        classes.append(cls)
    return functions, classes


if __name__ == "__main__":
    main()
