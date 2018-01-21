docker安装ES6



1、拉取java image

```Shell
docker pull java
docker run -d -it -p 9200:9200 -p 9300:9300 --name java-es6 java
```



2、下载ES6

```
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.1.2.zip
unzip elasticsearch-6.1.2.zip
```



3、修改max_map_count

注意，在容器里面修改会失败，改为在宿主机上修改，然后重启容器

```
sudo sysctl -w vm.max_map_count=262144
```



4、修改es配置使其可以被任意ip访问

```
vim config/elasticsearch.yml
network.host: 0.0.0.0
```



5、启动es

```
./bin/elasticsearch
```

用 Docker主机ip:9200 就可以访问es



