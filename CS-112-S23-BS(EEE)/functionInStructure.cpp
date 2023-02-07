#include <iostream>
using namespace std;

struct Student {
  string name;
  int marks;
  void print() {
    cout << name << " scored marks " << marks << endl;
  }
};

void myfunction1 (Student s){
  cout<<"I am calling structure containing a function and two variables in aother function"<<endl;
  s.print();
}

int main() {
  Student s1;
  s1.name = "John";
  s1.marks = 85;

  s1.print();

  Student s2;
  s2.name = "Usman";
  s2.marks = 25;

  s2.print();
  cout<<"-------------------------"<<endl;
  myfunction1(s2);

  return 0;
}


