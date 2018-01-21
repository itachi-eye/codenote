## Executor#submit(Runnable)的执行过程



```java
public interface Executor {
    void execute(Runnable command);
}
```

```java
public interface ExecutorService extends Executor {
    // shutdown
    // terminate
  
    // submit
    <T> Future<T> submit(Callable<T> task);
    <T> Future<T> submit(Runnable task, T result);
    Future<?> submit(Runnable task);
  
    // invokeAll
    // invokeAny
}
```

submit

Callable/Runnable --> FutureTask --> execute(ftask)

eg.

```java
Future<?> f1 = service.submit(()->{
    // Runnable run
});
System.out.println(f1.get()); // null
```

```java
Future<String> f2 = service.submit(()->{
    // Runnable run
}, "bb");
System.out.println(f2.get()); // bb
```

```java
Future<String> f3 = service.submit(()-> {
    // Callable call
    return "cc";
});
System.out.println(f3.get()); // cc
```

AbstractExecutorService#execute()方法：

```java
public <T> Future<T> submit(Callable<T> task) {
    if (task == null) throw new NullPointerException();
    RunnableFuture<T> ftask = newTaskFor(task); // @1
    execute(ftask); // @2
    return ftask;
}
```

@1：Runnable/Callable最终被包装到FutureTask对象中

@2：Executor#execute()执行FutureTask对象，Executor是接口，子类（如ThreadPoolExecutor）来实现，最后将ftask返回了，可以用ftask.get()获取结果。

---



FutureTask

```Java
Runnable, Future<V>
  -
  RunnableFuture<V>
  	-
    FutureTask<V>
```

FutureTask可以被execute(Runnable)执行run()方法，也可以直接执行run()方法。

Runnable最终被转为FutureTask中的callable属性。

```java
private Callable<V> callable;
private Object outcome;
private volatile Thread runner;

public FutureTask(Callable<V> callable) {
    if (callable == null)
        throw new NullPointerException();
    this.callable = callable;
    this.state = NEW;       // ensure visibility of callable
}
```



---

线程池执行情况

ThreadPoolExecutor#execute(Runnable)

```java
public void execute(Runnable command) {
    if (command == null)
        throw new NullPointerException();
    int c = ctl.get();
    if (workerCountOf(c) < corePoolSize) {
        if (addWorker(command, true)) // 将任务放入池中，并执行
            return;
        c = ctl.get();
    }
    if (isRunning(c) && workQueue.offer(command)) { // 将任务放入队列中
        int recheck = ctl.get();
        if (! isRunning(recheck) && remove(command))
            reject(command);
        else if (workerCountOf(recheck) == 0)
            addWorker(null, false); // 池中
    }
    else if (!addWorker(command, false))
        reject(command); // 拒绝
}
```

简化的addWorker(Runnable, boolean)

```java
private boolean addWorker(Runnable firstTask, boolean core) {
    
    boolean workerStarted = false;
    boolean workerAdded = false;
    Worker w = null;
    try {
        w = new Worker(firstTask); // 创建工作线程
        final Thread t = w.thread; // 工作线程
        if (t != null) {
            final ReentrantLock mainLock = this.mainLock;
            mainLock.lock(); // workers是set，非线程安全
            try {
                workers.add(w); // 加入池中
                workerAdded = true;
            } finally {
                mainLock.unlock();
            }
            if (workerAdded) {
                t.start(); // 启动新线程，执行Worker对象的run方法
                workerStarted = true;
            }
        }
    } finally {
        if (! workerStarted)
            addWorkerFailed(w);
    }
    return workerStarted;
}
```

创建工作线程代码：Worker是线程池中的工作者，应该与具体的任务分离。

```java
Worker(Runnable firstTask) {
    setState(-1); // inhibit interrupts until runWorker
    this.firstTask = firstTask;
    this.thread = getThreadFactory().newThread(this);
}
```

Worker自身是Runnable，创建的thread的参数Runnable是Worker对象，线程启动执行run方法

```java
public void run() {
    runWorker(this);
}
```

runWorker(Worker)代码

```java
final void runWorker(Worker w) {
    Thread wt = Thread.currentThread();
    Runnable task = w.firstTask; // 真正要执行的任务
    w.firstTask = null;
    w.unlock(); // allow interrupts
    try {
        // 创建时，task不是null，执行；task是null，从队列中取
        while (task != null || (task = getTask()) != null) {
            w.lock();
            try {
              
                task.run(); // 执行真正要执行的任务
                
            } finally {
                task = null;
                w.unlock();
            }
        }
    } finally {
        processWorkerExit(w, completedAbruptly); // Worker被清理，如空闲时间过长
    }
}
```

最终，通过ExecutorService#submit(Runnable)的任务，在新线程中调用run方法得到执行。



FutureTask.run()方法

```java
public void run() {
    try {
        Callable<V> c = callable;
        if (c != null && state == NEW) {
            V result;
            boolean ran;
            try {
                result = c.call(); // 执行
                ran = true;
            } catch (Throwable ex) {
                result = null;
                ran = false;
            }
            if (ran)
                set(result); // 执行结束之后，设置result
        }
    } finally {
        
    }
}
```

run方法实际执行的call



getTask()，从阻塞队列中获取任务

```java
private Runnable getTask() {
    boolean timedOut = false; // Did the last poll() time out?

    for (;;) {
        int c = ctl.get();
        int rs = runStateOf(c);

        // Check if queue empty only if necessary.
        if (rs >= SHUTDOWN && (rs >= STOP || workQueue.isEmpty())) {
            decrementWorkerCount();
            return null;
        }

        int wc = workerCountOf(c);

        // 是否需要减少Worker的数量，允许减少core数量或者Worker数量大于core数量
        boolean timed = allowCoreThreadTimeOut || wc > corePoolSize;

        if ((wc > maximumPoolSize || (timed && timedOut)) // @1
            && (wc > 1 || workQueue.isEmpty())) {
            if (compareAndDecrementWorkerCount(c)) // @1.1
                return null;
            continue;
        }

        try {
            Runnable r = timed ?
                workQueue.poll(keepAliveTime, TimeUnit.NANOSECONDS) : // @2
                workQueue.take(); // @3
            if (r != null)
                return r;
            timedOut = true;
        } catch (InterruptedException retry) {
            timedOut = false;
        }
    }
}
```

@1：减少Worker数量的条件，

1）Worker数大于max，或者，Worker数量大于core容量且取任务超时（即任务队列没有任务时间超过阈值，即Worker空闲时间超过阈值）

2）Worker至少有1个，或者任务队列为空

条件1和条件2同时满足，则减少一个Worker



@2：获取任务，等待keepAliveTime，如果这段时间取不到，则说明该Worker空闲了这么久

@3：Worker数量不大于core数量，直接获取任务，获取不到就阻塞。



---

主线程调用

FutureTask.get()

```java
public V get() throws InterruptedException, ExecutionException {
    int s = state;
    if (s <= COMPLETING) // 未结束
        s = awaitDone(false, 0L); // 等待结束
    return report(s);
}
```

主线程等待工作线程结束

```java
private int awaitDone(boolean timed, long nanos)
    throws InterruptedException {
    final long deadline = timed ? System.nanoTime() + nanos : 0L;
    WaitNode q = null;
    boolean queued = false;
    for (;;) { // 主线程循环等待工作线程执行结束，返回结果

        int s = state;
        if (s > COMPLETING) {
            return s; // 已完成，返回
        }
        else if (s == COMPLETING) // 进行中，
            Thread.yield(); // 主线程让步
        else if (q == null)
            q = new WaitNode();
        else if (!queued)
            queued = UNSAFE.compareAndSwapObject(this, waitersOffset,
                                                 q.next = waiters, q);
        else if (timed) {
            nanos = deadline - System.nanoTime();
            if (nanos <= 0L) {
                removeWaiter(q);
                return state;
            }
            LockSupport.parkNanos(this, nanos); // 主线程等待一定时间
        }
        else
            LockSupport.park(this); // 主线程等待
    }
}
```



---



总结：

1. Runnable/Callable被包装到FutureTask对象中
2. Executor#execute()方法执行FutureTask对象
3. 线程池中的Worker启动新线程，执行run方法，实际执行runWorker()
4. runWorker()执行FutureTask对象（新建时），或者从任务队列中取出一个任务，执行run方法
5. FutureTask对象的run()方法执行call()方法，真正执行任务，得到结果（可能需要很久）
6. 主线程调用get()，如果工作线程还没结束，则awaitDone()，主线程等待。

