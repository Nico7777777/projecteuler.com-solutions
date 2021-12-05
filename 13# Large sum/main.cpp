#include<fstream>
#include<iostream>
using namespace std;

string rez, a;
fstream f, g;
int cnt = 99;
string la_somme(string a, string b){//on suppose le dimension de string a peut-etre plus grande parce que on envoyer le solution comme le premier argument de la function, string a
    string x, deuxieme;
    int l = 0, cnta, cntb;
    for( cnta=a.length()-1, cntb=b.length()-1;   cntb>=0;   cnta--, cntb-- )
    {
        l += a[cnta] - '0' + b[cntb] - '0';
        deuxieme = char( 48 + l%10 );
        x.insert(0, deuxieme);
        l /= 10;
    }
    for(; cnta>=0; cnta-- )
    {
        l+= a[cnta] - '0';
        deuxieme = char( 48 + l%10 );
        x.insert(0, deuxieme);
        l /= 10;
    }
    if( l )
    {
        deuxieme = char( 48 + l%10 );
        x.insert(0, deuxieme);
    }
    return x;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie();
    f.open("in.txt", ios::in);
    g.open("out.txt", ios::out);
    f >> rez;
    for(; cnt; cnt--)
    {
        f>>a;
        rez = la_somme(rez, a);
    }
    cout<<rez<<endl;
}
