setwd("/Users/phbenham/Desktop/msSimulations_jan2017/2popAnalysis/NomConstant/")
options("scipen"=9999)
outfiles<-list.files(path ="/Users/phbenham/Desktop/msSimulations_jan2017/2popAnalysis/NomConstant/")
files<-lapply(outfiles,read.table)
i=0
for(file in files){
	i = i+1
	nam <- paste("pi",i, sep="")
	nam2<-paste("ss",i,sep="")
	assign(nam, file[,1])
	assign(nam2,file[,2])
}

#pi<-cbind(pi1,pi2,pi3,pi4,pi5,pi6,pi7,pi8,pi9,pi10,pi11,pi12,pi13,pi14,pi15,pi16,pi17,pi18,pi19,pi20,pi21,pi22,pi23,pi24)

#ss<-cbind(ss1,ss2,ss3,ss4,ss5,ss6,ss7,ss8,ss9,ss10,ss11,ss12,ss13,ss14,ss15,ss16,ss17,ss18,ss19,ss20,ss21,ss22,ss23,ss24)

pi<-cbind(pi1,pi2,pi3,pi4,pi5,pi6,pi7,pi8,pi9,pi10,pi11,pi12,pi13,pi14,pi15,pi16,pi17,pi18,pi19,pi20,pi21,pi22,pi23,pi24,pi25,pi26,pi27,pi28,pi29,pi30,pi31)

ss<-cbind(ss1,ss2,ss3,ss4,ss5,ss6,ss7,ss8,ss9,ss10,ss11,ss12,ss13,ss14,ss15,ss16,ss17,ss18,ss19,ss20,ss21,ss22,ss23,ss24,ss25,ss26,ss27,ss28,ss29,ss30,ss31)

colnames(pi)<-seq(500000,2000000,50000)
colnames(ss)<-seq(500000,2000000,50000)
#print(pi)
#print(ss)

ND2pi<-13.48
ND2ss<-86
NE<-seq(500000,2000000,50000)

quantilemat.pi<-data.frame(matrix(data=0, ncol=31,nrow=6))
rownames(quantilemat.pi) <- c(0.01,0.05,0.25,0.75,0.95,0.99)
colnames(quantilemat.pi) <- seq(500000,2000000,50000)

quantilemat.ss<-data.frame(matrix(data=0, ncol=31,nrow=6))
rownames(quantilemat.ss) <- c(0.01,0.05,0.25,0.75,0.95,0.99)
colnames(quantilemat.ss) <- seq(500000,2000000,50000)

for(b in 1:31){
	quantilemat.pi[,b]<-quantile(pi[,b], c(0.01,0.05,0.25,0.75,0.95,0.99),names=FALSE)
		
	quantilemat.ss[,b]<-quantile(ss[,b], c(0.01,0.05,0.25,0.75,0.95,0.99),names=FALSE)
}

nd2pi24<-rep(ND2pi,1,31)
nd2ss24<-rep(ND2ss,1,31)

quantilemat.pi<-t(quantilemat.pi)
quantilemat.ss<-t(quantilemat.ss)


par(mfrow=c(1,2),mar=c(5,4,2,2))

plot(NE,quantilemat.pi[,1], type='n', ylim=c(0,60), xlab ="Effective population size", ylab = "Pairwise differences")
points(NE,quantilemat.pi[,1], type='l', lty=1)
points(NE,quantilemat.pi[,2], type='l', lty=2, col="dark gray")
points(NE,quantilemat.pi[,3], type='l', lty=3, col = "gray")
points(NE,quantilemat.pi[,4], type='l', lty=3, col = "gray")
points(NE,quantilemat.pi[,5], type='l', lty=2, col = "dark gray")
points(NE,quantilemat.pi[,6], type='l', lty=1, col = "dark gray")
points(NE, nd2pi24, type='l', lty=2, lwd=1.5, col="blue")

plot(NE,quantilemat.ss[,1], type='n', ylim=c(0,200), xlab ="Effective population size", ylab = "Segregating Sites")
points(NE,quantilemat.ss[,1], type='l', lty=1)
points(NE,quantilemat.ss[,2], type='l', lty=2, col="dark gray")
points(NE,quantilemat.ss[,3], type='l', lty=3, col = "gray")
points(NE,quantilemat.ss[,4], type='l', lty=3, col = "gray")
points(NE,quantilemat.ss[,5], type='l', lty=2, col = "dark gray")
points(NE,quantilemat.ss[,6], type='l', lty=1, col = "dark gray")

points(NE, nd2ss24, type='l', lty=2, lwd=1.5, col="blue")

print(quantilemat.pi)
print(quantilemat.ss)
