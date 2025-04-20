import os
import sys

from config import CONFIG


def init_notebooks():
    # change to the main dir
    root_dir = CONFIG.project_root
    print(f'Project Directory is set as `{root_dir}`')
    os.chdir(root_dir)
    packages_dirs = [
        'models',
        'notebooks',
        'projects',
        'tutorials',
        'utils',
    ]
    for folder_name in packages_dirs:
        packages_dir = str(root_dir / folder_name)
        if packages_dir not in sys.path:
            sys.path.append(packages_dir)
