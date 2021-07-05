from flask import Flask, jsonify, request,render_template
from Model.model_login import login_get
from Model.getdata import get_token_db
from Model.getdata import get_table
from Model.conmysql import c_mysql2
from Model.get_data import get_data as get_datas
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 设置接口数据编码

# 数据格式转换
def set_json(data):
    return jsonify(data)
import jwt
import datetime
def set_jwts():
    dic = {
        'exp': datetime.datetime.now() + datetime.timedelta(days=1),  # 过期时间
        'iat': datetime.datetime.now(),  #  开始时间
    }

    return jwt.encode(dic, 'secret', algorithm='HS256')  # 加密生成字符串

def conbs(token):
    sql_data = get_token_db("sql_token", token)
    print(sql_data)
    if sql_data["code"] == 0:
        if sql_data["data"][0]["types"] == 1:
            host = sql_data["data"][0]["host"]
            host_user = sql_data["data"][0]["host_user"]
            host_passwd = sql_data["data"][0]["host_passwd"]
            host_db = sql_data["data"][0]["host_db"]
            port = sql_data["data"][0]["port"]
            return c_mysql2(host, port, host_user, host_passwd, host_db)
        else:
            return False
    else:
        return False
# print(set_jwts())
# exit()
# print(s)
# s = jwt.decode(s, 'secret', issuer='lianzong', algorithms=['HS256'])  # 解密，校验签名
# print(s)
# print(type(s))

# 设置跨域访问
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/')
def hello_world():
    data = {
        'code': 0,
        'msg': "访问成功",

    }
    return set_json(data)

@app.route('/get_jwts')
def indexs():

    return {"token":set_jwts()}


@app.route('/get_table',methods=["POST"])
def get_tables():

    token = request.form.get("token")
    table = request.form.get("table")
    page = int(request.form.get("page"))
    limit = int(request.form.get("limit"))
    if page:
        pass
    else:
        page=1
    if limit:
        pass
    else:
        limit=10
    cons = conbs(token)
    if cons:
        cursor = cons.cursor()
        sql = "select * from " + str(table) +" limit "+str((page-1)*limit)+","+str(limit)
        sql1 = "select * from " + str(table)
        cursor.execute(sql1)
        counts = len(cursor.fetchall())
        cursor.execute(sql)
        pw_id = cursor.fetchall()
        return get_datas(pw_id, cursor, counts)
    else:
        return {"code":201,"msg":"访问失败"}



@app.route('/get_tables',methods=["POST"])
def get_tabless():
    token = request.form.get("token")
    table = request.form.get("table")
    page = int(request.form.get("page"))
    limit = int(request.form.get("limit"))
    where = request.form.get("where")
    if page:
        pass
    else:
        page=1
    if limit:
        pass
    else:
        limit=10
    cons = conbs(token)
    if cons:
        cursor = cons.cursor()
        sql = "select * from " + str(table) +" where "+str(where)+" limit "+str((page-1)*limit)+","+str(limit)
        sql1 = "select * from " + str(table) +" where "+str(where)
        cursor.execute(sql1)
        counts = len(cursor.fetchall())
        cursor.execute(sql)
        pw_id = cursor.fetchall()
        return get_datas(pw_id, cursor, counts)
    else:
        return {"code":201,"msg":"访问失败"}
@app.route('/add_table',methods=["POST"])
def add_tables():
    import ast
    token = request.form.get("token")
    table = request.form.get("table")
    name_list=ast.literal_eval(request.form.get("name_list"))
    value_list=ast.literal_eval(request.form.get("value_list"))
    cons = conbs(token)
    if cons:
        try:
            cursor = cons.cursor()
            if len(name_list) > 1:
                sql = "INSERT INTO " + str(table) + " " + str(tuple(name_list)).replace("'", "") + " VALUES " + str(
                    tuple(value_list))
            else:
                sql = "INSERT INTO " + str(table) + " " + str(tuple(name_list)).replace("'", "").replace(",",
                                                                                                          "") + " VALUES " + str(
                    tuple(value_list)).replace(",", "")

            print(sql)
            cursor.execute(sql)
            cons.commit()
            cursor.close()
            cons.close()
            return {'code': 0, 'msg': "添加成功"}
        except:
            return {'code': 201, 'msg': "添加失败"}
    else:
        return {"code": 201, "msg": "访问失败"}
@app.route('/up_table',methods=["POST"])
def up_tables():
    import ast
    token = request.form.get("token")
    table = request.form.get("table")
    up_name = request.form.get("up_name")
    up_value = request.form.get("up_value")
    name_list=ast.literal_eval(request.form.get("name_list"))
    value_list=ast.literal_eval(request.form.get("value_list"))
    cons = conbs(token)
    if cons:
        try:
            cursor = cons.cursor()
            field=""
            for ns in range(len(name_list)):
                field = str(name_list[ns]) + " = '" + str(value_list[ns]) + "'," + field
            field = field[:len(field) - 1]



            sql = "UPDATE " + str(table) + " SET " + str(field) + " WHERE " + str(up_name) + " = '" + str(up_value) + "'"
            print(sql)
            cursor.execute(sql)
            cons.commit()
            cons.close()
            return {'code': 0, 'msg': "数据更新成功"}
        except:
            return {'code': 201, 'msg': "数据更新失败"}
    else:
        return {"code": 201, "msg": "访问失败"}
@app.route('/api')
def apis():
    return render_template("api.html")
@app.route('/list')
def lists():
    return render_template("list.html")

@app.route('/logins')
def logins():
    passwd = request.args.get("passwd")
    if passwd =="sqlroot":
        return {"code":1}
    else:
        return {"code":0}
if __name__ == '__main__':

    # field = ""
    # name_list=[1,2,3]
    # value_list=[1,2,3]
    #
    # print()
    # exit()
    app.run(host='0.0.0.0', port=8201)