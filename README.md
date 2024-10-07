Импортер для удобной и быстрой загрузки пакетов на Nexus. Использует `twine` для работы

# Запуск
1. Создать `.env` файл с следующим содержимым в корне проекта
```bash
LOG_LEVEL = "INFO"
PACKAGES_DIR = "path/to/deps"
NEXUS_URL = "target-Nexus-repository"
USERNAME = "your-username"
PASSWORD = "your-password"
```
2. Установить зависимости из requirements.txt командой
```bash
pip install reqirements
```
3. Есть два варианта:
    - Запустить команду:
        ```bash
        python3 src/main.py
        ```
    - Запустить через `F5` в **VSCode**


# Логи
В корне проекта будет создаваться файл `.log` содержащий логи и результаты выполнения команды. Чтобы поменять уровень нужно изменть поле `LOG_LEVEL` в .env файле