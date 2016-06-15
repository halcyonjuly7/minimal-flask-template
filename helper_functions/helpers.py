import os

def generate_filepath(project_location):
    file_path =  os.path.join(*project_location)
    return file_path


def create_file(file_path, file_format=None):
    with open(file_path, "w") as file:
        if file_format:
            file.write(file_format)
        else:
            file.write("")

# def create_files(file_paths, project_path):
#     for file in file_paths:
#         *file_location, file_format = file
#         file_path = generate_filepath(project_path, *file_location)
#         create_file(file_path, **file_format)

def create_files(file_paths):
    for file in file_paths:
        *file_location, file_format = file
        file_path = generate_filepath(file_location)
        create_file(file_path, **file_format)