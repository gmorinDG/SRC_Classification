class HelloWorld
	def initialize(name)
		@name = name.capitalize
	end

	def hello
		puts "Hello #{@name}!"
	end
end

hello = HelloWorld.new("World")
hello.hello