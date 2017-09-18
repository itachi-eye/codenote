# primitive type wrapper



- Object
  - Boolean
  - Character
  - Number
    - Byte
    - Short
    - Integer
    - Long
    - Float
    - Double


---



## Boolean

包装值

```java
private final boolean value;
```

valueOf(String) : equalsIgnoreCase

hashCode(): value ? 1231 : 1237

compare: true > false

logicAnd, logicOr, logicXor: 1.8



## Character





---



## Integer



> Integer.toString(i)

radix=10, 空间换时间+位操作

```java
q = (i * 52429) >>> (16+3); // q = i/10
r = i - ((q << 3) + (q << 1));  // r = i-(q*10)
```

radix!=10

```java
r = i % radix
i = i / radix
```



> Integer.toBinaryString(i)
>
> Integer.toOctalString(i)
>
> Integer.toHexString(i)

```java
toUnsignedString0(val, shift)
radix = 1<<shift
mask = raidx - 1
do
  buf[--pos] = digits[val & mask]
  val >>>= shift
while val > 0
```





string->integer





---

## Float

String->float

```java
valueOf(String)
parseFloat(String)
```

流程图：

```flow
st=>start: Start
e=>end: End
op1=>operation: trim()
sign_cond=>operation: charAt(0)
sign_sub=>operation: sub
sign_plus=>operation: plus

st->op1->sign_cond
sign_cond->sign_sub
sign_cond->sign_plus

```





float-> string

