线程池 - ThreadPoolExecutor



加入线程顺序：corePoolSize - workQueue - maximumPoolSize - RejectedExecutionHandler





Executors工厂方法创建线程池：

固定容量的线程池：**newFixedThreadPool**

```java
public static ExecutorService newFixedThreadPool(int nThreads) {
    return new ThreadPoolExecutor(nThreads, nThreads,
                                  0L, TimeUnit.MILLISECONDS,
                                  new LinkedBlockingQueue<Runnable>());
}
```

corePoolSize和maximumPoolSize一样，workQueue为无界容量。线程池满之后会放入阻塞队列中，不会被拒绝。不存在



单线程线程池：**newSingleThreadExecutor**

```java
public static ExecutorService newSingleThreadExecutor() {
    return new FinalizableDelegatedExecutorService
        (new ThreadPoolExecutor(1, 1,
                                0L, TimeUnit.MILLISECONDS,
                                new LinkedBlockingQueue<Runnable>()));
}
```

一个线程，无界阻塞队列。



可缓存的线程池：**newCachedThreadPool**

```java
public static ExecutorService newCachedThreadPool() {
    return new ThreadPoolExecutor(0, Integer.MAX_VALUE,
                                  60L, TimeUnit.SECONDS,
                                  new SynchronousQueue<Runnable>());
}
```

每提交一个任务，都会创建一个线程来执行任务，无任务的线程持续空闲60秒之后销毁。

SynchronousQueue是一个<u>零容量</u>的BlockingQueue，生产者线程对其的插入(put)操作必须等待消费者的移除(take)操作完成，反过来也一样。



