# java.util.concurrent.Lock&Condition

Lock接口

1、获取锁，获取不到就等待；手动释放。

```java
void lock();
void unlock();
```

2、尝试获取锁，能成功获取就获取，返回true，不能获取就返回false。总是立即返回。

```java
boolean tryLock();
```

3、尝试获取锁，能成功获取就获取，返回true，不能获取就等待一段时间，如果等待过程获取到了，就返回true，如果超时了还没获取到，就返回false

```java
boolean tryLock(long time, TimeUnit unit) throws InterruptedException;
```

4、能够响应中断的获取锁，如果成功就获取，如果不能获取就等待，等待过程可以响应中断。

```java
void lockInterruptibly() throws InterruptedException;
```

5、condition

```java
Condition newCondition();
```



 典型应用

```java
Lock lock = new ReentrantLock();
Condition saveCondition = lock.newCondition();
Condition drawCondition = lock.newCondition();
```





Lock实现是syn queue：双向链表

Condition是condition queue：单向链表



