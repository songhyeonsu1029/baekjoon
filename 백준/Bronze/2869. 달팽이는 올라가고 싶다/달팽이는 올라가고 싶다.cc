#include<iostream>
using namespace std;

int main()
{
    int a, b, v;
    cin >> a >> b >> v;
    
    v = v-a;
    int count = v / (a-b);
    if(v%(a-b) == 0){
        count += 1;
    }else count += 2;
    cout << count << endl;
}