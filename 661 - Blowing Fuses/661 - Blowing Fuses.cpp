#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,m,c;
    int cont = 1;
    while (scanf("%d %d %d",&n, &m, &c),(n || m || c)){
        int devices[n];
        int state[n];
        for (int i = 0; i < n;i++){
            scanf("%d",&devices[i]);
            state[i] = 0;
        }
        int maxi= 0;
        int total= 0;
        for (int i = 0; i < m; i++){
            int ope;
            scanf("%d",&ope);
            if (!state[ope-1]){
                state[ope-1] = 1;
                total += devices[ope-1];
                if (i == 0){maxi = total;}
                else{maxi = max(maxi,total);}
            }
            else{state[ope-1] = 0;total-= devices[ope-1];}
        }
        if (maxi > c){printf("Sequence %d\nFuse was blown.\n\n",cont);}
        else{printf("Sequence %d\nFuse was not blown.\nMaximal power consumption was %d amperes.\n\n",cont,maxi);}
        cont++;
    }
    return 0;
}
