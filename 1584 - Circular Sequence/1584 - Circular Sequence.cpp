#include <bits/stdc++.h>
#define out() freopen("err.txt","w",stdout)
using namespace std;
void smallest(string input){
    string mini = input;
    int occurs = 1,ascii,ascii2,pos = 0;
    ascii = input[0];
    for (int i = 1; i < input.length(); i++){
        ascii2 = input[i];
        if (ascii > ascii2){
            ascii = ascii2;
            pos = i;
            occurs = 0;
        }
        if (ascii == ascii2){
            occurs ++;
        }
    }
    occurs--;
    int pos2 = pos;
    for (int i = 0; i < input.length(); i++){
        bool bol = true;
        if (pos+i == input.length() && bol){
            pos = -i;
            bol = false;
        }
        mini[i] = input[pos+i];

    }
    string answer = input;
    for (int i = 0; i<occurs;i++){
        char a;
        bool bol2 = true;
        bool bol3 = true;
        a = mini[0];
        pos = input.find(a,pos2+1);
        bool bol = true;
        for (int k = 0; k < input.length();k++){
            if (pos+k == input.length() && bol){
                pos2 = pos;
                pos = -k;
                bol = false;
            }
            ascii = input[pos+k];
            ascii2 = mini[k];
            answer[k] = input[pos+k];
            if (ascii > ascii2){
                    bol3 = false;
            }
            if (ascii < ascii2 && bol3){
                bol2 = false;
            }
        }
        if (bol2 == false){
            mini = answer;
            bol2 = true;}
    }
    cout << mini<<endl;

}
int main(){
    int times;
    cin >> times;
    for (int i = 0 ; i < times; i++){
        string input;
        getline(cin,input);
        if (input  == "\0"){getline(cin,input);}
        smallest(input);
    }
    return 0;
}
