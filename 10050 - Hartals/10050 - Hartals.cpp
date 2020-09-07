#include<bits/stdc++.h>
using namespace std;
int main(){
    int cases;
    scanf("%d",&cases);
    for (int i = 0; i < cases; i++){
        int days,num;
        int res = 0;
        scanf("%d",&days);
        scanf("%d",&num);
        map<int,int> parties;
        for (int i = 0; i < num; i++ ){
            int var;
            scanf("%d",&var);
            for (int k = 1; k <= days; k++){
                if (k % var == 0 && k % 7 != 6 && k % 7 != 0 && parties.find(k)== parties.end() && k!= 6 && k!= 7){parties[k] = 1;res++;}
            }
        }
        cout << res<<endl;
    }
    return 0;
}
