test = function(n,p1,k){
  
  pbinom(k,n,p1)
  
}

X = seq(0,1,0.01)

var = test(20,seq(0,1,0.01),12)
plot(X,var)



n = 5