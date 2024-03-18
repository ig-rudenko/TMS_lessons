FROM python:3.10.13-alpine

# Создаем папку и переходим в неё.
WORKDIR /app

# Копируем `requirements.txt` в текущую папку.
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade --no-cache-dir pip && pip install --no-cache-dir -r requirements.txt;

COPY avatar.py .

CMD ["uvicorn", "avatar:app", "--host", "0.0.0.0"]