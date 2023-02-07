// Here in this code we will see how we can create arrays inside the structure
#include <iostream>
using namespace std;
// Creation of a structure named as Student with an array and a variable
struct Student {
  string name;
  int marks[3];
};

int main() {
// Creting 's' as type of student and then adding values to array using the s.marks[index]
  Student s;
  s.name = "John";
  s.marks[0] = 85;
  s.marks[1] = 90;
  s.marks[2] = 95;
  cout << s.name << " scored marks ";
  for (int i = 0; i < 3; i++) {
    cout << s.marks[i] << " ";
  }
  cout << endl;
  return 0;
}


