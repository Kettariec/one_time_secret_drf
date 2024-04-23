<h2 align="center">One-time note service</h2>

Service of one-time secret notes like a onetimesecret.com


<!-- USAGE EXAMPLES -->
## Usage

Before running the web application, create a database, create and apply migrations, install the necessary packages from the requirements.txt file and populate the .env file with .env.example. To run, use the command "python manage.py runserver".


### Docker 
Create Docker images and containers using commands: "docker-compose build" and "docker-compose up".


## Project structure

config/

    settings.py - application settings
    urls.py - routing file

keep_secrets/

    migrations/
        directory with migrations
    admin.py - admin settings
    models.py - application models
    serializers.py - application serializers
    services.py - service functions
    tests.py - application tests
    urls.py - application routing file
    views.py - controllers

manage.py - web application entry point.

requirements.txt - list of requirements for the project.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

kettariec@gmail.com

https://github.com/Kettariec/one_time_secret

<p align="right">(<a href="#readme-top">back to top</a>)</p>