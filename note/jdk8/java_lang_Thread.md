java.lang.Thread

[TOC]

## 定义

```java
public class Thread implements Runnable
```

Thread实现了Runnable的run方法

```java
@Override
public void run() {
  if (target != null) {
    target.run();
  }
}
```

这只是说明Thread类有run方法，说明直接执行thread.run实际是执行Runnable的一个普通方法



那为什么要实现Runnable接口呢？

启动线程的两种方式：

```java
// 方式一
Runnable task = new Runnable();
Thread t = new Thread(task);
t.start();
// 方式二
class MyThread extends Thread {
  @Override run() {}
}
new MyThread().start()
```

JVM是执行的Thread的run方法，所以，方式一是执行target的run，方式二是执行Thread子类的run。

实现Runnable接口目的就是方便重写run方法。



## 构造

```java
private void init(@Nullable ThreadGroup g,  // 线程组 
                  Runnable target,          // 执行run方法的对象
                  @NotNull String name,     // 线程名称
                  long stackSize,           // 栈大小
                  @Nullable AccessControlContext acc,
                  boolean inheritThreadLocals)
```

栈大小，是虚拟机为线程分配的地址空间的大小，限制线程的递归深度。与平台相关，在某些平台上可能无效，JVM会自动忽略。

Thread类的所有构造方法都是基于这个方法。



## 状态

java.lang.Thread.State类，是public的



## ID和Num

```java
private long tid;
private static long threadSeqNumber;
private static synchronized long nextThreadID() {
  return ++threadSeqNumber;
}
tid = nextThreadID();

private static int threadInitNumber;
private static synchronized int nextThreadNum() {
  return threadInitNumber++;
}
```

tid：是线程的id

threadInitNumber：是给线程取名字用的，默认线程名字为："Thread-" + nextThreadNum()

【为啥tid是从10开始的？？？】



## 异常

线程由于未捕获异常而退出时，JVM会通过`getUncaughtExceptionHandler`获取`UncaughtExceptionHandler`，并调用`uncaughtException`方法。

捕获run方法中的异常

```java
Runnable task = () -> {
    int x = 1 / 0;
};
Thread t = new Thread(task);

Thread.UncaughtExceptionHandler ueh = (t1, e) -> {
    System.out.println("i know");
};
t.setUncaughtExceptionHandler(ueh);

t.start(); // 输出i know
```

getUncaughtExceptionHandler：如果没有设置uncaughtExceptionHandler，会返回group

```java
public UncaughtExceptionHandler getUncaughtExceptionHandler() {
	return uncaughtExceptionHandler != null ?
		uncaughtExceptionHandler : group;
}
```

所以，group一定是实现了Thread.UncaughtExceptionHandler，

```java
public
class ThreadGroup implements Thread.UncaughtExceptionHandler {
```

实现的方法：

```java
public void uncaughtException(Thread t, Throwable e) {
    if (parent != null) {
        parent.uncaughtException(t, e);
    } else {
        Thread.UncaughtExceptionHandler ueh =
            Thread.getDefaultUncaughtExceptionHandler();
        if (ueh != null) {
            ueh.uncaughtException(t, e);
        } else if (!(e instanceof ThreadDeath)) {
            System.err.print("Exception in thread \""
                                + t.getName() + "\" ");
            e.printStackTrace(System.err);
        }
    }
}
```

责任链模式：如果自己处理不了，就交给父处理器来处理。最终给默认处理器处理。



## 优先级

```java
MIN_PRIORITY = 1
NORM_PRIORITY = 5
MAX_PRIORITY = 10
```



## native

Thread.currentThread()：当前线程

Thread.yield()：线程让步，放弃当前线程执行机会，让出CPU，让下一个线程先执行（也有可能下一个是自己）



## sleep

```java
public static native void sleep(long millis) throws InterruptedException;
public static void sleep(long millis, int nanos) throws InterruptedException
```

静态方法，当前线程进入睡眠，线程进入`TIMED_WAITING`状态，线程不会放弃任何锁。

## start

只有NEW状态的线程可以start，线程执行结束了再次start，报IllegalThreadStateException

## 中断

有个中断状态字段，

```java
private volatile Interruptible blocker;
```

如果设置了中断状态（即blocker不是null），那么执行blocker的interrupt(thread)来中断线程。

```java
public void interrupt() {
    if (this != Thread.currentThread())
        checkAccess();

    synchronized (blockerLock) {
        Interruptible b = blocker;
        if (b != null) {
            interrupt0();           // Just to set the interrupt flag
            b.interrupt(this);
            return;
        }
    }
    interrupt0();
}
```

默认情况下，blocker==null，调用interrupt方法只会设置状态位。

线程处于wait/join/sleep，已经设置了blocker，此时调用interrupt方法会中断线程。



检测中断

```java
public static boolean interrupted() {
  return currentThread().isInterrupted(true);
}
public boolean isInterrupted() {
  return isInterrupted(false);
}
private native boolean isInterrupted(boolean ClearInterrupted);
```

