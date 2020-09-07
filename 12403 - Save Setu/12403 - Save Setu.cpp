#include <bits/stdc++.h>
#define out() freopen("err.txt","w",stdout)
using namespace std;
int main(){
    int number = 0, account = 0;
    cin >> number;
    while(number!= 0){
        char word[7];
        char don[7]={"donate"};
        cin >> word;
        if (word[0] == don[0]){
            int money;
            cin >> money;
            account += money;
        }
        else {cout << account<<endl;}
        number--;
    }
    return 0;
}
