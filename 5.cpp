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

vector<double> jordan_gauss(matrix a, vector<double> f)
{
    int n = a.size();
    if (n!=f.size() || n!=a[0].size()){
        std::cout<<"Invalid sizes of matrices"<<std::endl;
        return vector<double>();
    }

    for (int i = 0; i<n; ++i) {
        int k = i;
        for (int j = i+1; j<n; ++j)
            if (std::abs(a[j][i]) > std::abs(a[k][i])) k = j;
        if (std::abs(a[k][i])<EPS) {
            std::cout<<std::abs(a[k][i])<<std::endl;
            std::cout<<"Non-invertible matrix"<<std::endl;
            return vector<double>();
        }
        std::swap(a[i], a[k]);
        std::swap(f[i], f[k]);
        f[i]/=a[i][i]; 
        for (int j = n-1; j>=0; --j) a[i][j]/=a[i][i]; 
        for (int j = i+1; j<n; ++j){
            f[j] -= f[i]*a[j][i];
            for (int t = n-1; t>=i; --t) a[j][t] -= a[i][t]*a[j][i];
        }
        for (int j = i-1; j>=0; --j){
            f[j] -= f[i]*a[j][i];
            for (int t = n-1; t>=i; --t) a[j][t] -= a[i][t]*a[j][i];
        }
    }
    return f;
}

void write_csv(matrix a, string str)
{
    if (a.size()!=2) return;
    fstream fout;
    fout.open(str, ios::out | ios::trunc);
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

void trig_interpolation(vector<vector<double>> points)
{
    int n = points[0].size();
    matrix a(n, vector<double>(n, 1));
    vector<double> f(n);
    for (int i = 0; i<n; ++i){
        for (int j = 1; j<n; ++j){
            a[i][j] = cos(points[0][i]*j);
        }
    }
    f = jordan_gauss(a, points[1]);
    int k = 100;
    matrix result(2, vector<double>(k*n));
    double x0 = points[0][0], x1 = points[0][n-1];
    for (int i = 0; i<n*k; ++i){
        double y = f[0], x = x0+i*(x1-x0)/(k*n);
        for (int j = 1; j<n; ++j) y += cos(j*x)*f[j];
        result[0][i] = x;
        result[1][i] = y;
    }
    write_csv(result, "result_points.csv");
}

int main()
{
    srand (time(NULL));

    // matrix points = generate_points(0, 5, -3, 3, 10);
    // write_csv(points, "init_points.csv");
    // trig_interpolation(points);

    function<double(double)> f3 = [](double x){
        return sin(x+2.5)*(10-x);
    };
    matrix points = gen_points_from_func(f3, 0, 10, 10);
    write_csv(points, "init_points.csv");
    trig_interpolation(points);

    return 0;
}

