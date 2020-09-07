#include <bits/stdc++.h>
using namespace std;
int main (){
    int n, q,cont = 1;
    cin >> n;cin >>q;
    while (n!= 0 && q!= 0){
        cout << "CASE# "<<cont<<":\n";
        vector <int> numbers;
        vector <int> queries;
        int num;
        for(int i = 0; i < n; i++){
            cin >> num;
            numbers.push_back(num);
        }
        sort(numbers.begin(), numbers.end());
        for (int i = 0; i < q; i++){
            cin >> num;
            int top = n,bottom = 0;
            bool bol = false;
            if (num > numbers[n/2] ){
                top = n;
                bottom = (n/2)+1;
            }
            else{
                top = (n/2)+1;
                bottom = 0;
            }
            for (int k = bottom; k < top; k++){
                if (num == numbers[k]){
                    cout << num << " found at "<<k+1<<endl;
                    bol = true;
                    break;
                }
            }
            if (!bol){cout << num <<" not found\n"; }
        }
        cont++;
        cin >>n;cin >>q;
    }
    return 0;
}
