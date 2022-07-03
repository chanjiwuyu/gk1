# 1
# a=input(':')
# for i in range(len(a)):
#     if int(a[i])<5:
#         a=a[0:i]+'5'+a[i::]
#         break
# b='零一二三四五六七八九'
# for i in a:
#     print(b[int(i)],end='')
# print(end='\n')
# 2
# a='abcdefghijklmnopqrstuvwxyz'
# b=input(':')
# c=[]
# for i in a:
#     c.append(b.count(i))
# print(c)
# 3
a=input()
yes=True
for i in range(len(a)):
    if i==2 or i==5:
        if a[i]==':':
            pass
        else:
            yes=False
            break
if yes:
    print(1)
else:
    print(0)