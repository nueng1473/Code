#x = rnorm(100)
#y = rnorm(100)
#plot(x, y, xlab = "This's X-axis", ylab = "This's Y-axis",col = "green")

#x = seq(1, 3)
x = seq(-pi, pi, length = 3)
y = x
f = outer(x, y, function(x, y)cos(y)/(1+x^2))
contour(x, y, f, xlab = "This's X-axis", ylab = "This's Y-axis",col = "green")
