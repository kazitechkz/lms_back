# Learning Management Service Backend

Learning Management Service Backend — это серверная часть для управления процессом обучения, разработанная на **FastAPI**. Приложение предоставляет REST API для работы с пользователями, ролями, организациями и курсами.

---

## Установка и настройка

### 1. Клонирование репозитория

```bash
git clone https://github.com/kazitechkz/lms_back.git
cd lms_back
```
### 2. Создание виртуального окружения

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения
Создайте файл .env в корневой директории и заполните его следующими параметрами:
```bash
APP_NAME=
APP_DESCRIPTION=
APP_VERSION=
APP_DEBUG=
APP_DOCS_URL=
APP_REDOC_URL=

DB_TYPE=
DB_CONNECTION=
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=

DB_POOL_SIZE=
DB_MAX_OVERFLOW=
DB_POOL_TIMEOUT=
DB_POOL_RECYCLE=

SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
REFRESH_TOKEN_EXPIRE_DAYS=
APP_STATUS=
```
### 5. Применение миграций базы данных
```bash
alembic upgrade head
```

### 6. Запуск сервера разработки
```bash
uvicorn app.main:app --reload
```

## Основные зависимости
```bash
fastapi==0.115.6 — веб-фреймворк для создания REST API
uvicorn==0.33.0 — сервер ASGI для запуска FastAPI
SQLAlchemy==2.0.36 — ORM для работы с базой данных
aiomysql==0.2.0 — асинхронный драйвер MySQL
pydantic==2.10.3 — валидация и работа с данными
alembic==1.14.0 — миграции базы данных
python-dotenv==1.0.1 — работа с переменными окружения
black==24.10.0 — автоматическое форматирование кода
isort==5.13.2 — упорядочение импортов
```
## Команды для разработки

### 1. Форматирование кода:
```bash
black .
```
### 2. Упорядочивание импортов:
```bash
isort .
```

### 3. Создание новой миграции:
```bash
alembic revision --autogenerate -m "Описание миграции"
```
### 4. Применение миграций:
```bash
alembic upgrade head
```

## Структура проекта
```bash
app/
├── adapters/          # API маршруты и DTO
├── core/              # Основные утилиты и базовые классы
├── entities/          # SQLAlchemy модели
├── infrastructure/    # Настройка базы данных и конфигураций
├── seeders/           # Сидеры для начальных данных
├── use_cases/         # Бизнес-логика (use cases)
├── main.py            # Точка входа
alembic/               # Миграции базы данных
.env                   # Переменные окружения
requirements.txt       # Зависимости
```

# Текущая стадия:
```bash
Разработка....
```