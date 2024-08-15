<h2 align="center">One-time note service</h2>

#### Service of one-time secret notes like a onetimesecret.com
#### Write a secret, determine the lifetime of the secret and receive a one-time key. When the secret's lifetime expires or is read, the secret is deleted. All secrets are stored in encrypted form and no one has access to them!


<!-- USAGE EXAMPLES -->
## Usage

Before running the web application, create a database, create and apply migrations, install the necessary packages from the requirements.txt file and populate the .env file with .env.example. To run, use the command "python manage.py runserver". Requests are sent via Postman in JSON format.


## Docker 
Create Docker images and containers using commands: "docker-compose build" and "docker-compose up".


## Project structure

config/

    celery.py - celery file
    settings.py - application settings
    urls.py - routing file

keep_secrets/

    migrations/
        directory with migrations
    admin.py - admin settings
    models.py - application models
    serializers.py - application serializers
    services.py - service functions
    tasks.py = periodic task
    tests.py - application tests
    urls.py - application routing file
    views.py - controllers

.gitignore - Git file.

Dockerfile <br>
docker-compose.yaml - Docker files.

env.example - example of filling environment variables.

manage.py - web application entry point.

requirements.txt - list of requirements for the project.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

kettariec@gmail.com

https://github.com/Kettariec/one_time_secret_drf
