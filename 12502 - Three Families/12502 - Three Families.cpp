#include <bits/stdc++.h>
#define in() freopen("in.txt","r",stdin)
#define out() freopen("out.txt","w",stdout)
#define err() freopen("err.txt","w",stderr)

using namespace std;

int main() {
    int cases, family_a, family_b, payment;
    scanf("%d", &cases);
    for (int i = 0; i < cases; i++){
        scanf("%d %d %d", &family_a, &family_b, &payment);
        int total = (payment* ((3*family_a) - family_a - family_b))/(family_a + family_b);
        printf("%d\n", total > 0 ? total : 0);
    }
    return 0;
}
