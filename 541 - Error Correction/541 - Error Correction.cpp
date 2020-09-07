#include <bits/stdc++.h>
using namespace std;
int main(){
    int cases;
    cin >> cases;
    while(cases != 0 ){
        vector <vector <int> > matriz(cases);
        vector <int> rows;
        vector <int> columns;
        for(int i = 0; i < cases; i++){
            matriz[i] = vector <int> (cases);
            int cont_rows = 0;
            for (int k = 0; k < cases; k++){
                int num;
                cin >> num;
                cont_rows += num;
                matriz[i][k] = num;
            }
            if (cont_rows % 2 != 0){
                rows.push_back(i+1);
            }
        }
        int y = rows.size();
        if (y > 1){cout << "Corrupt\n";}
        else{
            for(int i = 0; i < cases; i++){
                int cont_columns = 0;
                for(int k = 0; k<cases; k++){
                    cont_columns += matriz[k][i];
                }
                if(cont_columns % 2 != 0){
                    columns.push_back(i+1);
                }
            }
            int x = columns.size();
            if(x > 1){cout << "Corrupt\n";}
            else if (columns.size() == 1 && rows.size()==1){
                cout << "Change bit ("<<rows[0]<<","<<columns[0]<<")\n";}
            else{cout << "OK\n";}
            }
        cin >> cases;
    }
    return 0;
}
