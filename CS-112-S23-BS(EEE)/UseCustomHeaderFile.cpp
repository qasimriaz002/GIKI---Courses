#include "Student.h"
#include <iostream>

using namespace std;

int main(){

    Student s1;

    s1.percentage = 30.1;
    s1.roll_number = 12;

    cout<<"Percentage: "<<endl;
    cout<<s1.percentage<<endl;
    cout<<"Roll Number"<<endl;
    cout<<s1.roll_number<<endl;

    return 0;
}