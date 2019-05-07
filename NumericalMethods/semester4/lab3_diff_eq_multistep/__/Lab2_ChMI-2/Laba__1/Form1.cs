using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using ZedGraph;

namespace Laba__1
{
	public partial class Form1 : Form
	{
       
		public Form1()
		{
			InitializeComponent();
		}

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            DrawRK3H0();
            DrawRK3H1();
            DrawRK3H2();
            DrawRK4H0();
            DrawRK4H1();
            DrawRK4H2();
            Table();
        }

        public void DrawRK3H0()
	    {
            GraphPane panel = zedGraphControl1.GraphPane;

            panel.Title.Text = "Графіки функцій y = f(x)точ. i f(x,h0) ";
            panel.XAxis.Title.Text = "X";
            panel.YAxis.Title.Text = "Y";

            panel.CurveList.Clear();

            PointPairList list1 = new PointPairList();
            PointPairList list2 = new PointPairList();

            LineItem Line1 = panel.AddCurve("y = f(x)точ.", list1, Color.DarkBlue, SymbolType.None);
            LineItem Line2 = panel.AddCurve("y = f(x,h0)", list2, Color.Crimson, SymbolType.None);

            int n = (int)((DiffEquationsCauchy.B - DiffEquationsCauchy.A) / DiffEquationsCauchy.H0 + 1);
            dataGridView5.Rows.Clear();
            for (int i=0;i<n;++i)
            {
                dataGridView5.Rows.Add();
                dataGridView5[0, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[0][i];
                dataGridView5[1, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[1][i];
                dataGridView5[2, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[2][i];
                dataGridView5[3, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[1][i] -
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[2][i];
                dataGridView5[4, i].Value = (DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[1][i] -
                                             DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[2][i]) /
                                            DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[1][i] * 100;
                
                // добавим в список точку
                list1.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[0][i],
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[1][i]);  // график точной функции
                list2.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[0][i],
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[2][i]);  // график приближенной функции 
            }

            
            //Устанавливаем интересующий нас интервал по оси Х
            //для первой табл.
            panel.XAxis.Scale.Min = DiffEquationsCauchy.A;
            panel.XAxis.Scale.Max = DiffEquationsCauchy.B + 0.1;

            //Устанавливаем интересующий нас интервал по оси Y 
            //для первой табл.
            panel.YAxis.Scale.Min = 0;
            panel.YAxis.Scale.Max = 4.2;

            // !!!
            // Установим цвет рамки для всего компонента
            panel.Border.Color = Color.CadetBlue;

            // Установим цвет рамки вокруг графика
            panel.Chart.Border.Color = Color.Green;

            // Закрасим фон всего компонента ZedGraph
            // Заливка будет сплошная
            panel.Fill.Type = FillType.Solid;
            panel.Fill.Color = Color.DarkCyan;

            // Закрасим область графика (его фон) в черный цвет
            panel.Chart.Fill.Type = FillType.Solid;
            panel.Chart.Fill.Color = Color.Aqua;

            // Включим показ оси на уровне X = 0 и Y = 0, чтобы видеть цвет осей
            panel.XAxis.MajorGrid.IsZeroLine = true;
            panel.YAxis.MajorGrid.IsZeroLine = true;
            // Установим цвет осей
            panel.XAxis.Color = Color.Gray;
            panel.YAxis.Color = Color.Gray;

            // Включим сетку
            panel.XAxis.MajorGrid.IsVisible = true;
            panel.YAxis.MajorGrid.IsVisible = true;
            // Установим цвет для сетки
            panel.XAxis.MajorGrid.Color = Color.Cyan;
            panel.YAxis.MajorGrid.Color = Color.Cyan;

            // Установим цвет для подписей рядом с осями
            panel.XAxis.Title.FontSpec.FontColor = Color.White;
            panel.YAxis.Title.FontSpec.FontColor = Color.White;

            // Установим цвет подписей под метками
            panel.XAxis.Scale.FontSpec.FontColor = Color.GreenYellow;
            panel.YAxis.Scale.FontSpec.FontColor = Color.GreenYellow;

            // Установим цвет заголовка над графиком
            panel.Title.FontSpec.FontColor = Color.Chartreuse;
            //Вызываем метод AxisChange(), чтобы обновить данные  об осях
            //В противном случае на рисунке будет показана только часть графика,
            //которая уменшается в интервалы по осям, установленные по умолчанию
            zedGraphControl1.AxisChange();

            //Обновляем график
            zedGraphControl1.Invalidate();
			
	    }


        public void DrawRK3H1()
        {
            GraphPane panel = zedGraphControl2.GraphPane;

            panel.Title.Text = "Графіки функцій y = f(x)точ. i f(x,h1) ";
            panel.XAxis.Title.Text = "X";
            panel.YAxis.Title.Text = "Y";

            panel.CurveList.Clear();

            PointPairList list1 = new PointPairList();
            PointPairList list2 = new PointPairList();

            LineItem Line1 = panel.AddCurve("y = f(x)точ.", list1, Color.DarkBlue, SymbolType.None);
            LineItem Line2 = panel.AddCurve("y = f(x,h1)", list2, Color.Crimson, SymbolType.None);


            int n = (int)((DiffEquationsCauchy.B - DiffEquationsCauchy.A) / DiffEquationsCauchy.H1 + 1);
            dataGridView2.Rows.Clear();
            for (int i = 0; i < n; ++i)
            {
                dataGridView2.Rows.Add();
                dataGridView2[0, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[0][i];
                dataGridView2[1, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i];
                dataGridView2[2, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[2][i];
                dataGridView2[3, i].Value = (DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i] -
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[2][i]);
                dataGridView2[4, i].Value = (DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i] -
                                             DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[2][i]) /
                                            DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i] * 100;

                // добавим в список точку
                list1.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[0][i],
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i]);  // график точной функции
                list2.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[0][i],
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[2][i]);  // график приближенной функции 
              }


            //Устанавливаем интересующий нас интервал по оси Х
            //для первой табл.
            //Устанавливаем интересующий нас интервал по оси Х
            //для первой табл.
            panel.XAxis.Scale.Min = DiffEquationsCauchy.A;
            panel.XAxis.Scale.Max = DiffEquationsCauchy.B + 0.1;

            //Устанавливаем интересующий нас интервал по оси Y 
            //для первой табл.
            panel.YAxis.Scale.Min = 0;
            panel.YAxis.Scale.Max = 3.5;

            // !!!
            // Установим цвет рамки для всего компонента
            panel.Border.Color = Color.CadetBlue;

            // Установим цвет рамки вокруг графика
            panel.Chart.Border.Color = Color.Green;

            // Закрасим фон всего компонента ZedGraph
            // Заливка будет сплошная
            panel.Fill.Type = FillType.Solid;
            panel.Fill.Color = Color.DarkCyan;

            // Закрасим область графика (его фон) в черный цвет
            panel.Chart.Fill.Type = FillType.Solid;
            panel.Chart.Fill.Color = Color.Aqua;

            // Включим показ оси на уровне X = 0 и Y = 0, чтобы видеть цвет осей
            panel.XAxis.MajorGrid.IsZeroLine = true;
            panel.YAxis.MajorGrid.IsZeroLine = true;
            // Установим цвет осей
            panel.XAxis.Color = Color.Gray;
            panel.YAxis.Color = Color.Gray;

            // Включим сетку
            panel.XAxis.MajorGrid.IsVisible = true;
            panel.YAxis.MajorGrid.IsVisible = true;
            // Установим цвет для сетки
            panel.XAxis.MajorGrid.Color = Color.Cyan;
            panel.YAxis.MajorGrid.Color = Color.Cyan;

            // Установим цвет для подписей рядом с осями
            panel.XAxis.Title.FontSpec.FontColor = Color.White;
            panel.YAxis.Title.FontSpec.FontColor = Color.White;

            // Установим цвет подписей под метками
            panel.XAxis.Scale.FontSpec.FontColor = Color.GreenYellow;
            panel.YAxis.Scale.FontSpec.FontColor = Color.GreenYellow;

            // Установим цвет заголовка над графиком
            panel.Title.FontSpec.FontColor = Color.Chartreuse;
            //Вызываем метод AxisChange(), чтобы обновить данные  об осях
            //В противном случае на рисунке будет показана только часть графика,
            //которая уменшается в интервалы по осям, установленные по умолчанию
            zedGraphControl1.AxisChange();

            //Обновляем график
            zedGraphControl1.Invalidate();

        }

        public void DrawRK3H2()
        {
            GraphPane panel = zedGraphControl3.GraphPane;

            panel.Title.Text = "Графіки функцій y = f(x)точ. i f(x,h2) ";
            panel.XAxis.Title.Text = "X";
            panel.YAxis.Title.Text = "Y";

            panel.CurveList.Clear();

            PointPairList list1 = new PointPairList();
            PointPairList list2 = new PointPairList();

            LineItem Line1 = panel.AddCurve("y = f(x)точ.", list1, Color.DarkBlue, SymbolType.None);
            LineItem Line2 = panel.AddCurve("y = f(x,h2)", list2, Color.Crimson, SymbolType.None);

            int n = (int)((DiffEquationsCauchy.B - DiffEquationsCauchy.A) / DiffEquationsCauchy.H2 + 1);
            dataGridView3.Rows.Clear();
            for (int i = 0; i < n; ++i)
            {
                dataGridView3.Rows.Add();
                dataGridView3[0, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[0][i];
                dataGridView3[1, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i];
                dataGridView3[2, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[2][i];
                dataGridView3[3, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i] -
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[2][i];
                dataGridView3[4, i].Value = (DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i] -
                                             DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[2][i]) /
                                            DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i] * 100;

                // добавим в список точку
                list1.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[0][i],
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i]);  // график точной функции
                list2.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[0][i],
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[2][i]);  // график приближенной функции 
                }


            //Устанавливаем интересующий нас интервал по оси Х
            //для первой табл.
            panel.XAxis.Scale.Min = DiffEquationsCauchy.A;
            panel.XAxis.Scale.Max = DiffEquationsCauchy.B + 0.1;

            //Устанавливаем интересующий нас интервал по оси Y 
            //для первой табл.
            panel.YAxis.Scale.Min = 0;
            panel.YAxis.Scale.Max = 3.5;


            // !!!
            // Установим цвет рамки для всего компонента
            panel.Border.Color = Color.CadetBlue;

            // Установим цвет рамки вокруг графика
            panel.Chart.Border.Color = Color.Green;

            // Закрасим фон всего компонента ZedGraph
            // Заливка будет сплошная
            panel.Fill.Type = FillType.Solid;
            panel.Fill.Color = Color.DarkCyan;

            // Закрасим область графика (его фон) в черный цвет
            panel.Chart.Fill.Type = FillType.Solid;
            panel.Chart.Fill.Color = Color.Aqua;

            // Включим показ оси на уровне X = 0 и Y = 0, чтобы видеть цвет осей
            panel.XAxis.MajorGrid.IsZeroLine = true;
            panel.YAxis.MajorGrid.IsZeroLine = true;
            // Установим цвет осей
            panel.XAxis.Color = Color.Gray;
            panel.YAxis.Color = Color.Gray;

            // Включим сетку
            panel.XAxis.MajorGrid.IsVisible = true;
            panel.YAxis.MajorGrid.IsVisible = true;
            // Установим цвет для сетки
            panel.XAxis.MajorGrid.Color = Color.Cyan;
            panel.YAxis.MajorGrid.Color = Color.Cyan;

            // Установим цвет для подписей рядом с осями
            panel.XAxis.Title.FontSpec.FontColor = Color.White;
            panel.YAxis.Title.FontSpec.FontColor = Color.White;

            // Установим цвет подписей под метками
            panel.XAxis.Scale.FontSpec.FontColor = Color.GreenYellow;
            panel.YAxis.Scale.FontSpec.FontColor = Color.GreenYellow;

            // Установим цвет заголовка над графиком
            panel.Title.FontSpec.FontColor = Color.Chartreuse;
            //Вызываем метод AxisChange(), чтобы обновить данные  об осях
            //В противном случае на рисунке будет показана только часть графика,
            //которая уменшается в интервалы по осям, установленные по умолчанию
            zedGraphControl1.AxisChange();

            //Обновляем график
            zedGraphControl1.Invalidate();

        }



        public void DrawRK4H0()
        {
            GraphPane panel = zedGraphControl5.GraphPane;

            panel.Title.Text = "Графіки функцій y = f(x)точ. i f(x,h0) ";
            panel.XAxis.Title.Text = "X";
            panel.YAxis.Title.Text = "Y";

            panel.CurveList.Clear();

            PointPairList list1 = new PointPairList();
            PointPairList list2 = new PointPairList();

            LineItem Line1 = panel.AddCurve("y = f(x)точ.", list1, Color.DarkBlue, SymbolType.None);
            LineItem Line2 = panel.AddCurve("y = f(x,h0)", list2, Color.Crimson, SymbolType.None);

            int n = (int)((DiffEquationsCauchy.B - DiffEquationsCauchy.A) / DiffEquationsCauchy.H0 + 1);
            dataGridView6.Rows.Clear();
            for (int i = 0; i < n; ++i)
            {
                dataGridView6.Rows.Add();
                dataGridView6[0, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[0][i];
                dataGridView6[1, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[1][i];
                dataGridView6[2, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[3][i];
                dataGridView6[3, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[1][i] -
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[3][i];
                dataGridView6[4, i].Value = (DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[1][i] -
                                             DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[3][i]) /
                                            DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[1][i] * 100;

                // добавим в список точку
                list1.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[0][i],
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[1][i]);  // график точной функции
                list2.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[0][i],
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[3][i]);  // график приближенной функции 
            }


            //Устанавливаем интересующий нас интервал по оси Х
            //для первой табл.
            panel.XAxis.Scale.Min = DiffEquationsCauchy.A;
            panel.XAxis.Scale.Max = DiffEquationsCauchy.B + 0.1;

            //Устанавливаем интересующий нас интервал по оси Y 
            //для первой табл.
            panel.YAxis.Scale.Min = 0;
            panel.YAxis.Scale.Max = 4.2;

            // !!!
            // Установим цвет рамки для всего компонента
            panel.Border.Color = Color.CadetBlue;

            // Установим цвет рамки вокруг графика
            panel.Chart.Border.Color = Color.Green;

            // Закрасим фон всего компонента ZedGraph
            // Заливка будет сплошная
            panel.Fill.Type = FillType.Solid;
            panel.Fill.Color = Color.DarkCyan;

            // Закрасим область графика (его фон) в черный цвет
            panel.Chart.Fill.Type = FillType.Solid;
            panel.Chart.Fill.Color = Color.Aqua;

            // Включим показ оси на уровне X = 0 и Y = 0, чтобы видеть цвет осей
            panel.XAxis.MajorGrid.IsZeroLine = true;
            panel.YAxis.MajorGrid.IsZeroLine = true;
            // Установим цвет осей
            panel.XAxis.Color = Color.Gray;
            panel.YAxis.Color = Color.Gray;

            // Включим сетку
            panel.XAxis.MajorGrid.IsVisible = true;
            panel.YAxis.MajorGrid.IsVisible = true;
            // Установим цвет для сетки
            panel.XAxis.MajorGrid.Color = Color.Cyan;
            panel.YAxis.MajorGrid.Color = Color.Cyan;

            // Установим цвет для подписей рядом с осями
            panel.XAxis.Title.FontSpec.FontColor = Color.White;
            panel.YAxis.Title.FontSpec.FontColor = Color.White;

            // Установим цвет подписей под метками
            panel.XAxis.Scale.FontSpec.FontColor = Color.GreenYellow;
            panel.YAxis.Scale.FontSpec.FontColor = Color.GreenYellow;

            // Установим цвет заголовка над графиком
            panel.Title.FontSpec.FontColor = Color.Chartreuse;
            //Вызываем метод AxisChange(), чтобы обновить данные  об осях
            //В противном случае на рисунке будет показана только часть графика,
            //которая уменшается в интервалы по осям, установленные по умолчанию
            zedGraphControl1.AxisChange();

            //Обновляем график
            zedGraphControl1.Invalidate();

        }


        public void DrawRK4H1()
        {
            GraphPane panel = zedGraphControl6.GraphPane;

            panel.Title.Text = "Графіки функцій y = f(x)точ. i f(x,h1) ";
            panel.XAxis.Title.Text = "X";
            panel.YAxis.Title.Text = "Y";

            panel.CurveList.Clear();

            PointPairList list1 = new PointPairList();
            PointPairList list2 = new PointPairList();

            LineItem Line1 = panel.AddCurve("y = f(x)точ.", list1, Color.DarkBlue, SymbolType.None);
            LineItem Line2 = panel.AddCurve("y = f(x,h1)", list2, Color.Crimson, SymbolType.None);


            int n = (int)((DiffEquationsCauchy.B - DiffEquationsCauchy.A) / DiffEquationsCauchy.H1 + 1);
            dataGridView7.Rows.Clear();
            for (int i = 0; i < n; ++i)
            {
                dataGridView7.Rows.Add();
                dataGridView7[0, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[0][i];
                dataGridView7[1, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i];
                dataGridView7[2, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[3][i];
                dataGridView7[3, i].Value = (DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i] -
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[3][i]);
                dataGridView7[4, i].Value = (DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i] -
                                             DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[3][i]) /
                                            DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i] * 100;

                // добавим в список точку
                list1.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[0][i],
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i]);  // график точной функции
                list2.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[0][i],
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[3][i]);  // график приближенной функции 
            }


            //Устанавливаем интересующий нас интервал по оси Х
            //для первой табл.
            //Устанавливаем интересующий нас интервал по оси Х
            //для первой табл.
            panel.XAxis.Scale.Min = DiffEquationsCauchy.A;
            panel.XAxis.Scale.Max = DiffEquationsCauchy.B + 0.1;

            //Устанавливаем интересующий нас интервал по оси Y 
            //для первой табл.
            panel.YAxis.Scale.Min = 0;
            panel.YAxis.Scale.Max = 3.5;

            // !!!
            // Установим цвет рамки для всего компонента
            panel.Border.Color = Color.CadetBlue;

            // Установим цвет рамки вокруг графика
            panel.Chart.Border.Color = Color.Green;

            // Закрасим фон всего компонента ZedGraph
            // Заливка будет сплошная
            panel.Fill.Type = FillType.Solid;
            panel.Fill.Color = Color.DarkCyan;

            // Закрасим область графика (его фон) в черный цвет
            panel.Chart.Fill.Type = FillType.Solid;
            panel.Chart.Fill.Color = Color.Aqua;

            // Включим показ оси на уровне X = 0 и Y = 0, чтобы видеть цвет осей
            panel.XAxis.MajorGrid.IsZeroLine = true;
            panel.YAxis.MajorGrid.IsZeroLine = true;
            // Установим цвет осей
            panel.XAxis.Color = Color.Gray;
            panel.YAxis.Color = Color.Gray;

            // Включим сетку
            panel.XAxis.MajorGrid.IsVisible = true;
            panel.YAxis.MajorGrid.IsVisible = true;
            // Установим цвет для сетки
            panel.XAxis.MajorGrid.Color = Color.Cyan;
            panel.YAxis.MajorGrid.Color = Color.Cyan;

            // Установим цвет для подписей рядом с осями
            panel.XAxis.Title.FontSpec.FontColor = Color.White;
            panel.YAxis.Title.FontSpec.FontColor = Color.White;

            // Установим цвет подписей под метками
            panel.XAxis.Scale.FontSpec.FontColor = Color.GreenYellow;
            panel.YAxis.Scale.FontSpec.FontColor = Color.GreenYellow;

            // Установим цвет заголовка над графиком
            panel.Title.FontSpec.FontColor = Color.Chartreuse;
            //Вызываем метод AxisChange(), чтобы обновить данные  об осях
            //В противном случае на рисунке будет показана только часть графика,
            //которая уменшается в интервалы по осям, установленные по умолчанию
            zedGraphControl1.AxisChange();

            //Обновляем график
            zedGraphControl1.Invalidate();

        }

        public void DrawRK4H2()
        {
            GraphPane panel = zedGraphControl4.GraphPane;

            panel.Title.Text = "Графіки функцій y = f(x)точ. i f(x,h2) ";
            panel.XAxis.Title.Text = "X";
            panel.YAxis.Title.Text = "Y";

            panel.CurveList.Clear();

            PointPairList list1 = new PointPairList();
            PointPairList list2 = new PointPairList();

            LineItem Line1 = panel.AddCurve("y = f(x)точ.", list1, Color.DarkBlue, SymbolType.None);
            LineItem Line2 = panel.AddCurve("y = f(x,h2)", list2, Color.Crimson, SymbolType.None);

            int n = (int)((DiffEquationsCauchy.B - DiffEquationsCauchy.A) / DiffEquationsCauchy.H2 + 1);
            dataGridView1.Rows.Clear();
            for (int i = 0; i < n; ++i)
            {
                dataGridView1.Rows.Add();
                dataGridView1[0, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[0][i];
                dataGridView1[1, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i];
                dataGridView1[2, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[3][i];
                dataGridView1[3, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i] -
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[2][i];
                dataGridView1[4, i].Value = (DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i] -
                                             DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[3][i]) /
                                            DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i] * 100;

                // добавим в список точку
                list1.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[0][i],
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i]);  // график точной функции
                list2.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[0][i],
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[3][i]);  // график приближенной функции 
            }


            //Устанавливаем интересующий нас интервал по оси Х
            //для первой табл.
            panel.XAxis.Scale.Min = DiffEquationsCauchy.A;
            panel.XAxis.Scale.Max = DiffEquationsCauchy.B + 0.1;

            //Устанавливаем интересующий нас интервал по оси Y 
            //для первой табл.
            panel.YAxis.Scale.Min = 0;
            panel.YAxis.Scale.Max = 3.5;


            // !!!
            // Установим цвет рамки для всего компонента
            panel.Border.Color = Color.CadetBlue;

            // Установим цвет рамки вокруг графика
            panel.Chart.Border.Color = Color.Green;

            // Закрасим фон всего компонента ZedGraph
            // Заливка будет сплошная
            panel.Fill.Type = FillType.Solid;
            panel.Fill.Color = Color.DarkCyan;

            // Закрасим область графика (его фон) в черный цвет
            panel.Chart.Fill.Type = FillType.Solid;
            panel.Chart.Fill.Color = Color.Aqua;

            // Включим показ оси на уровне X = 0 и Y = 0, чтобы видеть цвет осей
            panel.XAxis.MajorGrid.IsZeroLine = true;
            panel.YAxis.MajorGrid.IsZeroLine = true;
            // Установим цвет осей
            panel.XAxis.Color = Color.Gray;
            panel.YAxis.Color = Color.Gray;

            // Включим сетку
            panel.XAxis.MajorGrid.IsVisible = true;
            panel.YAxis.MajorGrid.IsVisible = true;
            // Установим цвет для сетки
            panel.XAxis.MajorGrid.Color = Color.Cyan;
            panel.YAxis.MajorGrid.Color = Color.Cyan;

            // Установим цвет для подписей рядом с осями
            panel.XAxis.Title.FontSpec.FontColor = Color.White;
            panel.YAxis.Title.FontSpec.FontColor = Color.White;

            // Установим цвет подписей под метками
            panel.XAxis.Scale.FontSpec.FontColor = Color.GreenYellow;
            panel.YAxis.Scale.FontSpec.FontColor = Color.GreenYellow;

            // Установим цвет заголовка над графиком
            panel.Title.FontSpec.FontColor = Color.Chartreuse;
            //Вызываем метод AxisChange(), чтобы обновить данные  об осях
            //В противном случае на рисунке будет показана только часть графика,
            //которая уменшается в интервалы по осям, установленные по умолчанию
            zedGraphControl1.AxisChange();

            //Обновляем график
            zedGraphControl1.Invalidate();

        }

	    public void Table()
	    {
            int n = (int)((DiffEquationsCauchy.B - DiffEquationsCauchy.A) / DiffEquationsCauchy.H0 + 1);
            dataGridView4.Rows.Clear();
            for (int i = 0; i < n; ++i)
            {
                dataGridView4.Rows.Add();
                dataGridView4[0, i].Value = DiffEquationsCauchy.H0;
                dataGridView4[1, i].Value = DiffEquationsCauchy.ExactFunction(DiffEquationsCauchy.B) -
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[2][i];
                dataGridView4[2, i].Value = 100*(DiffEquationsCauchy.ExactFunction(DiffEquationsCauchy.B) -
                                                 DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H0)[2][i])/
                                            DiffEquationsCauchy.ExactFunction(DiffEquationsCauchy.B);

            }

            int k = (int)((DiffEquationsCauchy.B - DiffEquationsCauchy.A) / DiffEquationsCauchy.H1 + 1);
            for (int i = 0; i < k; ++i)
            {
                dataGridView4.Rows.Add();
                dataGridView4[3, i].Value = DiffEquationsCauchy.H1;
                dataGridView4[4, i].Value = DiffEquationsCauchy.ExactFunction(DiffEquationsCauchy.B) -
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[2][i];
                dataGridView4[5, i].Value = 100 * (DiffEquationsCauchy.ExactFunction(DiffEquationsCauchy.B) -
                                                 DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[2][i]) /
                                            DiffEquationsCauchy.ExactFunction(DiffEquationsCauchy.B);

            }

            int p = (int)((DiffEquationsCauchy.B - DiffEquationsCauchy.A) / DiffEquationsCauchy.H2 + 1);
            for (int i = 0 ; i < p; ++i)
            {
                dataGridView4.Rows.Add();
                dataGridView4[6, i].Value = DiffEquationsCauchy.H2;
                dataGridView4[7, i].Value = DiffEquationsCauchy.ExactFunction(DiffEquationsCauchy.B) -
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[2][i];
                dataGridView4[8, i].Value = 100 * (DiffEquationsCauchy.ExactFunction(DiffEquationsCauchy.B) -
                                                 DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[2][i]) /
                                            DiffEquationsCauchy.ExactFunction(DiffEquationsCauchy.B);

            }

	    }

        private void zedGraphControl1_Load(object sender, EventArgs e)
        {

        }

        private void zedGraphControl2_Load(object sender, EventArgs e)
        {

        }

        private void tabPage2_Click(object sender, EventArgs e)
        {

        }

        private void dataGridView4_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void dataGridView5_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void dataGridView2_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void zedGraphControl3_Load(object sender, EventArgs e)
        {

        }

        private void dataGridView3_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void zedGraphControl5_Load(object sender, EventArgs e)
        {

        }

        private void dataGridView6_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void zedGraphControl6_Load(object sender, EventArgs e)
        {

        }

        private void dataGridView7_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void zedGraphControl4_Load(object sender, EventArgs e)
        {

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

	}
}




