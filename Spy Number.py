import java.util.*;
public class crazy{
    public static void main(String[] args){
        Scanner r = new Scanner(System.in);
        int n = r.nextInt();
        int sum=0,pro=1;
        while(n>0){
            sum = sum+(n%10);
            pro = pro*(n%10);
            n = n/10;
        }
        if(pro == sum){
            System.out.println("Spy Number");
        }
        else {
            System.out.println("Not Spy Number");
        }
    }
}