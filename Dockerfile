# какой язык программирования
FROM python:latest

# Копирование всех файлов в нашем проекте во внутрь нашго контейнера
COPY . /code

# Назначить основную папку
WORKDIR /code

# Установка библиотек
RUN pip install -r requirements.txt

# Запуск проекта
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=2323"]

# В терминале docker run name