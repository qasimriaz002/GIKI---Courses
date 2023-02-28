#include <iostream>

using namespace std;

//  void SumNum(int n1, int n2){
//             cout<<n1+n2;
//         }
//  void SumNum(int n1, int n2, int n3){
//             cout<<n1+n2+n3;
//         }

class Person{
    
    public:
        string person_name;
        int person_age;
        string person_city;

        
        Person(const Person &p){
            person_name = p.person_name;
            person_city = p.person_city;
            person_age = p.person_age;
        }

        Person(){
            cout<<"An Object is created"<<endl;
            person_name = "Any Name";
            person_age = 45;
            person_city = "Any City";
        }

        void introduce_person(){
            cout<<"My name is: "<<person_name<<endl;
            cout<<"My age is: "<<person_age<<endl;
            cout<<"I live in: "<<person_city<<endl;
        }

};

int main(){
    // SumNum(2,3,5);
    // SumNum(2,3,5);

    Person p1;
    p1.person_name = "Usman";
    p1.person_age = 20;
    p1.person_city = "Isb";

    p1.introduce_person();

    Person p2 = p1;
    
    // Person p2(p1);
    p2.introduce_person();


    return 0;
}