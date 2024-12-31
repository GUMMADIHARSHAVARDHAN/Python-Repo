import java.util.*;

public class Nig {
        static int prime(int n) {
        if (n <= 1) {
            return 0; 
        }
        int c = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                c++;
            }
        }
        if (c == 2) {
            return 1; 
        } else {
            return 0; 
        }
    }

    public static void main(String[] args) {
        Scanner r = new Scanner(System.in);
        int a = r.nextInt();
        int b = r.nextInt();
        for (int i = a; i <= b; i++) {
            if (prime(i) == 1) {
                System.out.println(i);
            }
        }
    }
}
