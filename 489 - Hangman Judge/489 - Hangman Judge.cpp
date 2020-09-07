#include <bits/stdc++.h>
using namespace std;
int main(){
    //freopen("out.txt","w",stdout);
    int n;
    while (scanf("%d",&n),n != -1){
        string c1,c2;
        bool win = true,lose = true;
        cin >> c1;cin >> c2;
        vector <char> lis;
        int correct = 0,tries = 0;
        for (int i = 0; i < c2.size() && correct != c1.size() && tries < 7; i++){
            if (count(lis.begin(),lis.end(),c2[i]) == 0){
                lis.push_back(c2[i]);
                int var = count(c1.begin(),c1.end(),c2[i]);
                if (!var){tries+=1;}
                else{correct+=var;}
            }
        }
        cout << "Round "<<n<<endl;
        if (tries < 7){
            if (correct == c1.size()){cout <<"You win."<<endl;}
            else{cout << "You chickened out."<<endl;}
        }
        else{cout <<"You lose."<<endl;}
    }
    return 0;
}
