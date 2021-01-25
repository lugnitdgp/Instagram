# Instagram

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)<br>

A social blog app for posting and commenting pics.

## Starting the Project

1. Create a new directory

    ```shell
    mkdir Instagram
    cd Instagram
    ```

2. Create a **virtual environment** with venv (install virtualenv, if its not installed).

   ```shell
    sudo apt-get install python3-venv
    python3 -m venv env

    ```

3. Clone the project in the virtual environment directory.

    ```shell
    git clone https://github.com/lugnitdgp/Instagram.git

    ```

4. Activate the virtual environemnt.

    ### For Linux/Mac OSX

    ```shell
    source env/bin/activate

    ```

    ### For Windows

    ```shell
    .\Scripts\activate

    ```

5. Install the requirements.

    ```shell
    cd Instagram
    pip install -r requirements.txt

    ```


6. Run the Migrations
    ```
    python manage.py makemigrations

    python manage.py migrate

    ```
7. Run the development server
    ```
    python manage.py runserver

    ```
8. Head to server http://127.0.0.1:8000

9. Add Posts, Comments

## For contributors

Instagram uses the following technologies:

+ HTML/CSS/JavaScript
+ Python(Django)

If you want to contribute to this project, then have a look [here](https://github.com/lugnitdgp/Instagram/blob/master/CONTRIBUTING.md)
