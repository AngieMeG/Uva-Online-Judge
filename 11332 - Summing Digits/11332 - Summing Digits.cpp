#include <bits/stdc++.h>
#include <math.h>
#define out() freopen("err.txt","w",stdout)
using namespace std;
void digits(int number){
    if (number < 10){
        cout << number<<endl;
    }
    else{
        int cifras = 1, num = 0;
        cifras += log10(number);
        for (int i = 0; i < cifras; i++){
            num += number%10;
            number /= 10;
        }
        digits(num);
    }
}
int main(){
    int number;
    cin >> number;
    while(number != 0){
        digits(number);
        cin >> number;
    }
    return 0;
}
