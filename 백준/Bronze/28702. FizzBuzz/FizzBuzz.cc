#include<iostream>
#include<string>
#include<cctype>
using namespace std;

int main()
{
    string str1, str2, str3;

    // 각 문자열을 한 줄씩 입력 받기
    cin >> str1;
    cin >> str2;
    cin >> str3;
    
    int result =0;
    
    if(isdigit(str1[0])){
        int num1 = stoi(str1);
        result = num1 + 3;
    }else if(isdigit(str2[0])){
        int num2 = stoi(str2);
        result = num2 + 2;
    }else if(isdigit(str3[0])){
        int num3 = stoi(str3);
        result = num3 + 1;
    }
    
    if (result % 3 == 0 && result % 5 == 0) {
        cout << "FizzBuzz" << endl;
    } else if (result % 3 == 0) {
        cout << "Fizz" << endl;
    } else if (result % 5 == 0) {
        cout << "Buzz" << endl;
    } else {
        cout << result << endl;
    }

    return 0;
}