# -*- coding: utf-8 -*-
import time
import os
import datetime
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
for i in diff.ndiff(open(pre_config).readlines(),open(after_config).readlines()):
  file_write_diff.writelines(i)
file_write_diff.close()

#diff2.txt → 本当の差分を抽出
row_no = 0
f3 = open("diff.txt","r",encoding="utf_8")
f4 = open('diff2.txt','w',encoding="utf_8")

while True:
  line = f3.readline()
  if line:
    row_no += 1
    
    #事後コンフィグに追加または変更がある場合
    if line[0] == "!" or line[0] == "+":
      f4.write(line)    

    #事後コンフィグに削除がある場合
    elif "- " in line and "---" not in line:
      f4.write(line)

  else:
    break

f4.close()

#投入コンフィグ作成
f4 = open('diff2.txt','r',encoding="utf_8")
f5 = open('Input_config.txt','w',encoding="utf_8",newline='\n')

f5.write("conf\n\n")
while True:
  line = f4.readline()
  if line:
    #事後コンフィグに追加または変更がある場合
    if line[0] == "!" or line[0] == "+":
      f5.write(line[2:])
    #事後コンフィグに削除がある場合
    elif line[0] == "-":
      f5.write("delete "+line[2:])

  else:
    f5.write("\ncommit\n")  
    f5.write("save\n")

    break

