setwd("~/GitHub/The-Music-of-Primes/R Labs")
load("sbp.RData")
summary(sbp)

nSim = 10000
n = 10
meanArray = array(0,dim=nSim)

for (i in 1:nSim){ 
  sbpn = sbp[sample(length(sbp),n)]
  sbpnmean = mean(sbpn)
  meanArray[i] = sbpnmean
}

meana = mean(meanArray)
vara = var(meanArray)

n = 1000
meanArray = array(0,dim=nSim)

for (i in 1:nSim){ 
  sbpn = sbp[sample(length(sbp),n)]
  sbpnmean = mean(sbpn)
  meanArray[i] = sbpnmean
}

meanb = mean(meanArray)
varb = var(meanArray)