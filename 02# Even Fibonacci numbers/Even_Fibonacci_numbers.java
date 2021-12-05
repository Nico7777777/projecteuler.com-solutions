public class Even_Fibonacci_numbers {
    public static void main(String args[]){
        int premier = 1, deuxieme = 2, sum = 0;
        while(premier < 4000000){
            deuxieme += premier;
            premier = deuxieme - premier;
            if(premier%2 == 0) sum += premier;
        }
        System.out.println( sum );
    }
}
