#include <bits/stdc++.h>
using namespace std;
int main(){
    char letter;
    int cont = 0;
    while ((letter = getchar()) != EOF){
        if (letter >= '0' && letter <= '9'){cont += letter - 48;}
        else if (letter == '!' || letter == '\n'){printf("\n");}
        else if (letter == 'b'){
            for (int i = 0; i < cont; i++){printf(" ");}
            cont = 0;
        }
        else{
            for (int i = 0; i < cont; i++){printf("%c",letter);}
            cont = 0;
        }
    }
    return 0;
}
