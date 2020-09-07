/*(+i| a <= i <= b : i) = (a+b)n/2

     Donde n es la cantidad de numeros de la secuencia
     Por lo que b = a + (n-1)

     (+i| a <= i <= a + (n-1) : i) = (2a+ (n-1))n/2
*/

#include <bits/stdc++.h>
using namespace std;
int main(){
    long long sum, a, b;
    while(scanf("%lld", &sum) && sum + 1){
        for (long i = sqrt(2*sum); i >= 1; i--){
            a = (2*sum + i - i*i) / (2*i);
            if (2 * a * i + i * i - i == 2 * sum) { b = a + i -1; break;}
        }
        printf("%lld = %lld + ... + %lld\n", sum, a, b);
    }
    return 0;
}
