#include <bits/stdc++.h>
using namespace std;
int main(){
    int cases;
    while (scanf("%d",&cases),cases){
        long long total = 0;
        multiset <int> bills;
        for (int i = 0; i < cases; i++){
            int times;
            scanf("%d",&times);
            for (int k = 0; k < times; k++){
                int var;
                scanf("%d",&var);
                bills.insert(var);
            }
            multiset<int>::iterator low = bills.begin();
            multiset<int>::iterator high = --bills.end();
            total += *high - *low;
            bills.erase(low);bills.erase(high);
        }
        cout << total << endl;
    }
    return 0;
}
