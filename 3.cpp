#include <iostream>
#include <cmath>
#include <functional>
#define EPS 1E-9

using namespace std;

double derivative(function<double(double)> f, double x0)
{
    double h = EPS;
    return (f(x0+h) - f(x0-h))/(h*2);
}

double newton_solve_m(function<double(double)> f, double x, int n)
{
    double xp, k = derivative(f, x);
    while(n--) { 
        xp = x;
        x -= f(x)/k;
    }
    cout<< "|Xn - Xn-1| = " << abs(x - xp) << "\n|f(Xn)| = "<< abs(f(x))<<endl;
    return x;
}

int main()
{
    function<double(double)> f1 = [](double x){
        return x*x*x-0.2*x*x-0.2*x-1.2;
    };
    function<double(double)> f2 = [](double x){
        return x*x*x-4*x*x+10*x-4;
    };
    function<double(double)> f3 = [](double x){
        return sin(x)+x*x/100-15;
    };
    cout<<"Result f1: (n = 15, x0 = 1)\n"<<newton_solve_m(f1, 1, 15)<<endl;
    cout<<"Result f2: (n = 10, x0 = 0)\n"<<newton_solve_m(f2, 0, 10)<<endl;
    cout<<"Result f3: (n = 30, x0 = 0)\n"<<newton_solve_m(f3, 0, 30)<<endl;
}






