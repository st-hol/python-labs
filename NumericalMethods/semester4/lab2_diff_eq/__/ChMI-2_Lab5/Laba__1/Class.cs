using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Laba__1
{
    static partial class DiffEquationsCauchy
    {
       
        public static List<List<double>> Calculatе(double h)
        {
            int i;
            double x;
            List<List<double>> list = new List<List<double>>(); // динамический список хранящий другие списки

            List<double> yxk = new List<double>();       // список для добавления значений точной функции
            List<double> xk = new List<double>();        // список для добавления точек х
            List<double> yk3 = new List<double>();       // список для добавления приближенных значений методом Рунге-Кутта-Фельберга ІV

            double y = y0;                                    // y0 = 0 - початкова умова
            
            xk.Add(a);                                              // добавление точки x0
            yxk.Add(y0);                                            // добавление точки y0
            yk3.Add(y0);                                               // добавление точки y0

            for (x = a, i = 1; x <= b + h; x += h, ++i)
            {
                xk.Add(x + h);                                     //  добавления точек х
                yxk.Add(ExactFunction(x + h));                     //добавления значений точной функции
                yk3.Add(MethodRungeKuttaFehlberga3(x, y, h)); // добавление приближенных значений методом Рунге-Кутта-Фельберга ІV
                y = yk3[i];                                   // сохранение предидущего значения
            }

            list.Add(xk);
            list.Add(yxk);
            list.Add(yk3);

            return list;
        }

        private static double MethodRungeKuttaFehlberga3(double xk, double yk, double h)
        {
            double k0 = h * Differentialfunction(xk, yk);
            double k1 = h * Differentialfunction(xk + h / 4.0, yk + k0 / 4.0);
            double k2 = h * Differentialfunction(xk + 4.0 / 9 * h, yk + 4.0 / 81 * k0 + 32.0 / 81 * k1);
            double k3 = h * Differentialfunction(xk + 6.0 / 7 * h, yk + 57.0 / 98 * k0 - 437.0 / 343 * k1 + 1053.0 / 686 * k2);

            return (yk + 1.0 / 6 * k0 + 27.0 / 52 * k2 + 49.0 / 156 * k3);
        }


    }
}
