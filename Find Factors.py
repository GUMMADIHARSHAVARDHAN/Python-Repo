import java.util.*;
public class main{
    public static void main(String[] args)
    {
    Scanner r = new Scanner(System.in);
    int a=r.nextInt();
    for(int i=1;i<=a;i++){
        if(a%i==0){
        System.out.printf("%d ",i);
    }
    }
}
}