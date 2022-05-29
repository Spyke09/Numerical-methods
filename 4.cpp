#include <iostream>
#include <cmath>
#include <vector>
#define matrix vector<vector<double>>
#define EPS 10E-12
using namespace std;

void print(vector<double> a)
{
    for (int i = 0; i<a.size(); ++i){
        std::cout<<a[i]<<std::endl;
    }
    std::cout<<std::endl;
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

vector<double> matrix_vect_mul(const matrix &a, const vector<double> &b)
{
    int m1 = a.size(), n1 = a[0].size();
    if (n1!=b.size()) {
        std::cout<<"Invalid sizes in matrix_vect_mul"<<std::endl;
        return vector<double>();
    }
    vector<double> result(m1, 0);
    for (int i = 0; i<m1; ++i){
            for (int k = 0; k<n1; ++k) result[i] += a[i][k]*b[k];
    }
    return result;
}

double dot(const vector<double> &a, const vector<double> &b)
{
    if (a.size()!=b.size()) {
        std::cout<<"Invalid sizes in dot"<<std::endl;
        return 0;
    }
    double res = 0;
    for (int i = 0; i< a.size(); ++i) res += a[i]*b[i];
    return res;
}

double vect_norm(const vector<double> &a, const vector<double> &b)
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

vector<double> vect_scalar_mul(const vector<double>& a, double k)
{
    vector<double> b(a.size());
    for (int i = 0; i<a.size(); ++i)  b[i] = a[i]*k;
    return b;
}

double get_min_root(double a, double b, double c)
{
    return (-b-sqrt(b*b-4*a*c))/(2*a);
}

vector<double> find_eigenvector(const matrix& A, const matrix& B, int n)
{
    int len = A.size();
    vector<double> f, g, x(len, 1);
    double a, b, c, alpha, ro, beta, old_g, r = 1;
    int iter = n;
    while(--iter && (abs(r)>=EPS)){
        f = matrix_vect_mul(A, x);
        g = matrix_vect_mul(B, x);
        beta = dot(g, x);
        ro = dot(f, x)/beta;
        for (int i = 0; i < len; ++i){
            a = (g[i]*A[i][i]-f[i]*B[i][i])/beta;
            b = (A[i][i] - ro*B[i][i]);
            c = (f[i] - ro*g[i]);
            alpha = get_min_root(a, b, c);
            x[i] += alpha;
            old_g = g[i];
            for (int j = 0; j<len; ++j){
                f[j] += alpha*A[j][i];
                g[j] += alpha*B[j][i];
            }
            beta += alpha*(g[i]+old_g);
            ro += alpha/beta*alpha*sqrt(b*b-4*a*c);
        }
        r = vect_norm(f, vect_scalar_mul(g, ro));
    }
    cout<<"N = "<<n<<endl;
    if (iter==0){
        cout<<"Error (norm of residual vector): "<<r<<endl;
    } else {
        cout<<"Number of iteration (accuracy achieved): "<<n-iter<<endl;
    }
    return x;
}

double find_eigenvalue(const matrix& A, const matrix& B, const vector<double>& x){
    return dot(matrix_vect_mul(A, x), x)/dot(matrix_vect_mul(B, x), x);
}

int main()
{
    matrix a = {{1, 0.77, -0.25, 0.54},
                {0.77, 1.00, 0.35, 0.43},
                {-0.25, 0.35, 1, -0.74},
                {0.54, 0.43, -0.74, 1}};

    matrix b = {{1, 0.42, 0.54, 0.66},
                {0.42, 1.00, 0.32, 0.44},
                {0.54, 0.32, 1, 0.22},
                {0.66, 0.44, 0.22, 1}};

    //b = matrix_mul(b,b);

    vector<double> x0 = find_eigenvector(a, b, 200);
    
    cout<<"Result value: "<<find_eigenvalue(a, b, x0)<<endl;
    cout<<"Result vector: "<<endl;
    print(x0);
}
