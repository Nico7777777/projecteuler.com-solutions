//
// Created by nick on 12/25/23.
//
#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
using namespace std;
vector<int> findPeriod(int n) {
    vector<int> remainders;
    int remainder = 1;

    while (remainder != 0 && find(remainders.begin(), remainders.end(), remainder) == remainders.end()) {
        remainders.push_back(remainder);
        remainder = (remainder * 10) % n;
    }

    return remainders;
}

void transformFraction(int n) {
    vector<int> period = findPeriod(n);

    // Identifică cifrele în perioadă și cele non-periodice
    cout << "Cifrele non-periodice: ";
    for (int i = 1; i < period[0]; ++i) {
        std::cout << i;
    }

    cout << "\nCifrele in perioada: ";
    for (size_t i = 1; i < period.size(); ++i) {
        cout << period[i];
    }
}

vector<pair<int, int>> transforma_numitor(int n) {
    vector<pair<int,int>> x;
    pair<int, int> p_la_alfa;
    int p = 2, alfa;
    while (n != 1) {
        if (n % p == 0) {
            alfa = 0;
            while (n % p == 0) {
                ++alfa;
                n /= p;
            }
            p_la_alfa.first = p;
            p_la_alfa.second = alfa;
            x.push_back(p_la_alfa);
        }
        ++p;
    }
    return x;
}

int main() {
    int n;
    cout << "Introduceti n pentru 1/n: ";
    cin >> n;

    transformFraction(n);

    return 0;
}
