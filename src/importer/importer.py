import os
import subprocess
from logging import Logger
from src import config


def get_packages_names(path: str, logger: Logger) -> list:
    packages = []
    for filename in os.listdir(path):
        file_name = os.path.basename(filename)

        if file_name.split(".")[-1] != "whl":
            logger.warning(
                f"Файл {file_name} не имеет требуемого расширения \".whl\""
                )
            continue

        packages.append(file_name)


def download_packages(logger: Logger):
    packages_dir = config.PACKAGES_DIR
    nexus_url = config.NEXUS_URL
    username = config.USERNAME
    password = config.PASSWORD

    packages = get_packages_names(packages_dir, logger)

    if not packages:
        return None

    for package in packages:
        try:
            package_path = os.path.join(packages_dir, package)
            subprocess.run(
                [
                    "twine",
                    "upload",
                    "-r",
                    nexus_url,
                    "-u",
                    username,
                    "-p",
                    password,
                    package_path,
                ],
                check=True,
            )
        except Exception as e:
            logger.error(str(e))
            continue
