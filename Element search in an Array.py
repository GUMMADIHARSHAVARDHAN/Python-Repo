import java.util.*;

public class crazy {
    public static void main(String[] args) {
        Scanner r = new Scanner(System.in);
        int n = r.nextInt();
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = r.nextInt();
        }

        int key = r.nextInt();

        int c = 0;
        int j=0;
        for (int i = 0; i < n; i++) {
            if (key == a[i]) {
                c++;
                break;
            }
            j++;
        }

        if (c>0) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }
    }
}

