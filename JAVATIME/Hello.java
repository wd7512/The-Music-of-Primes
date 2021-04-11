
 public class Hello {
     public static void main(String[] args) {
         int fib0 = 0;
         int fib1 = 0;
         int fib2 = 1;
         for (int i = 0; i < 100; i++) {
             fib0 = fib1;
             fib1 = fib2;
             fib2 = fib1 + fib0;
             System.out.println(fib2);
             if (fib2 < 0) {
                 System.out.println(" uhh what " + i);
             }
         }
         
         
     }
 }
 