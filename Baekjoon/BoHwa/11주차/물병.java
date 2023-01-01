import java.util.Scanner;

public class Main {
		public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n, k, answer = 0;

		n = sc.nextInt();
		k = sc.nextInt();

		if (n <= k)
			System.out.println(0);

		else {
			while (true) {
				int count = 0;
				int copyN = n;
				while (copyN > 0) {
					if (copyN % 2 == 1) {
						count++;
					}
					copyN /= 2;
				}
				if (count <= k)
					break;
				answer++;
				n++;
			}
			System.out.println(answer);
		}

	}
}

