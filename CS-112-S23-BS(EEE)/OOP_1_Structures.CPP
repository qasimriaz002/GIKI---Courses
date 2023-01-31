#include <iostream>

using namespace std;

// We are creating a sample structure to represent an human.

struct human
{
    /* data */
    string h_name;
    int h_age;

};

int main(){
    // Creating multipal humans in main.

    human h1, h2;                   //Declayring 2 different humans h1, h2
    
    h1.h_name = "Usman";            //Initializing h1 by adding values to its variables
    h1.h_age = 51;

    h2.h_name = "Hassan";           //Initializing h1 by adding values to its variables
    h2.h_age = 13; 

    human h3 = {"Qasim", 15};       //Declayraiton and initilization at same step for h3.

    // Getting data out of structures

    cout<<"--------------"<<endl;
    cout<<"First Human"<<endl;
    cout<<"--------------"<<endl;
    cout<<"Name: "<<h1.h_name<<endl<<"Age: "<<h1.h_age<<endl;

    cout<<"--------------"<<endl;
    cout<<"Second Human"<<endl;
    cout<<"--------------"<<endl;
    cout<<"Name: "<<h2.h_name<<endl<<"Age: "<<h2.h_age<<endl;

    cout<<"--------------"<<endl;
    cout<<"Third Human"<<endl;
    cout<<"--------------"<<endl;
    cout<<"Name: "<<h3.h_name<<endl<<"Age: "<<h3.h_age<<endl;

    return 0;
}