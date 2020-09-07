#include <bits/stdc++.h>
using namespace std;
int main (){
    int cases;
    cin >> cases;
    vector <string> countries;
    for (int i = 0; i < cases; i++){
        string countrie, name;
        cin >> countrie;
        getline(cin, name);
        countries.push_back(countrie);
    }
    sort(countries.begin(), countries.end());
    string c;
    c = countries[0];
    int cont = 1;
    for (int i = 1; i <= cases; i++){
        if (countries[i] == c){
            cont++;
        }
        else{
            cout << c<<" "<<cont<<endl;
            cont = 1;
            c = countries[i];
        }
    }
    return 0;
}
