<h2 align="center">Сервис одноразовых записок</h2>

Cервис одноразовых секретных записок наподобие onetimesecret.com


<!-- USAGE EXAMPLES -->
## Usage

Перед запуском web-приложения создайте базу данных, создайте и примените миграции, установите необходимые пакеты из файла requirements.txt и заполните файл .env по образцу .env.example. Для запуска используйте команду "python manage.py runserver" либо через конфигурационные настройки PyCharm.


### Docker 
Создать образы и контейнеры DOCKER с помощью команд: "docker-compose build" и "docker-compose up".


## Структура проекта

config/

    settings.py - настройки приложений
    urls.py - файл маршрутизации

keep_secrets/

    migrations/
        папка с миграциями
    admin.py - настройки админки
    models.py - модели приложения
    serializers.py - сериализаторsы
    services.py - сервисные функции
    tests.py - тесты
    urls.py - файл маршрутизации приложения
    views.py - контроллеры

manage.py - точка входа веб-приложения

requirements.txt - список зависимостей для проекта.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

kettariec@gmail.com

https://github.com/Kettariec/one_time_secret

<p align="right">(<a href="#readme-top">back to top</a>)</p>