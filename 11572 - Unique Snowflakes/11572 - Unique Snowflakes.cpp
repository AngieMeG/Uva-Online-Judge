#include <bits/stdc++.h>
using namespace std;
int main(){
    map <int, bool> dic;
    deque <int> q;
    int cases,res, cant, snowflake;
    scanf("%d",&cases);
    while (cases--){
        scanf("%d",&cant);
        dic.clear();
        q.clear();
        res = 0;
        while (cant--){
            scanf("%d",&snowflake);
            if (dic.find(snowflake) == dic.end() || dic[snowflake] == false){
                dic[snowflake] = true;
                q.push_back(snowflake);
            }
            else{
                res = max(res, (int)q.size());
                q.push_back(snowflake);
                while (dic[snowflake]){
                    dic[q.front()] = false;
                    q.pop_front();
                }
                dic[snowflake] = true;
            }
            res = max(res, (int)q.size());
        }
        printf("%d\n", res);
    }
    return 0;
}
