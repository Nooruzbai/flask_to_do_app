A simple TODO application for demonstration.

Technologies utilized in the application:

Python3 --version 3.12
Flask
Flask-login
Flask-wtforms
SQLAalchemy
Postgresql
Bootstrap
In order to install and launch the application, please follow the steps below:

If you do not have git, please install it.

Clone the repository from the GitHub using this command: git clone https://github.com/Nooruzbai/flask_to_do_app.git

After cloning the repository, please go to cloned folder and execute the commands in Linux or Windows command line bellow:

Create virtual environment:
python3 -m venv venv.

Activate the virtual environment:
for Linux: source venv/bin/activate
for Windows: python3 venv\Scripts\activate

Install the dependencies:
pip install -r requirements.txt

In the main directory "flask_to_do_app" create a ".env" file.

Fill the ".env" file with data:

SECRET_KEY=create a secret key
POSTGRES_HOST=localhost
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
UPLOAD_PATH=source/static/uploads

In the main directory "flask_to_do_app" create a ".flaskenv" file.

Fill the file with folowing data:
FLASK_APP=source:create_app
FLASK_ENV=development
FLASK_DEBUG=1(In development mode, if not put FALSE)

Run: flask db migrate
Run: flask run

Please register and login with right credentials.

If you have encountered any issues, please write me to "nooruzbay@gmail.com".