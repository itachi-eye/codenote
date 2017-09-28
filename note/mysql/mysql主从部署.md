# docker模拟mysql主从部署

## 1、环境准备

拉取mysql镜像

```shell
docker pull mysql
```

准备两个mysql配置文件：

```properties
# 主库配置文件my-master.cnf
[mysqld]
log-bin = mysql-bin
server-id = 1

# 从库配置文件my-slave.cnf
[mysqld]
server-id = 2
```

启动两个容器：主库，端口3307；从库，端口3308

```shell
docker run -d -e MYSQL_ROOT_PASSWORD=root \
 --name mysql-master \
  -v /root/mysql/my-master.cnf:/etc/mysql/my.cnf \
  -p 3307:3306 mysql

docker run -d -e MYSQL_ROOT_PASSWORD=root \
 --name mysql-slave \
  -v /root/mysql/my-slave.cnf:/etc/mysql/my.cnf \
  -p 3308:3306 mysql
```

环境已准备好。

具体参数如下：

**ip**

本机：172.18.134.10

master容器：172.17.0.2

slave容器：172.17.0.3

**shell**

```shell
# 本机 -> master
mysql -h172.18.134.10 -P3307 -uroot -proot

# 本机 -> slave
mysql -h172.18.134.10 -P3308 -uroot -proot

```



## 2、主库配置

新建一个用户专门用来同步master，

```sql
CREATE USER 'backup'@'%' IDENTIFIED BY '123456';
```

给backup用户分配备份的权限

```sql
GRANT REPLICATION SLAVE ON *.* to 'backup'@'%' identified by '123456';
```

主库配置完成。

查看主库状态：

```sql
show master status;
```

记住查询结果，后面会用。

File: mysql-bin.000003

Position: 688



## 3、从库配置

从库通过IO线程连接master，所以需要指定master的信息，包括host, port, user, password

```sql
change master to master_host='172.17.0.2', 
	master_port=3306, 
	master_user='backup', 
	master_password='123456', 
	master_log_file='mysql-bin.000003', 
	master_log_pos=688;
start slave;
```

查看从库状态，

```shell
show slave status\G
```

如果输出，

```text
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 172.17.0.2
                  Master_User: root
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000003
          Read_Master_Log_Pos: 688
               Relay_Log_File: 6b0f3668aa62-relay-bin.000002
                Relay_Log_Pos: 913
        Relay_Master_Log_File: mysql-bin.000003
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
```
则说明连接成功。

## 4、测试

在master上操作，更改都会显示在slave上。

