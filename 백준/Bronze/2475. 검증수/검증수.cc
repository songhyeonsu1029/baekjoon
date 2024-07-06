#include<iostream>
using namespace std;

int main()
{
    int num;
    int sum = 0;
    int ans;
    for(int i=0; i<5; i++){
        cin >> num;
        
        sum += num * num;
    }
    ans = sum%10;
    cout << ans << endl;
    return 0;
}