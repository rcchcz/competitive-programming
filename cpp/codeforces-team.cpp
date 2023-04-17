// https://codeforces.com/contest/231/problem/A
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, a, k, k_total;
    k_total = 0;

    cin >> n;

    for(int i = 0; i < n; ++i) {
        k = 0;
        for(int j = 0; j < 3; ++j) {
            cin >> a;
            if(a == 1) ++k;
        }
        if(k > 1) ++k_total;
    }   

    cout << k_total;
}