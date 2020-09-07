#include <bits/stdc++.h>
using namespace std;
int main(){
    int cases;
    cin >> cases;
    while(cases != 0){
        int ans = cases, d = -cases, r = -cases;
        string highway;
        cin >> highway;
        for (int i = 0; i < cases; i++){
            if (highway[i] == 'Z'){
                ans = 0;
                break;
            }
            else if(highway[i] == 'D'){
                ans = min(ans, i - r);
                d = i;
            }
            else if(highway[i] == 'R'){
                ans = min(ans, i -d);
                r = i;
            }
        }
        cout <<ans <<endl;
        cin >> cases;
    }
    return 0;
}
