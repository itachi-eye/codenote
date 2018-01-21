# sed

[TOC]

## p

```shell
sed -n -f sed-script.sed passwd.txt
sed -n -e '/^root/p' -e '/^nobody/p' passwd.txt

sed -n \
> -e '/^root/p' \
> -e '/^nobody/p' \
> passwd.txt

sed -n '{
quote> /^root/p
quote> /^nobody/p
quote> }' passwd.txt

sed -n '2p' employee.txt
sed -n '2,4p' employee.txt #第2行-第4行
sed -n '2,$p' employee.txt
sed -n '/Jane/p' employee.txt #匹配Jane的行
sed -n '/Jason/,4p' employee.txt #匹配Jason的行到第4行
sed -n '/Jason/,/Jane/ p' employee.txt #匹配Jason的行到匹配Jane的行

# linux
sed -n '2,+3p' employee.txt # 2,3,4,5
sed -n '2~3p' employee.txt # 2,5,8,11...
```



## d

```shell
sed d employee.txt
sed '2 d' employee.txt
sed 1,2d employee.txt
sed '1,2 d' employee.txt
sed '2,$d' employee.txt
sed '1~2d' employee.txt # delete 1,3,5,7

sed '/Jason/d' employee.txt
sed '/Jason/,3d' employee.txt # 第一次匹配Jason的行 - 第3行
sed '/^$/ d' employee.txt # 删除空行
sed '/^[#_]/d' passwd.txt # 删除开头是#或者_的行
```



## w

```shell
sed 'w output.txt' employee.txt # 保存到output.txt，同时打印全部行到屏幕
sed -n 'w output.txt' employee.txt #同上，不打印到屏幕
sed -n '2 w output.txt' employee.txt #保存第2行
sed -n '1,4 w output.txt' employee.txt
sed -n '/Jane/ w output.txt' employee.txt
sed -n '/Jason/,4 w output.txt' employee.txt
sed -n '/Jason/,/Jane/ w output.txt' employee.txt

```



## s

```shell
sed '[address/pattern-range] s/original/replacement/[flag]' input-file 
```



```shell
sed 's/Manager/Director/' employee.txt

# flag

sed '/105/s/Manager/Director/g' employee.txt # 包含105的行进行替换
sed '/105/s/a/AA/2' employee.txt #包含105的行，第2个a替换成AA
sed -n 's/a/AA/3p' employee.txt #只打印第2个a替换成AA的行，没改变的不打印

sed -n 's/John/JJJJ/p' employee.txt > output.txt
#等效于
sed -n 's/John/JJJJ/w output.txt' employee.txt

sed 's/^/ls -l /e' files.txt # 执行ls -l 每一行


# 分界符 可以用任何一个字符作为分界符
sed -n 's/jason/JJJJ/ip' employee.txt
sed -n 's|jason|John|ip' employee.txt
sed -n 's@jason@John@ip' employee.txt
sed -n 's!jason!John!ip' employee.txt
sed -n 's^jason^John^ip' employee.txt
sed -n 's1jason1John1ip' employee.txt
sed -n 'sXjasonXJohnXip' employee.txt
sed -n 's jason John ip' employee.txt

```



获取匹配到的模式 &

```shell
# 开头的三个数字加上[]
sed 's/^[0-9][0-9][0-9]/[&]/' employee.txt 

# 每一行加上<>
sed 's/^.*$/<&>/' employee.txt  
```



匹配组 `\( ` 和  `\)`

```shell
sed 's/\([^,]*\).*/\1/g' employee.txt
```



---

正则

```shell

'^ $ .'
'* \+ \?'
'[0-9] [234] [^2]'
'a\|b'
'a\{m\}  a\{m,n\}'
'\b'


```



直接写入文件

`-i`

```shell
sed -i 's/john/JJJJ/i' employee.txt # 直接将修改写入原文件
sed -i 's jjjj John i' employee.txt # 空格作为分界符

sed -ibak 's/john/JJJJ/i' employee.txt #原文件备份到employee.txtbak
sed -i.bak 's/JJJJ/John/' employee.txt #原文件备份到employee.txt.bak
```



---

## a

指定位置后追加新行

```shell
sed '3 a -------' employee.txt #第3行后插入一行
sed '3,4 a -----' employee.txt #第3、4行后各插入一行
sed '$ a -------' employee.txt #最后插入一行
sed '/Jason/a --' employee.txt #在匹配Jason后插入一行


```























