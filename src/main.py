import logging
from src.importer.importer import download_packages


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


logger.info("Начата загрузка пакетов...")
download_packages(logger)
logger.info("Загрузка завершена!")
