select  version();

select now();

show databases;

use python6;

show tables ;

create table classes(
    id int unsigned auto_increment primary key not null,
        name varchar(10)
);
create table students(
    id int unsigned primary key  auto_increment not null ,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(6,2),
    gender enum('male','female','trans','confidential'),
    cls_id int unsigned default 0
);
create database demo charset ='utf8';
show create database demo;
DROP database demo;
alter table students add birthday DATE;
alter table students change birthday birth date not null ;
alter table students drop birth;

insert into classes values (0,'p5');
insert into classes values (0,'p6');

insert into students values (0,'正义',24,172,1,1);
insert into students(name,age) value ('wuji',24);
insert into students(name) values('lichuang'),('jiebao'),('pengpeng');
alter table students add birthday date;
update students set birthday='1998-07-22' where name='正义';
delete from students where id=4;
drop table students;

create table students(
    id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('male','female','trans','confidential') default 'confidential',
    cls_id int unsigned default 0,
    is_delete bit default 0
);

INSERT INTO students(name,age,height,gender,cls_id,is_delete)
VALUES
	( '小明', 18, 180.00, 2, 1, 0 ),
	( '小月月', 18, 180.00, 2, 2, 1 ),
	( '彭于晏', 29, 185.00, 1, 1, 0 ),
	( '刘德华', 59, 175.00, 1, 2, 1 ),
	( '黄蓉', 38, 160.00, 2, 1, 0 ),
	( '凤姐', 28, 150.00, 4, 2, 1 ),
	( '王祖贤', 18, 172.00, 2, 1, 1 ),
	( '周杰伦', 36, NULL, 1, 1, 0 ),
	( '程坤', 27, 181.00, 1, 2, 0 ),
	( '刘亦菲', 25, 166.00, 2, 2, 0 ),
	( '金星', 33, 162.00, 3, 3, 1 ),
	( '静香', 12, 180.00, 2, 4, 0 ),
	( '郭靖', 12, 170.00, 1, 4, 0 ),
	( '周杰', 34, 176.00, 2, 5, 0 );

insert into classes values (0, "python_01期"), (0, "python_02期");
truncate table classes;
select id as 序号,name as 姓名 from students;
select s.name,s.age from students s;
select distinct age from students;

select * from students where id>3;
select * from students where name = "黄蓉";
select * from students where is_delete=0;

select * from students where id>5 and gender='female';

select * from students where name like "小__";
select * from students where id between 3 and 8;
select * from students where id in (2,3,7);
select * from students where height is not null;
select * from students where gender='male' and is_delete=0 order by height desc;
select * from students order by age desc,height ;

select count(*) from students;
select max(age) from students;
select min(id) from students where is_delete=0;

select gender,count(*) from students group by gender;
select gender,avg(age) from students group by gender;
select gender,avg(height) as new_height from students where height is not null group by gender order by new_height;
select gender,group_concat(name) from students group by gender;
select gender,count(*) as gender_num from students group by gender having gender_num>=1;
select gender,count(*) as gender_num from students group by gender with rollup ;

select *,rank() over (partition by cls_id order by age desc) as rank1,
					dense_rank() over (partition by cls_id order by age desc) as dense_rank1,
					row_number() over (partition by cls_id order by age desc) as row_num  from students;