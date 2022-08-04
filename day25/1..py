# Creator:justice 廖振谊
# Creat time:2022/6/27 10:39
from pymysql import *

def main():
    conn=connect(host='192.168.119.130',user='root',password='123',
                 database='python6',charset='utf8')
    cs1=conn.cursor()
    # count=cs1.execute("delete from students where name = '小明'")
    # count=cs1.execute("insert into students values "
    #                   "(1,'小明',18,182,'male',1,0)")
    # count=cs1.execute("update students set name='小明明' where name='小明'")
    # count=cs1.execute('select name from students '
    #                   'where age=(select max(age) from students)')
    # count = cs1.execute("select name from students where age>18")
    # for i in range(count):
    #     name=cs1.fetchone()
    #     print(name)
    # print(count)

    id='1 or 1'
    sql='select name from students where id={}'.format(id)
    count=cs1.execute(sql)
    print(count)

    count=cs1.execute('select name from students where id=%s',id)
    print(count)
    print(cs1.fetchone())
    conn.commit()
    cs1.close()
    conn.close()

if __name__ == '__main__':
    main()