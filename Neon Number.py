import java.util.*;
public class giri{
    public static void main(String[] args){
        Scanner r = new Scanner(System.in);
        int n = r.nextInt();
        int a=n*n;
        int sum=0;
        while(a>0){
            sum = sum+(a%10);
            a = a/10;
        }
        if(n==sum){
            System.out.println("Neon Number");
        }
        else {
            System.out.println("Not Neon Number");
        }
    }
}