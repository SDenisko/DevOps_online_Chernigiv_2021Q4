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


mysql> USE DevOpsOnline;

Database changed

mysql> show tables;

-------------
show tables
--------------

Empty set (0.00 sec)

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


mysql> DESCRIBE customer;

+------------+-------------+------+-----+---------+----------------+

| Field      | Type        | Null | Key | Default | Extra          |

+------------+-------------+------+-----+---------+----------------+

| id         | int         | NO   | PRI | NULL    | auto_increment |

| postalCode | varchar(15) | YES  |     | NULL    |                |

+------------+-------------+------+-----+---------+----------------+



mysql> DESCRIBE product;

+--------------+-------------+------+-----+---------+----------------+

| Field        | Type        | Null | Key | Default | Extra          |

+--------------+-------------+------+-----+---------+----------------+

| id           | int         | NO   | PRI | NULL    | auto_increment |

| product_name | varchar(50) | NO   |     | NULL    |                |

| price        | varchar(7)  | NO   |     | NULL    |                |

| qty          | varchar(4)  | NO   |     | NULL    |                |

+--------------+-------------+------+-----+---------+----------------+



mysql> DESCRIBE product_transaction;

+----------+------+------+-----+---------+-------+

| Field    | Type | Null | Key | Default | Extra |

+----------+------+------+-----+---------+-------+

| prod_id  | int  | NO   | PRI | NULL    |       |

| trans_id | int  | NO   | PRI | NULL    |       |

+----------+------+------+-----+---------+-------+




mysql> DESCRIBE transactions;

+----------+-----------+------+-----+---------+----------------+

| Field    | Type      | Null | Key | Default | Extra          |

+----------+-----------+------+-----+---------+----------------+

| id       | int       | NO   | PRI | NULL    | auto_increment |

| cust_id  | int       | YES  | MUL | NULL    |                |

| timedate | timestamp | YES  |     | NULL    |                |

+----------+-----------+------+-----+---------+----------------+



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


mysql> SELECT * FROM customer;

+----+------------+

| id | postalCode |

+----+------------+

|  1 | 14000      |

|  2 | 14001      |

|  3 | 14002      |

|  4 | 14003      |

+----+------------+


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


mysql> SELECT * FROM transactions;

+----+---------+---------------------+

| id | cust_id | timedate            |

+----+---------+---------------------+

|  1 |       2 | 2021-11-24 12:27:34 |

|  2 |       3 | 2021-11-24 12:37:34 |

|  3 |       4 | 2021-11-24 12:38:34 |

|  4 |       1 | 2021-11-24 12:39:34 |

+----+---------+---------------------+


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


 ################ incorrect INSERT ##############

mysql> INSERT INTO product_transaction (prod_id, trans_id) VALUES (6, 2);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`DevOpsOnline`.`product_transaction`, CONSTRAINT `product_transaction_ibfk_1` FOREIGN KEY (`prod_id`) REFERENCES `product` (`id`))




mysql> SELECT * FROM product_transaction WHERE trans_id =1;

+---------+----------+

| prod_id | trans_id |

+---------+----------+

|       1 |        1 |

|       2 |        1 |

|       3 |        1 |

+---------+----------+


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


mysql> SELECT product_name FROM product WHERE id =5;

+--------------+

| product_name |

+--------------+

| meat_pig     |

+--------------+


mysql> SELECT product_name FROM product WHERE id >2;

+--------------+

| product_name |

+--------------+

| bread        |

| sausages     |

| meat_pig     |

+--------------+


mysql> SELECT id AS 'номер', product_name AS 'Продукт питания' FROM product WHERE id >2;


+------------+-------------------------------+

| номер      | Продукт питания               |

+------------+-------------------------------+

|          3 | bread                         |

|          4 | sausages                      |

|          5 | meat_pig                      |

+------------+-------------------------------+


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


mysql> SELECT * FROM product WHERE price LIKE "1%" AND qty LIKE "7%";

+----+--------------+--------+-----+

| id | product_name | price  | qty |

+----+--------------+--------+-----+

|  2 | meat         | 100UAH | 7kg |

|  3 | bread        | 19UAH  | 7   |

|  5 | meat_pig     | 100UAH | 7kg |

+----+--------------+--------+-----+


mysql> SELECT * FROM product WHERE price LIKE "1%" OR qty LIKE "%kg";

+----+--------------+--------+------+

| id | product_name | price  | qty  |

+----+--------------+--------+------+

|  2 | meat         | 100UAH | 7kg  |

|  3 | bread        | 19UAH  | 7    |

|  4 | sausages     | 80UAH  | 12kg |

|  5 | meat_pig     | 100UAH | 7kg  |

+----+--------------+--------+------+


########### DDL ############33


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



mysql> SELECT AVG(age_days) FROM product;


+---------------+

| AVG(age_days) |

+---------------+

|       30.0000 |

+---------------+


mysql> SELECT MAX(age_days), MIN(age_days) FROM product;


+---------------+---------------+

| MAX(age_days) | MIN(age_days) |

+---------------+---------------+

|            50 |            10 |

+---------------+---------------+


mysql> SELECT age_days, COUNT(age_days) FROM product GROUP BY age_days;        


 +----------+-----------------+

| age_days | COUNT(age_days) |

+----------+-----------------+

|       10 |               1 |

|       20 |               2 |

|       30 |               1 |

|       40 |               1 |

|       50 |               1 |

+----------+-----------------+


####### users and privileges #############


Let's create two users and database for test privileges in MySql:


mysql> Create user 'user1'@'localhost' identified by 'user1';
Query OK, 0 rows affected (0.22 sec)

mysql> create user 'user2'@'localhost' identified by 'user2';
Query OK, 0 rows affected (1.03 sec)


mysql> select user from mysql.user;


+------------------+

| user             |

+------------------+

| debian-sys-maint |

| mysql.infoschema |

| mysql.session    |

| mysql.sys        |

| root             |

| user1            |

| user2            |

+------------------+


mysql> CREATE DATABASE test_priv;
Query OK, 1 row affected (0.06 sec)

mysql> SHOW DATABASES;

+--------------------+

| Database           |

+--------------------+

| DevOpsOnline       |

| information_schema |

| mysql              |

| performance_schema |

| sys                |

| test_priv          |

+--------------------+


Attached "all privileges" to user1:

mysql> Grant all privileges on test_priv.* TO 'user1'@'localhost';
Query OK, 0 rows affected (0.65 sec)

Attached "Create" privileges to user2 for test_priv DB. It can creates tables.


mysql> Grant create on test_priv.* TO 'user2'@'localhost';
Query OK, 0 rows affected (0.30 sec)



Check grants for both users:



mysql> show grants for 'user1'@'localhost';


+--------------------------------------------------------------+

| Grants for user1@localhost                                   |

+--------------------------------------------------------------+

| GRANT USAGE ON *.* TO `user1`@`localhost`                    |

| GRANT ALL PRIVILEGES ON `test_priv`.* TO `user1`@`localhost` |

+--------------------------------------------------------------+



mysql> show grants for 'user2'@'localhost';


+------------------------------------------------------+

| Grants for user2@localhost                           |

+------------------------------------------------------+

| GRANT USAGE ON *.* TO `user2`@`localhost`            |

| GRANT CREATE ON `test_priv`.* TO `user2`@`localhost` |

+------------------------------------------------------+


Let's login with user1 and check privileges of them:


root@devopsonline:/home/mrbit# mysql -u user1 -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.



mysql> use test_priv;
Database changed

mysql> create table table1 (id INT auto_increment PRIMARY KEY, column1 VARCHAR(15));
Query OK, 0 rows affected (0.48 sec)



Repeate the same for USER2:

root@devopsonline:/home/mrbit# mysql -u user2 -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)



mysql> show databases;


+--------------------+

| Database           |

+--------------------+

| information_schema |

| test_priv          |

+--------------------+


mysql> use test_priv;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed


mysql> create table table2 (id INT auto_increment PRIMARY KEY, column1 VARCHAR(15));
Query OK, 0 rows affected (0.54 sec)


mysql> drop table table2;
ERROR 1142 (42000): DROP command denied to user 'user2'@'localhost' for table 'table2'



GRANTS ARE  WORKING!


Let's look to DB mysql:


mysql> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed


mysql> show tables;


+------------------------------------------------------+

| Tables_in_mysql                                      |

+------------------------------------------------------+

| columns_priv                                         |

| component                                            |

| db                                                   |

| default_roles                                        |

| engine_cost                                          |

| func                                                 |

| general_log                                          |

| global_grants                                        |

| gtid_executed                                        |

| help_category                                        |

| help_keyword                                         |

| help_relation                                        |

| help_topic                                           |

| innodb_index_stats                                   |

| innodb_table_stats                                   |

| password_history                                     |

| plugin                                               |

| procs_priv                                           |

| proxies_priv                                         |

| replication_asynchronous_connection_failover         |

| replication_asynchronous_connection_failover_managed |

| replication_group_configuration_version              |

| replication_group_member_actions                     |

| role_edges                                           |

| server_cost                                          |

| servers                                              |

| slave_master_info                                    |

| slave_relay_log_info                                 |

| slave_worker_info                                    |

| slow_log                                             |

| tables_priv                                          |

| time_zone                                            |

| time_zone_leap_second                                |

| time_zone_name                                       |

| time_zone_transition                                 |

| time_zone_transition_type                            |

| user                                                 |

+------------------------------------------------------+



mysql> select * from server_cost;


+------------------------------+------------+---------------------+---------+---------------+

| cost_name                    | cost_value | last_update         | comment | default_value |

+------------------------------+------------+---------------------+---------+---------------+

| disk_temptable_create_cost   |       NULL | 2021-11-23 09:26:08 | NULL    |            20 |

| disk_temptable_row_cost      |       NULL | 2021-11-23 09:26:08 | NULL    |           0.5 |

| key_compare_cost             |       NULL | 2021-11-23 09:26:08 | NULL    |          0.05 |

| memory_temptable_create_cost |       NULL | 2021-11-23 09:26:08 | NULL    |             1 |

| memory_temptable_row_cost    |       NULL | 2021-11-23 09:26:08 | NULL    |           0.1 |

| row_evaluate_cost            |       NULL | 2021-11-23 09:26:08 | NULL    |           0.1 |

+------------------------------+------------+---------------------+---------+---------------+


mysql> select host, user, show_db_priv from user;


+-----------+------------------+--------------+

| host      | user             | show_db_priv |

+-----------+------------------+--------------+

| localhost | debian-sys-maint | Y            |

| localhost | mysql.infoschema | N            |

| localhost | mysql.session    | N            |

| localhost | mysql.sys        | N            |

| localhost | root             | Y            |

| localhost | user1            | N            |

| localhost | user2            | N            |

+-----------+------------------+--------------+


################## PART 2 ####################

There are two wayes for export DB from local host to RDS AWS: use S3 service+RDS service and use RDS service+command line.
I desided use second variant:  
 
Backup of db:

root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# mysqldump -u root DevOpsOnline > task4.1/DevOpsOnline.sql

root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4# mysql -u user1 -p
Enter password:


Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 18
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)


mysql> select * from product_transaction;


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


mysql> delete from product_transaction where prod_id = 1;
Query OK, 1 row affected (0.37 sec)


mysql> select * from product_transaction;


+---------+----------+

| prod_id | trans_id |

+---------+----------+

|       2 |        1 |

|       3 |        1 |

|       3 |        2 |

|       4 |        2 |

|       5 |        2 |

+---------+----------+


Restore of DB:


root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4/task4.1# mysql -u root DevOpsOnline < DevOpsOnline.sql
root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4/task4.1# mysql -u root
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 37
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its affiliates. 
Other names may be trademarks of their respective owners.


mysql> use DevOpsOnline;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed


mysql> select * from product_transaction;


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


Let's export our DB to RDS AWS.

First of oll should create RDS AWS public database and add rule for access from local host:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/dcbda3a3d4e312134ec56a66f50d5ac6d44b8f78/task4.1/images/exportDB1.jpg" width="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/dcbda3a3d4e312134ec56a66f50d5ac6d44b8f78/task4.1/images/exportDB2.JPG" width="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/dcbda3a3d4e312134ec56a66f50d5ac6d44b8f78/task4.1/images/exportDB3.jpg" width="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/dcbda3a3d4e312134ec56a66f50d5ac6d44b8f78/task4.1/images/exportDB4.jpg" width="300">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/676b6f1be4265695dd0ae9d63a11da988638166a/task4.1/images/rules.JPG" width="300">


Try to connect:

mysql -u root -h devopsonlinelocal.cpriyhidtmjl.us-east-2.rds.amazonaws.com -p;
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 27
Server version: 8.0.23 Source distribution

Copyright (c) 2000, 2021, Oracle and/or its affiliates.



mysql> create database DevOpsLocal;
Query OK, 1 row affected (0.26 sec)


mysql> show databases;


+--------------------+

| Database           |

+--------------------+

| DevOpsLocal        |

| information_schema |

| mysql              |

| performance_schema |

| sys                |

+--------------------+



mysql> use DevOpsLocal;
Database changed

mysql> show tables;
Empty set (0.20 sec)

mysql> quit;

Export local DB to RDS AWS MySQL:

>mysql -u root -h devopsonlinelocal.cpriyhidtmjl.us-east-2.rds.amazonaws.com -p DevOpsLocal < DevOpsOnline.sql;
Enter password:

connect and check result:

root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4/task4.1# mysql -u root -h devopsonlinelocal.cpriyhidtmjl.us-east-2.rds.amazonaws.com -p;
Enter password:

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 33
Server version: 8.0.23 Source distribution

Copyright (c) 2000, 2021, Oracle and/or its affiliates.



mysql> use DevOpsLocal;

Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed


mysql> show tables;


+-----------------------+

| Tables_in_DevOpsLocal |

+-----------------------+

| customer              |

| product               |

| product_transaction   |

| transactions          |

+-----------------------+


Let's try SELECT from the tables:

mysql> select * from customer;

+----+------------+

| id | postalCode |

+----+------------+

|  1 | 14000      |

|  2 | 14001      |

|  3 | 14002      |

|  4 | 14003      |

+----+------------+


mysql> select * from product;

+----+--------------+--------+------+----------+

| id | product_name | price  | qty  | age_days |

+----+--------------+--------+------+----------+

|  1 | milk         | 27UAH  | 27L  |       10 |

|  2 | meat         | 100UAH | 7kg  |       20 |

|  3 | bread        | 19UAH  | 7    |       30 |

|  4 | sausages     | 80UAH  | 12kg |       40 |

|  5 | meat_pig     | 100UAH | 7kg  |       50 |

|  6 | meat_cow     | 120UAH | 7kg  |       20 |

+----+--------------+--------+------+----------+


mysql> select * from product where age_days > 20;


+----+--------------+--------+------+----------+

| id | product_name | price  | qty  | age_days |

+----+--------------+--------+------+----------+

|  3 | bread        | 19UAH  | 7    |       30 |

|  4 | sausages     | 80UAH  | 12kg |       40 |

|  5 | meat_pig     | 100UAH | 7kg  |       50 |

+----+--------------+--------+------+----------+


ALL DONE!


Now let's try create the dump file of the RDS DB to the local host: 

mysql> create table testRDS (id INT PRIMARY KEY, second_column INT);
Query OK, 0 rows affected (0.24 sec)

mysql> show tables;

+-----------------------+

| Tables_in_DevOpsLocal |

+-----------------------+

| customer              |

| product               |

| product_transaction   |

| testRDS               |

| transactions          |

+-----------------------+


mysqldump -u root -h devopsonlinelocal.cpriyhidtmjl.us-east-2.rds.amazonaws.com -p DevOpsLocal > DevOpsLocalRDS.sql;
Enter password:
Warning: A partial dump from a server that has GTIDs will by default include the GTIDs of all transactions, even those that changed suppressed parts of the database. If you don't want to restore GTIDs, pass --set-gtid-purged=OFF. To make a complete dump, pass --all-databases --triggers --routines --events.


root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4/task4.1# ls
DevOpsLocalRDS.sql  DevOpsOnline2sql  DevOpsOnline.sql  images  readme.md  test_priv.sql

root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4/task4.1# mysql -u root DevOpsLocalRDS < DevOpsLocalRDS.sql
root@devopsonline:/home/mrbit/DevOps_online_Chernigiv_2021Q4/task4.1# mysql -u root
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 53
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

mysql> use DevOpsLocalRDS;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed

mysql> show lables;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'lables' at line 1

mysql> show tables;

+--------------------------+

| Tables_in_DevOpsLocalRDS |

+--------------------------+

| customer                 |

| product                  |

| product_transaction      |

| testRDS                  |

| transactions             |

+--------------------------+

DUMP is DONE and CHACKED.

################# PART 3 #######################

I created AWS DynamoDB table, added some items to it and try use Query and Scan filters.
 
For create table we can use AWS CLI or DynamoDB web page. For create table in CLI we should know which format of file  use, for example json.
In this case should be created json file with text:

{
    "TableName": "DevOpsOnline",
    "AttributeDefinitions": [
        { "AttributeName": "Names", "AttributeType": "SecondNames" }
      ],
    "KeySchema": [
      { "AttributeName": "Names"
        , "KeyType": "HASH" }
    ],
    "ProvisionedThroughput": {
      "ReadCapacityUnits": 10,
      "WriteCapacityUnits":10 
    }
}

Command should be like that:

aws dynamodb create-table --cli-input-json <path to json file>

But, i decided use web page. Results:

<img src="" width="300" >

<img src="" width="300" >

<img src="" width="300" >

<img src="" width="300" >

<img src="" width="300" >
