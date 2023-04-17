// https://atcoder.jp/contests/abc222/tasks/abc222_b
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, P, a, t;
    t = 0;
    cin >> N >> P;

    while(N--) {
        cin >> a;
        if(a < P) t++;
    }

    cout << t;
}