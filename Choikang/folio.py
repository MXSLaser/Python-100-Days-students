count=0
wide=0.0001
while wide<8848:
    wide*=2
    count+=1
print('一共对折了%d次,厚度为%f'%(count,wide))