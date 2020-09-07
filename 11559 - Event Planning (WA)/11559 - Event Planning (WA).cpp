#include <bits/stdc++.h>
#define out() freopen("err.txt","w",stdout)
using namespace std;
int main(){
    //out();
    int n,b,h,w;
    long ans = 2000001;
    while (scanf("%d %d %d %d\n", &n, &b, &h, &w) == 4){
        for(int i = 0; i < h; i++){
            int price;
            cin >> price;
            if (price*n <= b){
                int cost = price * n;
                bool bol = false;
                for(int k = 0; k < w; k++){
                    int beds;
                    cin >> beds;
                    if (beds >= n){
                        bol = true;
                        break;
                    }
                }
                if (cost <= ans && bol ){ans = cost;}
            }
            else{
                string trash;
                cin >> trash;
            }
        }
        if (ans > b){cout<<"stay home\n";}
        else{cout <<ans<<endl;}
    }

    return 0;
}
