#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#define matrix std::vector<std::vector<double>>
#define vect std::vector<double>
#define EPS 1E-9

void print(matrix a)
{
    for (int i = 0; i<a.size(); ++i){
        for (int j = 0; j<a[0].size(); ++j){
            std::cout<<a[i][j]<<" ";
        }
        std::cout<<std::endl;
    }
    std::cout<<std::endl;
}

void print(vect a)
{
    for (int i = 0; i<a.size(); ++i){
        std::cout<<a[i]<<std::endl;
    }
    std::cout<<std::endl;
}

matrix matrix_mul(const matrix &a, const matrix &b)
{
    int m1 = a.size(), n1 = a[0].size(), m2 = b.size(), n2 = b[0].size();
    if (n1!=m2) {
        std::cout<<"Invalid sizes in matrix_mul"<<std::endl;
        return matrix();
    }
    matrix result(m1, std::vector<double>(n2));
    for (int i = 0; i<m1; ++i){
        for (int j = 0; j<n2; ++j)
            for (int k = 0; k<n1; ++k) result[i][j] += a[i][k]*b[k][j];
    }
    return result;
}

vect matrix_vect_mul(const matrix &a, const vect &b)
{
    int m1 = a.size(), n1 = a[0].size();
    if (n1!=b.size()) {
        std::cout<<"Invalid sizes in matrix_vect_mul"<<std::endl;
        return vect();
    }
    vect result(m1, 0);
    for (int i = 0; i<m1; ++i){
            for (int k = 0; k<n1; ++k) result[i] += a[i][k]*b[k];
    }
    return result;
}

double matrix_norm(const matrix &a, const matrix &b)
{
    double norm2 = 0;
    if (a.size()!=b.size() || a[0].size()!=b[0].size()) {
        std::cout<<"Invalid sizes in matrix_norm"<<std::endl;
        return -1;
    }
    for (int i = 0; i<a.size(); ++i)
        for (int j = 0; j<a[0].size(); ++j)
            norm2 += (a[i][j]-b[i][j])*(a[i][j]-b[i][j]);
    return std::sqrt(norm2);
}

double vect_norm(const vect &a, const vect &b)
{
    double norm2 = 0;
    if (a.size()!=b.size()) {
        std::cout<<"Invalid sizes in vect_norm"<<std::endl;
        return -1;
    }
    for (int i = 0; i<a.size(); ++i)
            norm2 += (a[i]-b[i])*(a[i]-b[i]);
    return std::sqrt(norm2);
}

bool check_convergence(const matrix &a)
{
    double temp;
    for (int i = 0; i<a.size(); ++i){
        temp = 0;
        for (int j = 0; j<a[i].size(); ++j){
            if (i!=j) temp += std::abs(a[i][j]);
        }
        if (a[i][i]<=temp){
            std::cout<<"Not convergence"<<std::endl;
            return false;
        } 
    }
    return true;
}

std::vector<double> zeidel_nekrasov(const matrix &a, const vect &f, int n)
{
    int m = a.size();
    if (m!=a[0].size() || m!=f.size() || !check_convergence(a)) {
        std::cout<<"Invalid inputs in zeidel_nekrasov"<<std::endl;
        return vect();
    }
    vect x = vect(m, 0);
    for (int k = 0; k<n; ++k){
        for (int i = 0; i<m; ++i){
            x[i] = f[i];
            for (int j = 0; j<i; ++j) x[i] -= a[i][j]*x[j];
            for (int j = i+1; j<m; ++j) x[i] -= a[i][j]*x[j];
            x[i]/=a[i][i];
        }
    }
    return x;
}

int main()
{
    matrix a = {{1, 0.17, -0.25, 0.54},
                {0.47, 1.00, 0.07, -0.32},
                {-0.11, 0.35, 2, -0.24},
                {0.15, 0.43, 0.36, 1}};

    vect f = {1.00, 0.42, 0.54,  0.66};
    int n = 25;
    vect result = zeidel_nekrasov(a, f, n);
    if (result.size()!=0){
        std::cout<<std::endl;
        std::cout<<"Number of iterations: "<<n<<std::endl;
        std::cout<<"Calculation result: (vector X)"<<std::endl;
        print(result);
        std::cout<<"Product of matrices A and X: (it is matrix f)"<<std::endl;
        print(matrix_vect_mul(a, result));
        std::cout<<"Matrix difference norm: ";
        std::cout<<vect_norm(f, matrix_vect_mul(a, result))<<std::endl<<std::endl;
    }
    std::cout<<std::endl;
    for (int i = 1; i<13; ++i){
        vect result = zeidel_nekrasov(a, f, 2*i+1);
        std::cout<<"Number of iterations: "<<2*i+1<<"; Matrix difference norm: ";
        std::cout<<vect_norm(f, matrix_vect_mul(a, result))<<std::endl;
    }
    return 0;
}