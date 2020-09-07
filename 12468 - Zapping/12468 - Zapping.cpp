#include <bits/stdc++.h>
#define out() freopen("err.txt","w",stdout)
using namespace std;
int main(){
    out();
    int x,y;
    cin >> x;
    cin >> y;
    while(x != -1 && y != -1){
        if(abs(x-y) <50 ){
            cout << abs(x-y) << endl;
        }
        else{
            int cont = 0,var = x;
            x = min(var,y);
            y = max(var,y);
            //cout << x << " "<< y<<endl;
            cont = (99 - y)+1;
            y = 0;
            cont += abs(y-x);
            cout << cont << endl;
        }
        cin >> x;
        cin >> y;
    }

    return 0;
}
