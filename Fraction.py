class Fraction(object): 
    def __init__ (self,num,den = None):
        if den == 0:
            raise Exception("denominator cannot be zero")
        if (not den):
            den = 1
        if(num == 0): 
            self.num = 0
            self.den = 1
        if num != int(num): 
            raise Exception("numerator must be an integer")
        if den != int(den):
            raise Exception("denominator must be an integer")
        div = self.gcd(num,den)
        num //= div
        den //= div
        self.num = int(num)
        self.den = int(den)
        
    def gcd (self,a,b):
        if (b == 1) or (a == 1):
            return 1
        remainder = 0
        while b!=0: 
            remainder = a % b 
            a = b
            b = remainder
        return a
    
    def __str__(self):
        return "\\frac{" + str(self.num) + "}{" + str(self.den) + "}"
    
    def __add__(self,f):
        #declare variables so that you don't modify value of original fractions
        a = self.num 
        b = self.den
        c = f.num
        d = f.den
        #find GCD to get LCM of denominators 
        div = self.gcd(b,d)
        lcm = b//div   #lcm(b,d) = b*d / gcd(b,d)
        lcm *= d
        a *= lcm//b    
        c *= lcm//d
        a += c   #once they have common denominator you add numerators 
        return Fraction(a, lcm) 
 
    def __sub__(self,f):
        a = f.num *-1
        b = f.den
        return self + Fraction(a,b)

    def __mul__(self,f):
        if (self.num == 0) or (f.num == 0):
            return Fraction(0,1)
        #declare variables so that you don't modify value of original fractions
        a = self.num 
        b = self.den
        c = f.num
        d = f.den
        div = self.gcd(a,d)
        a //= div
        d //= div
        div2 = self.gcd(b,c)
        b //= div2
        c //= div2
        return Fraction(a*c,b*d)
        
    def __truediv__(self,f):
        if(f.num == 0):
            raise Exception("Cannot divide by zero")
        #division is same as multiplying by the reciprocal 
        a = f.den
        b = f.num
        return self * Fraction(a,b)
        
    def decToFrac(self,dec): 
        den = 1
        while(int(dec) != dec):
            dec *= 10
            den *= 10
        return Fraction(dec,den)

    def floyd(self,f, x0):
        
        #mu = 0
        #lam = 0
        #if(x0 == 0):
        #    return lam,mu

        tortoise = f(x0) # f(x0) is the element/node next to x0.
        hare = f(f(x0))
        while tortoise != hare:
            #mu += 1
            #if(tortoise == 0):
                #return lam,mu
            tortoise = f(tortoise)
            hare = f(f(hare))
  
        mu = 0
        tortoise = x0
        while tortoise != hare:
            tortoise = f(tortoise)
            hare = f(hare)   # Hare and tortoise move at same speed
            mu += 1
 
        lam = 1
        hare = f(tortoise)
        while tortoise != hare:
            hare = f(hare)
            lam += 1
 
        return lam, mu

    def frac_to_repeating_decimal(self):
        a = self.num
        b = self.den
        decimalList = []

        
        f = lambda x: (x%b) *10 


        (lam,mu) = self.floyd(f,a) #apply floyd's algorithm to find the first repitition

        tortoise = a 
        for x in range(lam + mu):
            decimalList.append(tortoise//b)
            tortoise = f(tortoise)

        return decimalList,mu,lam
        #not the most optimal algorithm but very easy to understand

        
        # f = lambda r: r % b 
        # r = a % b 

    
    #discrete logarithm 
    def findSmallestRepeatedNines(d):

        #10^n-1 congruent to 0 mod d
        n = 1 #finding the shortest cycle length 
        u = 10**n - 1
        while(u%d != 0):
            n += 1
            u = 10**n - 1
        

        #print(u)
        repetend = u//d
        print(repetend)
        return (repetend,n)
    
    def round(self,n:int): 
        '''
        int -> Fraction 
        round to n decimal places
        '''
        #a/b ~ x/10^n 
        a = self.num
        b = self.den
        x = 10**n * a
        x /= b
        x = round(x)
        return Fraction(x,10**n)

    def __float__ (self):
        return self.num/self.den



    #def method to convert back to float and also scientific notation? 

    #if number is less than 0 should always put the negative sign on numerator not denominator
    #sign = -1 or sign = 1

    


        
#---------------------------------------------------------------------------------

factorialSet = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000, 51090942171709440000, 1124000727777607680000]
#
n = len(factorialSet)
sum = 0
sum = Fraction(sum)
sumArray = []
for x in range(n):
    sum += Fraction(1,factorialSet[x])
    sumArray.append(sum)

for x in sumArray:
    print(x)

'''
# \frac{1}{1}
# \frac{2}{1}
# \frac{5}{2}
# \frac{8}{3}
# \frac{65}{24}
# \frac{163}{60}
# \frac{1957}{720}
# \frac{685}{252}
# \frac{109601}{40320}
# \frac{98641}{36288}
# \frac{9864101}{3628800}
# \frac{13563139}{4989600}
# \frac{260412269}{95800320}
# \frac{8463398743}{3113510400}
# \frac{47395032961}{17435658240}
# \frac{888656868019}{326918592000}
# \frac{56874039553217}{20922789888000}
# \frac{7437374403113}{2736057139200}
# \frac{17403456103284421}{6402373705728000}
# \frac{82666416490601}{30411275102208}
# \frac{6613313319248080001}{2432902008176640000}
# \frac{69439789852104840011}{25545471085854720000}
# \frac{611070150698522592097}{224800145555521536000}
# '''





d = Fraction(3,14)
e = d.frac_to_repeating_decimal()
print(e)

d = Fraction(3,16)
e = d.frac_to_repeating_decimal()
print(e)

d = Fraction(65583,39848)
e = float(d)
print(e)
f = d.round(3)
print(f)
print(float(f))


# inputs= [7,13,17,23,29,31,37,43,53,91,161]

#     for x in inputs:
#         findSmallestRepeatedNines(x) 
# 142857 , 76923, 588235294117647, 434782608695652173913, 32258064516129, 27, 23255813953488372093
# 188679245283, 10989, 6211180124223602484472049689440993788819875776397515527950310559

