class multiples_of_3_or_5{
    public static void main(String[] args){
        int solution = 0;
        for(int i=3; i<1000; i++)
            if(i%3 == 0 || i%5 == 0)
                solution += i;
        System.out.println(solution);
    }
}
