#include <bits/stdc++.h>
using namespace std;
int main(){
    //freopen("out.txt","w",stdout);
    map <string, string> dic;
    string var, key, value;
    while (getline(cin,var),var != ""){
        stringstream sin(var);
        sin >> value >> key;
        dic[key] = value;
    }
    while(getline(cin, var)){
        if (dic.find(var) != dic.end()){cout << dic[var] <<endl;}
        else{cout << "eh"<<endl;}
    }
    return 0;
}
