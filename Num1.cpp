#include <iostream>
#include <cmath>
#include <fstream>
#include <unistd.h>
#define H_START 0.5
#define H_LIMIT 10e-20
#define X_VALUE 0.2
using namespace std;


void SolveA_f(const float X) {
    float Dh = 0.0;
    float h = H_START;
    string filename = "resultsA_f.csv";

    ofstream fout;
    fout.open(filename, ios::trunc);
    fout << "h" << ";" << "E(h)" << endl;
    while (h > H_LIMIT) 
    {
        Dh = (sin(X+h) - sin(X) ) / h;
        fout << h << ";" << fabs(Dh - cos(X)) << endl;
        h = 0.8 * h;
    }
    fout.close();
    cout << "Pomyslnie zapisano do pliku " << filename << "!" << endl;
    sleep(1);

    
}

void SolveA_d(const double X) {
    double Dh = 0.0;
    double h = H_START;
    string filename = "resultsA_d.csv";

    ofstream fout;
    fout.open(filename, ios::trunc);
    fout << "h" << ";" << "E(h)" << endl;
    while (h > H_LIMIT) 
    {
        Dh = (sin(X+h) - sin(X) ) / h;
        fout << h << ";" << fabs(Dh - cos(X)) << endl;
        h = 0.8 * h;
    }
    fout.close();
    cout << "Pomyslnie zapisano do pliku " << filename << "!" << endl;
    sleep(1);

    
}

void SolveB_f(const float X) {
    float Dh = 0.0;
    float h = H_START;
    string filename = "resultsB_f.csv";

    ofstream fout;
    fout.open(filename, ios::trunc);
    fout << "h" << ";" << "E(h)" << endl;
    while (h > H_LIMIT) 
    {
        Dh = (sin(X+h) - sin(X-h) ) / (2*h);
        fout << h << ";" << fabs(Dh - cos(X)) << endl;
        h = 0.8 * h;
    }
    fout.close();
    cout << "Pomyslnie zapisano do pliku " << filename << "!" << endl;
    sleep(1);
    

}

void SolveB_d(const double X) {
    double Dh = 0.0;
    double h = H_START;
    string filename = "resultsB_d.csv";

    ofstream fout;
    fout.open(filename, ios::trunc);
    fout << "h" << ";" << "E(h)" << endl;
    while (h > H_LIMIT) 
    {
        Dh = (sin(X+h) - sin(X-h) ) / (2*h);
        fout << h << ";" << fabs(Dh - cos(X)) << endl;
        h = 0.8 * h;
    }
    fout.close();
    cout << "Pomyslnie zapisano do pliku " << filename << "!" << endl;
    sleep(1);
    
}

char menu() {
    cout << "------------------------"<<endl;
    cout <<"-----------Menu----------"<<endl;
    cout <<"Wybierz wzor oraz typ: "<<endl;
    cout <<"1.Dh = (sin(x+h) - sin(x)) / h   (FLOAT)" << endl;
    cout <<"1.Dh = (sin(x+h) - sin(x)) / h   (DOUBLE)" << endl;
    cout <<"3.Dh = (sin(x+h) - sin(x-h)) / (2*h)  (FLOAT)"<< endl;
    cout <<"4.Dh = (sin(x+h) - sin(x-h)) / (2*h)  (DOUBLE)"<< endl;
    cout <<"5. Wyjscie z programu "<< endl;
    cout << "Twoj wybor: ";
    char choice;
    cin >> choice;
    return choice;
}

int main() {
    while(1)
    {
        switch(menu())
        {
            case '1':
                SolveA_f(X_VALUE);
                break;
            case '2':
                SolveA_d(X_VALUE);
                break;
            case '3':
                SolveB_f(X_VALUE);
                break;
            case '4':
                SolveB_d(X_VALUE);
                break;
            case '5':
                cout <<"Koniec programu!"<<endl;
                exit(0);
            default:
                cout << "Wybrano niedostepna opcje!" << endl;

        }
    }
    

    
    




    return 0;
}