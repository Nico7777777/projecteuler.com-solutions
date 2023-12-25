//
// Created by nick on 12/25/23.
//
#include <iostream>
#include <fstream>
#include <vector>
#define limit 10000
#define SIZE 50000000

typedef unsigned long long ULL;
using namespace std;
vector<int> primes;
struct n_la_p{
    int n, p;
};
struct N_descompus{
    vector<n_la_p> powers;
    int factors = 0;
};
ofstream file1, file2;

ULL generate_triangle_number(int n) {
   ULL x = n * static_cast<ULL>(n + 1) / 2;
   return x;
}

void SieveOfAtkin(vector<int> &p)
{
    bool sieve[limit + 1];
    for (int i = 0; i <= limit; i++)
        sieve[i] = false;

    // 2 and 3 are known to be prime
    sieve[2] = true;
    sieve[3] = true;

    for (int x = 1; x * x <= limit; x++) {
        for (int y = 1; y * y <= limit; y++) {

            // Condition 1
            int n = (4 * x * x) + (y * y);
            if (n <= limit
                && (n % 12 == 1 || n % 12 == 5))
                sieve[n] ^= true;

            // Condition 2
            n = (3 * x * x) + (y * y);
            if (n <= limit && n % 12 == 7)
                sieve[n] ^= true;

            // Condition 3
            n = (3 * x * x) - (y * y);
            if (x > y && n <= limit
                && n % 12 == 11)
                sieve[n] ^= true;
        }
    }

    // Mark all multiples
    // of squares as non-prime
    for (int r = 5; r * r <= limit; r++) {
        if (sieve[r]) {
            for (int i = r * r; i <= limit; i += r * r)
                sieve[i] = false;
        }
    }

    // Print primes using sieve[]
    for (int a = 1; a <= limit; a++)
        if (sieve[a])
            p.push_back(a);
}

N_descompus descompunere(ULL n) {
    N_descompus N;
    int z, f = 2;
    while (n != 1) {
        if (n % f == 0) {
            n_la_p w{};
            z = 0;
            while(n % f == 0) {
                n /= f;
                z++;
            }
            w.n = f;
            w.p = z;
            N.powers.push_back(w);
        }
        f++;
    }
    N.factors = 1;
    for(auto power : N.powers)
        N.factors *= (power.p + 1);
    return N;
}

void pregenerate(vector<N_descompus> &v) {
    ofstream file3;
    file3.open("triangular numbers1.txt");
    for(int i = 1; i <= SIZE; ++i) {
        N_descompus n;
        v.push_back(descompunere(generate_triangle_number(i)));
        file3 << i << ": " << generate_triangle_number(i) << '\n';
    }
    file3.close();
}


int main() {
    file1.open("primes.txt");
    file2.open("triangular numbers.txt");
    vector<N_descompus> sir; /// Aici facem sirul de numere stocate ca descompunere
    pregenerate(sir);

    SieveOfAtkin(primes);

    for(auto i = 0; i < primes.size(); ++i)
        file1 << "Al " << i+1 << " numar prim: " << primes[i] << '\n';
    for(auto i = 0; i < sir.size(); ++i) {
        file2 << "Al " << i+1 << " numar triangular:\n";
        file2 << "Numar factori: " << sir[i].factors << '\n';
        for(auto power : sir[i].powers)
            file2 << power.n << "^" << power.p <<"; ";
        file2 << "\n\n";
    }
    file1.close();
}