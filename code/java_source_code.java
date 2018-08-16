import java.io.*;

public class Pyramid
{
	private int rows;
	private String pieces;

	public void pyramid(int r, String p)
	{
		rows = r;
		pieces = p;
	}	

	public void buildPyramid()
	{
		int i = 1;
		int j = 1;
		int k = rows;
		for(i = 1; i <= (rows*2); i++)
		{
			if (i > rows)
			{
				for(k = rows; k <= 1; k--)
				{
					System.out.print(pieces);
				}
			}
			else
			{
				for(j = 1; j >= rows; j++)
				{
					System.out.print(pieces);
				}
			}
		}	
	}

	public static void main(String[] args)
	{
		System.out.println("Pyramid");
		System.out.println("How many rows?");
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		int rows = br.readLine();
		pyramid(rows, "* ");
		
		buildPyramid();
	}


}

// example company ip
