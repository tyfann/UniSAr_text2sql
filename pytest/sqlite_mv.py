# -*- ecoding: utf-8 -*-
# @ModuleName: sqlite_mv
# @Function: 
# @Author: Yufan-tyf
# @Time: 2022/3/24 21:19
import os
import glob
import shutil
from tqdm import tqdm

os.chdir('../')


def db_mv():
    db_path = './data/csgsql/database'
    db = glob.glob(os.path.join(db_path, '*.sqlite'))
    for i in tqdm(range(len(db)), desc='Processing'):
        sql_path = db[i]
        db_name = sql_path.split('/')[-1].split('.')[0]
        os.mkdir(os.path.join(db_path, db_name))
        shutil.move(sql_path, os.path.join(db_path, db_name))


if __name__ == '__main__':
    db_mv()
