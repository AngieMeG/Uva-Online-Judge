#include <bits/stdc++.h>
#define out() freopen("err.txt","w",stdout)
using namespace std;
int main(){
    string word;
    getline(cin,word);
    int cont = 1;
    vector <string> words;
    vector <string> len;
    words.push_back("HELLO");
    words.push_back("HOLA");
    words.push_back("HALLO");
    words.push_back("BONJOUR");
    words.push_back("CIAO");
    words.push_back("ZDRAVSTVUJTE");
    len.push_back("ENGLISH");
    len.push_back("SPANISH");
    len.push_back("GERMAN");
    len.push_back("FRENCH");
    len.push_back("ITALIAN");
    len.push_back("RUSSIAN");
    while (word != "#"){
        bool bol = false;
        cout << "Case "<<cont<<": ";
        for (int i = 0; i < len.size(); i++){
            if (word == words[i]){
                cout << len[i]<<endl;
                bol = true;
                break;
            }
        }
        if (bol == false){cout<<"UNKNOWN"<<endl;}
        cont++;
        getline(cin,word);
        if (word == "\0"){getline(cin,word);}
    }

    return 0;
}
