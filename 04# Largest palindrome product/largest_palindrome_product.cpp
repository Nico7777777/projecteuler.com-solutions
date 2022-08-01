#include<iostream>
using namespace std;
int largestPalindrome = 0, a = 999, b, db;
bool isPalindrome(int x)
{
	int cop = x, res = 0;
	while( cop )
	{
		res = res*10 + cop%10;
		cop /= 10;
	}
	return (res==x);
}
int main()
{
	while( a >= 100 )
	{
		if( a % 11 == 0 )
		{
			b = 999;
			db = 1;
		}
		else
		{
			b = 990;
			db = 11;
		}
		while( b >= a )
		{
			if( a * b <= largestPalindrome ) break;
			if( isPalindrome( a * b ) ) largestPalindrome = a * b;
			b -= db;
		}
		a--;
	}
	cout<<largestPalindrome;
}
