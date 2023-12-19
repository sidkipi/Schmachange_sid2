use database DEMO1_DB;
use schema PUBLIC;

create table fidely_test_users if not exists(
  name varchar (100),  -- variable string column
  preferences string, -- column used to store JSON type of data
  created_at timestamp
);
