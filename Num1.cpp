#include <iostream>
#include <cmath>
#include <fstream>
#include <unistd.h>
#include <limits>
#define H_START 0.5
#define H_LIMIT 10e-20
#define X_VALUE 0.2
using namespace std;


void SolveA_f(const float x, string filename, const float hIteration=0.80) {
    float Dh = 0.0, E = 0.0;
    float h = H_START;
    float lowestE=1.0, optimalH=0.0;

    ofstream fout;
    fout.open(filename, ios::trunc);
    fout << "h" << ";" << "E(h)" << endl;
    while (h > H_LIMIT) 
    {
        Dh = (sin(x+h) - sin(x) ) / h;
        E = fabs(Dh - cos(x));
        fout << h << ";" << E << endl;

        if (lowestE > E ) {
            lowestE = E;
            optimalH = h;
        }

        h = hIteration * h;
        
    }
    fout.close();
    cout << "Najmniejszy blad wynosi E(h) = " << lowestE << " dla h = " << optimalH << "!" << endl;
    cout << "Wyniki pomyslnie zapisano do pliku " << filename << "!" << endl;
    sleep(1);

    
}

void SolveA_d(const double x, string filename, const double hIteration=0.80) {
    double Dh = 0.0, E = 0.0;
    double h = H_START;
    double lowestE=1.0, optimalH = 0.0; 

    ofstream fout;
    fout.open(filename, ios::trunc);
    fout << "h" << ";" << "E(h)" << endl;
    while (h > H_LIMIT) 
    {
        Dh = (sin(x+h) - sin(x) ) / h;
        E = fabs(Dh - cos(x));

        fout << h << ";" << E << endl;

        if (lowestE > E ) {
            lowestE = E;
            optimalH = h;
        }

        h = hIteration * h;
    }
   
    fout.close();
    cout << "Najmniejszy blad wynosi E(h) = " << lowestE << " dla h = " << optimalH << "!" << endl;

    cout << "Wyniki pomyslnie zapisano do pliku " << filename << "!" << endl;
    sleep(1);

    
}

void SolveB_f(const float x, string filename, const float hIteration=0.8) {
    float Dh = 0.0, E=0.0;
    float h = H_START;
    float lowestE=1.0, optimalH=0.0;


    ofstream fout;
    fout.open(filename, ios::trunc);
    fout << "h" << ";" << "E(h)" << endl;
    while (h > H_LIMIT) 
    {
        Dh = (sin(x+h) - sin(x-h) ) / (2*h);
        E = fabs(Dh - cos(x));

        fout << h << ";" << E << endl;

        if (lowestE > E ) {
            lowestE = E;
            optimalH = h;
        }
        h = hIteration * h;
    }
    fout.close();
    cout << "Najmniejszy blad wynosi E(h) = " << lowestE << " dla h = " << optimalH << "!" << endl;
    cout << "Pomyslnie zapisano do pliku " << filename << "!" << endl;
    sleep(1);
    

}

void SolveB_d(const double x, string filename, const double hIteration = 0.80) {
    double Dh = 0.0, E = 0.0;
    double h = H_START;
    double lowestE=1.0, optimalH = 0.0;


    ofstream fout;
    fout.open(filename, ios::trunc);
    fout << "h" << ";" << "E(h)" << endl;
    while (h > H_LIMIT) 
    {
        Dh = (sin(x+h) - sin(x-h) ) / (2*h);
        E = fabs(Dh - cos(x));

        fout << h << ";"<< E << endl;

        if (lowestE > E ) {
            lowestE = E;
            optimalH = h;
        }
        h = hIteration * h;
    }
    fout.close();
    cout << "Najmniejszy blad wynosi E(h) = " << lowestE << " dla h = " << optimalH << "!" << endl;
    cout << "Wyniki pomyslnie zapisano do pliku " << filename << "!" << endl;
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
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // clear buffer
    
    return choice;
}

int main(int argc, char *argv[]) {

    if (argc != 5)
    {
        cerr << "Wrong number of args!" << endl;
        exit(1);
    }
    while(1)
    {
        switch(menu())
        {
            case '1':
                SolveA_f(X_VALUE, argv[1]);
                break;
            case '2':
                SolveA_d(X_VALUE, argv[2]);
                break;
            case '3':
                SolveB_f(X_VALUE, argv[3]);
                break;
            case '4':
                SolveB_d(X_VALUE, argv[4]);
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