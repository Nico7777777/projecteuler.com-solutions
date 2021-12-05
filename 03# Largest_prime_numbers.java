class Largest_prime_numbers {
    public static void main(String[] args){
        long a = 600851475143L, factor = 2;
        System.out.println(a);
        while( a != 1 )
        {
            if( a%factor == 0)
                while(a%factor == 0) a /= factor;
            factor += 1;
        }
        System.out.println(--factor);
    }
}
