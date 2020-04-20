DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS user_category;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS requests;
DROP TABLE IF EXISTS resources;
DROP TABLE IF EXISTS resource_category;
DROP TABLE IF EXISTS resource_details;
DROP TABLE IF EXISTS transactions;

CREATE TYPE availability AS ENUM('available', 'purchased', 'reserved');

CREATE TABLE user_category (
    ucid SERIAL PRIMARY KEY,
    ucName VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE users (
    uid SERIAL PRIMARY KEY,
    ucid INTEGER NOT NULL,
    ufirstName VARCHAR(50) NOT NULL,
    ulastName VARCHAR(50) NOT NULL,
    udob TIMESTAMP NOT NULL,
    uemail VARCHAR(100) UNIQUE NOT NULL,
    upassword VARCHAR(200) NOT NULL,
    FOREIGN KEY (ucid) REFERENCES user_category(ucid)
);

CREATE TABLE payments (
    pid SERIAL PRIMARY KEY,
	uid INTEGER NOT NULL,
	pNumber INTEGER NOT NULL,
	pType VARCHAR(50) NOT NULL,
	pProvider VARCHAR(50) NOT NULL,
	pExpDate TIMESTAMP NOT NULL,
    FOREIGN KEY (uid) REFERENCES users(uid)
);

CREATE TABLE resource_category (
    rcid SERIAL PRIMARY KEY,
    rcName VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE resources (
    rid SERIAL PRIMARY KEY,
    rName VARCHAR(30) NOT NULL,
    rcId INTEGER NOT NULL,
    FOREIGN KEY (rcId) REFERENCES resource_category(rcid)
);

CREATE TABLE requests (
    reqId SERIAL PRIMARY KEY,
    reqQuantity INTEGER NOT NULL,
    reqPostDate TIMESTAMP NOT NULL,
    reqDispatchDate TIMESTAMP NOT NULL,
    reqLocation VARCHAR(50),
    requestUid INTEGER NOT NULL,
    supplierUid INTEGER,
    rid INTEGER,
    FOREIGN KEY (rid) REFERENCES resources(rid),
    FOREIGN KEY (supplierUid) REFERENCES users(uid),
    FOREIGN KEY (requestUid) REFERENCES users(uid)
);

CREATE TABLE resource_details (
    rid INTEGER PRIMARY KEY,
    rquantity INTEGER DEFAULT 0,
    rlocation VARCHAR(100),
    ravailability availability NOT NULL,
    supplierUid INTEGER,
    rPrice FLOAT(10) NOT NULL,
    FOREIGN KEY (rid) REFERENCES resources(rid),
    FOREIGN KEY (supplierUid) REFERENCES users(uid)
);

CREATE TABLE transactions (
	tid SERIAL PRIMARY KEY,
	tdate TIMESTAMP NOT NULL,
	tquantity INTEGER NOT NULL,
	uid INTEGER NOT NULL,
	supplierUid INTEGER NOT NULL,
	rid INTEGER NOT NULL,
	tamount FLOAT(10) NOT NULL,
    FOREIGN KEY (uid) REFERENCES users(uid),
    FOREIGN KEY (supplierUid) REFERENCES users(uid),
    FOREIGN KEY (rid) REFERENCES resources(rid)
);

