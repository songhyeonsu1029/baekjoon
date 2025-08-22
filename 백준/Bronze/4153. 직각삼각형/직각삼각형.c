int main(void){

    int a, b, c;

    while(1)
    {
        scanf("%d %d %d", &a, &b, &c);
        if(a == 0 && b == 0 && c == 0){
            break;
        }
        
        if(a < b){
            int max = b;
            b = a;
            a = max;
        }
        if(a < c){
            int max = c;
            c = a;
            a = max;
        }

        if(a*a == b*b + c*c){
            printf("right\n");
        }else
            printf("wrong\n");
    }
    
    return 0;
}