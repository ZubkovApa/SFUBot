\# Telegram бот — школа кулинарии (минимальный проект)





Проект: бот для первичной консультации клиентов школы кулинарии.





Особенности:

\- Python + aiogram (polling)

\- Хранение данных: SQLite (локально)

\- Интерфейс: кнопки (главное меню), многошаговая анкета (FSM)

\- Язык: русский

\- Не используется Google Sheets





\## Быстрый старт (локально)

1\. Склонируй проект или создай структуру файлов по содержимому этого репозитория.

2\. Создай виртуальное окружение и установи зависимости:





```bash

python -m venv venv

source venv/bin/activate # или venv\\Scripts\\activate на Windows

pip install -r requirements.txt

```





3\. Создай файл `.env` по образцу `.env.example` и вставь туда BOT\_TOKEN.





4\. Инициализируй БД (опционально — приложение создаст таблицы автоматически при первом запуске).





```bash

python -m app.create\_db

```





5\. Запусти бота (polling):





```bash

python -m app.main

```





\## Структура проекта

\- app/main.py — запуск polling

\- app/bot.py — инициализация aiogram

\- app/config.py — чтение env

\- app/handlers/ — handlers и маршруты

\- app/db.py — работа с SQLite

\- app/models.py — SQL схемы (создаются автоматически)

\- app/create\_db.py — создание БД

\- requirements.txt — зависимости



