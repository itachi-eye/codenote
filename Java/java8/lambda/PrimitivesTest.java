package lambda;

import java.util.Arrays;
import java.util.List;
import java.util.LongSummaryStatistics;
import java.util.Optional;
import java.util.function.ToLongFunction;

/**
 * 基本类型的lambda
 *
 */
public class PrimitivesTest {

	public static void main(String[] args) {

	}

	public static void func4() {
		Optional<String> ao = Optional.of("abc");
		System.out.println(ao.isPresent()); // true
		
		ao.ifPresent(o -> System.out.println(o.toUpperCase())); // ABC
	}

	public static void func3() {
		List<String> lStrings = Arrays.asList("12345", "3456", "5678", "3456");
		String r =  lStrings.stream()
						.reduce((s1, s2) -> s1 + s2)
						.get();
		System.out.println(r);
	}

	public static void func2() {
		List<String> lStrings = Arrays.asList("12345", "3456", "5678", "3456");
		LongSummaryStatistics statistics = 
				lStrings.stream()
					.mapToLong(s -> Long.valueOf(s).longValue())
					.summaryStatistics();
		System.out.println(statistics.getSum());
	}

	public static void func1() {
		String lo = "12345";
		System.out.println(Long.valueOf(lo).longValue());
		
		ToLongFunction<String> tl = s -> Long.valueOf(s).longValue();
		long r = tl.applyAsLong("123456789");
		System.out.println(r);
	}

}
