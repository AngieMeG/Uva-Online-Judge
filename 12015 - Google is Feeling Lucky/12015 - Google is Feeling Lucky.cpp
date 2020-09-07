#include <bits/stdc++.h>
using namespace std;
int main(){
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; i++){
        cout << "Case #"<<i+1<<":\n";
        vector <string> ans;
        vector <int> ans_num;
        string url;
        cin >> url;
        int num;
        cin >> num;
        ans.push_back(url);
        ans_num.push_back(num);
        for(int k = 1; k < 10; k++){
            cin >> url;
            cin >> num;
            if( num > ans_num[0]){
                int var = ans_num.size();
                for(int j = 0; j < var; j++){
                    ans_num.pop_back();
                    ans.pop_back();
                }
                ans_num.push_back(num);
                ans.push_back(url);
            }
            else if (num == ans_num[0]){
                ans_num.push_back(num);
                ans.push_back(url);
            }
        }

        for(int k = 0; k < ans.size();k++ ){
            cout <<ans[k] << endl;
        }
    }
    return 0;
}
