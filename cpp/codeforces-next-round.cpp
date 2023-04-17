// https://codeforces.com/contest/158/problem/A
#include <bits/stdc++.h>
using namespace std;

int main() {    
    int n, k, a, count;
    count  = 0;

    cin >> n >> k;
    int v[n];
    
    for(int i = 0; i < n; ++i) {
        cin >> a;
        v[i] = a;
    }

    for(int i = 0; i < n; ++i) {
        if(v[i] >= v[k - 1] && v[i] > 0) ++count;
    }

    cout << count;
}