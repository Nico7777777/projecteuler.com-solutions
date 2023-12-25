#include <iostream>
#include <cstring>

const char* ones[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
    "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};

const char* tens[] = {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

int func(unsigned long long n){
    if(0 <= n and n < 20)
        return strlen(ones[n]);
    else if(20 <= n and n <= 90 and n % 10 == 0)
        return strlen(tens[n/10]);
    else if(20 < n and  n < 100)
        return strlen(tens[n/10]) + strlen(ones[n%10]);
    else if(100 <= n and n <= 900 and n % 100 == 0)
        return strlen(ones[n/100]) + strlen("hundred");
    else if(100 < n and n < 1000)
        return strlen(ones[n/100]) + strlen("hundredand") + func(n%100);
    /*else if(n == 1000)*/
    return strlen("onethousand");
}

int main(){
    unsigned long long count = 0;
    for(int i = 1; i <= 1000; ++i){
        count += func(i);
        //printf("%d: %d\n", i, func(i));
    }
    printf("%lld", count);
}