using System;
using System.Drawing;
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

            LineItem line1 = panel.AddCurve("y = f(x)точ.", list1, Color.DarkBlue, SymbolType.None);
            LineItem line2 = panel.AddCurve("y = f(x,h0)", list2, Color.Crimson, SymbolType.None);
            line1.Line.Width = 2;
            line2.Line.Width = 2;

            int n = DiffEquations.N;
            dataGridView5.Rows.Clear();
            for (int i=0;i<n;++i)
            {
                dataGridView5.Rows.Add();
                dataGridView5[0, i].Value = DiffEquations.Calculate(DiffEquations.N1)[0][i];
                dataGridView5[1, i].Value = DiffEquations.Calculate(DiffEquations.N1)[1][i];
                dataGridView5[2, i].Value = DiffEquations.Calculate(DiffEquations.N1)[2][i];
                dataGridView5[3, i].Value = DiffEquations.Calculate(DiffEquations.N1)[1][i] -
                    DiffEquations.Calculate(DiffEquations.N1)[2][i];
                dataGridView5[4, i].Value = (DiffEquations.Calculate(DiffEquations.N1)[1][i] -
                                             DiffEquations.Calculate(DiffEquations.N1)[2][i]) /
                                            DiffEquations.Calculate(DiffEquations.N1)[1][i] * 100;
                
                list1.Add(DiffEquations.Calculate(DiffEquations.N1)[0][i],
                    DiffEquations.Calculate(DiffEquations.N1)[1][i]);  // график точной 
                // добавим в список точку
                list2.Add(DiffEquations.Calculate(DiffEquations.N1)[0][i],
                    DiffEquations.Calculate(DiffEquations.N1)[2][i]);  // график точной функции
            }
          
            
            //Устанавливаем интересующий нас интервал по оси Х
            //для первой табл.
            panel.XAxis.Scale.Min = DiffEquations.A;
            panel.XAxis.Scale.Max = DiffEquations.B + 0.1;

            //Устанавливаем интересующий нас интервал по оси Y 
            //для первой табл.
            panel.YAxis.Scale.Min = -0.8;
            panel.YAxis.Scale.Max = 0.1;

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

            LineItem line1 = panel.AddCurve("y = f(x)точ.", list1, Color.DarkBlue, SymbolType.None);
            LineItem line2 = panel.AddCurve("y = f(x,h1)", list2, Color.Crimson, SymbolType.None);
            line1.Line.Width = 2;
            line2.Line.Width = 2;


            int n = DiffEquations.N;
            dataGridView1.Rows.Clear();
            for (int i = 0; i < n; ++i)
            {
                dataGridView1.Rows.Add();
                dataGridView1[0, i].Value = DiffEquations.Calculate(DiffEquations.N2)[0][i];
                dataGridView1[1, i].Value = DiffEquations.Calculate(DiffEquations.N2)[1][i];
                dataGridView1[2, i].Value = DiffEquations.Calculate(DiffEquations.N2)[2][i];
                dataGridView1[3, i].Value = (DiffEquations.Calculate(DiffEquations.N2)[1][i] -
                    DiffEquations.Calculate(DiffEquations.N2)[2][i]);
                dataGridView1[4, i].Value = (DiffEquations.Calculate(DiffEquations.N2)[1][i] -
                                             DiffEquations.Calculate(DiffEquations.N2)[2][i]) /
                                            DiffEquations.Calculate(DiffEquations.N2)[1][i] * 100;

                list1.Add(DiffEquations.Calculate(DiffEquations.N1)[0][i],
                   DiffEquations.Calculate(DiffEquations.N1)[1][i]);  // график точной функции

                // добавим в список точку
                list2.Add(DiffEquations.Calculate(DiffEquations.N2)[0][i],
                    DiffEquations.Calculate(DiffEquations.N2)[2][i]);  // график приближенной функции 
              }

            //Устанавливаем интересующий нас интервал по оси Х
            //для первой табл.
            //Устанавливаем интересующий нас интервал по оси Х
            //для первой табл.
            panel.XAxis.Scale.Min = DiffEquations.A;
            panel.XAxis.Scale.Max = DiffEquations.B + 0.1;

            //Устанавливаем интересующий нас интервал по оси Y 
            //для первой табл.
            panel.YAxis.Scale.Min = -0.8;
            panel.YAxis.Scale.Max = 0;

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

	    private void DrawH2()
        {
            GraphPane panel = zedGraphControl3.GraphPane;

            panel.Title.Text = "Графіки функцій y = f(x)точ. i f(x,h2) ";
            panel.XAxis.Title.Text = "X";
            panel.YAxis.Title.Text = "Y";

            panel.CurveList.Clear();

            PointPairList list1 = new PointPairList();
            PointPairList list2 = new PointPairList();

            var line1 = panel.AddCurve("y = f(x)точ.", list1, Color.DarkBlue, SymbolType.None);
            var line2 = panel.AddCurve("y = f(x,h2)", list2, Color.Crimson, SymbolType.None);
            line1.Line.Width = 2;
            line2.Line.Width = 2;

            int n = DiffEquations.N3;
            dataGridView2.Rows.Clear();
            for (int i = 0; i < n; ++i)
            {
                dataGridView2.Rows.Add();
                dataGridView2[0, i].Value = DiffEquations.Calculate(DiffEquations.N3)[0][i];
                dataGridView2[1, i].Value = DiffEquations.Calculate(DiffEquations.N3)[1][i];
                dataGridView2[2, i].Value = DiffEquations.Calculate(DiffEquations.N3)[2][i];
                dataGridView2[3, i].Value = DiffEquations.Calculate(DiffEquations.N3)[1][i] -
                    DiffEquations.Calculate(DiffEquations.N3)[2][i];
                dataGridView2[4, i].Value = (DiffEquations.Calculate(DiffEquations.N3)[1][i] -
                                             DiffEquations.Calculate(DiffEquations.N3)[2][i]) /
                                            DiffEquations.Calculate(DiffEquations.N3)[1][i] * 100;

                // добавим в список точку
                list1.Add(DiffEquations.Calculate(DiffEquations.N3)[0][i],
                    DiffEquations.Calculate(DiffEquations.N3)[1][i]);  // график точной функции
                list2.Add(DiffEquations.Calculate(DiffEquations.N3)[0][i],
                    DiffEquations.Calculate(DiffEquations.N3)[2][i]);  // график приближенной функции 
                }


            //Устанавливаем интересующий нас интервал по оси Х
            //для первой табл.
            panel.XAxis.Scale.Min = DiffEquations.A;
            panel.XAxis.Scale.Max = DiffEquations.B + 0.1;

            //Устанавливаем интересующий нас интервал по оси Y 
            //для первой табл.
            panel.YAxis.Scale.Min = -0.8;
            panel.YAxis.Scale.Max = 0.01;


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
            int n = DiffEquations.N;
            int k = 0;
            dataGridView3.Rows.Add();
            dataGridView3[0, k++].Value = "n = 5";
            for (int i = 0; i < n; ++i)
            {
                if (i == DiffEquations.N / 2 || i == DiffEquations.N-2)
                    
                {
                    dataGridView3.Rows.Add();
                    dataGridView3[0, k].Value = DiffEquations.Calculate(DiffEquations.N1)[0][i];
                    dataGridView3[1, k].Value = DiffEquations.Calculate(DiffEquations.N1)[1][i];
                    dataGridView3[2, k].Value = DiffEquations.Calculate(DiffEquations.N1)[2][i];
                    dataGridView3[3, k].Value = DiffEquations.Calculate(DiffEquations.N1)[1][i] -
                                                DiffEquations.Calculate(DiffEquations.N1)[2][i];
                    dataGridView3[4, k].Value = (DiffEquations.Calculate(DiffEquations.N1)[1][i] -
                                                 DiffEquations.Calculate(DiffEquations.N1)[2][i])/
                                                DiffEquations.Calculate(DiffEquations.N1)[1][i]*100;
                    ++k;
                }

            }
            dataGridView3.Rows.Add();
            dataGridView3[0, k++].Value = "n = 20";
            for (int i = 0; i < n; ++i)
            {
                if (i == DiffEquations.N / 2 || i == DiffEquations.N - 2)
                {
                    dataGridView3.Rows.Add();
                    dataGridView3[0, k].Value = DiffEquations.Calculate(DiffEquations.N2)[0][i];
                    dataGridView3[1, k].Value = DiffEquations.Calculate(DiffEquations.N2)[1][i];
                    dataGridView3[2, k].Value = DiffEquations.Calculate(DiffEquations.N2)[2][i];
                    dataGridView3[3, k].Value = DiffEquations.Calculate(DiffEquations.N2)[1][i] -
                                                DiffEquations.Calculate(DiffEquations.N2)[2][i];
                    dataGridView3[4, k].Value = (DiffEquations.Calculate(DiffEquations.N2)[1][i] -
                                                 DiffEquations.Calculate(DiffEquations.N2)[2][i]) /
                                                DiffEquations.Calculate(DiffEquations.N2)[1][i] * 100;
                    ++k;
                }

            }
            dataGridView3.Rows.Add();
            dataGridView3[0, k++].Value = "n = 50";
            for (int i = 0; i < n; ++i)
            {
                if (i == DiffEquations.N / 2 || i == DiffEquations.N - 2)
                {
                    dataGridView3.Rows.Add();
                    dataGridView3[0, k].Value = DiffEquations.Calculate(DiffEquations.N3)[0][i];
                    dataGridView3[1, k].Value = DiffEquations.Calculate(DiffEquations.N3)[1][i];
                    dataGridView3[2, k].Value = DiffEquations.Calculate(DiffEquations.N3)[2][i];
                    dataGridView3[3, k].Value = DiffEquations.Calculate(DiffEquations.N3)[1][i] -
                                                DiffEquations.Calculate(DiffEquations.N3)[2][i];
                    dataGridView3[4, k].Value = (DiffEquations.Calculate(DiffEquations.N3)[1][i] -
                                                 DiffEquations.Calculate(DiffEquations.N3)[2][i]) /
                                                DiffEquations.Calculate(DiffEquations.N3)[1][i] * 100;
                    ++k;
                }

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

       
        private void dataGridView3_CellContentClick_1(object sender, DataGridViewCellEventArgs e)
        {

        }

	}
}




