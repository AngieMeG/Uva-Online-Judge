#include <bits/stdc++.h>
#define out() freopen("err.txt","w",stdout)
using namespace std;
int main(){
    int cont = 1;
    string word;
    getline(cin,word);
    if (word == "\0"){getline(cin,word);}
    while(word != "*"){
        cout << "Case "<<cont<<": ";
        if(word == "Hajj"){
            cout << "Hajj-e-Akbar\n";
        }
        else{cout << "Hajj-e-Asghar\n";}
        getline(cin,word);
        if (word == "\0"){getline(cin,word);}
        cont++;
    }
    return 0;
}
