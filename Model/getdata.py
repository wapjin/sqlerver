from .conmysql import c_mysql
from .get_data import get_data

# 获取指定所有表格数据


def get_table(table, page, limit):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where  order by id desc limit "+str((page-1)*limit)+","+str(limit)
    sql1 = "select * from "+str(table)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return get_data(pw_id, cursor, counts)


# 获取未接单表格数据


def get_tableall(table, page, limit):
    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where ISNULL(caigou_name)>0 and ISNULL(uid)>0  and  ISNULL(dtime)>0 order by id desc limit "+str((page-1)*limit)+","+str(limit)
    sql1 = "select * from "+str(table)+" where ISNULL(caigou_name)>0 and ISNULL(uid)>0  and  ISNULL(dtime)>0 "
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)

# 获取未接单表格数据


def get_token_db(table, uid):

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where token='"+str(uid)+"'"
    sql1 = "select * from "+str(table)+" where token='"+str(uid)+"'"
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)
# 采购单列表
def get_tablemyallsd(table, uid, page, limit):

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from x_order a join x_orders b on a.orderid=b.id and a.uid="+str(uid)+" and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0 order by a.id desc limit "+str((page-1)*limit)+","+str(limit)
    sql1 = "select * from x_order a join x_orders b on a.orderid=b.id and a.uid="+str(uid)+" and ISNULL(a.dtime)>0 and  ISNULL(b.typess)>0 "
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)


# 获取列表
def get_tablemyalls(table, uid, page, limit):

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where orderid='"+str(uid)+"'  and  ISNULL(dtime)>0 order by id desc limit "+str((page-1)*limit)+","+str(limit)
    sql1 = "select * from "+str(table)+" where orderid='"+str(uid)+"'  and  ISNULL(dtime)>0 "
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)


# 搜索单号是否重复
def get_orderid(table,uid,page, limit):

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where order_id='"+str(uid)+"' order by id desc limit "+str((page-1)*limit)+","+str(limit)
    sql1 = "select * from "+str(table)+" where order_id='"+str(uid)+"'"
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)

# 搜索单号是否重复
def get_xiadan(table,uid,page, limit):

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where xiadan_time='"+str(uid)+"' order by id desc limit "+str((page-1)*limit)+","+str(limit)
    sql1 = "select * from "+str(table)+" where xiadan_time='"+str(uid)+"'"
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)

# 搜索我的采购单
def get_s_myorder(table,uid,order_id,dingding_name,dingding_bumen,dingding_xm,dingding_endtime,dingding_type,xiadan_time,gaizhang_type,fapiao_type,page, limit):

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    where =""
    if order_id:
        where +=" and order_id like '%"+order_id+"%'"
    if dingding_name:
        where +=" and dingding_name like '%"+dingding_name+"%'"
    if dingding_xm:
        where +=" and dingding_xm='"+dingding_xm+"'"
    if dingding_bumen:
        where +=" and dingding_bumen like '%"+dingding_bumen+"%'"
    if dingding_type:
            where +=" and dingding_type='"+dingding_type+"'"
    if dingding_endtime:
            where +=" and dingding_endtime like '%"+dingding_endtime+"%'"
    if xiadan_time:
            where +=" and xiadan_time like '%"+xiadan_time+"%'"

    if fapiao_type:
        if fapiao_type=="未签字":
            where += " and (ISNULL(fapiao_type)>0 or fapiao_type='' or fapiao_type='未签字') "
        else:
            where +=" and fapiao_type = '"+fapiao_type+"'"

    if gaizhang_type:
        if gaizhang_type == "未审批":
            where += " and (ISNULL(gaizhang_type)>0 or gaizhang_type='' or  gaizhang_type='未审批')"
        else:
            where +=" and gaizhang_type = '"+gaizhang_type+"'"


    sql = "select * from "+str(table)+" where uid='"+str(uid)+"' and   ISNULL(dtime)>0 "+str(where)+" order by id desc limit "+str((page-1)*limit)+","+str(limit)
    sql1 = "select * from "+str(table)+" where uid='"+str(uid)+"' and  ISNULL(dtime)>0 "+str(where)
    print(sql)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)

# 搜索未接单的采购单
def get_s_order(table,order_id,dingding_name,dingding_bumen,dingding_xm,dingding_endtime,dingding_type,xiadan_time,page, limit):
    where = ""
    if order_id:
        where += " and order_id like '%" + order_id + "%'"
    if dingding_name:
        where += " and dingding_name like '%" + dingding_name + "%'"
    if dingding_xm:
        where += " and dingding_xm='" + dingding_xm + "'"
    if dingding_bumen:
        where += " and dingding_bumen like '%" + dingding_bumen + "%'"
    if dingding_type:
        where += " and dingding_type='" + dingding_type + "'"
    if dingding_endtime:
        where += " and dingding_endtime like '%" + dingding_endtime + "%'"
    if xiadan_time:
        where += " and xiadan_time like '%" + xiadan_time + "%'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where ISNULL(uid)>0  and  ISNULL(dtime)>0 "+str(where)+"  order by id desc limit "+str((page-1)*limit)+","+str(limit)
    sql1 = "select * from "+str(table)+" where ISNULL(uid)>0 and  ISNULL(dtime)>0 "+str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)
# 搜索所有的采购单
def get_s_allorder(table,order_id,dingding_name,dingding_bumen,dingding_xm,dingding_endtime,dingding_type,xiadan_time,page, limit):
    where = ""
    if order_id:
        where += " and order_id like '%" + order_id + "%'"
    if dingding_name:
        where += " and dingding_name like '%" + dingding_name + "%'"
    if dingding_xm:
        where += " and dingding_xm='" + dingding_xm + "'"
    if dingding_bumen:
        where += " and dingding_bumen like '%" + dingding_bumen + "%'"
    if dingding_type:
        where += " and dingding_type='" + dingding_type + "'"
    if dingding_endtime:
        where += " and dingding_endtime like '%" + dingding_endtime + "%'"
    if xiadan_time:
        where += " and xiadan_time like '%" + xiadan_time + "%'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where  ISNULL(dtime)>0 "+str(where)+"  order by id desc limit "+str((page-1)*limit)+","+str(limit)
    sql1 = "select * from "+str(table)+" where   ISNULL(dtime)>0 "+str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)
# 搜索用户

def get_suser(table,gonghao,name,page, limit):

    where = ""
    if gonghao:
        where += " and gonghao = '" + gonghao + "'"
    if name:
        where += " and name like '%" + name + "%'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where ISNULL(dtime)>0 "+str(where)+"  order by id desc limit "+str((page-1)*limit)+","+str(limit)
    sql1 = "select * from "+str(table)+" where ISNULL(dtime)>0 "+str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)

# 搜索统一的基础

def all_s_list(table,name,page, limit):

    where = ""
    if name:
        where += " and name like '%" + name + "%'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where ISNULL(dtime)>0 "+str(where)+"  order by id desc limit "+str((page-1)*limit)+","+str(limit)
    sql1 = "select * from "+str(table)+" where ISNULL(dtime)>0 "+str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)

# 搜索供货单位信息

def danwei_s_list(table,gonghuo_danwe,gonghuo_name,gonghuo_itel,gonghuo_dizhi,page, limit):

    where = ""
    if gonghuo_danwe:
        where += " and gonghuo_danwe like '%" + gonghuo_danwe + "%'"
    if gonghuo_name:
        where += " and gonghuo_name like '%" + gonghuo_name + "%'"
    if gonghuo_itel:
        where += " and gonghuo_itel like '%" + gonghuo_itel + "%'"
    if gonghuo_dizhi:
        where += " and gonghuo_dizhi like '%" + gonghuo_dizhi + "%'"

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where ISNULL(dtime)>0 "+str(where)+"  order by id desc limit "+str((page-1)*limit)+","+str(limit)
    sql1 = "select * from "+str(table)+" where ISNULL(dtime)>0 "+str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)
# 获取统计数据 yufu_time zhongqi_time yukuan_time
def get_tongji(table,yers,finds):

    where = ""

    # where += " and "+str(finds)+" like '%"+yers+"%' "
    # if caigou_name:
    #     where += " and caigou_name like '%" + caigou_name + "%' "
    # if gongyi_name:
    #     where += " and gonghuo_danwe like '%" + gongyi_name + "%' "
    # if xm_name:
    #     where += " and dingding_xm like '%" + xm_name + "%' "

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where ISNULL(uid)=0 "+str(where)
    sql1 = "select * from "+str(table)+" where ISNULL(uid)=0 "+str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)


# 反获取项目名
def getid(table,id):

    where = ""

    where += "  id = '"+str(id)+"' "
    # if caigou_name:
    #     where += " and caigou_name like '%" + caigou_name + "%' "
    # if gongyi_name:
    #     where += " and gonghuo_danwe like '%" + gongyi_name + "%' "
    # if xm_name:
    #     where += " and dingding_xm like '%" + xm_name + "%' "

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where "+str(where)
    sql1 = "select * from "+str(table)+" where  "+str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)

# 获取统计数据
def get_tongjigg(table):

    where = ""

    where += " and ISNULL(dtime)>0 "
    # if caigou_name:
    #     where += " and caigou_name like '%" + caigou_name + "%' "
    # if gongyi_name:
    #     where += " and gonghuo_danwe like '%" + gongyi_name + "%' "
    # if xm_name:
    #     where += " and dingding_xm like '%" + xm_name + "%' "

    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where ISNULL(uid)=0 "+str(where)
    sql1 = "select * from "+str(table)+" where ISNULL(uid)=0 "+str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)
def get_tongjis(table,yers,finds,xm_name,g):

    where = ""
    print(xm_name)
    print(g)
    where += " and "+str(finds)+" like '%"+yers+"%' "
    where += " and "+g+" = '"+str(xm_name)+"' "


    db = c_mysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from "+str(table)+" where ISNULL(uid)=0 "+str(where)
    sql1 = "select * from "+str(table)+" where ISNULL(uid)=0 "+str(where)
    cursor.execute(sql1)
    counts = len(cursor.fetchall())
    cursor.execute(sql)
    pw_id = cursor.fetchall()
    return  get_data(pw_id,cursor,counts)