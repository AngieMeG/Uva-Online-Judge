#include <bits/stdc++.h>
using namespace std;
int main (){
    //freopen("out.txt","w",stdout);
    long n;
    scanf("%d",&n);
    for(int i = 0; i < n; i++){
        int k;
        double cont = 0;
        scanf("%d",&k);
        string letter;
        vector <float> cost;
        string character;
        double value;
        for(int j = 0; j < k; j++){
            cin >> character >> value;
            letter.append(character);
            cost.push_back(value/100);
        }
        int var;
        cin >> var;
        string line;
        for (int j = 0; j < var; j++){
            getline(cin, line);
            if (line == "\0"){getline(cin,line);}
            for (int z = 0; z < line.size(); z++){
                int c;
                c = letter.find(line[z], 0);
                if (c >= 0){cont+= cost[c];}
            }
        }
        printf("%0.2lf$\n",cont);
    }
    return 0;
}

