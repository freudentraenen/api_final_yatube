<h1>API для проекта Yatube</h1>
<h3>Описание:</h3>
<p>
  API для социальной сети Yatube, предоставляющий возможности получения информации о публикациях, сообществах и комментариях.<br>
  Кроме этого для авторизованных пользователей доступен следующий функционал:
  <ul>
    <li>Создавать, редактировать и удалять собственные публикации и комментарии.</li>
    <li>Подписываться на других пользователей.</li>
    <li>Получать информацию об уже существующих.</li>
  </ul>
  Полный функционал сервиса можно узнать из документации: /redoc/
</p>
<h3>Как запустить проект:</h3>
<p>
  <ol>
    <li>
      Клонировать репозиторий и перейти в него в командной строке:<br>
      <ul>
        <li>git clone git@github.com:freudentraenen/api_final_yatube.git</li>
        <li>cd api_final_yatube</li>
      </ul>
    </li>
    <li>
      Cоздать и активировать виртуальное окружение:<br>
      <ul>
        <li>python -m venv venv</li>
        <li>source venv/scripts/activate</li>
      </ul>
    </li>
    <li>
      Установить зависимости из файла requirements.txt:<br>
      <ul>
        <li>python -m pip install --upgrade pip</li>
        <li>pip install -r requirements.txt</li>
      </ul>
    </li>
    <li>
      Выполнить миграции:<br>
      <ul>
        <li>python manage.py makemigrations</li>
        <li>python manage.py migrate</li>
      </ul>
    </li>
    <li>
      Запустить проект:<br>
      <ul>
        <li>python manage.py runserver</li>
      </ul>
    </li>
  </ol>
</p>
<h3>Примеры запросов к API:</h3>
<p>
  <ul>
    <li>
      Получение всех публикаций. Возможно указать параметры limit и offset:<br>
      path: GET /api/v1/posts/?limit=2&offset=4
    </li>
    <li>
      Получение информации о сообществе:<br>
      path: GET /api/v1/groups/{id}/
    </li>
    <li>
      Добавление комментария:<br>
      path: POST /api/v1/posts/{post_id}/comments/<br>
      body: {<br>
                "text": "string"<br>
            }<br>
    </li>
    <li>
      Удаление собственной публикации:<br>
      path: DELETE /api/v1/posts/{post_id}<br>
    </li>
  </ul>
</p>
