DROP TABLE IF EXISTS resources
DROP TABLE IF EXISTS resource_details
DROP TABLE IF EXISTS users
DROP TABLE IF EXISTS disasters
DROP TABLE IF EXISTS requests

CREATE TABLE resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id
    quantity INTEGER DEFAULT 0,
    availability ENUM('purchase', 'reserve') NOT NULL
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
    user_category_id
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dob TIMESTAMP NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password 
);

CREATE TABLE user_category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE disasters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    disaster_type ---Earthquake, hurricane twunami tornado
    city VARCHAR(50)
    country
);

CREATE TABLE requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    requester_id --FK,
    supplier_id -- FK,
    resource_id -- FK,
    quantity         ,
    request_date     ,
    dispatch_date    ,
    location         ,
);

