#include <bits/stdc++.h>
#define out() freopen("err.txt","w",stdout)
using namespace std;
int main(){
    int cases;
    cin >> cases;
    for (int i = 0; i < cases; i++ ){
        string word;
        getline(cin,word);
        if (word == "\0"){getline(cin,word);}
        int errors_one = 0, errors_two = 0, errors_three = 0;
        string test_one = "one",test_two = "two", test_three = "three";
        for (int k = 0; k < 5; k++){
            if (k < 3){
                if (word[k] != test_one[k]){errors_one++;}
                if(word[k] != test_two[k]){errors_two++;}
            }
            else{
                if(word[k] != test_three[k]){errors_three++;}
            }
        }
        if(errors_one <=1){cout<<1<<endl;}
        else if(errors_two <= 1){cout<<2<<endl;}
        else if(errors_three <= 1){cout<<3<<endl;}
    }
    return 0;
}
