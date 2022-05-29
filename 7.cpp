#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <functional>
#define matrix vector<vector<double>>
#define EPS 10E-12

using namespace std;

class MyFunc
{
    private:
        int size;
        function<double(vector<double>)> f;
    public:
        MyFunc(int size, function<double(vector<double>)> f): f(f), size(size){}

        int get_size(){return size;}

        double value(vector<double> x)
        {
            if (x.size() == size){
                return f(x);
            } else {
                return 0;
            }
            
        }
};

double integrate_1(MyFunc f)
{
    int n = f.get_size();
    double u = sqrt(n/3.0), a = pow(2, n-1)/n, res = 0;
    vector<double> x(n, 0);
    for (int i = 0; i<n; ++i){
        x[i] = u;
        res += a*f.value(x);
        x[i] = -u;
        res += a*f.value(x);
        x[i] = 0;
    }
    return res;
}


int main()
{
    MyFunc f1(1, [](vector<double> x){ return cos(x[0])+sin(2*x[0]); });
    MyFunc f2(2, [](vector<double> x){ return 1/(x[0]*x[0]+1)+cos(x[1]); });
    MyFunc f3(3, [](vector<double> x){ return cos(x[0])+sin(2*x[1])-1/(x[2]*x[2]+5); });
    MyFunc f4(4, [](vector<double> x){ return x[0]*x[0]+2*x[1]-6*x[2]*x[2]-x[3]+1; });
    MyFunc f5(4, [](vector<double> x){ return (x[0]+x[1]+1)/(x[2]*x[2]+10-x[3]); });
    fstream fout; fout.precision(100);
    fout.open("integrate_results.csv", ios::out | ios::trunc);
    fout<<integrate_1(f1)<<"\n";
    fout<<integrate_1(f2)<<"\n";
    fout<<integrate_1(f3)<<"\n";
    fout<<integrate_1(f4)<<"\n";
    fout<<integrate_1(f5)<<"\n";
    fout.close();
}