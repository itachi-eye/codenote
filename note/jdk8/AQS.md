AQS

[TOC]

## Node

java.util.concurrent.locks.AbstractQueuedSynchronizer.Node

```java
volatile int waitStatus;
```

节点状态字段，只能取5个值：1，-1，-2，-3，0。非负（即1）表示不需要被singal，只需要比较符号。默认情况下，初始为0，condition下为CONDITION。CAS修改。

SIGNAL = -1：该节点的后继节点正在或者即将被blocked（通过park），所以该节点必须在被release或者cancel之前unpark它的后继节点。为避免竞争，acquire方法需要首先假设有个signal节点，然后执行acquire方法。



head指针，节点没有线程，可以看做是头哨兵。



---

## acquire(int)

独占模式，获取资源，忽略中断

大致步骤：

1. 尝试获取资源。成功直接返回，失败进入2
2. 构造节点，包装线程，加入队尾
3. 不断重复：【尝试获取资源-找SIGNAL节点-等待-唤醒】，直到成功获取资源，返回
4. 等待过程不响应中断，在成功获取资源之后，如果@3检测到被中断过，此时自我中断，将中断补上。

```java
public final void acquire(int arg) {
    if (!tryAcquire(arg) &&
        acquireQueued(addWaiter(Node.EXCLUSIVE), arg))
        selfInterrupt();
}
```

tryAcquire是子类定义：

​	返回true，表示获取成功，直接返回；比如第一个线程调用lock，就直接获取到了，线程正常执行；

​	返回false，表示获取失败，入队；比如第二个之后的线程调用lock，就被阻塞了。

**addWaiter**

```java
private Node addWaiter(Node mode) {
    Node node = new Node(Thread.currentThread(), mode);
    // Try the fast path of enq; backup to full enq on failure
    Node pred = tail;
    if (pred != null) {
        node.prev = pred;
        if (compareAndSetTail(pred, node)) {
            pred.next = node;
            return node;
        }
    }
    enq(node);
    return node;
}
```

进入等待队列

如果，tail节点存在，且CAS设置node为新tail成功，则node正常入队。

否则，进去enq

**enq**

```java
private Node enq(final Node node) {
    for (;;) {
        Node t = tail;
        if (t == null) { // Must initialize
            if (compareAndSetHead(new Node())) // @1
                tail = head;
        } else {
            node.prev = t;
            if (compareAndSetTail(t, node)) { // @2
                t.next = node;
                return t;
            }
        }
    }
}
```

如果，等待队列中没有任何节点，比如第二个线程被阻塞，@1初始化了一个新节点（不包装线程），head和tail都指向这个节点，@2将node设置为新的tail，成功则返回，失败则重试。

也就是，head是一个哨兵节点，不包含实际线程，head的下一个节点才是队列的第一个真正节点。



线程入队后，就找个事给它做，或者让它等待。

**acquireQueued**

```java
final boolean acquireQueued(final Node node, int arg) {
    boolean failed = true;
    try {
        boolean interrupted = false;
        for (;;) {
            final Node p = node.predecessor();
            if (p == head && tryAcquire(arg)) { // @1
                setHead(node);
                p.next = null; 
                failed = false;
                return interrupted;
            }
            if (shouldParkAfterFailedAcquire(p, node) &&
                parkAndCheckInterrupt()) // 在这里阻塞，也在这里唤醒
                interrupted = true;
        }
    } finally {
        if (failed)
            cancelAcquire(node);
    }
}
```

```java
private void setHead(Node node) {
    head = node;
    node.thread = null;
    node.prev = null;
}
```

@1：只有@1一个出口。上面说了，head的后继是第一个等待节点，所以总是第一个等待节点满足p==head，所以，线程在@1条件处无法通过，不断在for循环中空转。

如果占用资源的线程释放资源(release)，就会unpark后继第一个节点，此时再执行@1，则可以通过，设置node为head，清除node的线程信息，作为头哨兵。



**shouldParkAfterFailedAcquire & parkAndCheckInterrupt**

```java
private static boolean shouldParkAfterFailedAcquire(Node pred, Node node) {
    int ws = pred.waitStatus;
    if (ws == Node.SIGNAL)
        return true; // 前驱是SIGNAL，可以安全park
    if (ws > 0) { 
        // 如果前驱放弃了等待 
        do {
            node.prev = pred = pred.prev;
        } while (pred.waitStatus > 0); // 一直往前找上一个没有放弃的节点
        pred.next = node;
    } else {
        // 前驱没有放弃，把前驱等待状态设为SIGNAL
        compareAndSetWaitStatus(pred, ws, Node.SIGNAL); 
    }
    return false; // 不能安全park，退出进入外部循环
}
```

```java
private final boolean parkAndCheckInterrupt() {
    LockSupport.park(this);
    return Thread.interrupted();
}
```

线程park之后，进入阻塞，只有unpark和中断可以唤醒。



## release(int)

独占模式，释放资源。

1. tryRelease()释放资源，如果释放成功（state==0），则返回true，进入2；否则false，方法退出
2. 唤醒等待队列中head节点后面第一个有效节点。

```java
public final boolean release(int arg) {
    if (tryRelease(arg)) { // 释放资源，完全释放才返回true
        Node h = head;
        if (h != null && h.waitStatus != 0)
            unparkSuccessor(h); // 唤醒head的下一个线程，也就是第一个有效线程
        return true;
    }
    return false;
}
```

tryRelease是待实现的方法，根据这个方法的返回值来判断是否完成释放资源。如果彻底释放，state=0，就会唤醒等待队列中的下一个等待线程。

```java
private void unparkSuccessor(Node node) {
    /*
     * node为当前节点，释放node后面第一个仍在等待的线程
     */
    int ws = node.waitStatus;
    if (ws < 0)
        compareAndSetWaitStatus(node, ws, 0); // 置node状态为0

    Node s = node.next;
    if (s == null || s.waitStatus > 0) {
        s = null;
        // 反向找最前面那个还有效的节点
        for (Node t = tail; t != null && t != node; t = t.prev)
            if (t.waitStatus <= 0)
                s = t;
    }
    if (s != null)
        LockSupport.unpark(s.thread); // 唤醒后继线程
}
```



## acquireInterruptibly(int)

独占模式，能响应中断的获取资源。

```java
public final void acquireInterruptibly(int arg)
        throws InterruptedException {
    if (Thread.interrupted()) // 获取资源之前判断是否被中断
        throw new InterruptedException();
    if (!tryAcquire(arg))
        doAcquireInterruptibly(arg); // 获取资源失败，等待状态可被中断
}
```

在获取资源之前，首先执行Thread.interrupted()，判断线程是否被中断。

与acquireQueued代码基本相同

```java
private void doAcquireInterruptibly(int arg)
    throws InterruptedException {
    final Node node = addWaiter(Node.EXCLUSIVE); // 入队
    boolean failed = true;
    try {
        for (;;) {
            final Node p = node.predecessor();
            if (p == head && tryAcquire(arg)) {
                setHead(node);
                p.next = null; // help GC
                failed = false;
                return;
            }
            if (shouldParkAfterFailedAcquire(p, node) &&
                parkAndCheckInterrupt())
                throw new InterruptedException(); // 不同
        }
    } finally {
        if (failed)
            cancelAcquire(node);
    }
}
```

不同之处是，在线程被park处于等待态，然后被unpark或者interrupt唤醒或中断之后，抛出一个InterruptedException，然后执行cancelAcquire。

cancelAcquire的过程：

1. node的thread属性置null，waitStatus置CANCELLED
2. 如果node的前一个节点也是CANCELLED，一起处理了




---



## acquireShared(int)

共享模式，获取资源，成功则返回，失败则进入等待队列，直到获取资源为止。

忽略中断。

```java
public final void acquireShared(int arg) {
    if (tryAcquireShared(arg) < 0)
        doAcquireShared(arg);
}
```

tryAcquireShared：获取资源，返回值

<0：获取失败

=0：获取成功，但是没有剩余的

\>0：获取成功，还有剩余

获取失败后通过doAcquireShared进入等待队列。

```java
private void doAcquireShared(int arg) {
    final Node node = addWaiter(Node.SHARED); // 入队
    boolean failed = true;
    try {
        boolean interrupted = false;
        for (;;) {
            final Node p = node.predecessor(); // 前驱
            if (p == head) { // node是第二个节点
                int r = tryAcquireShared(arg); // 尝试获取资源 @1
                if (r >= 0) {  // 获取到了
                    // 更新head，剩余资源可唤醒后面的线程
                    setHeadAndPropagate(node, r);
                    p.next = null; 
                    if (interrupted) // 如果等待过程中被中断，此时将中断补上
                        selfInterrupt(); 
                    failed = false;
                    return;
                }
            }
            // 获取不到资源，park
            if (shouldParkAfterFailedAcquire(p, node) &&
                parkAndCheckInterrupt()) // 在这里阻塞，也在这里唤醒
                interrupted = true;
        }
    } finally {
        if (failed)
            cancelAcquire(node);
    }
}
```

```java
private void setHeadAndPropagate(Node node, int propagate) {
    Node h = head; // Record old head for check below
    setHead(node);
    /*
     * 传播，如果还有剩余的资源，尝试继续唤醒后面的
     */
    if (propagate > 0 || h == null || h.waitStatus < 0 ||
        (h = head) == null || h.waitStatus < 0) {
        Node s = node.next;
        if (s == null || s.isShared())
            doReleaseShared();
    }
}
```

@1：按照顺序获取资源，如果一个节点获取大量资源阻碍后面小资源获取，那么将一直阻塞。





## releaseShared(int)

共享模式，释放资源。唤醒后继，并让资源量传播下去。

```java
public final boolean releaseShared(int arg) {
    if (tryReleaseShared(arg)) {
        doReleaseShared();
        return true;
    }
    return false;
}
```

tryReleaseShared，尝试释放资源，

​	返回true，释放成功，则执行doReleaseShared

​	返回false，释放失败，则直接退出返回false



tryReleaseShared由子类实现。



**doReleaseShared**

共享模式，释放资源。通知后继节点，并确保资源能够传播下去。

```java
private void doReleaseShared() {
    for (;;) {
        Node h = head;
        if (h != null && h != tail) {
            int ws = h.waitStatus;
            if (ws == Node.SIGNAL) {
                if (!compareAndSetWaitStatus(h, Node.SIGNAL, 0))
                    continue;            // loop to recheck cases
                unparkSuccessor(h); // 唤醒后继
            }
            else if (ws == 0 &&
                     !compareAndSetWaitStatus(h, 0, Node.PROPAGATE))
                continue;                // loop on failed CAS
        }
        if (h == head)                   // loop if head changed
            break;
    }
}
```





e.g

共享资源数为10，六个线程，分别需要资源2，8，1，2，3，5

| 执行情况       | 剩余资源    | 等待队列             | 备注          |
| ---------- | ------- | ---------------- | ----------- |
| t1开始       | 8       |                  |             |
| t2开始       | 0       |                  |             |
| t3开始       | 0       | head->t3         |             |
| t1结束       | 0->2->1 | head             | 唤醒t3，获取1个资源 |
| t4,t5,t6开始 | 1       | head->t4->t5->t6 |             |
| t2结束       | 9->7->4 | head->t6         | 唤醒t4，t4唤醒t5 |











