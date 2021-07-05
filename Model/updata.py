# 更新信息
from .conmysql import  c_mysql


def up_table(table,field,id):
    # try:

        db = c_mysql()
        # 使用cursor()方法获取操作游标 UPDATE `s_kanban`.`s_user` SET `name` = '张三', `passwd` = '123456', `phone` = '17764119120', `department` = '无', `type` = 1, `part` = '管理员', `ctime` = '2020-09-30 08:44:25', `stime` = NULL WHERE `id` = 1;
        cursor = db.cursor()
        sql = "UPDATE "+str(table)+" SET "+str(field)+" WHERE id = '"+str(id)+"'"
        print(sql)
        cursor.execute(sql)
        db.commit()
        db.close()
        return {'code': 0, 'msg': "操作成功"}

