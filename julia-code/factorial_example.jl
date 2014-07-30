function fact(n)
    if n == 0
        return 1
    end
    return n*fact(n-1)
end

for n =1:21
  println("The Factorial of " , n , " is ", fact(n))
end
