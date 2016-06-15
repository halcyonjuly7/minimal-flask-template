import os


class CreateDirectories:
    def __init__(self, project_path):
        self.project_path = project_path

    def _create_root_directories(self):
        root_dirs = [("config",), ("project",)]
        self._create_folders(root_dirs)

    def _create_project_directories(self):
        project_dirs = [("project", "core"),
                        ("project", "static"),
                        ("project", "templates")]
        self._create_folders(project_dirs)

    def _create_core_directories(self):
        core_folders = [("project", "core", "apps"), ("project", "core", "misc")]
        self._create_folders(core_folders)

    def _create_folders(self, folders):
        for folder in folders:
            path = os.path.join(self.project_path,  *folder)
            os.makedirs(path)

    def _create_app_directories(self):
        app_dirs = [("project", "core", "apps", "celery"), ("project", "core", "apps","index")]
        self._create_folders(app_dirs)

    def create_initial_directories(self):
        self._create_root_directories()
        self._create_project_directories()
        self._create_core_directories()
        self._create_app_directories()




