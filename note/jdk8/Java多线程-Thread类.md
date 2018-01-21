# Thread

## thread.join()

用法：

```java
// 当前线程t1
try {
  t2.join(); // t2进来，先执行t2
} catch (InterruptedException e) {
}
```

执行顺序：t1 — t2 — t1

源码：

```java
public final synchronized void join(long millis)
throws InterruptedException {
    long base = System.currentTimeMillis();
    long now = 0;

    if (millis == 0) {
        while (isAlive()) {
            wait(0);
        }
    } else {
        while (isAlive()) {
            long delay = millis - now;
            if (delay <= 0) {
                break;
            }
            wait(delay);
            now = System.currentTimeMillis() - base;
        }
    }
}
```

注意：

在t1中调用t2.join()，锁对象是t2，调用线程是t1，所以wait的是t1。

## Thread.yield()

使当前线程从执行状态（运行状态）变为可执行态（就绪状态），让出CPU。

## Thread.sleep()



## 线程中断

thread.interrupt()，中断线程，设置线程的中断状态位，为true

线程之后是停止，等待还是继续运行取决于程序本身。

线程会不时的检查这个状态位，判断线程是否应该被中断

```java
// 静态方法，判断当前是否被中断，并且清除中断位
public static boolean interrupted() {
    return currentThread().isInterrupted(true);
}

// 判断是否被中断
public boolean isInterrupted() {
    return isInterrupted(false);
}

private native boolean isInterrupted(boolean ClearInterrupted);
```

1 使用中断标志中断非阻塞状态的线程

2 使用thread.interrupt()中断非阻塞状态的线程

3 使用thread.interrupt()中断阻塞状态的线程

​	在sleep，wait，join等阻塞线程的地方，抛出一个InterruptedException，同时清除中断标志位。

4 死锁状态线程无法被中断

5 中断io操作：socker，channels，抛出异常



