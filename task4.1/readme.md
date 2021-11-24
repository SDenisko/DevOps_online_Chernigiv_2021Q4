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

<img src="" width="300">

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



