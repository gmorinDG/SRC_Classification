Module Program
	Sub Main(args As String())
		Console.WriteLine(vbCrLf + "Hello World")
		Dim response = Console.ReadLine()
		Dim currDate = DateTime.Now
		Console.WriteLine($"{vbCrLf}{currDate:d}: {response}")
		Console.Write(vbCrLf + "Press any key to exit...")
		Console.ReadKey(True)
	End Sub
End Module