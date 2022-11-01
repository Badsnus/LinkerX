LinkerX
---

### Про проект:

Rest api проект для получения ссылок нужной длинны (от 5 до 1000 символов), то
есть может работать и как "сократитель" ссылок, так и их "удлинитель".
Также по всем ссылкам можно смотреть статистику переходов по ним (ip,
user-agent, время перехода)

Проект написан на python + django 3.2 + django rest framework

Методы API
---

## Auth

### POST api/v1/auth/users/

Создание пользователя

Параметры:

email, username, password - strings

### POST api/v1/auth/token/login/

Получение токена

Параметры:

username, password - strings

### POST api/v1/auth/token/logout/

Деактивация токена

## Links

## Запросы нужно отправлять

Authorization Token {TOKEN}

### POST api/v1/links/

Создание ссылки

Параметры:

length_url - Длина новой ссылки, целое число от 5 до 1000

long_url - ссылка для редиректа

### GET api/v1/links/{id}/

Получение информации о ссылке


Инструкция по установке
---

#### 1)Клонируем репозиторий

    git clone https://github.com/Badsnus/LinkerX

#### 2)Создаем виртуальное окружение и активируем его

    python -m venv venv

    Windows: venv\Scripts\activate.bat
    Linux и MacOS: source venv/bin/activate

#### 3)Заходим в директорию репозитория

    cd LinkerX

#### 4) Устанавливаем зависимости

    pip install -r requirements.txt

#### 5)Заходим в директорию джанго проекта

    cd LinkerX

#### 6) .env.example -> .env

    Eсть файл .env.example его нужно переименовать в .env

#### 7) Start

    python manage.py runserver



