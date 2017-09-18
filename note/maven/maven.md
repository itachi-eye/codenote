# maven

### 1. 切换环境

setting.xml有两个位置，

全局：${M2_HOME}/conf/setting.xml

用户：~/.m2/setting.xml

用户设置优先，可以在.m2目录下建立多个setting.xml，使用哪个时将当前设置改为setting.xml，切换使用。



### 2. 指令

1 创建项目

```shell
mvn archetype:generate
```

普通java项目选择quickstart，web项目选择webapp



2 编译源代码

```shell
mvn clean compile
```

首先执行`clean:clean` ，删除target目录下文件，

然后执行`resources:resources` ，

最后执行`compile:compile`



3 测试

```shell
mvn clean test
```



4 打包

```shell
mvn clean package
```

在pom.xml中，定义打包类型，`<packaging>jar</packaging>` ，默认为jar，在target目录中生成 test-app-1.0-SNAPSHOT.jar，web项目打包成war。



5 安装

```shell
mvn clean install
```

将生成的jar或者war安装到mavne本地仓库中，其他maven项目可以使用



6 运行jar

默认打包生成的jar不能直接运行

在pom.xml中加入

```xml
<build>  
<plugins>  
    <plugin>  
        <groupId>org.apache.maven.plugins</groupId>  
        <artifactId>maven-shade-plugin</artifactId>  
        <version>1.4</version>  
        <executions>  
        <execution>  
            <phase>package</phase>  
            <goals>  
            <goal>shade</goal>  
            </goals>  
            <configuration>  
            <transformers>  
                <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">  
                    <mainClass>com.llq.App</mainClass>  
                </transformer>  
            </transformers>  
            </configuration>  
        </execution>  
        </executions>  
    </plugin>  
</plugins>  
</build> 
```

然后重新`mvn clean install ` ，生成jar包，执行

```shell
java -jar target/test-app-1.0-SNAPSHOT.jar
```

即可





