# Character

## 术语

- 代码点 (code point)：指在Unicode编码表中一个字符所对应的代码值。如汉字“一”的代码点是U+4E00，英文字母“A”的代码点是U+0041。
- 代码单元( code unit)：规定16bits的存储容量就是一个代码单元。



 [Java中的char类型和Unicode编码](http://blog.csdn.net/fhx19900918/article/details/8135019)



> 用计算机表示一个字符分两步：
>
> 1、字符=>用一个数字表示（Unicode）
>
> 2、将这个数字存起来（UTF-8，UTF-16等）



**Java中char是2字节=16位，因此在Java程序内部使用UTF-16编码存储，用一个或者两个16位来表示字符**



代码平面

![代码平面](http://img.blog.csdn.net/20140825134623312?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvenhob28=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

BMP划分

![BMP](http://img.blog.csdn.net/20140825164706298?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvenhob28=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



[图说我对Unicode的几点理解](http://blog.csdn.net/zxhoo/article/details/38819517)





## API



1、0-127缓存，valueOf()走缓存

```java
Character a = 'a';
Character b = Character.valueOf('a');
a == b // true

Character a = '\u1234';
Character b = Character.valueOf('\u1234');
a == b // false
```

2、hashCode()，返回char的int值

3、代码点

```java
isValidCodePoint(int codePoint)
isBmpCodePoint(int codePoint)
isSupplementaryCodePoint(int codePoint)
static int	codePointAt(char[] a, int index)
static int	codePointAt(char[] a, int index, int limit)
static int	codePointAt(CharSequence seq, int index)
static int	codePointBefore(char[] a, int index)
static int	codePointBefore(char[] a, int index, int start)
static int	codePointBefore(CharSequence seq, int index)
static int	codePointCount(char[] a, int offset, int count)
static int	codePointCount(CharSequence seq, int beginIndex, int endIndex)
```

eg：

```java
String s = "a李𝕫";
s.length() // 4
Character.codePointCount(s, 0, s.length()) // 3
Character.codePointAt(s, 0) // 97=0x61
Character.codePointAt(s, 1) // 26446=0x674e
Character.codePointAt(s, 2) // 120171=0x1d56b
```





4、替代区域

```java
isHighSurrogate(char ch)
isLowSurrogate(char ch)
isSurrogate(char ch)
isSurrogatePair(char high, char low)
public static char highSurrogate(int codePoint)
public static char lowSurrogate(int codePoint)
```

5、替代值 => 代码点

```java
static int toCodePoint(char high, char low)
```

6、代码点 => UTF-16

```java
static char[] toChars(int codePoint)
static int toChars(int codePoint, char[] dst, int dstIndex)
```



判断字符是否是汉字：

```java
//使用UnicodeScript方法判断
public boolean isChineseByScript(char c) {
    Character.UnicodeScript sc = Character.UnicodeScript.of(c);
    if (sc == Character.UnicodeScript.HAN) {
        return true;
    }
    return false;
}
```

