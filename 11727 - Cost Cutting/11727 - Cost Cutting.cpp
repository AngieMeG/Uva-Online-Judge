#include <bits/stdc++.h>
using namespace std;
int main(){
    int cases ,cont = 1;
    scanf("%d",&cases);
    while(cases--){
        vector <int> vec;
        for (int i = 0; i < 3; i++){
            int c;
            scanf("%d",&c);
            vec.push_back(c);
        }
        sort(vec.begin(),vec.end());
        printf("Case %d: %d\n",cont , vec[1]);
        cont++;
    }

    return 0;
}
