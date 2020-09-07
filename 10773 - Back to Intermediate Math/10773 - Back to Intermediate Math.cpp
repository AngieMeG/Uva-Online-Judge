#include <bits/stdc++.h>
using namespace std;
int main(){
    int cases, cont = 1;
    double fastest_path, shortest_path, d, v, u;
    scanf("%d",&cases);
    while (cases--){
        scanf("%lf %lf %lf",&d, &v, &u);
        if (u == 0 || v == 0 || v >= u){printf("Case %d: can't determine\n", cont);}
        else{
            fastest_path = d/u;
            shortest_path = d/(sqrt(u*u - v*v));
            printf("Case %d: %.3lf\n", cont, fabs(shortest_path - fastest_path));
        }
        cont++;
    }
    return 0;
}
