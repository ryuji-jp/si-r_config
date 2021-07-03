# -*- coding: utf-8 -*-

import time
#import diff
#import ssh
#import log_replace
import os
import datetime
#from pyfiglet import Figlet
import sys
import difflib as diff
from difflib import HtmlDiff

#入力受付
pre_config = sys.argv[1]
after_config = sys.argv[2]

print("事前コンフィグ → "+pre_config)
print("事後コンフィグ → "+after_config)

#入力受付で得たファイル名を読み込む
with open(pre_config) as f: f1 = f.readlines()
with open(after_config) as f: f2 = f.readlines()

#差分比較HTML → diff.html
df = HtmlDiff()
now = datetime.datetime.now()

file_write = open("diff.html".format(now), mode='w')

file_write.writelines(df.make_file(f1, f2))

file_write.close()

#差分比較 txt形式 → diff.txt
file_write_diff = open("diff.txt".format(now), mode='w')
for i in diff.context_diff(f1, f2, fromfile=pre_config, tofile=after_config):
	file_write_diff.writelines(i)
file_write_diff.close()

#diff.txt 抽出
row_no = 0
f3 = open("diff.txt","r",encoding="utf_8")
f4 = open('diff2.txt','w',encoding="utf_8")

w = ["!","*","-"]

while True:
  line = f3.readline()
  if line:
    row_no += 1
    if row_no > 2:
        if "---" in line:
            while True:
                line = f3.readline()
                if "!" not in line:
                    f4.write(line)
                
                else:
                    f4.write(line)
                    break

  else:
    break



'''

#ssh
device_path = "input/device"

device_file = os.listdir(device_path)
device_files = [f for f in device_file if os.path.isfile(os.path.join(device_path, f))]
print(device_files)

for dev in device_files:
    ssh.ssh_log(dev)


#logリプレース
log_path = "input/log"

log_file = os.listdir(log_path)
log_files = [f for f in log_file if os.path.isfile(os.path.join(log_path, f))]
print(log_files)

for log in log_files:
    log_replace.replace(log)

print("-----------------------------")

#diff
for log in log_files:
    diff.diff_log(log)

#finish
f = Figlet(font="slant")
msg = f.renderText("FINISH !")
print(msg)

'''
