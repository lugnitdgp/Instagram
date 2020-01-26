# Instagram

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)<br>

A social blog app for posting and commenting pics.



##  Starting the Project


1. Create a **virtual environment** with venv (install virtualenv, if its not installed).

    ```
    venv instagram

    ```

2. Clone the project in the virtual environment directory.

    ```
    cd Instagam
    git clone https://github.com/lugnitdgp/Instagram.git

    ```

3. Activate the virtual environemnt.

    #### For Linux/Mac OSX   
    ```
    source bin/activate

    ```

    #### For Windows
    ```
    .\Scripts\activate

    ```

4. Install the requirements.

    ```
    cd instagram
    pip install -r requirements.txt

    ```


5. Run the Migrations
    ```
    python manage.py makemigrations

    python manage.py migrate

    ```
6. Run the development server
    ```
    python manage.py runserver

    ```
7. Head to server http://127.0.0.1:8000

8. Add Posts, Comments

## For contributors

Instagram uses the following technologies:

+ HTML/CSS/JavaScript
+ Pyhton(Django)

If you want to contribute to this project, then have a look [here](https://github.com/lugnitdgp/Instagram/blob/master/CONTRIBUTING.md)
