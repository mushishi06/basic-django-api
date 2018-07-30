# basic-django-api
Django app API demo will allow the user call a API and get back a list of active
items.

The items will be customisable by the Django default admin pages.

The API will respond with a list of all currently active items.

## Requirements
1. An API that responds to a `GET` request and returns a list of active items.
2. Django admin page where the items parameters can be customised and new items
can be added.
3. Item attributes must consist of code, name and active.
4. Ensure that duplicate items cannot be added.

### Items:
Code | Name |  Active
------------ | ------------- | -------------
KET | Kettle | true
SPN | Spoon | fale
FRK | Fork | true

## Optional Requirement
We now want to group these items up into the specific categories mentioned below.

Once you have grouped each item into a category, add a `POST` request endpoint.

The API will accept the category name and return a list of items in that category that are active.

### Categories:
Category | Code
------------ | -------------
Appliance | KET
Cutlery | SPN
Cutlery | FRK

* Think about how you want these items to be grouped in the database and an optimum way
of querying for these items.

# Launch:

- Clone this repo.

- Create a [virtual env](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv "Virtual env's Setup docs")

	- Install virtual env `pip install virtualenv`

	- `cd basic-django-api` and `virtualenv basic-django-api`

	- To begin using the virtual environment, it needs to be activated: `source basic-django-api/bin/activate`

- Install the dependency (`pip3 install -r requirements.txt`)

- Once all are setup go to `~/basic-django-api/basic_api/` (`cd` cmd) and run `python manage.py runserver`

# More informations:

### Admin.

Once the server is running you can access to the django admin trougth the url:

`http://127.0.0.1:8000/admin`

The admin access is Username: `admin`, Password: `a1b2c3d4`

This API accept two entries point:

	- `GET` on  `/item` give a list of active items.

	- `POST` on  `/item` create an active item. The minimum required is `{ "name": "spoon", "code": "SPN"}`

	- `GET` on  `/item/{id}` give a the detail of the item.

	- `PUT` on  `/item/{id}` Update the item.

	- `DELETE` on  `/item/{id}` Delete the item.


	- `GET` on  `/category` give a list of categories.

	- `POST` on  `/category` create a category. The minimum required is `{ "name": "appliance"}`

	- `GET` on  `/category/{id}` give a the detail of the category.

	- `PUT` on  `/category/{id}` Update the category.


	- `GET` on  `/category/{name}` give a list of active items for this category.
