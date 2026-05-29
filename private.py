class myClass:

    _privayeVar = 27;

    def _privMeth(self):
        print ("I'm inside class myClass")

    def hello(self):
        print ("Private variable value: ", myClass._privayeVar)

foo = myClass()
foo.hello()
foo._privateMeth()