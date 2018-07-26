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
