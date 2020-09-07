#include <bits/stdc++.h>
using namespace std;
void aux(vector<int> lis){
    if (lis.size() == 2){
        printf("%d\nRemaining card: %d\n",lis[0],lis[1]);
    }
    else{
        printf("%d, ",lis[0]);
        lis.erase(lis.begin());
        int bol = lis[0];
        lis.erase(lis.begin());
        lis.push_back(bol);
        aux(lis);
    }
}
int main(){
    int number;
    scanf("%d",&number);
    while(number != 0){
        vector<int> lis;
        for (int i = 1; i <= number; i++){lis.push_back(i);}
        cout << "Discarded cards:";
        if (number == 1){printf("\nRemaining card: %d\n",number);}
        else{cout << " ";aux(lis);}
        scanf("%d",&number);
    }
    return 0;
}
