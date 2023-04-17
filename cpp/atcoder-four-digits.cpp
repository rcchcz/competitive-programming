// https://atcoder.jp/contests/abc222/tasks/abc222_a
#include <bits/stdc++.h>
using namespace std;

string f(string s) {
    int z = 4 - s.size();
    stringstream sss;

    for(int i = 0; i < z; i++) {
        sss << 0;
    }

    sss << s;
    string res = sss.str();

    return res;
}

int main() {
    int N;
    cin >> N;

    stringstream ss;
    ss << N;
    string s = ss.str();

    if(s.size() < 4) cout << f(s);
        else cout << s;
}