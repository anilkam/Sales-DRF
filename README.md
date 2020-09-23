# DRF-Cart-App

A simple sales web application using ​Django Rest Framework​ + SQLite3

Prerequisites
-------------------------

Python 3.6+

pipenv

Setup
-------------------------

Clone/Download project repository

Install Packages from `Pipfile`:

    $ pipenv install

Run
-------------------------

Activate the Pipenv shell:

    $ pipenv shell

Run server:

    $ python manage.py runserver


API Endpoints
-------------------------

### User related
* List Users with Contents of their Carts: `GET /users/`
* Add New User : `POST /users/`
```
{
    "username": "[1 to 150 char. Letters, digits and @/./+/-/_ only.]",
    "first_name": "[0 to 150 chars]",
    "last_name": "[0 to 150 chars]"
}
```
* Delete User: `DELETE /users/{user_id}/`

### Product related
* List Products: `GET /products/`
* Add Product: `POST /products/`
```
{
    "name": "[1 to 100 chars]",
    "description": "[0 to 300 chars]",
    "price": [positive float]
}
```
* Retrieve Product Details: `GET /products/{product_id}`
* Delete Product: `DELETE /products/{product_id}/`

### Cart related
* Add Product to Customer's Cart : `POST /carts/`
```
{
    "user": [user_id],
    "product": [product_id],
    "quantity": [integer between 0 and 100]
}
```
* Delete Product from Customer's Cart: `DELETE /carts/{cart_id}/`