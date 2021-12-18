CREATE TABLE test.covid19_cases(
    id int primary key auto_increment,
    province	   varchar(256),
    country	   varchar(256),
    lat		   decimal(9,6),
    lon	   decimal(9,6),
    date	   DATE,
    cases	   int,
    type	   varchar(5)
 );

CREATE TABLE test.consolidate_covid19_cases(
id int primary key auto_increment,
province       varchar(256),
country        varchar(256),
lat            decimal(9,6),
lon       decimal(9,6),
year_id int,
month_id int,
total decimal(20,2)
);

