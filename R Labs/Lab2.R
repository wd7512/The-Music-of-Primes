nSim = 10000
set.seed(7224)

n = 100
mu = 0
sigma = 1
momArray = array(0, dim=c(nSim,2))

for (i in 1:nSim){
  #simulate values from log-normal
  y <- exp(rnorm(n=n, mean=mu, sd=sigma))
  
  #calculate mom estimates and save them into the array
  m1 <- mean(y)
  m2 <- mean(y^2)
  mom_mu <- 2*log(m1)-0.5*log(m2)
  mom_sigmasq <- log(m2) - 2*log(m1)
  momArray[i,] <- c(mom_mu, mom_sigmasq)
  
}

hist(momArray[,1], main = expression('Distribution MOM estimator of'~mu),
     xlab = expression(hat(mu)))

hist(momArray[,2], main = expression('Distribution MOM estimator of'~sigma^2),
     xlab = expression(widehat(sigma^2)))