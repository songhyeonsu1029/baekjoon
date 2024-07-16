#include<iostream>
#include<string>
using namespace std;

int main()
{
    int n;
    string str;
    cin >> n;
    cin >> str;
    long long r = 31;
    long long R = 1;
    long long m = 1234567891;
    long long hash =0;
    
    for(int i=0; i<str.length(); i++){
        hash += ((str[i] - 'a' + 1)*R)%m;
        R *= r;
    }
    cout << hash;
}