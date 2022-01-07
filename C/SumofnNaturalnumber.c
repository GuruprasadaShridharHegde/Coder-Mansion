#include<stdio.h>
int main()
{
    int sum=0,n;
    printf("Enter the first N Natural Number\n");
    scanf("%d",&n);
    sum=(n*(n+1))/2;
    printf("sum is %d",sum);
    return 0;
}