<h1>Alpha</h1>
<h2>О проекте</h2>

<p>Этот учебный проект, сделан в процессе обучения Django.
Все требуемые пакеты находиться в файле requirements.txt.</p>
<p>Если вы загрузили проект в компютер, вам понадобиться создать в корневой директории одну папку со имением - env </p>
<p>После создание директории создайте 4 файла</p>

Первый файл __.backend__

<p>Содержание на примере:</p>

```commandline
SECRET_KEY= #здесь секретный ключ   Django
DEBUG=True
SHOW_DOCS=True

ALLOWED_HOSTS=*

POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER= # имя пользователя 
POSTGRES_PASSWORD= # пароль от БД
POSTGRES_DB= # имя БД

REDIS_CELERY_URL=redis://redis:6379/2

GUNICORN_WORKERS=2

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = # здесь ваш почта в формате str
EMAIL_HOST_PASSWORD = # здесь ваш api ключ
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```
 
Воторй файл  __.db__
<p>Содержание на примере:</p>

```commandline
POSTGRES_USER= # имя пользователя 
POSTGRES_PASSWORD= # пароль от БД
POSTGRES_DB= # имя БД
```
 
Третии файл  __.worker__
<p>Содержание на примере:</p>

```commandline
GUNICORN_WORKERS=2
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER= # имя пользователя 
POSTGRES_PASSWORD= # пароль от БД
POSTGRES_DB= # имя БД

REDIS_CELERY_URL=redis://redis:6379/2

MEDIA_ROOT=/media
STATIC_ROOT=/static
```

Четвертый файл  __.redis__

```commandline
# файл может быть путой
```
### Запуск Docker
<p>Вы можете запускать проект через Docker следующим командам:</p>

```
docker-compose --build -d # запуск контейнеры в фоновом режиме
```

<p>Проект работает через REST API, благодаря SWAGGER вы можете познакомиться со всеми API локально через ссылку: </p>

```
http://127.0.0.1:8000/swagger/
```

### Файловая структура

<p>Все файлы проекта находится в директории app</p>
<a href="https://github.com/Kaisar283/Alpha/tree/Dj_RS/app/Alpha">Alpha</a><span> - Главый файл</span><br>
<a href="https://github.com/Kaisar283/Alpha/tree/Dj_RS/app/accounts">accounts</a><span> - Приложение о пользователей</span><br>
<a href="https://github.com/Kaisar283/Alpha/tree/Dj_RS/app/product">products</a><span> - Приложение о продуктах</span><br>
<a href="https://github.com/Kaisar283/Alpha/tree/Dj_RS/app/utils">utils</a><span> - Приложение хранить все статичные данные</span><br>
<a href="https://github.com/Kaisar283/Alpha/tree/Dj_RS/app/docker">docker</a><span> -Содержит все Docker файлы</span><br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
