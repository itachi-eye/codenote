java.util.concurrent.CountDownLatch

计数器，倒计数

## 使用

首先，在构造函数中传入一个初始计数值；

**等待线程**，使用await()，使自己进入等待状态，直到计数器减到0或者被中断，才能被唤醒；

**工作线程**，完成自己的工作后，使用countDown()使计数减1



Demo：
运动员赛跑，先准备，等待裁判吹哨，开跑，所有人都跑到终点，比赛结束。

两个Latch：

一个是裁判用的倒计数器，所有人准备好后await，等待裁判吹哨。

一个是赛场用的倒计数器，运动员到一个减一个数，所有人都到了，比赛结束。

运动员类：

```java
class Player implements Runnable {

    private CountDownLatch beginLatch;
    private CountDownLatch finishLatch;

    Player(CountDownLatch beginLatch, CountDownLatch finishLatch) {
        this.beginLatch = beginLatch;
        this.finishLatch = finishLatch;
    }

    @Override
    public void run() {
        String name = Thread.currentThread().getName();
        Random random = new Random();
        try {
            System.out.println(name + " ready");
            beginLatch.await(); // 准备，等待吹哨
            
            System.out.println(name + " run");
            Thread.sleep(random.nextInt(100) + 1000); // 比赛耗时
            System.out.println(name + " finish");
            
            finishLatch.countDown(); // 跑到终点，计数减1
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

主函数：

```java
public static void main(String[] args) throws Exception {
    // write your code here

    final int N = 10;
    CountDownLatch beginLatch = new CountDownLatch(3); // 倒数3个数
    CountDownLatch finishLatch = new CountDownLatch(N);

    // 创建运动员线程并start
    for (int i = 0; i < N; i++) {
        new Thread(new Player(beginLatch, finishLatch)).start();
    }

    Thread.sleep(2000); // 准备时间

    beginLatch.countDown(); // 3
    beginLatch.countDown(); // 2
    beginLatch.countDown(); // 1
    System.out.println("race begin");

    finishLatch.await(); // 等待所有人到达终点
    System.out.println("all finish");

}
```



Demo2：

```java
final int N = 3;
CountDownLatch latch = new CountDownLatch(N);
for (int i = 0; i < N; i++) {
    new Thread(()-> {
        try {
            Thread.sleep(1000);
            latch.countDown(); // 工作线程在这里减1
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }).start();
}

latch.await(); // 主线程在这里等待
System.out.println("end");
```



## 源码

构造函数

```java
public CountDownLatch(int count) {
    if (count < 0) throw new IllegalArgumentException("count < 0");
    this.sync = new Sync(count);
}
```

初始化内部类，自定义线程同步类，继承自AQS

```java
class Sync extends AbstractQueuedSynchronizer
```

```Java
Sync(int count) {
    setState(count);
}
```

初始化资源state为给定的一个值，一般跟同步线程数一致。





**await**

使线程进入等待队列，即调用await的线程，等待资源为0。

```java
public void await() throws InterruptedException {
    sync.acquireSharedInterruptibly(1); // 这个1没有使用
}
```

AQS：

```java
public final void acquireSharedInterruptibly(int arg)
        throws InterruptedException {
    if (Thread.interrupted())
        throw new InterruptedException();
    if (tryAcquireShared(arg) < 0)
        doAcquireSharedInterruptibly(arg);
}
```

CountDownLatch#Sync#tryReleaseShared：

```java
protected int tryAcquireShared(int acquires) {
    return (getState() == 0) ? 1 : -1;
}
```

tryAcquireShared在AQS里的语义是：

返回 < 0：没有资源，进入等待队列

返回 = 0：获取成功，但没有剩余资源

返回 > 0：获取资源成功

在CountDownLatch中，state初始为N>0，等待线程调用await，tryAcquireShared返回-1，线程进入等待队列。



doAcquireSharedInterruptibly：进入队列，等待，检查条件，唤醒。





**countDown**

计数器减1，如果减到0则释放所有await的线程。

```java
public void countDown() {
    sync.releaseShared(1);
}
```

AQS：

```java
public final boolean releaseShared(int arg) {
    if (tryReleaseShared(arg)) { // 尝试释放资源
        doReleaseShared(); // state=0，唤醒后继节点
        return true;
    }
    return false; // 释放资源失败
}
```

CountDownLatch#Sync#tryReleaseShared：

```java
protected boolean tryReleaseShared(int releases) {
    for (;;) {
        int c = getState();
        if (c == 0)
            return false; // 资源为0，释放失败
        int nextc = c-1;
        if (compareAndSetState(c, nextc))
            return nextc == 0; // @1
    }
}
```

tryReleaseShared()只在next==0的情况返回true，其他情况都返回false。也就是，只在state=0的情况下，才会doReleaseShared()唤醒第一个等待线程。



第一个等待线程被unpark之后，检查条件

```java
final Node p = node.predecessor();
if (p == head) {
    int r = tryAcquireShared(arg);
    if (r >= 0) {
        setHeadAndPropagate(node, r); // @1 doReleaseShared()
        p.next = null; 
        failed = false;
        return;
    }
}
```

```java
protected int tryAcquireShared(int acquires) {
    return (getState() == 0) ? 1 : -1;
}
```

因为state被减为0，所以条件一直满足到@1，第一个线程启动，同时传播资源，唤醒后面的线程，doReleaseShared()。

等待队列中的所有线程都满足条件，并且一个接一个传播唤醒，所有等待线程都会重新开始执行。



----



调用await进行等待的为A类线程，调用countDown的为B类线程，

初始，设置state=N，countDown一次state减1，





