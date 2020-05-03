DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS user_category;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS requests;
DROP TABLE IF EXISTS resources;
DROP TABLE IF EXISTS resource_category;
DROP TABLE IF EXISTS resource_details;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS medications;
DROP TABLE IF EXISTS canned_foods;
DROP TABLE IF EXISTS baby_foods;
DROP TABLE IF EXISTS waters;
DROP TABLE IF EXISTS dry_foods;
DROP TABLE IF EXISTS fuels;
DROP TABLE IF EXISTS heavy_equipments;
DROP TABLE IF EXISTS power_generators;
DROP TABLE IF EXISTS NCES medical_devices;
DROP TABLE IF EXISTS batteries;
DROP TABLE IF EXISTS tools;
DROP TABLE IF EXISTS ices;
DROP TABLE IF EXISTS waters;

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
	tpayerpid INTEGER NOT NULL,
	tsupplierpid INTEGER NOT NULL,
	rid INTEGER NOT NULL,
	tamount FLOAT(10) NOT NULL,
    FOREIGN KEY (tpayerpid) REFERENCES payments(pid),
    FOREIGN KEY (tsupplierpid) REFERENCES payments(pid),
    FOREIGN KEY (rid) REFERENCES resources(rid)
);

-------------------------------------------------------------------------
----------------------------RESOURCES TABLES-----------------------------
-------------------------------------------------------------------------

CREATE TABLE medications (
    mid SERIAL PRIMARY KEY,
    mmanufacturer VARCHAR(50) NOT NULL,
    msize VARCHAR(50) NOT NULL,
 );

CREATE TABLE canned_foods (
    canid SERIAL PRIMARY KEY,
    canbrand VARCHAR(50) NOT NULL,
    cantype VARCHAR(50) NOT NULL,
 );

CREATE TABLE baby_foods (
    bid SERIAL PRIMARY KEY,
    bflavor VARCHAR(50) NOT NULL,
    bbrand VARCHAR(50) NOT NULL,
);

CREATE TABLE waters (
    wid SERIAL PRIMARY KEY,
    wcontainertype VARCHAR(50) NOT NULL,
    wcontainersize VARCHAR(50) NOT NULL,
);

CREATE TABLE dry_foods (
    dryid SERIAL PRIMARY KEY,
    drybrand VARCHAR(50) NOT NULL,
    drytype VARCHAR(50) NOT NULL,

);

CREATE TABLE fuels (
    fid SERIAL PRIMARY KEY,
    fbrand VARCHAR(50) NOT NULL,
    ftype VARCHAR(50) NOT NULL,
    fvolume VARCHAR(50) NOT NULL,
);

CREATE TABLE heavy_equipments (
    hid SERIAL PRIMARY KEY,
    hbrand VARCHAR(50) NOT NULL,
    htype VARCHAR(50) NOT NULL,
);

CREATE TABLE clothings (
    clothid SERIAL PRIMARY KEY,
    clothbranch VARCHAR(50) NOT NULL,
    clothmaterial VARCHAR(50) NOT NULL,
    clothtype VARCHAR(50) NOT NULL,
);

CREATE TABLE power_generators (
    genid SERIAL PRIMARY KEY,
    genbrand VARCHAR(50) NOT NULL,
    gentype VARCHAR(50) NOT NULL,
    genpower VARCHAR(50) NOT NULL,
);

CREATE TABLE medical_devices (
    meddevid SERIAL PRIMARY KEY,
    meddevbrand VARCHAR(50) NOT NULL,
    meddevtype VARCHAR(50) NOT NULL,
);

CREATE TABLE batteries (
    batid SERIAL PRIMARY KEY,
    battype VARCHAR(50) NOT NULL,
    batsize VARCHAR(50) NOT NULL,
);

CREATE TABLE tools (
    toolid SERIAL PRIMARY KEY,
    toolbrand VARCHAR(50) NOT NULL,
    tooltype VARCHAR(50) NOT NULL,
    toolsize VARCHAR(50) NOT NULL,
);

CREATE TABLE ices (
    iid SERIAL PRIMARY KEY,
    ibrand VARCHAR(50) NOT NULL,
    ibagsize VARCHAR(50) NOT NULL,
    iweight VARCHAR(50) NOT NULL,
);


CREATE TABLE resources (
    rid SERIAL PRIMARY KEY,
    mid INTEGER,
    canid INTEGER,
    bid INTEGER,
    did INTEGER,
    fid INTEGER,
    hid INTEGER,
    clothid INTEGER,
    genid INTEGER,
    meddevid INTEGER,
    batid INTEGER,
    toolid INTEGER,
    iid INTEGER,
    wid INTEGER,
    FOREIGN KEY (mid) REFERENCES medications(mid),
    FOREIGN KEY (canid) REFERENCES canned_foods(canid),
    FOREIGN KEY (bid) REFERENCES baby_foods(bid),
    FOREIGN KEY (did) REFERENCES waters(did),
    FOREIGN KEY (fid) REFERENCES dry_foods(fid),
    FOREIGN KEY (hid) REFERENCES fuels(hid),
    FOREIGN KEY (clothid) REFERENCES heavy_equipments(clothid),
    FOREIGN KEY (genid) REFERENCES power_generators(genid),
    FOREIGN KEY (meddevid) REFERENCES medical_devices(meddevid),
    FOREIGN KEY (batid) REFERENCES batteries(batid),
    FOREIGN KEY (toolid) REFERENCES tools(toolid),
    FOREIGN KEY (iid) REFERENCES ices(iid),
    FOREIGN KEY (wid) REFERENCES waters(wid),
);

