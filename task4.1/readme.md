Databases Before all need install database server. My work PC are VirtualBox Ubuntu server 20.04 LTS. I decided use ports for install Database. 
Sequence of actions:
1. Update of ports:

task4.1$ sudo apt update

2. Install of Mysql-server from ports:

$ sudo apt install mysql-server
$ sudo mysql -v
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Reading history-file /root/.mysql_history
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>



3. MySQL this is relation DB. As i understood in MySQL, scheme is synonymous with database. But, as i read in other source, in the Oracle Database product, a scheme represents only a part of a database: the tables and other objects are owned by a single user.
There are some rules for creating tables in DB: 
1. one cell - one value. 
2. each record should has unique identifier (id).
And at last, before create DB, we need to decide on the relationship between the tables (scheme). 
There are three variants:
- one-to-many;
- one-to-one;
- many-to-many;
I decided chose "one-to-one" point.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/6bc50eb3fead23a5ed6b4d5c2a1043e72b706f3b/task4.1/images/scheme_db.jpg" width="300">

So, let's create DBs in MySql:

mysql> CREATE DATABASE DevOpsOnline;
--------------
CREATE DATABASE DevOpsOnline
--------------

Query OK, 1 row affected (0.34 sec)

mysql> show tables;
--------------
show tables
--------------

ERROR 1046 (3D000): No database selected
mysql> USE DevOpsOnline;
Database changed
mysql> show tables;
--------------
show tables
--------------

Empty set (0.00 sec)

mysql>USE DevOpsOnline;
 
mysql>CREATE TABLE customer (id INT AUTO_INCREMENT PRIMARY KEY, postalCode VARCHAR(15) default NULL);
 
mysql>CREATE TABLE product (id INT AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(50) NOT NULL, price VARCHAR(7) NOT NULL, qty VARCHAR(4) NOT NULL);
 
mysql>CREATE TABLE transactions (id INT AUTO_INCREMENT PRIMARY KEY, cust_id INT, timedate TIMESTAMP, FOREIGN KEY(cust_id) REFERENCES customer(id));
 
mysql>CREATE TABLE product_transaction (prod_id INT, trans_id INT, PRIMARY KEY(prod_id, trans_id), FOREIGN KEY(prod_id) REFERENCES product(id), FOREIGN KEY(trans_id) REFERENCES transactions(id));

mysql> show tables;
+------------------------+
| Tables_in_DevOpsOnline |
+------------------------+
| customer               |
| product                |
| product_transaction    |
| transactions           |
+------------------------+
4 rows in set (0.01 sec)

mysql> DESCRIBE customer;
+------------+-------------+------+-----+---------+----------------+
| Field      | Type        | Null | Key | Default | Extra          |
+------------+-------------+------+-----+---------+----------------+
| id         | int         | NO   | PRI | NULL    | auto_increment |
| postalCode | varchar(15) | YES  |     | NULL    |                |
+------------+-------------+------+-----+---------+----------------+
2 rows in set (0.01 sec)

mysql> DESCRIBE product;
+--------------+-------------+------+-----+---------+----------------+
| Field        | Type        | Null | Key | Default | Extra          |
+--------------+-------------+------+-----+---------+----------------+
| id           | int         | NO   | PRI | NULL    | auto_increment |
| product_name | varchar(50) | NO   |     | NULL    |                |
| price        | varchar(7)  | NO   |     | NULL    |                |
| qty          | varchar(4)  | NO   |     | NULL    |                |
+--------------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

mysql> DESCRIBE product_transaction;
+----------+------+------+-----+---------+-------+
| Field    | Type | Null | Key | Default | Extra |
+----------+------+------+-----+---------+-------+
| prod_id  | int  | NO   | PRI | NULL    |       |
| trans_id | int  | NO   | PRI | NULL    |       |
+----------+------+------+-----+---------+-------+
2 rows in set (0.00 sec)

mysql> DESCRIBE transactions;
+----------+-----------+------+-----+---------+----------------+
| Field    | Type      | Null | Key | Default | Extra          |
+----------+-----------+------+-----+---------+----------------+
| id       | int       | NO   | PRI | NULL    | auto_increment |
| cust_id  | int       | YES  | MUL | NULL    |                |
| timedate | timestamp | YES  |     | NULL    |                |
+----------+-----------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

let's fill the tables, and at the end try enter incorrect INSERT for check relationship between tables. 

mysql> show tables;
+------------------------+
| Tables_in_DevOpsOnline |
+------------------------+
| customer               |
| product                |
| product_transaction    |
| transactions           |
+------------------------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM customer;
+----+------------+
| id | postalCode |
+----+------------+
|  1 | 14000      |
|  2 | 14001      |
|  3 | 14002      |
|  4 | 14003      |
+----+------------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM product;
+----+--------------+--------+------+
| id | product_name | price  | qty  |
+----+--------------+--------+------+
|  1 | milk         | 27UAH  | 27L  |
|  2 | meat         | 100UAH | 7kg  |
|  3 | bread        | 19UAH  | 7    |
|  4 | sausages     | 80UAH  | 12kg |
|  5 | meat_pig     | 100UAH | 7kg  |
+----+--------------+--------+------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM transactions;
+----+---------+---------------------+
| id | cust_id | timedate            |
+----+---------+---------------------+
|  1 |       2 | 2021-11-24 12:27:34 |
|  2 |       3 | 2021-11-24 12:37:34 |
|  3 |       4 | 2021-11-24 12:38:34 |
|  4 |       1 | 2021-11-24 12:39:34 |
+----+---------+---------------------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM product_transaction;
+---------+----------+
| prod_id | trans_id |
+---------+----------+
|       1 |        1 |
|       2 |        1 |
|       3 |        1 |
|       3 |        2 |
|       4 |        2 |
|       5 |        2 |
+---------+----------+
6 rows in set (0.00 sec)

mysql> INSERT INTO product_transaction (prod_id, trans_id) VALUES (6, 2);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`DevOpsOnline`.`product_transaction`, CONSTRAINT `product_transaction_ibfk_1` FOREIGN KEY (`prod_id`) REFERENCES `product` (`id`))
mysql>


########SELECT##########

mysql> SELECT * FROM product_transaction WHERE trans_id =1;
+---------+----------+
| prod_id | trans_id |
+---------+----------+
|       1 |        1 |
|       2 |        1 |
|       3 |        1 |
+---------+----------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM product;
+----+--------------+--------+------+
| id | product_name | price  | qty  |
+----+--------------+--------+------+
|  1 | milk         | 27UAH  | 27L  |
|  2 | meat         | 100UAH | 7kg  |
|  3 | bread        | 19UAH  | 7    |
|  4 | sausages     | 80UAH  | 12kg |
|  5 | meat_pig     | 100UAH | 7kg  |
+----+--------------+--------+------+
5 rows in set (0.01 sec)

mysql> SELECT product_name FROM product WHERE id =5;
+--------------+
| product_name |
+--------------+
| meat_pig     |
+--------------+
1 row in set (0.00 sec)
mysql> SELECT product_name FROM product WHERE id >2;
+--------------+
| product_name |
+--------------+
| bread        |
| sausages     |
| meat_pig     |
+--------------+
3 rows in set (0.00 sec)

mysql> SELECT id AS 'номер', product_name AS 'Продукт питания' FROM product WHER
E id >2;
+------------+-------------------------------+
| номер      | Продукт питания               |
+------------+-------------------------------+
|          3 | bread                         |
|          4 | sausages                      |
|          5 | meat_pig                      |
+------------+-------------------------------+
3 rows in set (0.00 sec)
mysql> SELECT * FROM product ORDER BY product_name;
+----+--------------+--------+------+
| id | product_name | price  | qty  |
+----+--------------+--------+------+
|  3 | bread        | 19UAH  | 7    |
|  2 | meat         | 100UAH | 7kg  |
|  5 | meat_pig     | 100UAH | 7kg  |
|  1 | milk         | 27UAH  | 27L  |
|  4 | sausages     | 80UAH  | 12kg |
+----+--------------+--------+------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM product WHERE price LIKE "1%" AND qty LIKE "7%";
+----+--------------+--------+-----+
| id | product_name | price  | qty |
+----+--------------+--------+-----+
|  2 | meat         | 100UAH | 7kg |
|  3 | bread        | 19UAH  | 7   |
|  5 | meat_pig     | 100UAH | 7kg |
+----+--------------+--------+-----+
3 rows in set (0.00 sec)
mysql> SELECT * FROM product WHERE price LIKE "1%" OR qty LIKE "%kg";
+----+--------------+--------+------+
| id | product_name | price  | qty  |
+----+--------------+--------+------+
|  2 | meat         | 100UAH | 7kg  |
|  3 | bread        | 19UAH  | 7    |
|  4 | sausages     | 80UAH  | 12kg |
|  5 | meat_pig     | 100UAH | 7kg  |
+----+--------------+--------+------+
4 rows in set (0.00 sec)
mysql> ALTER TABLE product CHANGE age age_days INT;
Query OK, 0 rows affected (0.39 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from product;
+----+--------------+--------+------+----------+
| id | product_name | price  | qty  | age_days |
+----+--------------+--------+------+----------+
|  1 | milk         | 27UAH  | 27L  |       10 |
|  2 | meat         | 100UAH | 7kg  |       20 |
|  3 | bread        | 19UAH  | 7    |       30 |
|  4 | sausages     | 80UAH  | 12kg |       40 |
|  5 | meat_pig     | 100UAH | 7kg  |       50 |
+----+--------------+--------+------+----------+
5 rows in set (0.00 sec)
mysql> SELECT AVG(age_days) FROM product;
+---------------+
| AVG(age_days) |
+---------------+
|       30.0000 |
+---------------+
1 row in set (0.00 sec)
mysql> SELECT MAX(age_days), MIN(age_days) FROM product;
+---------------+---------------+
| MAX(age_days) | MIN(age_days) |
+---------------+---------------+
|            50 |            10 |
+---------------+---------------+
1 row in set (0.00 sec)
mysql> SELECT age_days, COUNT(age_days) FROM product GROUP BY age_days;         +----------+-----------------+
| age_days | COUNT(age_days) |
+----------+-----------------+
|       10 |               1 |
|       20 |               2 |
|       30 |               1 |
|       40 |               1 |
|       50 |               1 |
+----------+-----------------+
5 rows in set (0.00 sec)
