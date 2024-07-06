#include <iostream>
using namespace std;

int main()
{
    int t;
    int h, w, n;
    
    cin >> t;
    for(int i=0; i<t; i++){
        int xx, yy;
        cin >> h >> w >> n;
        if(n%h == 0){
            yy = h;
            xx = n/h;
        }else{
            yy = n%h;
            xx = n/h + 1;
        }
        int result = yy*100+xx;
        cout << result << endl;
    }
    return 0;
}