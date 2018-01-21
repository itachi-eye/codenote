awk





```shell
awk -F: '/mail/{print $1}' passwd.txt
awk -F',' '/Manager/{print $2,$3}' employee.txt
awk '/103/{print $1,$2}' items-sold.txt
```

默认分界符是空格。



```shell
BEGIN {
    FS=","
    OFS=":"
    print "---header---"
}
/John/{
    print $1,$3
}
END {
    print "---footer---"
}
```

内置变量

FS：输入字段分隔符

OFS：输出字段分隔符

RS：记录分隔符

ORS：输出记录分隔符

FILENAME：文件名

```shell
awk -F"," 'BEGIN{RS=":";ORS="\n====\n"}{print $1,$2}' 
```



NR：记录的序号，多个文件持续增加

FNR：记录在文件中的序号

