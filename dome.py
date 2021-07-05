import requests as go
import json
#
data={
    "table":"sql_token",
    "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjU1NjgyOTUsImlhdCI6MTYyNTQ4MTg5NX0.5DsA6JHe2jbKYHJ7HpUznFMOGY6ZK9LpYYHchB5d5iQ",
    "limit":10,
    "page":1
}
print(json.loads(go.post("http://172.16.1.121:8200/get_table",data=data).text))
exit()
# data1={
# "table":"sql_token",
# "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjU0MTI4NDMsImlhdCI6MTYyNTMyNjQ0M30.cF0knkos36HfmFfBMBEwp05P9HXrwqZ-vZZJR8Q2YDA",
# "limit":10,
# "page":1,
# "where":"id='1'",
# }
# print(json.loads(go.post("http://172.16.1.121:8200/get_tables",data=data1).text))

datas={
    "table":"sql_user",
    "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjU0MTI4NDMsImlhdCI6MTYyNTMyNjQ0M30.cF0knkos36HfmFfBMBEwp05P9HXrwqZ-vZZJR8Q2YDA",
    "name_list":"['user','passwd']",
    "value_list":"['jinjin',123456]",


}
print(json.loads(go.post("http://172.16.1.121:8200/add_table",data=datas).text))
