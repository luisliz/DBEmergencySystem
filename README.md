# DBEmergencySystem
The Database project made by Luis Liz, Yeniel Diaz and Jorge Vega

# Important notes  
UI Can be found in https://github.com/luisliz/DBEmergencyUI

The database is remotely hosted. 

## Automatically run

(cd into the project first ofc...)

#### Windows
`run.bat`

#### Linux/MacOS 
`run.bash` 

##### if you run into problems running in linux look for dos2unix because this script was made in macos. 


## Manually Running the project 
#### Variables in  Linux & Mac (the right choice)💖
`$export FLASK_APP=app`

`$export FLASK_ENV=development`

`$flask run`

#### Variables in Windows 🤢
`set FLASK_APP=app`

`set FLASK_ENV=development`

`flask run`

## Python virtual environment system 
#### Activate
```cd to api folder``` 

```source venv/bin/activate```

#### To deactivate simply run 

```deactivate```

### Some of the operations supported:

1. Register as a system administrator: 
   - Get user by id: http://localhost:5000/users/<int:uid>
   - Get admins http://localhost:5000/users/categories/admin
   - Get users http://localhost:5000/users/categories/user
  
2. Register as a person in need of resources: 
	 - Get user: http://localhost:5000/users/<int:uid>
	 - Get user http://localhost:5000/users/categories/<string:category>
  
3. Register as a person that supplies resources: 
	 - Get user: http://localhost:5000/users/<int:uid>
	 - Get all users http://localhost:5000/users/
  
4. Add a request for a given resource: 
	 - Get request: http://localhost:5000/requests/<int:reqid>
	 - Get all request http://localhost:5000/requests/  
  
5. Announce the availability of a resource: 
   - http://127.0.0.1:5000/resources/available/ 

6. Reserve or purchase a resource. Free resources are reserved. Otherwise, they are purchased 
These are PUT routes
   - Reserve a resource http://127.0.0.1:5000/resources/reserve/<int:rid>/ 
   - Purchase a resource http://127.0.0.1:5000/resources/purchase/<int:rid>/
  
Both these routes must include the form data of the transaction:
  
|Key|Value|Explanation|
|-----|-----|----------|
|tdate|2021-02-15|Year-month-day|
|tquantity|10|Number of items |
|tpayerpid|2|Payer (user) id |
|tsupplierpid|4|Supplier (user) id|
|tamount|0|Amount of money involved in transaction|

To confirm a transaction was created, we use the route for get all transactions:
   - http://127.0.0.1:5000/transaction/
  
7. Browse resources being requested - GET of all resources contained on a specific request (based on request id)
   - Get requests by resource:  http://127.0.0.1:5000/requests/resources/<int:rid>/
  
8. Browse resources available 
   - Get all resources: http://127.0.0.1:5000/resources/ 

9. ~~See detail of resources, including location on a Google Map (Not required, Extra credit)~~

10. Keyword search resources being requested, with sorting by resource name 
    - http://127.0.0.1:5000/resources/requested/search/baby_foods 

11. Keyword search resources available, with sorting by resource name
    - http://127.0.0.1:5000/resources/available/search/heavy_equipments

12. Statistics:
    - http://127.0.0.1:5000/resources/statistics

**POSTS (form-data in postman)** 

Post Person: 
http://127.0.0.1:5000/users/

Postman must Include the form data of the request:

|Key|Value|Explanation|
|---|---|---|
|ucid|1|User rank: 1 for user; 2 for supplier; 3 for admin|
|ufirstname|Pancho|Name of the user|
|ulastname|Rivera|Last name of the user|
|udob|2020-01-14|year-month-day - Date of birth|
|uemail|pancho.rivera@gmail.com|A valid email. If not exists an error will be produced|
|upassword|panchitomaster123|Any string for password|



Post Request: 
http://127.0.0.1:5000/requests/

Postman must Include the form data of the request:

|Key|Value|Explanation|
|---|---|---|
|reqpostdate|2021-02-15|Year-month-day|
|reqlocation|Ponce|Location for the request|
|requestuid|3|Id of the user making the request|
|supplieruid|null|Id of supplier, initially null|



Post Resources: 
http://127.0.0.1:5000/resources/add

Postman must Include the form data of the resources. The first six items (rname, rquantity, rlocation, ravailability, supplieruid, rprice) are standard and must be included for all resources. The rest of the items depend on the category of the resource being added, refer to the ER diagram to see which fields must be included:

|Key|Value|Explanation|
|---|---|---|
|rname|medications|Name of the resource (which actually matches the resource category name)|
|rquantity|1|Amount of items for this resource to add|
|rlocation|Guayama|Location of the resource|
|ravailability|available|Availability status of the resource|
|supplieruid|3|User id of the supplier|
|rprice|4.00|Price of the resource|
|mmanufacturer|Bayer|Medication manufacturer|
|msize|1 pill box|String describing the size of the medication container|
|mname|heart pills|Name of the medication|



