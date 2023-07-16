from pathlib import Path
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--module", type=str)

args = parser.parse_args()
module = args.module


def generate_file_path(week_number: int, module_name: str) -> str:
    return f"{os.getcwd()}/{module_name}/{module_name.split('-')[0]} week {week_number:02d}.md"


def generate_file(week_number: int, module_name: str):
    Path(generate_file_path(week_number, module_name)).touch()


def generate_all_files(module_name: str):
    Path(f"{os.getcwd()}/{module_name}").mkdir()
    for i in range(10):
        generate_file(i+1, module_name)


generate_all_files(module)
