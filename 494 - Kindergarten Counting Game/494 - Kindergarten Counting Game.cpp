#include <bits/stdc++.h>
using namespace std;
int main(){
    char input[1001];
    bool flag = true;
    int cont;
    while (gets(input)){
        cont = 0;
        for (int i = 0; input[i]; i++){
            if(('a' <= input[i] && 'z' >= input[i])  || ('A' <= input[i] && 'Z' >= input[i])){
                if(flag){cont++;flag = false;}
            }
            else{if(flag == false){flag = true;}}
        }
        printf("%d\n",cont);

    }
    return 0;
}
