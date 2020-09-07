#include <bits/stdc++.h>
using namespace std;
int main(){
    int num, numerator, denominator, temp;
    float value;
    while (cin >> num){
        value = ceil((-1 + sqrt(1 + 4*2*num))/2);
        numerator = value - (num - 1 - (((value - 1) * value)/2));
        denominator = 1 + (num - 1 - (((value - 1) * value)/2));
        if ((int)value % 2 == 0){
            temp = numerator; numerator = denominator; denominator = temp;
        }
        printf("TERM %d IS %d/%d\n",num, numerator, denominator);
    }
}
