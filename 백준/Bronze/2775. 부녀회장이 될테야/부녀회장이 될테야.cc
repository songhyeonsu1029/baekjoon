#include<iostream>
using namespace std;

int getnum(int x, int y){
    if(y == 1) return 1;
    else if(x == 0) return y;
    else return getnum(x,y-1) + getnum(x-1,y);
}

int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++){
        int k, n;
        cin >> k;
        cin >> n;
        cout << getnum(k,n) << endl;
    }
}