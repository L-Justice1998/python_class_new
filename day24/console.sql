use python6;
show tables;
select * from students limit 5,5;
insert into classes value('1','python1');
insert into classes value('2','python2');
select * from students s inner join classes c on s.cls_id = c.id;
select s.name,s.cls_id,c.name from students s left join classes c on s.cls_id = c.id;
select s.name,s.cls_id,c.name from students s right join classes c on s.cls_id = c.id;
create table areas(
    aid int primary key,
    atitle varchar(100),
    pid int
);
select count(*) from areas ;
select a.aid,a.atitle,b.atitle from areas a inner join areas b on a.pid=b.aid where b.atitle='广东省';
select a.aid,a.atitle,b.atitle from areas a inner join areas b on a.pid=b.aid where b.atitle='茂名市';

select name,height from students where height>(select avg(height) from students);
select name from students where id in(select distinct cls_id from students);
select avg(height) from students;
select avg(age) from students;
update students set height=192 where name='刘德华';
select * from students where (height,age)=(select max(height),max(age) from students);