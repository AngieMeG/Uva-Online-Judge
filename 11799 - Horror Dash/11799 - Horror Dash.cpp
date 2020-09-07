#include <bits/stdc++.h>
#define out() freopen("err.txt","w",stdout)
using namespace std;
int main(){
    int times;
    cin >> times;
    for (int i = 1;  i <= times; i++){
        int n, number;
        cin >> n;
        cin >> number;
        int maximo = number;
        for (int k = 1; k < n; k++){
            int number2;
            cin >> number2;
            maximo = max(maximo, number2);
        }
        cout << "Case " << i << ": "<< maximo << endl;
        }
    return 0;
}
