#include <bits/stdc++.h>
using namespace std;
int main(){
    int cases, sample;
    scanf("%d",&cases);
    while (cases--){
        scanf("%d",&sample);
        int lis[sample], above = 0;
        float avg = 0;
        for (int i = 0; i < sample; i++){
            scanf("%d",&lis[i]);
            avg += lis[i];
        }
        avg /= sample;
        for (int i = 0; i < sample; i++){
            if (lis[i] > avg){above ++;}
        }
        printf("%0.3f%%\n",(above*100.000)/sample);
    }
    return 0;
}
