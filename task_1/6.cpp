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

void write_csv(matrix a, string str)
{
    if (a.size()!=2) return;
    fstream fout;
    fout.open(str, ios::out | ios::trunc);
    fout.precision(16);
    for (int i =0; i<a[0].size(); ++i) fout<<a[0][i]<<","<<a[1][i]<<"\n";
    fout.close();
}

vector<vector<double>> generate_points(double x0, double x1, double y_min, double y_max, int n)
{
    vector<double> vx(n+1, 0);
    vector<double> vy(n+1, 0);
    int h = y_max - y_min;
    for (int i = 0; i<n+1; ++i){
        vx[i] = x0 + i*(x1-x0)/n;
        vy[i] = y_min + rand()/(double(RAND_MAX) + 1.0) * h;
    }
    return (vector<vector<double>>){vx, vy};
}

vector<vector<double>> gen_points_from_func(function<double(double)> f, double x0, double x1, int n)
{
    vector<double> vx(n+1, 0);
    vector<double> vy(n+1, 0);
    for (int i = 0; i<n+1; ++i){
        vx[i] = x0 + i*(x1-x0)/n;
        vy[i] = f(vx[i]);
    }
    return (vector<vector<double>>){vx, vy};
}

double integrate(function<double(double)>* f, double x0, double x1)
{
    cout<<"start\n";
    double h = 0.0000001, s = 0;
    while(x0+h<=x1){
        s += (f[0](x0)*f[1](x0)*f[2](x0)+f[0](x0+h)*f[1](x0+h)*f[2](x0+h))/2*h;
        x0+=h;
    }
    cout<<"finish\n"<<endl;
    return s;
}

void rms_approximation(function<double(double)> f)
{
    vector<function<double(double)>> func = {
        [](double x){return 1/sqrt(M_PI);},
        [](double x){return x*sqrt(2/M_PI);},
        //[](double x){return (2*pow(x, 2)-1)*sqrt(2/M_PI);},
        //[](double x){return (4*pow(x, 3)-3*x)*sqrt(2/M_PI);},
        //[](double x){return (8*pow(x, 4)-8*pow(x, 2)+1)*sqrt(2/M_PI);}
    };
    function<double(double)> ro = [](double x){ return 1/pow(1-x*x, 0.5); };
    vector<double> a(func.size(), 0);
    for (int i = 0; i<func.size(); ++i){
        function<double(double)> vectf[] = {func[i], ro, f};
        a[i] = integrate(vectf, -1+0.00000001, 1-0.00000001);
    }
    double k = 10000;
    matrix result(2, vector<double>(k,0));
    double x0 = -1, x1 = 1;
    for (int i = 0; i<k; ++i){
        double x = x0+i*(x1-x0)/(k), y = 0;
        for (int j = 0; j<func.size(); ++j) y += func[j](x)*a[j];
        result[0][i] = x;
        result[1][i] = y;
    }
    write_csv(result, "result_points.csv");
}

int main()
{
    function<double(double)> f3 = [](double x){
        return 1.5*cos(300*x)+4*sin(4*x)+sin(x*25)+(40-x*x/100);
    };
    rms_approximation(f3);
    return 0;
}

