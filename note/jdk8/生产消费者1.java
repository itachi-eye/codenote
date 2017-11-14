
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class Main {

    public static void main(String[] args) throws Exception {
        // write your code here

        List<Integer> taskQueue = new ArrayList<>();
        Producer producer = new Producer(taskQueue, 101);
        Consumer consumer = new Consumer(taskQueue, 100);
        new Thread(producer, "producer").start();
        new Thread(consumer, "consumer").start();
    }

}


class Producer implements Runnable {

    private final int MAX_CAPACITY = 5;

    private final List<Integer> taskQueue;
    private int produceTime;

    public Producer(List<Integer> taskQueue, int produceTime) {
        this.taskQueue = taskQueue;
        this.produceTime = produceTime;
    }

    private void produce(int task) throws InterruptedException {
        synchronized (taskQueue) {
            while (taskQueue.size() == MAX_CAPACITY) {
                System.out.println("Queue is full");
                taskQueue.wait();
            }
        }
        TimeUnit.MILLISECONDS.sleep(produceTime); // 生产过程释放锁
        synchronized (taskQueue) {
            taskQueue.add(task);
            System.out.println("Produced: " + task);
            taskQueue.notifyAll();
        }
    }

    @Override
    public void run() {
        int counter = 0;
        while (true) {
            try {
                produce(counter++);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class Consumer implements Runnable {

    private List<Integer> taskQueue;
    private int consumeTime;

    public Consumer(List<Integer> taskQueue, int consumeTime) {
        this.taskQueue = taskQueue;
        this.consumeTime = consumeTime;
    }

    private void consume() throws InterruptedException {
        synchronized (taskQueue) {
            while (taskQueue.size() == 0) {
                System.out.println("Queue is empty " + Thread.currentThread().getName() + " is waiting , size: " + taskQueue.size());
                taskQueue.wait();
            }
        }
        TimeUnit.MILLISECONDS.sleep(consumeTime);
        synchronized (taskQueue) {
            int task = taskQueue.remove(0);
            System.out.println("Consumed: " + task);
            taskQueue.notifyAll();
        }
    }

    @Override
    public void run() {
        while (true) {
            try {
                consume();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }
}