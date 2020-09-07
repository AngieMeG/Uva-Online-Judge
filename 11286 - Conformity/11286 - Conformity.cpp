//Conformity UVA - 11286
//Use of map (dictionary)
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    while (scanf("%d",&n),n){
        map <vector<int>, int> dic;
        for (int i =0; i < n; i++){
            vector <int>lis;
            for (int k = 0; k < 5; k++){
                int var;
                scanf("%d",&var); lis.push_back(var);
            }
            sort(lis.begin(),lis.end());
            if (dic.find(lis) != dic.end()){dic[lis]++;}
            else{dic[lis] = 1;}
        }
        map<int, int> res;
        int maxi = 0;
        map <vector<int>, int> ::iterator itr;
        for (itr = dic.begin();itr != dic.end(); ++itr){
            if (maxi < itr->second){maxi = itr -> second;}
            if (res.find(itr->second) != res.end()){res[itr->second]+=itr->second;}
            else{res[itr->second]= itr-> second;}
        }
        //cout << maxi<<endl;
        cout << res[maxi]<<endl;
    }
    return 0;
}
