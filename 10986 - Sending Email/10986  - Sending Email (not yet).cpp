#include <bits/stdc++.h>
#define inf 500000001
using namespace std;
int main(){
    int cases;
    for (int i= 1;i < scanf("%d",&cases),cases+1;i++){
        int n,m,s,t;
        while (scanf("%d %d %d %d",&n,&m,&s,&t)){
            long long di[n];
            for (int k = 0; k<n; k++){di[k] = inf;}
            int graph [m*2][3];
            di[s] = 0;
            for (int k = 0; k<m; k++){
                int c1,c2,c3;
                scanf("%d %d %d",&c1,&c2,&c3);
                graph[k][0] = c1;graph[k][1] = c2;graph[k][2] = c3;
                graph[k][0] = c2;graph[k][1] = c1;graph[k][2] = c3;
            }
            for (int k = 0; k<n-1;k++){
                for (int j = 0; j < m*2;j++){
                    if (di[graph[j][0]] != inf){
                        cout <<di[graph[j][0]] <<endl;
                        if(di[graph[j][0]] + graph[j][2] < di[graph[j][1]]){di[graph[j][1]] = di[graph[j][0]]+graph[j][2];}
                    }
                }
            }
            cout << "aaaaaaaaaa\n";
            if (di[t] == inf){cout<<"Case #"<<i<<" "<<"unreachable\n";}
            else{cout<<"Case #"<<i<<" "<<di[t]<<endl;}
        }
    }
    return 0;
}
