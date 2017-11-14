# wait，notify，notifyAll

## 方法

java.lang.Object

```java
public final native void wait() throws InterruptedException;
public final native void wait(long millis, int nanos) throws InterruptedException;
public final void wait(long millis) throws InterruptedException {
    wait(millis, 0);
}

public final native void notify();
public final native void notifyAll();

```

wait()：使调用该方法的线程释放锁，从运行状态退出，进入等待队列，直到被唤醒。

wait(long timeout)：等待一段时间是否有线程唤醒锁，如果没有，超时自动唤醒。

wait(long timeout, int nanos)：等待唤醒时间纳秒级别。

notify()：随机唤醒等待队列中的等待同一个锁的一个线程，使这个线程退出等待队列，进入可运行状态。

notifyAll()：唤醒所有等待同样锁的所有线程，从等待队列中退出，进入可运行状态。

## 注意点

1. 在调用wait或者notify之前，必须获得该对象的对象锁，即，只能在同步方法中调用；
2. 执行完wait之后释放对象锁，所以其他线程可以获得执行机会，才能唤醒；
3. 执行notify之后，不会立即退出让wait的线程执行，必须要先把同步块中的程序执行完，退出同步块，才会释放锁，让等待线程执行；
4. notify每次通知一个线程，多次调用通知线程数增加，可将wait线程全部唤醒。

## 原理

每个对象都有个monitor，初始是0，执行完synchronized值就是1。

wait/notify需要在获得monitor的线程中才可以执行。

所以，**wait/notify需要在synchronized中执行**。

其中，wait又会释放掉锁，破坏掉同步。

## 互斥和协同

Java语言的同步机制在底层实现上只有两种方式：互斥和协同。

互斥：即synchronized内置锁。

协同：即内置条件队列，wait/notify/notifyAll。

条件队列中是**处于等待状态的线程**，等待特定条件为真。每个Java对象都可以作为一个锁，同样每个Java对象都可以作为一个条件队列。通过wait/notify/notifyAll来操作条件队列。

> 可以理解为：有一个队列，o.wait()就push进去，o.notify()就pull出来。

要调用条件队列的任何一个方法，都必须要获得对象上的锁。

线程是用来工作的，不应该处于等待状态，处于等待状态的条件队列中的线程，一定是执行不下去的。

## 在while中等待

```java
while(condition is not true) {
  lock.wait()
}
```

解释：

在一般情况下，总应该调用notifyAll唤醒所有需要被唤醒的线程。可能会唤醒其他一些线程，但这不影响程序的正确性，这些线程醒来之后，会检查他们正在等待的条件（循环检测），如果发现条件不满足，就会继续等待



## 显示锁和显示条件队列

显示锁：Lock，对应内置锁synchronized

显示条件队列：Condition，对应内置条件队列，对应方法是await, signal, signalAll

## 问题

1. notifyAll唤醒所有线程，但不是所有线程都能执行，必须要等待对象锁被释放，获取锁之后才能执行。可以说，notifyAll让线程进入锁池。
2. ​