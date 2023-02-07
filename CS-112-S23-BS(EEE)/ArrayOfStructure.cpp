// Here in this code we will see how we can create arrays inside the structure
#include <iostream>
using namespace std;
// Creation of a structure named as Student with an array and a variable
struct Student {
  string name;
  int marks[3];
};

int main() {
// Creting 's' as type of student and then adding values to marks array using the s.marks[index] using index of s.
    Student s[2];

    s[0].name = "John";
    s[0].marks[0] = 85;
    s[0].marks[1] = 90;
    s[0].marks[2] = 95;

    s[1].name = "Jane";
    s[1].marks[0] = 80;
    s[1].marks[1] = 70;
    s[1].marks[2] = 60;

    for (int i = 0; i < 2; i++) {
        cout << s[i].name << " scored marks ";
        for (int j = 0; j < 3; j++) {
        cout << s[i].marks[j] << " ";
        }
        cout << endl;
    }

  return 0;
}



