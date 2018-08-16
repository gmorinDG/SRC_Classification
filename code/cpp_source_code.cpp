#include <iostream>
using namespace std;

class Rectangle
{
    private:
	int width;
	int height;

    public:
	Rectangle(int w, int h)
	{
		width = w;
		height = h;

	}
	
	void setDimensions(int w, int h)
	{
		width = w;
		height = h;
	}
	
	int area() 
	{
		return width * height;
	}

	int getWidth()
	{
		return width;
	}

	int getHeight()
	{
		return height;
	}
};

int main(int argc, char *argv[])
{
	Rectangle rect(10, 5);
	cout << "width = " << rect.getWidth() << ", height = " << rect.getHeight();
	return 0;
}
