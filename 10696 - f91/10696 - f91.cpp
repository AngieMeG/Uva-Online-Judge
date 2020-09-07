#include <bits/stdc++.h>
#define out() freopen("err.txt","w",stdout)
using namespace std;

int f91(int number){
    if ( number <= 100 ){
        int var;
        var = f91(number+11);
        return f91(var);
    }
    else{
        return number - 10;
    }
}

int main(){
    int number;
    cin >> number;
    while (number != 0){
        int answer = f91(number);
        cout << "f91(" << number << ") = "<< answer <<endl;
        cin >> number;
    }
    return 0;
}
