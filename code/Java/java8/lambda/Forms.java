package lambda;

import java.util.Arrays;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.function.Predicate;

public class Forms {

	public static void main(String[] args) {

		form8();
	}

	public static void form1() {
		Runnable runnable = new Runnable() {
			@Override
			public void run() {
				System.out.println("runnable");
			}
		};

		Runnable runnable2 = () -> System.out.println("runnable2");

		ExecutorService service = Executors.newCachedThreadPool();
		service.execute(runnable);
		service.execute(runnable2);
		service.shutdown();
	}

	public static void form2() {
		Human human = () -> System.out.println("man run");
		human.run(); // output: man run
	}

	public static void form3() {
		Man man1 = new Man("zhangsan", 12) {
			@Override
			public void run() {
				System.out.println(getName() + " run");
			}
		};
		man1.run();
		System.out.println(man1.toString());

		// 无法使用lambda来构造对象
	}

	public static void form4() {
		BinaryOperator<Integer> add = (x, y) -> x + y;
		int r = add.apply(1, 3);
		System.out.println(r); // 4

		BinaryOperator<Integer> max = (x, y) -> x > y ? x : y;
		r = max.apply(1, 3);
		System.out.println(r);

		BinaryOperator<Long> gcd = (Long x, Long y) -> {
			long t = 0l;
			if (x < y) {
				t = x;
				x = y;
				y = t;
			}
			t = x % y;
			while (t != 0) {
				x = y;
				y = t;
				t = x % y;
			}
			return y;
		};
		long r2 = gcd.apply(100L, 128L);
		System.out.println(r2);
	}

	public static void form5() {
		Predicate<Integer> gt5 = new Predicate<Integer>() {
			@Override
			public boolean test(Integer t) {
				return t > 5;
			}
		};
		Predicate<Integer> lt9 = new Predicate<Integer>() {
			@Override
			public boolean test(Integer t) {
				return t < 9;
			}
		};
		Predicate<Integer> at = gt5.and(lt9);

		for (int i = 0; i < 12; i++) {
			System.out.println(i + " " + at.test(i));
		}
	}

	public static void form6() {
		Predicate<Integer> gt5 = x -> x > 5;
		Predicate<Integer> at = gt5.and(x -> x < 9);
		
		for (int i = 0; i < 12; i++) {
			System.out.println(i + " " + at.test(i));
		}
	}
	
	public static void form7() {
		Predicate<String> p = String::isEmpty;
		for (String str : Arrays.asList("", "aa", "bb")) {
			System.out.println(p.test(str));
		}
	}
	
	public static void form8() {
		Function<String, Integer> calc = x -> Integer.valueOf(x) + 1;
		Integer r = calc.andThen(x -> x * 2 - 1)
			.andThen(x -> x - 5)
			.apply("5").intValue();
		System.out.println(r);
	}

}

class MyRunnable implements Runnable {

	private int limit;

	public MyRunnable(int limit) {
		this.limit = limit;
	}

	@Override
	public void run() {
		for (int i = 0; i < limit; i++) {
			System.out.println(i);
		}
	}

}

interface Human {
	void run();
}

abstract class Man implements Human {
	private String name;
	private int age;

	public Man(String name, int age) {
		this.name = name;
		this.age = age;
	}

	public String getName() {
		return name;
	}

	@Override
	public String toString() {
		return "Man [name=" + name + ", age=" + age + "]";
	}

}