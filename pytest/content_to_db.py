# -*- ecoding: utf-8 -*-
# @ModuleName: content_to_db
# @Function: 
# @Author: Yufan-tyf
# @Time: 2022/3/24 20:56
import json
import os
import sqlite3
import glob
import shutil

os.chdir('..')


def generate_sql(sql_len):
    sql = '('
    for i in range(sql_len):
        if i == sql_len - 1:
            sql += '?)'
        else:
            sql += '?, '
    return sql


if __name__ == '__main__':
    csgsql_path = './data/csgsql'

    with open(os.path.join(csgsql_path, 'db_content.json')) as f:
        csgsql_content = json.load(f)

    for single_db in csgsql_content:
        conn = sqlite3.connect(os.path.join(csgsql_path, 'database', single_db['db_id'] + '.sqlite'))
        cursor = conn.cursor()

        for table in single_db['tables'].keys():
            sql = "create table " + table + "("
            for index, header in enumerate(single_db['tables'][table]['header']):
                if index == len(single_db['tables'][table]['header']) - 1:
                    if single_db['tables'][table]['type'][index] == "number":
                        sql += " " + header + " int"
                    else:
                        sql += " " + header + " " + single_db['tables'][table]['type'][index]
                else:
                    if single_db['tables'][table]['type'][index] == "number":
                        sql += " " + header + " int,"
                    else:
                        sql += " " + header + " " + single_db['tables'][table]['type'][index] + ","
            sql += ");"

            cursor.execute(sql)

            sql = 'insert into ' + table + ' values' + generate_sql(len(single_db['tables'][table]['header']))

            with conn:
                conn.executemany(sql, single_db['tables'][table]['cell'])
