package lambda;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class CollectionStream {

	public static void main(String[] args) {

		func5();
	}

	public static void func5() {
		Integer r = Stream.of(1, -2, 3, -4)
			.max(Comparator.comparing(x -> Math.abs(x)))
			.get();
		System.out.println(r); // -4
	}

	public static void func4() {
		Integer r = Stream.of(1, 2, 3, 4)
			.reduce((x, y) -> x + y)
			.get();
		System.out.println(r);
	}
	
	// flatMap: T => Stream<R>
	public static void func3() {
		List<Integer> list1 = Arrays.asList(1, 2);
		List<Integer> list2 = Arrays.asList(3, 4);
		List<Integer> to = Stream.of(list1, list2)
			.flatMap(ls -> ls.stream())
			.collect(Collectors.toList());
		System.out.println(to); // [1, 2, 3, 4]
	}

	// map: T => R
	public static void func2() {
		List<String> strList = Stream.of("a", "b", "c")
				.map(s -> s.toUpperCase())
				.collect(Collectors.toList());
		System.out.println(strList);// [A, B, C]
	}

	static void fun1() {
		List<String> strList = Arrays.asList("aaa", "bbb", "ccc", "abc", "cdef");
		System.out.println(strList);

		long cnt = strList.stream()
					.filter(s -> s.startsWith("a"))
					.count();
		System.out.println(cnt);// 2
	}
}
