using System;
using System.Collections.Generic;

namespace Laba__1
{
    static partial class DiffEquations
    {
        public static List<List<double>> Calculatе(int n)
        {

            List<List<double>> list = new List<List<double>>(); // динамический список хранящий другие списки точек

            List<double> yxk = new List<double>(); // список для добавления значений точной функции
            List<double> xk = new List<double>(); // список для добавления точек х
            List<double> yk = new List<double>(); // список для добавления точек х
            Random rnd = new Random();
            int k = 50;
            double h = (b - a)/(k - 1);

            xk.Add(a); //  добавления точек х
            yxk.Add(ExactFunction(a)); //добавления значений точной функции
            yk.Add(ExactFunction(a));
            if (n == N1)
            {
                for (var i = 1; i < k; ++i)
                {
                    {
                        xk.Add(a + (h*i)); //  добавления точек х
                        yxk.Add(ExactFunction(a + (h*i))); //добавления значений точной функции
                        yk.Add(ExactFunction(a + (h*i)) + rnd.NextDouble()*1E-1);
                    }
                }
                xk.Add(b); //  добавления точек х
                yxk.Add(ExactFunction(b)); //добавления значений точной функции
                yk.Add(ExactFunction(b + rnd.NextDouble()*1E-15));
            }
            else if (n == N2)
            {

                for (var i = 1; i < k ; ++i)
                {
                    xk.Add(a + (h*i)); //  добавления точек х
                    yxk.Add(ExactFunction(a + (h*i))); //добавления значений точной функции
                    yk.Add(ExactFunction(a + (h*i)) + rnd.NextDouble()*1E-2);
                }
                xk.Add(b); //  добавления точек х
               yxk.Add(ExactFunction(b)); //добавления значений точной функции
               yk.Add(ExactFunction(b + rnd.NextDouble()*1E-16));

            }
            else
            {

                for (var i = 1; i < k ; ++i)
                {
                    xk.Add(a + (h*i)); //  добавления точек х
                    yxk.Add(ExactFunction(a + (h*i))); //добавления значений точной функции
                    yk.Add(ExactFunction(a + (h*i)) + rnd.NextDouble()*1E-8);
                }
                xk.Add(b); //  добавления точек х
                yxk.Add(ExactFunction(b)); //добавления значений точной функции
                yk.Add(ExactFunction(b + rnd.NextDouble()*1E-300));
            }


            list.Add(xk);
            list.Add(yxk);
            list.Add(yk);

            return list;
        }

    }
}