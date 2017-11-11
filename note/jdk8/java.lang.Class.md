# java.lang.Class

[TOC]

## 概述

- 每个类都对应一个Class对象，JVM加载管理。
- 创建某个类的实例时，先检查该类对应的Class对象是否存在；如果不存在，JVM根据类名查找对应的字节码文件，创建对应的Class对象，然后再创建实例。
- 基本类型，void，数组都有对应的Class对象，且与包装类型不同。相同**类型**和**维数**的数组共用一个Class对象。
- Class对象代表着一个类的字节码，JVM提供`forName()`方法加载字节码到内存，并用Class对象封装。

![alt](http://img.blog.csdn.net/20170430160610299?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

1. 加载：通过一个类的完全限定查找此类字节码文件，并利用字节码文件创建一个Class对象
2. 链接：验证字节码的安全性和完整性；准备阶段为**静态域**分配存储空间
3. 初始化：执行静态初始化器和初始化静态域；如果有父类，先初始化父类。该阶段才真正开始执行类中定义的Java代码。

## 获取Class对象

1 Class静态方法加载字节码

```java
static Class<?> forName(String className)
static Class<?> forName(String name, boolean initialize, ClassLoader loader)
```

2 通过类来获得

```java
Class<T> c = T.class;
```

3 通过对象获得，继承自Object

```java
Class<?> c = t.getClass();
```

> forName()和getClass()，会触发类的初始化阶段
>
> T.class，不会触发初始化

#### 基本类型的Class对象

基本类型都有对应的Class对象；包装类型有一个字段`TYPE`，指向对应基本类型的Class对象。

```java
public static final Class<Integer>  TYPE = (Class<Integer>) Class.getPrimitiveClass("int");
```

测试

```java
int.class == Integer.class; // false
int.class == Integer.TYPE; // true
```

形式

```java
Class c1 = int.class; // ok
Class<?> c2 = int.class; // ok
Class<Integer> c3 = int.class; // ok
Class<int> c4 = int.class; // wrong
```

> 带泛型的Class\<T\> 优于 带通配符的Class<?> 优于 不带泛型的Class，
>
> Class\<T\> 确保在编译期间保证类型的正确性
>
> Class<?> 告诉编译器，确实是采用任意类型的泛型，而不是忘记泛型约束
>
> Class，会引起类型的混乱

#### 数组的Class对象





## Class对象包含类的所有类型信息

### 1 名称

```java
String getSimpleName()
String getName()
String getCanonicalName()
```

举例：

|             | getSimpleName | getName              | getCanonicalName    |
| ----------- | ------------- | -------------------- | ------------------- |
| int         | int           | int                  | int                 |
| int[]       | int[]         | [I                   | int[]               |
| int\[\]\[\] | int\[\]\[\]   | [[I                  | int\[\]\[\]         |
| Integer     | Integer       | java.lang.Integer    | java.lang.Integer   |
| Integer[]   | Integer[]     | [Ljava.lang.Integer; | java.lang.Integer[] |
| 内部类A        | A             | Out$A                | Out.A               |

### 2 构造器

2.1 返回访问权限是public的构造器

```java
Constructor<?>[] getConstructors()
Constructor<T> getConstructor(Class<?>... parameterTypes)
```

举例：

```java
Class<Integer> c = Integer.class;
Constructor<?>[] constructors = c.getConstructors();
for (Constructor con : constructors) {
    p(con);
}
//public java.lang.Integer(int)
//public java.lang.Integer(java.lang.String) throws java.lang.NumberFormatException
```

举例2：

```java
Class<Integer> c = Integer.class;
Constructor<Integer> con1 = c.getConstructor(int.class);

Constructor<Integer> con2 = c.getConstructor(String.class);
```

2.2 返回**所有**声明的构造器，public，protected，private

```java
Constructor<?>[] getDeclaredConstructors()
Constructor<T> getDeclaredConstructor(Class<?>... parameterTypes)
```

### 3 属性

```java
Field[] getFields()
Field getField(String name)
Field[] getDeclaredFields()
Field getDeclaredField(String name)
```

### 4 方法

```java
Method[] getMethods()
Method getMethod(String name, Class<?>... parameterTypes)
Method[] getDeclaredMethods()
Method getDeclaredMethod(String name, Class<?>... parameterTypes)
```

### 5 接口和父类

```java
Class<?>[] getInterfaces() // 获取该类实现的所有接口
Type[] getGenericInterfaces() // 获取接口的类型

Class<? super T> getSuperclass() // 父类
Type getGenericSuperclass() // 父类类型
```

### 6 Resource

```java
URL getResource(String name)
InputStream getResourceAsStream(String name)
```

举例：

不以`/`开头，在该类所在的包里取资源

```java
getResource("") // ...bin/com/llq
getResource("abc") // ...bin/com/llq/abc 如果abc存在
```

以`/`开头，从classpath路径下获取资源

```java
getResource("/"); // ...bin
getResource("/com/llq/abc"); // ...bin/com/llq/abc
```



## Class对象方法

```java
static Class<?> forName(String className)
static Class<?> forName(String name, boolean initialize, ClassLoader loader)


String getSimpleName()
String getName()
String getCanonicalName()

// 构造器
Constructor<?>[] getConstructors()
Constructor<T> getConstructor(Class<?>... parameterTypes)
Constructor<?>[] getDeclaredConstructors()
Constructor<T> getDeclaredConstructor(Class<?>... parameterTypes)

// 属性
Field[] getFields()
Field getField(String name)
Field[] getDeclaredFields()
Field getDeclaredField(String name)

// 方法
Method[] getMethods()
Method getMethod(String name, Class<?>... parameterTypes)
Method[] getDeclaredMethods()
Method getDeclaredMethod(String name, Class<?>... parameterTypes)

// 类作用域
Class<?>[] getClasses() // 外部类，获取定义在该类内部的public类
Class<?>[] getDeclaredClasses() // 外部类，获取定义在该类内部的所有类
Class<?> getDeclaringClass() // 内部类，获取该类外部的类

// 接口和父类
Class<?>[] getInterfaces() // 获取该类实现的接口
Type[] getGenericInterfaces() // 获取接口的类型

Class<? super T> getSuperclass() // 父类
Type getGenericSuperclass() // 父类类型

// 注解
Annotation[] getAnnotations() // 获取类的所有注解
<A extends Annotation>A getAnnotation(Class<A> annotationClass) // 获取指定注解
Annotation[] getDeclaredAnnotations()
<A extends Annotation>A getDeclaredAnnotation(Class<A> annotationClass)

AnnotatedType[] getAnnotatedInterfaces()
AnnotatedType getAnnotatedSuperclass()
<A extends Annotation>A[] getAnnotationsByType(Class<A> annotationClass)
<A extends Annotation>A[] getDeclaredAnnotationsByType(Class<A> annotationClass)



Class<?> getEnclosingClass()
Constructor<?> getEnclosingConstructor()
Method getEnclosingMethod()


// 资源
URL getResource(String name)
InputStream getResourceAsStream(String name)


// 其他信息
int getModifiers() // 修饰符
Object[] getSigners() // 签名
T[] getEnumConstants() // 枚举类的常量对象
Package getPackage() // 包
ClassLoader getClassLoader() // 加载器
ProtectionDomain getProtectionDomain() // ProtectionDomain


// 数组
Class<?> getComponentType() // 数组，成员的Class类型
TypeVariable<Class<T>>[] getTypeParameters()


// 判断
boolean isAnnotation()
boolean isAnnotationPresent(Class<? extends Annotation> annotationClass)
boolean isArray()
boolean isEnum()
boolean isInstance(Object obj)
boolean isInterface()
boolean isLocalClass() // 是否局部内部类
boolean isMemberClass() // 是否成员内部类
boolean isAnonymousClass() // 是否匿名内部类
boolean isPrimitive()
boolean isSynthetic() // 合成类，由编译器引入的字段、方法、类或其他结构，主要用于JVM内部使用
boolean isAssignableFrom(Class<?> cls)



// other
<U> Class<? extends U> asSubclass(Class<U> clazz)
T cast(Object obj)
T newInstance()

boolean desiredAssertionStatus()

String getTypeName()

String toGenericString()
String toString()
```





