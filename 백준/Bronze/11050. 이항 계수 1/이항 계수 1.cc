#include<iostream>
using namespace std;

int fact(int a){
    int ans =1 ;
    for(int i=a; i>0; i--){
        ans *= i;
    }
    return ans;
}

int main()
{
    int n, k;
    cin >> n >> k;
    
    int ans = fact(n)/(fact(n-k)*fact(k));
    
    cout << ans << endl;
}