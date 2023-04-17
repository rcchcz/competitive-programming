// https://codeforces.com/contest/266/problem/B
#include <bits/stdc++.h>
using namespace std;
 
int main() {    
    int n, t;
    string q;
    cin >> n >> t;
    cin >> q;

    for(auto i = 0; i < t; i++) {
        for(auto j = 0; j < n - 1; ) {
            if(q[j] == 'B' && q[j + 1] == 'G') {
                swap(q[j], q[j + 1]);
                j += 2;
            } else { j++; }
        }
    }

    cout << q;
}