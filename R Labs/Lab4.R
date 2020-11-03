setwd("~/GitHub/The-Music-of-Primes/R Labs")
load('sbp.RData')

mu = mean(sbp)

n = 5
sbpsample = sbp[sample(length(sbp),n)]

mean(sbpsample) - qt(0.975,df=n-1)*sd(sbpsample)/sqrt(n)

mean(sbpsample) + qt(0.975,df=n-1)*sd(sbpsample)/sqrt(n)

nSim = 10000
n = 100

ciArray = array(0, dim=c(nSim,2))
for (i in 1:nSim) {
  sbpsample = sbp[sample(length(sbp),n)]
  ciArray[i,1] = mean(sbpsample) - qt(0.975,df=n-1)*sd(sbpsample)/sqrt(n) #adds lower and upper CI
  ciArray[i,2] = mean(sbpsample) + qt(0.975,df=n-1)*sd(sbpsample)/sqrt(n)
}

mean((ciArray[,1]<mu) & (mu<ciArray[,2])) #avg number of CI that satisfy Mu
#it is below 95% as hist(sbp) is not normally distributed but right skewed