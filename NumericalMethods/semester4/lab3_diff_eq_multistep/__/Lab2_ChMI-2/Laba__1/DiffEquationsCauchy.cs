using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Laba__1
{
    static  class DiffEquationsCauchy
    {
        private static double a = 0.0;
        private static double b = 2.0;   
        private static double y0 = 1.0;
        private static double h0 = 0.5;
        private static double h1 = h0/5.0;
        private static double h2 = h0/21.0;
       
        public static double H0
        {
            get { return h0; }
            set { value = h0; }
        }

        public static double H1
        {
            get { return h1; }
            set { value = h1; }
        }

        public static double H2
        {
            get { return h2 ; }
            set { value = h2; }
        }
        public static double A
        {
            get { return a; }
            set { value = a; }
        }

        public static double B
        {
            get { return b; }
            set { value = b; }
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
            List<List<double>> list = new List<List<double>>(); // динамический список хранящий другие списки

            List<double> yxk = new List<double>();       // список для добавления значений точной функции
            List<double> xk = new List<double>();        // список для добавления точек х
            List<double> yk3 = new List<double>();       // список для добавления приближенных значений методом Рунге-Кутта-Фельберга ІІІ
            List<double> yk4 = new List<double>();       // список для добавления приближенных значений методом Рунге-Кутта-Фельберга ІV

            double y = y0;                                    // y0 = 0 - початкова умова
            double y2 = y0;                                   // y0 = 0 - початкова умова

            xk.Add(a);                                              // добавление точки x0
            yxk.Add(y0);                                            // добавление точки y0
            yk3.Add(y0);                                             // добавление точки y0
            yk4.Add(y0);                                               // добавление точки y0


            for ( x = a, i=1; x <= b + h; x += h,++i)
            {
                xk.Add(x+h);                                     //  добавления точек х
                yxk.Add(ExactFunction(x+h));                     //добавления значений точной функции
                yk3.Add(MethodRungeKuttaFehlberga3(x, y, h));  // добавление приближенных значений методом Рунге-Кутта-Фельберга ІІІ
                y = yk3[i];                                    // сохранение предидущего значения                             
                yk4.Add(MethodRungeKuttaFehlberga4(x, y2, h)); // добавление приближенных значений методом Рунге-Кутта-Фельберга ІV
                y2 = yk4[i];                                   // сохранение предидущего значения
            }

            list.Add(xk);
            list.Add(yxk);
            list.Add(yk3);
            list.Add(yk4);

            return list;
        }

        private static double MethodRungeKuttaFehlberga3(double xk, double yk, double h)
        {
            double k0 = h * Differentialfunction(xk, yk);
            double k1 = h * Differentialfunction(xk + h / 4.0, yk + k0 / 4.0);
            double k2 = h * Differentialfunction(xk + 4.0 / 9 * h, yk + 4.0 / 81 * k0 + 32.0 / 81 * k1);
            double k3 = h * Differentialfunction(xk + 6.0 / 7 * h, yk + 57.0 / 98 * k0 - 437.0 / 343 * k1 + 1053.0 / 686 * k2);

            return (yk + 1.0/6*k0 + 27.0/52*k2 + 49.0/156*k3);
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
        
    }
}
