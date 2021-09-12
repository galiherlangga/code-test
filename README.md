# code-test
Backend web test with django based registration form

# Installation
1. First create python environment
    ```
    $ python3 -m venv env
    ```
2. Update and activate env
    ```
    $ python3 -m pip install --upgrade pip

    # For Linux User
    $ source ./env/bin/activate 

    # For Windows User
    $ ./env/Script/activate
    ```
3. Install required packages
    ```
    $ python3 -r req.txt
    ```
4. Copy the file ./project/project/config-sample.ini and rename it to config.ini
5. Database migration
    ```
    $ python3 manage.py makemigrations
    $ python3 manage.py migrate
    ```
6. Run the program
    ```
    $ python3 manage.py runserver
    ```