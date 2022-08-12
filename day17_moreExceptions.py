class Calculator:
    
    def power(self, n, p):
        if n < 0 or p < 0:
            myError = ValueError('n and p should be non-negative')
            raise myError
        else:
            return n**p





myCalculator = Calculator()
print(myCalculator.power(3,5))