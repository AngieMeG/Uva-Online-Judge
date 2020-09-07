#include <bits/stdc++.h>
#define out() freopen("err.txt","w",stdout)
using namespace std;
int main(){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        int num,ans;
        cin >> num;
        ans = (num*315)+36962;
        cout << abs((ans/10)%10) << endl;
    }
    return 0;
}
