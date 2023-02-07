#include <iostream>
using namespace std;
// creating a function that takes as variable as pointers in its argument

void myfunction(int *ptr, int n){
    *ptr = 20;
    n = 100;
    cout<<"Printing address from a function: "<<ptr<<endl;
    cout<<"Printing value from a function: "<<*ptr<<endl;
}

// int *ptr = x;

int main(){
    int x = 10;
    int y = 90;
    myfunction(&x,y);
    cout<<"Printing value of x form main function: "<<x<<endl;

    cout<<"Printing value of y form main function: "<<y<<endl;

    return 0;
}