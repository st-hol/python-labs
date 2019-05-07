#include <iostream>

#define N 10
#define con 1

using namespace std;

main(){
	double 	A[N] = {0.0, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2},
			B[N] = {5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4},
			C[N] = {0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2.1, 0.0},
			D[N] = {2.45, 3.38, 4.30, 5.30, 6.38, 7.54, 8.78, 10.10, 11.50, 9.76},								// Äëÿ ñ = 1
			//D[N] = {0.470, 0.860, 1.222, 1.646, 2.132, 2.680, 3.290, 3.962, 4.696, 2.272},						// Äëÿ c = 0.1
			//D[N] = {0.25220, 0.58280, 0.88342, 1.24406, 1.66472, 2.14540, 2.68610, 3.28682, 3.94756, 1.44832},	// Äëÿ ñ = 0,001
			T[N] = {};
			
	for(int i = 0; i < N; i++) B[i] *= con;
			
	for(int i = 0; i < N; i++){
		if(i == 0) cout << B[0] << "\t" << C[0] << "\t\t= " << D[0] << endl;
		else if(i != N - 1) cout << A[i] << "\t" << B[i] << "\t" << C[i] << "\t= " << D[i] << endl;
		else cout << "\t" <<  A[i] << "\t" << B[i] << "\t= " << D[i] << endl;
	}
			
	for(int i = 1; i < N; i++){
		B[i] = B[i] - A[i] * C[i - 1] / B[i - 1];
		D[i] = D[i] - A[i] * D[i - 1] / B[i - 1];
	}
	
	cout << endl;
	for(int i = 0; i < N; i++){
		if(i == 0) cout << B[0] << "\t" << C[0] << "\t\t= " << D[0] << endl;
		else if(i != N - 1) cout << " " << "\t" << B[i] << "\t" << C[i] << "\t= " << D[i] << endl;
		else cout << "\t" << " " << "\t" << B[i] << "\t= " << D[i] << endl;
	}
	
	for(int i = N - 1; i >= 0; i--){
		if(i == N - 1) T[i] = D[i] / B[i];
		else T[i] = (D[i] - C[i] * T[i + 1]) / B[i];
	}
	
	cout << endl;
	for(int i = 0; i < N; i++){
		cout << T[i] << " ";
	}
}
