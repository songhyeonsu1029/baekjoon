#include<iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int count = 1;
    int first = 1;
    int last = 1;
    
    while(true){
        if(first<=n && n<=last){
            cout << count;
            break;
        }
        count++;
        first = last +1;
        last += 6*(count-1);
    }
}