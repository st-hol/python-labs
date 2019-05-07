using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Laba__1
{
    static partial  class DiffEquationsCauchy
    {
        private static double a = 0.0;
        private static double b = 2.0;   
        private static double y0 = 1.0;
        private static double h0 = 0.5;
        private static double h1 = h0/5.0;
        private static double h2 = h0/25.0;
       
        public static double H0
        {
            get { return h0; }
            set { h0 = value ; }
        }

        public static double H1
        {
            get { return h1; }
            set { h1 = value; }
        }

        public static double H2
        {
            get { return h2 ; }
            set { h2 = value; }
        }
        public static double A
        {
            get { return a; }
            set { a = value; }
        }

        public static double B
        {
            get { return b; }
            set { b = value; }
        }

        public static double ExactFunction(double x)                             //  функция возвращает точное значение
        {
            return 2*Math.Pow(Math.E, x)/(1 + Math.Pow(Math.E, x)*(Math.Cos(x) + Math.Sin(x)));
        }

        public static double Differentialfunction(double x, double y)            // функция возвращает уравнение y'= 
        {
            return y - Math.Pow(y, 2)*Math.Cos(x);
        }

        public static List<List<double>> Calculate(double h)
        {
            int i;
            double x;
            double[] prevY = new double[6];

            List<List<double>> list = new List<List<double>>(); // динамический список хранящий другие списки

            List<double> yxk = new List<double>();       // список для добавления значений точной функции
            List<double> xk = new List<double>();        // список для добавления точек х
            List<double> yk = new List<double>();        // список для добавления точек х
            double y = y0;                                    // y0 = 0 - початкова умова
           
            xk.Add(a);                                              // добавление точки x0
            yxk.Add(y0);                                            // добавление точки y0
            yk.Add(y0);

            for ( x = a, i=1; x <= b + h; x += h,++i)
            {
                xk.Add(x+h);                                     //  добавления точек х
                yxk.Add(ExactFunction(x+h));                     //добавления значений точной функции
                prevY[0] = Differentialfunction(x,y);
                prevY[1] = Differentialfunction(x-h, MethodRungeKuttaFehlberga4(x - 2* h, ExactFunction( x - 2* h ), h));
                prevY[2] = Differentialfunction(x - 2 * h, MethodRungeKuttaFehlberga4(x - 3 * h, ExactFunction(x - 3 * h), h));
                prevY[3] = Differentialfunction(x - 3 * h, MethodRungeKuttaFehlberga4(x - 4 * h, ExactFunction(x - 4 * h), h));
                prevY[4] = Differentialfunction(x - 4 * h, MethodRungeKuttaFehlberga4(x - 5 * h, ExactFunction(x - 5 * h), h));
                prevY[5] = Differentialfunction(x - 5 * h, MethodRungeKuttaFehlberga4(x - 6 * h, ExactFunction(x - 6 * h), h));
                yk.Add(MultistepMethod(x+h,y,h,prevY));
                y = yk[i];

            }

            list.Add(xk);
            list.Add(yxk);
            list.Add(yk);

            return list;
        }

        private static double MethodRungeKuttaFehlberga4(double xk, double yk, double h)
        {
            double k0 = h * Differentialfunction(xk, yk);
            double k1 = h * Differentialfunction(xk + 2.0/9*h , yk + 2.0/9* k0 );
            double k2 = h * Differentialfunction(xk + h/3.0, yk + 1.0 / 12 * k0 + 1.0 / 4 * k1);
            double k3 = h * Differentialfunction(xk + 3.0 / 4 * h, yk + 69.0 / 128 * k0 - 243.0 / 128 * k1 + 135.0 / 64 * k2);
            double k4 = h * Differentialfunction(xk + h, yk - 17.0 / 12 * k0 + 27.0 / 4 * k1 - 27.0 / 5 * k2 + 16.0/15 * k3);

            return (yk + 1.0 / 9 * k0 + 9.0 / 20 * k2 + 16.0 / 45 * k3 + 1.0/12 * k4);
        }

        private static double MultistepMethod(double xk, double yk, double h, double[] yprev)
        {
            double c = (yk + h / 1440.0 * (1427 * yprev[0] - 798 * yprev[1] + 482 * yprev[2] - 173 * yprev[3] +
                                       27 * yprev[4]));
            double b = 1 - 475 * h / 1440.0;
            double a = 475.0/1440.0*h*Math.Cos(xk);

            double d = Math.Pow(Math.Pow(b, 2) + 4 * a * c, 1.0 / 2);

            return (-b + d) / (2 * a);
        }
        
    }
}
