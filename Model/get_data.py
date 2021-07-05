# 表格数据格式化
def get_data(pw_id,cursor,counts):
    try:

        jsonData = []
        # print(len(parameters))
        # print(counts)
        for row in range(len(pw_id)):
            data = {}
            # print(parameters[row])
            for i in range(len(cursor.description)):
                data[cursor.description[i][0]] = pw_id[row][i]

            jsonData.append(data)
        # # print(jsonData)
        if counts != 0:
            return {"code": 0, "msg": "成功", "count": counts, "data": jsonData}
        else:
            return {'code': 201, 'msg': "无数据"}

    except:
        return {'code': 201, 'msg': "无数据"}