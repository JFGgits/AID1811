import pymysql

host = 'localhost'
user = 'root'
password = '123456'
dbname = 'bank'

db_conn = None  # 连接对象


# 打印菜单
def print_menu():
    menu = '''
    --------------- 账户管理系统 ---------------
        1 - 查询账户信息
        2 - 新建账户
        3 - 修改账户
        4 - 删除账户
        q - 退出
    '''
    print(menu) #打印菜单
    return


# 连接
def conn_database():
    global db_conn
    db_conn = pymysql.connect(host,user,\
                password,dbname)
    if not db_conn:
        print("连接数据失败")
        return -1
    else:
        return 0


# 关闭数据库连接
def close_database():
    global db_conn
    if db_conn:
        db_conn.close()


# 查询数据
def query_acct():
    global db_conn
    try:
        cursor = db_conn.cursor()   # 获取游标
        sql = '''select * from acct'''
        cursor.execute(sql)   # 执行sql语句
        result = cursor.fetchall()
        for r in result:
            acct_no = r[0]
            acct_name = r[1]
            if r[6]:    # 不为空
                balance = float(r[6])
            else:
                balance = 0.00
            print("账号:%s 姓名:%s 余额:%.2f"%\
                    (acct_no, acct_name, balance))
        cursor.close()
    except Exception as e:
        print("查询数据异常")
        print(e)


# 插入数据
def insert_acct():
    try:
        # 准备数据
        acct_no = input("请输入账号:")
        acct_name = input("请输入户名:")
        acct_type = input("请选择账户类型 1-借记卡 2-理财卡:")
        balance = float(input("请输入开户金额:"))
        assert acct_type in ["1","2"]#判断acct_type是否合法
        assert balance >= 10.00
        
        # 拼装SQL语句, 执行插入
        sql = '''insert into acct(acct_no, acct_name,
                                  acct_type, balance)
                values('%s', '%s', %s, %.2f) 
        ''' % (acct_no, acct_name, acct_type, balance)
        # 获取游标,执行
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql)  #执行
        db_conn.commit()     #提交
        print("插入数据成功")        
    except Exception as e:
        db_conn.rollback()
        print("插入数据异常")
        print(e)


# 修改数据
def update_acct():
    try:
        # 准备数据
        acct_no_update = input("请输入账号:")
        balance_update = float(input("请输入开户金额:"))
        
        # 拼装SQL语句, 执行插入
        sql = '''update acct
                    set balance = balance + %s 
                 where acct_no = '%s'
        ''' % (balance_update, acct_no_update)
        # 获取游标,执行
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql)  #执行
        db_conn.commit()     #提交
        print("修改数据成功")        
    except Exception as e:
        db_conn.rollback()
        print("修改数据异常")
        print(e)


# 删除数据
def del_acct():
    try:
        acct_no_del = input("请输入要删除的账号:")

        # 拼装SQL语句，执行删除
        sql = '''delete from acct
                 where acct_no = '%s'
        ''' % acct_no_del

        # 获取游标，执行
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql)
        db_conn.commit()
        print("删除数据成功")        
    except Exception as e:
        db_conn.rollback()
        print("删除数据异常")
        print(e)



# 主函数
def main():
    # 连接
    if conn_database() < 0:
        return
    while True:
        print_menu()    # 打印菜单
        oper = input("请选择操作:")
        if not oper:
            continue
        elif oper == '1':
            # 查询数据
            query_acct()
        elif oper == '2':
            # 插入数据
            insert_acct()
        elif oper == '3':
            # 修改数据
            update_acct()
        elif oper == '4':
            # 删除数据
            del_acct()
        elif oper == 'q':
            # 退出
            break
        else:
            print("请输入正确的指令")
            continue
    # 关闭数据库连接对象
    close_database()

if __name__ == '__main__':
    main()