// https://codeforces.com/gym/102861/problem/B
#include <bits/stdc++.h>
using namespace std;


int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int n;
    cin>>n;
    vector<vector<int>> grid(100, vector<int> (100, 0));

    int d,l,r,c;
    bool e = false;
    
    for(auto k=0; k<n; k++){
        cin>>d>>l>>r>>c;
        if(d == 0){
            for(auto i=1; i<=l; i++){
                if(c+i-1 < 0 || c+i-1 > 10 || r < 1 || r > 10 || c < 1 || c > 10 || grid[r][c+i-1] != 0) e = true;
                    else grid[r][c+i-1] = 1;
            }
        } else {
            for(auto i=1; i<=l; i++){
                if(r+i-1 < 0 || r+i-1 > 10 || r < 1 || r > 10 || c < 1 || c > 10 || grid[r+i-1][c] != 0) e = true;
                    else grid[r+i-1][c] = 1;
            }
        }
    }

    if(e) cout << 'N';
        else cout << 'Y';

}