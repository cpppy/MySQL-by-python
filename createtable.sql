create table csdntable
(
	id int(10) unsigned not null auto_increment primary key,
	word char(50) not null,
	rate float not null,
	website char(10) default 'othersites'
);

create table zhihutable
(
	id int(10) unsigned not null auto_increment primary key,
	word char(50) not null,
	rate float not null,
	website char(10) default 'othersites'
);

create table buptbbstable
(
	id int(10) unsigned not null auto_increment primary key,
	word char(50) not null,
	rate float not null,
	website char(10) default 'othersites'
);

create table ustcbbstable
(
	id int(10) unsigned not null auto_increment primary key,
	word char(50) not null,
	rate float not null,
	website char(10) default 'othersites'
);

create table baiduQAtable
(
	id int(10) unsigned not null auto_increment primary key,
	word char(50) not null,
	rate float not null,
	website char(10) default 'othersites'
);

create table othersitestable
(
	id int(10) unsigned not null auto_increment primary key,
	word char(50) not null,
	rate float not null,
	website char(10) default 'othersites'
);


