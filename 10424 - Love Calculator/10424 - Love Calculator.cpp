#include <bits/stdc++.h>
#include <string>
using namespace std;
int r (string c1){
    int suma = 0;
    string c;
    stringstream ss;
    for (int i = 0; i < c1.length();i++ ){     //lower()
        if (c1.at(i) >= 65 && c1.at(i)<=91){
                c += (c1.at(i)+32);
        }
        else{c+=c1.at(i);}
    }
    for (int i = 0; i < c1.length();i++){
        if (c.at(i)>= 97 && c.at(i)<=122){
            suma+=(c.at(i)-96);
        }
    }
    while(suma>= 10){
        stringstream ss;
        ss << suma;
        string str = ss.str();
        suma = 0;
        for (int i = 0; i<str.length();i++){
            suma += (str.at(i)-48);}
    }

    return suma;
}
int main(){
    while (1){
    string c1;
    getline(cin,c1);
    if (c1 == "\0"){break;}
    int s1 = r(c1);
    string c2;
    getline(cin,c2);
    int s2 = r(c2);
    float res =(float) s1/s2;
    printf("%.2lf",res > 1? 100/res : 100* res);
    cout<< " %\n";
    }
    return 0;
}
