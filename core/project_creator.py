import argparse
from core.create_directories import CreateDirectories
from core.create_files import CreateFiles



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p")
    args = parser.parse_args()
    return args.path



def create_project():
    path = get_args()
    initial_directories = CreateDirectories(path)
    initial_files = CreateFiles(path)

    initial_directories.create_initial_directories()
    initial_files.create_initial_files()






