DROP TABLE IF EXISTS resources
DROP TABLE IF EXISTS resource_details
DROP TABLE IF EXISTS users
DROP TABLE IF EXISTS disasters
DROP TABLE IF EXISTS requests

CREATE TABLE resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id
    quantity INTEGER DEFAULT 0,
    availability ENUM('available', 'purchased', 'reserved') NOT NULL
);

CREATE TABLE resource_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resource_id  -- FK
    quantity INTEGER DEFAULT 0,
    location VARCHAR(100),
    supplier_id --FK
);

CREATE TABLE resource_category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_rank
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password 
);

CREATE TABLE user_category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE payment (
	user_id PRIMARY KEY AUTOINCREMENT --FK  
	credit_card_number INTEGER(50) NOT NULL, 
	card_provider NOT NULL
	card_type NOT NULL
	exp_date NOT NULL 
); 

CREATE TABLE transactions (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	payment_date 
	payment_amount DECIMAL(18,2) 
	resources_ids INTEGER[] --List of resource ids 
); 
-- CREATE TABLE disasters (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     disaster_type ---Earthquake, hurricane twunami tornado
--     city VARCHAR(50)
--     country
-- );

CREATE TABLE requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    requester_id --FK,
    supplier_id -- FK,
    resource_id -- FK,
    quantity INTEGER NOT NULL,
    request_date     NOT NULL,
    dispatch_date    DEFAULT NULL,
    location         NOT NULL,
);

