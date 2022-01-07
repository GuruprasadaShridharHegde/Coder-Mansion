#include<iostream>
using namespace std;
int main() 
{ 
    //for initialize variable
    int Number, i, Sum = 0;
    //to take user input
    cout<<"\n Kindly Insert an Integer Variable\n"; cin>>Number;

    //use for loop for these condition
    for(i = 1; i <= Number; i++)
    {
       Sum = Sum + i;
    }

    //display
    cout<<"Sum of Natural Numbers: "<< Sum;

    return 0;
}