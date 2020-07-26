import java.util.Scanner;

public class SWEA_2072_홀수만더하기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			int sum = 0;
			for(int j=0; j<10; j++) {
				int num = sc.nextInt();
				if(num%2 != 0)
					sum = sum + num;
			}
			System.out.println("#" + test_case + " " + sum);
		}
	}
}
