// https://codeforces.com/contest/282/problem/A
#include <bits/stdc++.h>
using namespace std;
 
int main() {    
    int n, x;
    x = 0;
    string s;
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> s;
        if(s[0] == '+' || s[1] == '+') x++;
            else if(s[0] == '-' || s[1] == '-') x--;
    }
    cout << x;
}