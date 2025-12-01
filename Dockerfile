# Используем стабильный образ Python
FROM python:3.11-slim

# 1. Установка системных зависимостей для сборки uWSGI и gettext
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        build-essential \
        # gettext вам нужен для работы с переводами 
        gettext \
    && rm -rf /var/lib/apt/lists/*

# Создание рабочего каталога
WORKDIR /app

# 2. Установка Python-зависимостей, включая uWSGI
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Копирование всего кода (включая mysite_uwsgi.ini)
COPY . .

# 4. Сбор статических файлов и миграции (выполняются во время сборки образа)
# Настройка переменной окружения для Django
ENV DJANGO_SETTINGS_MODULE=MyEngSite.settings 

# ВНИМАНИЕ: Выполняйте эти команды после COPY . .
# Сбор статических файлов (обязательно для продакшена)
RUN python manage.py collectstatic --noinput 
# Применение миграций (обязательно для продакшена)
RUN python manage.py migrate

# БЕЗОПАСНОСТЬ: создание непривилегированного пользователя и смена владельца
# Запуск от непривилегированного пользователя - хорошая практика безопасности
RUN groupadd -r appuser && useradd -r -g appuser appuser
RUN chown -R appuser:appuser /app
USER appuser

# 5. Открытие порта (для uWSGI)
EXPOSE 8000

# 6. Запуск uWSGI вместо runserver
# Команда запуска uWSGI, использующая INI-файл
CMD ["uwsgi", "--ini", "mysite_uwsgi.ini"]