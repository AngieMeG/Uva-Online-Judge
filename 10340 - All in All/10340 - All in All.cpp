#include <bits/stdc++.h>
using namespace std;
int main(){
    //freopen("out.txt","w",stdout);
    string s, t;
    int sizes, sizet, ps;
    while (cin >> s >> t){
        sizes = s.size();
        sizet = t.size();
        ps = 0;
        for (int i = 0; i < sizet; i++){
            if (s[ps] == t[i]) {ps ++;}
        }
        if (ps == sizes) {printf("Yes\n");}
        else{printf("No\n");}
    }
    return 0;
}
