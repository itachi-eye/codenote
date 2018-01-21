LockSupport

提供基本的阻塞源语。用于创建锁和其他同步器。

```java
public static void unpark(Thread thread);
public static void park();
public static void parkNanos(long nanos);
public static void parkUntil(long deadline);
```

park：使用许可证，没有的话就阻塞

unpark：给某个线程派发一个许可证。



unpark可以在park之前给线程分配一个许可。多次分配，只有一个。不可重复使用。



park阻塞的线程，unpark唤醒，且能响应中断，但不抛出异常。