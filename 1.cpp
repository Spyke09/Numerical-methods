#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#define matrix std::vector<std::vector<double>>
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

matrix jordan_gauss(matrix a, matrix f)
{
    int n = a.size(), l = f[0].size();
    if (n!=f.size() || n!=a[0].size()){
        std::cout<<"Invalid sizes of matrices"<<std::endl;
        return matrix();
    }

    for (int i = 0; i<n; ++i) {
        int k = i;
        for (int j = i+1; j<n; ++j)
            if (std::abs(a[j][i]) > std::abs(a[k][i])) k = j;
        if (std::abs(a[k][i])<EPS) {
            std::cout<<std::abs(a[k][i])<<std::endl;
            std::cout<<"Non-invertible matrix"<<std::endl;
            return matrix();
        }
        std::swap(a[i], a[k]);
        std::swap(f[i], f[k]);
        for (int j = 0; j<l; ++j) f[i][j]/=a[i][i]; 
        for (int j = n-1; j>=0; --j) a[i][j]/=a[i][i]; 
        for (int j = i+1; j<n; ++j){
            for (int t = 0; t<l; ++t) f[j][t] -= f[i][t]*a[j][i];
            for (int t = n-1; t>=i; --t) a[j][t] -= a[i][t]*a[j][i];
        }
        for (int j = i-1; j>=0; --j){
            for (int t = 0; t<l; ++t) f[j][t] -= f[i][t]*a[j][i];
            for (int t = n-1; t>=i; --t) a[j][t] -= a[i][t]*a[j][i];
        }
    }
    return f;
}

matrix matrix_mul(const matrix &a, const matrix &b)
{
    int m1 = a.size(), n1 = a[0].size(), m2 = b.size(), n2 = b[0].size();
    if (n1!=m2) return std::vector<std::vector<double>>();
    std::vector<std::vector<double>> result(m1, std::vector<double>(n2));
    for (int i = 0; i<m1; ++i){
        for (int j = 0; j<n2; ++j)
            for (int k = 0; k<n1; ++k) result[i][j] += a[i][k]*b[k][j];
    }
    return result;
}

double matrix_norm(const matrix &a, const matrix &b)
{
    double norm2 = 0;
    if (a.size()!=b.size() || a[0].size()!=b[0].size()) return -1;
    for (int i = 0; i<a.size(); ++i)
        for (int j = 0; j<a[0].size(); ++j)
            norm2 += (a[i][j]-b[i][j])*(a[i][j]-b[i][j]);
    return std::sqrt(norm2);
}

int main()
{
    matrix a = {{1, 0.17, -0.25, 0.54},
                {0.47, 1.00, 0.67, -0.32},
                {-0.11, 0.35, 1, -0.74},
                {0.55, 0.43, 0.36, 1}};

    matrix f = {{1, 0.42, 0.54, 0.66},
                {0.42, 1.00, 0.32, 0.44},
                {0.54, 0.32, 1, 0.22},
                {0.66, 0.44, 0.22, 1}};

    matrix result = jordan_gauss(a, f);
    if (result.size()!=0){
        std::cout<<std::endl;
        std::cout<<"Calculation result: (matrix X)"<<std::endl;
        print(result);
        std::cout<<"Product of matrices A and X: (it is matrix F)"<<std::endl;
        print(matrix_mul(a,result));
        std::cout<<"Matrix difference norm: ";
        std::cout<<matrix_norm(f, matrix_mul(a,result))<<std::endl<<std::endl;
        
    }
}