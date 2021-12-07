#include <iostream>
using namespace std;
int main()
{
  int n;
  cout<<"Enter a number: "; 
  cin>>n;
  if(n==0)
    cout<<"The number is Zero"; 
  else if(n>0)
    cout<<"The number is Positive";
  else
    cout<<"The number is Negative";
}