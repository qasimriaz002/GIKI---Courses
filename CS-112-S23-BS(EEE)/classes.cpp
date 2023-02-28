#include <iostream>

using namespace std;

class Person{
    
    private:
        string person_name;
        int person_age;
        string person_city;
    
    public:
        void set_personName(string name){
            person_name = name;
        }
        void set_personAge (int age){
            person_age = age;
        }
        void set_personCity(string city){
            person_city = city;
        }

        string get_personName(){
            return person_name;
        }
        int get_personAge (){
            return person_age;
        }
        string get_personCity(){
            return person_city;
        }

        void introduce_person(){
            cout<<"My name is: "<<person_name<<endl;
            cout<<"My age is: "<<person_age<<endl;
            cout<<"I live in: "<<person_city<<endl;
            }

        void introduce_person(int y){
            cout<<"My name is: "<<person_name<<endl;
            cout<<"My age is: "<<person_age<<endl;
            cout<<"I live in: "<<person_city<<endl;
            cout<<"Add new value"<<y<<endl;
            }

};

int main(){

    Person p1;

    p1.set_personName("Usman");
    p1.set_personAge(34);
    p1.set_personCity("Lahore");
    p1.introduce_person();
    p1.introduce_person(4);

    // int x = 
    cout<<p1.get_personAge();

    return 0;
}