#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false); // 입출력 속도 향상을 위한 설정
    cin.tie(NULL);

    int n;
    cin >> n;

    // 숫자의 범위가 1부터 10,000까지이므로 10,001 크기의 배열을 생성
    int count[10001] = {0};

    // 숫자의 빈도 수를 카운트
    for (int i = 0; i < n; i++) {
        int number;
        cin >> number;
        count[number]++;
    }

    // 카운트 배열을 사용하여 정렬된 숫자 출력
    for (int i = 1; i <= 10000; i++) {
        while (count[i] > 0) {
            cout << i << '\n';
            count[i]--;
        }
    }

    return 0;
}
