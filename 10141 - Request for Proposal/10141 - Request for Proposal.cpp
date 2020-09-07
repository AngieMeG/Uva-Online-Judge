#include <bits/stdc++.h>
using namespace std;
int main (){
    int n , p, cont = 0;
    string trash;
    scanf("%d %d",&n,&p);
    while(n != 0  && p != 0){
        cont++;
        for(int i = 0; i < n; i++){
            cin.ignore();
            getline(cin, trash);
        }
        string ans;
        double compliance = -1.00;
        double price = 0;
        for (int i = 0; i < p; i++){
            string var;
            getline(cin,var);
            if (var == "\0"){getline(cin,var);}
            float met;
            double priceb;
            scanf("%lf %f",&priceb,&met);
            if (met/n > compliance){
                ans = var;
                compliance = met/n;
                price = priceb;
            }
            else if (met/n == compliance){
                if (price > priceb){
                    ans = var;
                    compliance = met/n;
                    price = priceb;
                }
            }
            for(int k = 0; k < met; k++){
                getline(cin,trash);
                if (trash == "\0"){getline(cin, trash);}
            }
        }
        cout << "RFP #"<<cont<<"\n"<<ans<<"\n";
        scanf("%d %d",&n,&p);
        if (n != 0 && p!= 0){
            cout <<"\n";}
    }
    return 0;
}
