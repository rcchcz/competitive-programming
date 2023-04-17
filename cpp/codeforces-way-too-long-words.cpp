// https://codeforces.com/contest/71/problem/A
#include <bits/stdc++.h>
using namespace std;

int main() {
    string str;
    int n;
    cin >> n;
    for(int i = 0; i < n; ++i) {
        cin >> str;
        if(str.size() > 10) cout << str[0] <<  str.size() - 2 << str[str.size() - 1] << '\n';
            else cout << str << '\n';
    }
}