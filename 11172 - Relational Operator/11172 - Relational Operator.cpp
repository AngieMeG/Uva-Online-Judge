#include <bits/stdc++.h>
using namespace std;
int main(){
    int cases;
    scanf("%d",&cases);
    while(cases--){
        int num1,num2;
        scanf("%d %d",&num1, &num2);
        if (num1 == num2){cout << "=\n";}
        else{
            cout << (num1 > num2 ? ">\n" : "<\n");
        }
    }
    return 0;
}
