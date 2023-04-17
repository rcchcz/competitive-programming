// https://atcoder.jp/contests/abc219/tasks/abc219_a
#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int X;
    cin >> X;

    if(X >= 0 && X < 40) cout << 40 - X;
    else if(X >= 40 && X < 70) cout << 70 - X;
    else if(X >= 70 && X < 90) cout << 90 - X;
    else if(X >= 90) cout << "expert";

}