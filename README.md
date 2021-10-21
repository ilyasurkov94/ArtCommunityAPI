# Api_Final_Yatube

---

### Описание

---

Проект предназначен для создания пользователями постов, содержаших тест и изображения. Посты можно отнести к различным группам.
Есть возможность писать комментарии к постам, а так же оформлять подписки на авторов. 

---

### Технологии

---

Для API в проекте созданы сериализаторы и вью сеты для каждой модели:

Model       Serializer          ModelViewSet
---
Post    -  PostSerializer    -  PostViewSet
Group   -  GroupSerializer   -  GroupViewSet
Comment -  CommentSerializer -  CommentViewSet
Follow  -  FollowSerializer  -  FollowViewSet

---

### Установка

---

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ilyasurkov94/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

---

### Примеры работы API
---

GET-запрос на /api/v1/posts/

    Форма:
limit - integer (Количество публикаций на страницу)
offset - integer (Номер страницы после которой начинать выдачу)

    Ответ:
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}

---

POST-запрос на /api/v1/posts/

   Форма:
text(required) - string (текст публикации)
image - string or null <binary>
group - integer or null (id сообщества)

    Ответ:
{
"text": "string",
"image": "string",
"group": 0
}

---

PUT-запрос на /api/v1/posts/{id}/

    PATH PARAMETERS:
id (required) - integer (id публикации)

    REQUEST BODY SCHEMA: 
text (required) - string (текст публикации)
image -	string or null <binary>
group - integer or null (id сообщества)

---

С полным списком можно ознакомить по ссылке http://127.0.0.1:8000/redoc/