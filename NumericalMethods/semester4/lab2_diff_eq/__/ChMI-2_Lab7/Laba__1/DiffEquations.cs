using System;
using System.Collections.Generic;

namespace Laba__1
{
    static partial class DiffEquations
    {
        private const double a = 0.0;
        private const double b = 1.0;
        private const double y0 = 0.0;
        private const int n1 = 3;
        private const int n2 = 20;
        private const int n3 = 50;
        private const int pointsNumber = 50;
        private const double ay = 1.0/400;


        public static int N1
        {
            get { return n1; }
        }

        public static int N2
        {
            get { return n2; }
        }

        public static int N3
        {
            get { return n3 ; }
        }

        public static double A
        {
            get { return a; }
        }

        public static double B
        {
            get { return b; }
        }

        public static int N
        {
            get { return pointsNumber; }
        }

        public static double ExactFunction(double x)                             //  функция возвращает точное значение
        {
            return (Math.Pow(Math.E, ((x - 1)/Math.Pow(ay, 1.0/2))) + Math.Pow(Math.E, (-x/Math.Pow(ay, 1.0/2))))/
                   (1 + Math.Pow(Math.E, -1.0/Math.Pow(ay, 1.0/2))) -
                   Math.Pow(Math.Cos(Math.PI*x), 2);
        }

        
        public static List<List<double>> Calculate(int n)
        {
            List<List<double>> list = new List<List<double>>(); // динамический список хранящий другие списки точек
            
            List<double> yxk = new List<double>(); // список для добавления значений точной функции
            List<double> xk = new List<double>(); // список для добавления точек х
            List<double> yk = new List<double>(); // список для добавления точек х
            double[,] A = new double[pointsNumber, pointsNumber];
            double[] B = new double[pointsNumber];
            double[] Cj = new double[pointsNumber];
            double h = (b - a)/(pointsNumber - 1);

            for (var i = 0; i < pointsNumber; ++i)
            {
                xk.Add(a + h*i); //  добавления точек х
                yxk.Add(ExactFunction(a + h*i)); //добавления значений точной функции
                for (var j = 0; j < pointsNumber; ++j)
                {
                    A[i, j] = ay * (-Math.Pow((j + 1) * Math.PI, 2) * Math.Sin(Math.PI * xk[i] * (j + 1)))
                        - Math.Sin(Math.PI * xk[i] * (j + 1));
                }
                B[i] = Math.Pow(Math.Cos(Math.PI * xk[i]), 2) + 2 * ay * Math.Pow(Math.PI, 2) * Math.Cos(2 * Math.PI * xk[i]);
            }

           // Cj = Jordan(A, B);
            yxk[N - 1] = 0;
            int info;
            var rep = new alglib.densesolverlsreport();
            alglib.rmatrixsolvels(A, B.Length, B.Length, B, 0, out info, out rep, out Cj);
            
            for (var i = 0; i < xk.Count; ++i)
            {
                double u = 0;
                for (var j = 0; j < n; ++j)
                {
                    u += Cj[j]*Math.Sin((j + 1)*Math.PI*xk[i]);
                }
                yk.Add(u);
            }
  
            list.Add(xk);
            list.Add(yxk);
            list.Add(yk);

            return list;
        }

      
        public static double[] Jordan(double[,] A, double[] B)
        {
            var X = new double[B.Length];
            for (var k = 0; k < B.Length-1; k++)
            {
                 var amax=Math.Abs(A[k,k]);
                   var H=k;

                   for (var i=k+1; i<B.Length;i++)
                   {
                       if (Math.Abs(A[i,k])>amax) 
                       {
                       amax = Math.Abs(A[i,k]);
                       H=i;
                       }
                   }

                       if ( H!=k) 
                       {
                           for (var j=k; j<B.Length;j++)
                           {
                               var c = A[k,j];
                               A[k,j] = A[H,j];
                               A[H,j] = c;
                           }

                           var temp = B[k];
                           B[k] = B[H];
                           B[H] = temp;
                       }
           
                for (var i = 0; i < B.Length; i++)
                {

                    if (i != k)
                    {
                        var r = A[i, k] / A[k, k];
                        r *= 1.1;

                        for (var j = 0; j < B.Length; j++)
                            A[i, j] = A[i, j] - r * A[k, j];

                        B[i] = B[i] - r*B[k];
                    }
                    X[i] = B[i] / A[i, i];
                }
            }
            return X;
        }

    }
}
