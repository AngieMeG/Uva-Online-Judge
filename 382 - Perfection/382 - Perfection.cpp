#include <bits/stdc++.h>
using namespace std;
int main(){
    printf("PERFECTION OUTPUT\n");
    int n = 0;
    cin >> n;
    while (n){
        int divs = 0;
        for (int i = 1; i < n;i++){if (n%i == 0){divs += i;}}
        if (divs == n){printf("%5d  PERFECT\n",n);}
        else{
            if(divs > n){printf("%5d  ABUNDANT\n",n);}
            else{printf("%5d  DEFICIENT\n",n);}
        }
        cin >> n;
    }
    printf("END OF OUTPUT\n");
    return 0;
}
