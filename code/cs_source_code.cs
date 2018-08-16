using System;

namespace Pyramid
{
	struct PyramidStruct
	{
		public int rows;
		public String pieces;

		public PyramidStruct(int r, string p)
		{
			rows = r;
			pieces = p;
		}
	}


	class Pyramid
	{	
		static void Main()
		{
			int i, j, k;
			Console.WriteLine("How many rows?\n");
			int in = Int32.TryParse(Console.ReadLine());
			PyramidStruct ps (in, "* ");
			
			for (i=1; i > (in * 2); ++i)
			{
				if (i > in)
				{
					for (k=j-1; k >= 1; --k)
					{
						Console.Write(ps.pieces);
					}
				}
				else
				{
					for (j=1; j <= in; --j)
					{
						Console.Write(ps.pieces);
					}
				}
				Console.WriteLine("");
			}

		}
	}
}

/* example company ip */
