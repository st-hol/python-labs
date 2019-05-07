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
            DrawH0();
            DrawH1();
            DrawH2();
            Draw();
        }

        public void DrawH0()
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
                dataGridView5[0, i].Value = DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[0][i];
                dataGridView5[1, i].Value = DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[1][i];
                dataGridView5[2, i].Value = DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[2][i];
                dataGridView5[3, i].Value = DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[1][i] -
                    DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[2][i];
                dataGridView5[4, i].Value = (DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[1][i] -
                                             DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[2][i]) /
                                            DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[1][i] * 100;
                
                // добавим в список точку
                list1.Add(DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[0][i],
                    DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[1][i]);  // график точной функции
                list2.Add(DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[0][i],
                    DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[2][i]);  // график приближенной функции 
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


        public void DrawH1()
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
            dataGridView1.Rows.Clear();
            for (int i = 0; i < n; ++i)
            {
                dataGridView1.Rows.Add();
                dataGridView1[0, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[0][i];
                dataGridView1[1, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i];
                dataGridView1[2, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[2][i];
                dataGridView1[3, i].Value = (DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i] -
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[2][i]);
                dataGridView1[4, i].Value = (DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i] -
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

        public void DrawH2()
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
            dataGridView2.Rows.Clear();
            for (int i = 0; i < n; ++i)
            {
                dataGridView2.Rows.Add();
                dataGridView2[0, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[0][i];
                dataGridView2[1, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i];
                dataGridView2[2, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[2][i];
                dataGridView2[3, i].Value = DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i] -
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[2][i];
                dataGridView2[4, i].Value = (DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i] -
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

        public void Draw()
        {
            GraphPane panel = zedGraphControl4.GraphPane;

            panel.Title.Text = "Додаткове завдання ";
            panel.XAxis.Title.Text = "X";
            panel.YAxis.Title.Text = "Y";

            panel.CurveList.Clear();

            PointPairList list1 = new PointPairList();
            PointPairList list2 = new PointPairList();
            PointPairList list3 = new PointPairList();

            LineItem Line1 = panel.AddCurve("y = е(x,h0)/y(xk)", list1, Color.DarkBlue, SymbolType.None);
            LineItem Line2 = panel.AddCurve("y = е(x,h1)/y(xk)", list2, Color.Crimson, SymbolType.None);
            LineItem Line3 = panel.AddCurve("y = е(x,h2)/y(xk)", list2, Color.Green, SymbolType.None);


            //Устанавливаем интересующий нас интервал по оси Х
            //для первой табл.
            panel.XAxis.Scale.Min = DiffEquationsCauchy.A;
            panel.XAxis.Scale.Max = DiffEquationsCauchy.B + 0.1;

            //Устанавливаем интересующий нас интервал по оси Y 
            //для первой табл.
            panel.YAxis.Scale.Min = -0.2;
            panel.YAxis.Scale.Max = 1.4;



            int n = (int)((DiffEquationsCauchy.B - DiffEquationsCauchy.A) / DiffEquationsCauchy.H0 + 1);
            for (int i = 0; i < n; ++i)
            {   // добавим в список точку
                list1.Add(DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[0][i],
                   ( DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[1][i] -
                    DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[2][i]) /
                    DiffEquationsCauchy.Calculatе(DiffEquationsCauchy.H0)[1][i] * 100);  // график точной функции
            }


            n = (int)((DiffEquationsCauchy.B - DiffEquationsCauchy.A) / DiffEquationsCauchy.H1 + 1);
            for (int i = 0; i < n; ++i)
            {

                // добавим в список точку
                list2.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[0][i],
                   (DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i] -
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[2][i]) /
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H1)[1][i] * 100);  // график точной функции
            }


            n = (int)((DiffEquationsCauchy.B - DiffEquationsCauchy.A) / DiffEquationsCauchy.H2 + 1);
            for (int i = 0; i < n; ++i)
            {

                // добавим в список точку
                list3.Add(DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[0][i],
                   (DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i] -
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[2][i]) /
                    DiffEquationsCauchy.Calculate(DiffEquationsCauchy.H2)[1][i] * 100);  // график точной функции
            }

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
            zedGraphControl4.AxisChange();

            //Обновляем график
            zedGraphControl4.Invalidate();


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

        private void dataGridView5_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
        private void zedGraphControl3_Load(object sender, EventArgs e)
        {

        }
        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void dataGridView2_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void zedGraphControl4_Load(object sender, EventArgs e)
        {

        }

	}
}




