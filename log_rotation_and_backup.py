#!/bin/python3
import os
import shutil
import gzip
import datetime

logdir="/root/logs"
backupdir='/root/backup'
cutoff_days=7

os.makedirs(backupdir, exist_ok=True)

for file in os.listdir(logdir):
    if file.endswith(".log"):
        path=os.path.join(logdir,file)
        mtime=datetime.datetime.fromtimestamp(os.path.getmtime(path))
        print(f"mtime is:{mtime}")
        if (datetime.datetime.now() - mtime).days<cutoff_days:
            with open(path,'rb') as f_in, gzip.open(f"{backupdir}/{file}.gz",'wb') as f_out:
                shutil.copyfileobj(f_in,f_out)
            os.remove(path)
print("Old logs compressed and backed up.")
