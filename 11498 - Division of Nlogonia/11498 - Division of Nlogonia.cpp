#include <bits/stdc++.h>
#define out() freopen("err.txt","w",stdout)
using namespace std;
int main(){
    int n;
    cin >> n;
    while ( n!= 0){
        int x_division, y_division;
        cin >> x_division;
        cin >> y_division;
        for(int i =0; i < n; i++){
            int x,y;
            cin >> x;
            cin >> y;
            if (x == x_division || y == y_division){
                cout << "divisa"<< endl;
            }
            else{
                if ( y > y_division){cout << "N";}
                else if ( y < y_division){cout << "S";}
                if ( x > x_division){cout << "E\n";}
                else if ( x < x_division){cout << "O\n";}
            }
        }
        cin >> n;
    }
    return 0;
}
