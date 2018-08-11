BEGIN TRANSACTION;
CREATE TABLE "orders" (
	`index`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`address`	TEXT,
	`wif`	TEXT,
	`private_key`	TEXT,
	`paid`	INTEGER,
	`address_salt`	INTEGER,
	`item_index`	INTEGER,
	`item_amount`	INTEGER,
	`btc_address`	TEXT,
	`order_price`	REAL,
	`date`	INTEGER,
	`note`	TEXT
);
CREATE TABLE "items" (
	`name`	TEXT NOT NULL,
	`ind`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`price`	REAL NOT NULL,
	`visible`	INTEGER,
	`description`	TEXT,
	`pcs`	TEXT
);
INSERT INTO `items` VALUES ('Project hat',1,1.0,-1,'Donations are pretty much welcome . 1KsxhDfYbF7Lg47wqeTgcZQgTVS18mzZrd','1,5,10,50,100');
CREATE TABLE `btc` (
	`rate`	REAL
);
INSERT INTO `btc` VALUES (5354.86);
COMMIT;
