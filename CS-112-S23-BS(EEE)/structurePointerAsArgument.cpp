#include <iostream>
using namespace std;
// creating a function that takes as variable as pointers in its argument

struct Student {
  string name;
  int marks;
};

void myfunction(Student *ptr){
    // *ptr->name
    cout<<"Printing value of a structure from a function: ";
    cout<<ptr->name<<endl;
    cout<<ptr->marks<<endl;
    // cout<<"Printing value from a function: "<<*ptr<<endl;
}

// int *ptr = x;

int main(){
    Student s1;
    s1.name = "Usman";
    s1.marks = 20;
    cout<<"Printing value of a structure from main function: ";
    cout<<s1.name<<endl;
    cout<<s1.marks<<endl;
    myfunction(&s1);


    return 0;
}