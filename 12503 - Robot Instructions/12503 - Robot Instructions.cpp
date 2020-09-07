#include <bits/stdc++.h>
#define out() freopen("err.txt","w",stdout)
using namespace std;
int robot(vector <int>ins, string order){
    if (order == "LEFT"){
        return -1;
    }
    else if (order == "RIGHT"){
        return 1;
    }
    else if(order == "SAME"){
        string var;
        cin >> var;
        int position;
        cin >> position;
        if(ins[position-1] == -1){var = "LEFT";}
        else{var = "RIGHT";}
        return robot(ins,var);

    }

}
int main(){
    int times;
    cin >> times;
    for(int i = 0; i < times; i++){
        int number,cont = 0;
        cin >> number;
        vector <int> ins;
        for(int k = 0; k < number; k++){
            string order;
            cin >> order;
            ins.push_back(robot(ins,order));
            cont += ins[k];
        }
        cout << cont<< endl;
    }
    return 0;
}
