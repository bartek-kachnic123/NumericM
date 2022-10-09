#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;


void SolveA() {
    const float X = 0.2;
    float Dh = 0.0;
    const float h = pow(2, -16);
    float a = pow(2, -16);
    float b = pow(2, -2);

    ofstream fout;
    fout.open("results.csv", ios::trunc);
    fout << "h" << ";" << "E(h)" << endl;
    while (a <= b) 
    {
        Dh = (sin(X+a) - sin(X) ) / a;
        fout << a << ";" << fabs(Dh - cos(X)) << endl;
        a += h;
    }
    fout.close();
    
}

void SolveA_d() {
    const double X = 0.2;
    double Dh = 0.0;
    const double h = pow(2, -16);
    double a = pow(2, -16);
    double b = pow(2, -2);

    ofstream fout;
    fout.open("results1_d.csv", ios::trunc);
    fout << "h" << ";" << "E(h)" << endl;
    while (a <= b) 
    {
        Dh = (sin(X+a) - sin(X) ) / a;
        fout << a << ";" << fabs(Dh - cos(X)) << endl;
        a += h;
    }
    fout.close();
    
}

void SolveB() {
    const float X = 0.2;
    float Dh = 0.0;
    const float h = pow(2, -16);
    float a = pow(2, -16);
    float b = pow(2, -2);

    ofstream fout;
    fout.open("results2.csv", ios::trunc);
    fout << "h" << ";" << "E(h)" << endl;
    while (a <= b) 
    {
        Dh = (sin(X+a) - sin(X-a) ) / 2*a;
        fout << a << ";" << fabs(Dh - cos(X)) << endl;
        a += h;
    }
    fout.close();
    
}


int main() {
    SolveA();
    SolveA_d();
    //SolveB();
    




    return 0;
}