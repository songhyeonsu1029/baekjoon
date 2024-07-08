#include<iostream>
using namespace std;

int main()
{
    int n;
    int count = 0;
    cin >> n;
    
    for(int i=0; i<n; i++){
        int num;
        bool flag = false;
        cin >> num;
        if(num == 1) continue;
        for(int j=2; j<num; j++){
            if(num%j == 0){
                flag = true;
                break;
            }
        }            
        if(!flag) count++;
    }
    cout << count << endl;
}