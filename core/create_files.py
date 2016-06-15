import os
from text_formats.format import root_run, root_init, celery_worker, celery_task, views, blueprint_init, helper_functions, html_format, celery_runner

from helper_functions.helpers import generate_filepath, create_file, create_files

class CreateFiles:
    def __init__(self, project_path):
        self.project_path = project_path

    def _create_root_files(self):
        root_files = [(self.project_path, "run.py", {"file_format": root_run}),
                      (self.project_path, "project", "__init__.py", {"file_format": root_init}),
                      (self.project_path, "config", "development.py", {"file_format": ""}),
                      (self.project_path, "celery_app.py", {"file_format": celery_runner})]

        create_files(root_files)

    def _create_other_init_files(self):
        init_locations = [(self.project_path, "project", "core", "__init__.py", {"file_format": ""}),
                          (self.project_path, "project", "core", "misc", "__init__.py", {"file_format": ""}),
                          (self.project_path, "project", "core", "apps", "__init__.py", {"file_format": ""}),
                          (self.project_path, "project", "core", "apps", "celery", "__init__.py", {"file_format": ""})]

        create_files(init_locations)

    def _create_app_files(self):
        apps_location = os.path.join(self.project_path, "project", "core", "apps")
        app_files = [(apps_location, "celery", "tasks.py", {"file_format": celery_task}),
                     (apps_location, "celery", "worker.py", {"file_format": celery_worker}),
                     (apps_location, "index", "views.py", {"file_format": views }),
                     (apps_location, "index", "__init__.py", {"file_format": blueprint_init("index")})]
        create_files(app_files)


    def _create_misc_files(self):
        misc_location = os.path.join(self.project_path, "project", "core", "misc")
        misc_files = [(misc_location, "helpers.py", {"file_format": helper_functions})]
        create_files(misc_files)

    def _create_html_files(self, *pages):
        html_folder = os.path.join(self.project_path, "project", "templates")
        html_files = []
        for page in pages:
            html_page = "{page}.html".format(page=page)
            html_file = (os.path.join(html_folder, html_page), {"file_format": html_format})
            html_files.append(html_file)
        create_files(html_files)

    def create_initial_files(self):
        self._create_root_files()
        self._create_other_init_files()
        self._create_app_files()
        self._create_misc_files()
        self._create_html_files("index")




