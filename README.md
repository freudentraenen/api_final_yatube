# API для проекта Yatube

### Описание:
API для социальной сети Yatube, предоставляющий возможности получения информации о публикациях, сообществах и комментариях.
Кроме этого для авторизованных пользователей доступен следующий функционал:
* Создавать, редактировать и удалять собственные публикации и комментарии.
* Подписываться на других пользователей.
* Получать информацию об уже существующих.
Полный функционал сервиса можно узнать из документации: /redoc/

### Как запустить проект:


1. Клонировать репозиторий и перейти в него в командной строке:

    ```
    git clone git@github.com:freudentraenen/api_final_yatube.git`
    ```

    ```
    cd api_final_yatube`
    ```

2. Cоздать и активировать виртуальное окружение:

    ```
    python -m venv venv
    ```

    ```
    source venv/scripts/activate
    ```

3. Установить зависимости из файла requirements.txt:

    ```
    python -m pip install --upgrade pip
    ```

    ```
    pip install -r requirements.txt
    ```

4. Выполнить миграции:

    ```
    python manage.py makemigrations
    ```

    ```
    python manage.py migrate
    ```

5. Запустить проект:

    ```
    python manage.py runserver
    ```

### Примеры запросов к API:

* Получение всех публикаций. Возможно указать параметры limit и offset:

  Запрос:
  
  ```
  GET /api/v1/posts/?limit=100&offset=300
  ```

  Ответ:

  ```
  {
      "count": 123,
      "next": "http://api.example.org/accounts/?offset=400&limit=100",
      "previous": "http://api.example.org/accounts/?offset=200&limit=100",
      "results": [
          {
              "id": 0,
              "author": "testuser",
              "text": "test text",
              "pub_date": "2019-08-24T14:15:22Z",
              "image": "string",
              "group": 0
          }
      ]
  }
  ```

* Получение информации о сообществе:

  Запрос:
  
  ```
  GET /api/v1/groups/{id}/
  ```
  
  Ответ:
  
  ```
  {
    "id": 0,
    "title": "test title",
    "slug": "test-slug",
    "description": "test description"
  }
  ```

* Добавление комментария:

  Запрос:
  
  ```
  POST /api/v1/posts/{post_id}/comments/
  ```
  
  ```
  {
    "text": "string"
  }
  ```
  
  Ответ:
  
  ```
  {
    "id": 0,
    "author": "testuser",
    "text": "test text",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
  ```

* Удаление собственной публикации:

  Запрос:
  
  ```
  DELETE /api/v1/posts/{post_id}
  ```
  
  Ответ:
  
  ```
  ```
