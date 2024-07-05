#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t;
    string s;
    
    cin >> t;
    for(int i=0; i<t; i++){
        cin >> s;
        int sum = 0;
        int count =1;
        for(int j=0; j<s.length(); j++){
            if(s[j]=='O') sum += count++;
            else if(s[j]=='X') count = 1;
        }
        cout << sum << '\n';
    }
    return 0;
}