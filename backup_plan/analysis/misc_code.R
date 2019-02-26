require(mgcv)

########### READING IN DATA AND SUBSETTING #####################

# read in data, change date column to date type
data <- read.csv(file="G:/My Drive/Year 2/Thesis/Backup_Plan/all_data/cardio_resp_renal/all_data_weather_mortality_population_dow.csv", header=TRUE, sep=",")
data$date <- as.Date(data$date, "%m/%d/%Y")

# subset data by summer months and climate regions
summer_months <- c('04', '05', '06', '07', '08', '09')
data <- subset(data, format.Date(date, "%m") %in% summer_months)

n_data <- data[which(data$clim_div=='NORTHERN'),]
tw_data <- data[which(data$clim_div=='TIDEWATER'),]
cm_data <- data[which(data$clim_div=='CENTRAL MOUNTAIN'),]
wp_data <- data[which(data$clim_div=='WESTERN PIEDMONT'),]
ep_data <- data[which(data$clim_div=='EASTERN PIEDMONT'),]
swm_data <- data[which(data$clim_div=='SOUTHWESTERN MOUNTAIN'),]

############ NORTHERN CLIMATE DIVISION #######################
hist(n_data$death_count, breaks=20)
plot(n_data$tmmx_f, n_data$death_count)
n_data_1988 <- subset(n_data, format.Date(date, "%Y") %in% 1979)

library(plyr)
ddply(n_data, .(cut(n_data$tmmx_f, 5)), colwise(mean))
tapply(n_data$death_count, cut(n_data$tmmx_f, seq(40, 110, by=10)), mean)
tapply(tw_data$death_count, cut(tw_data$tmmx_f, seq(40, 110, by=10)), mean)
tapply(cm_data$death_count, cut(cm_data$tmmx_f, seq(40, 110, by=10)), mean)
tapply(ep_data$death_count, cut(ep_data$tmmx_f, seq(40, 110, by=10)), mean)
tapply(wp_data$death_count, cut(wp_data$tmmx_f, seq(40, 110, by=10)), mean)
tapply(swm_data$death_count, cut(swm_data$tmmx_f, seq(40, 110, by=10)), mean)

n_loess <- loess(death_count ~ tmmx_f, data = n_data, span=0.25)
smoothed25 <- predict(n_loess)
plot(n_data$death_count, x=n_data$tmmx_f, main="Loess Smoothing and Prediction", xlab="tmmx_f", ylab="daily death count")
lines(smoothed25, x=n_data$tmmx_f, col="red")

n_loess <- loess(death_count ~ as.numeric(date), data=n_data)
smoothed25 <- predict(n_loess)
plot(n_data$death_count, x=n_data$date, main="Loess Smoothing and Prediction", xlab="date", ylab="daily death count")
lines(smoothed25, x=n_data$date, col="red")

n_loess <- loess(death_count ~ as.numeric(date), data=n_data_1988)
smoothed25 <- predict(n_loess)
plot(n_data_1988$death_count, x=n_data_1988$date, main="Loess Smoothing and Prediction", xlab="date", ylab="daily death count")
lines(smoothed25, x=n_data_1988$date, col="red")

n_gam <- gam(death_count ~ dow + s(tmmx_f) + s(rmax) + s(year) + offset(log(tot_pop)), family=poisson, data=n_data, method="REML", all.terms=TRUE)
plot(n_gam, rug=TRUE, residuals=TRUE, pch=1, cex=1, shade=TRUE, shade.col="lightblue", seWithMean=TRUE, trans=exp)
coef(n_gam)

# bin data into average deaths per 


p1<- ggplot(n_data, aes(x=year, y=death_count)) + geom_line() + geom_smooth(se = FALSE, method='loess', span=0.25)
p2<- ggplot(n_data, aes(x=tmmx_f, y=death_count)) + geom_line() + geom_smooth(se = FALSE, method='loess', span=0.25)
plot_grid(p1, p2, ncol = 1)

p1<- ggplot(tw_data, aes(x=year, y=death_count)) + geom_line() + geom_smooth(se = FALSE, method='loess', span=0.25)
p2<- ggplot(tw_data, aes(x=tmmx_f, y=death_count)) + geom_line() + geom_smooth(se = FALSE, method='loess', span=0.25)
plot_grid(p1, p2, ncol = 1)

n_data1979_1987 = n_data_1988 <- subset(n_data, format.Date(date, "%Y") %in% 1979:1987)
n_glm <- glm(death_count ~ heat_index + dow + year, offset=log(tot_pop), data=n_data1979_1987, family="poisson")
n_glm2 <- glm(death_count ~ rmax + offset(log(tot_pop)), family=poisson, data=n_data1979_1987)
n_data1988 = n_data_1988 <- subset(n_data, format.Date(date, "%Y") %in% 1988)
deaths_1988_pred <- exp(predict(n_glm2, n_data1988))

plot(n_data1988$tmmx_f, deaths_1988_pred)
plot(n_data1988$death_count, deaths_1988_pred)



# shuffle
n_data_shuffle <- n_data[sample(nrow(n_data)),]
smp_size <- floor(0.75 * nrow(n_data_shuffle))
train_ind <- sample(seq_len(nrow(n_data_shuffle)), size = smp_size)
train <- n_data_shuffle[train_ind, ]
test <- n_data_shuffle[-train_ind, ]

glm <- glm(death_count ~ tmmx_f + rmax + dow + year + offset(log(tot_pop)), data=train, family="poisson")
pred <-  exp(predict(glm, test))
plot(pred, test$death_count)

gam <- gam(death_count ~ dow + s(tmmx_f) + s(rmax) + s(year) + offset(log(tot_pop)), family=quasipoisson, data=train, method="REML", all.terms=TRUE)
pred <-  exp(predict(gam, test))
plot(pred, test$death_count)
########### TIDEWATER CLIMATE DIVISION #######################
hist(tw_data$death_count, breaks=20)
plot(tw_data$tmmx_f, tw_data$death_count)

tw_loess <- loess(death_count ~ tmmx_f, data = tw_data, span=0.25)
smoothed25 <- predict(tw_loess)
plot(tw_data$death_count, x=tw_data$tmmx_f, main="Loess Smoothing and Prediction", xlab="tmmx_f", ylab="daily death count")
lines(smoothed25, x=tw_data$tmmx_f, col="red")

# tried to adjust k to make rmax significant but can't
tw_gam <- gam(death_count ~ dow + s(tmmx_f, k=100) + s(rmax, k=100) + s(year) + offset(log(tot_pop)), family=poisson, data=tw_data, method="REML", all.terms=TRUE)
plot(tw_gam, rug=TRUE,pch=1, cex=1, shade=TRUE, shade.col="lightblue", seWithMean=TRUE, residuals=TRUE, trans=exp)

# keep in mind these test statistics are approximate -- a good way to check if a term is significant is if you can't
# draw a horizontal line through the 95% CI
summary(tw_gam)

# we see from the partial effect plots that the s(tmmx_f) is non-linear.
plot(tw_gam)
gam.check(tw_gam)


########### CENTRAL MOUNTAIN CLIMATE DIVISION #######################
hist(cm_data$death_count, breaks=20)
plot(cm_data$tmmx_f, cm_data$death_count)

cm_loess <- loess(death_count ~ tmmx_f, data = cm_data, span=0.25)
smoothed25 <- predict(cm_loess)
plot(cm_data$death_count, x=cm_data$tmmx_f, main="Loess Smoothing and Prediction", xlab="tmmx_f", ylab="daily death count")
lines(smoothed25, x=cm_data$tmmx_f, col="red")



########### WESTERN PIEDMONT CLIMATE DIVISION #######################
hist(wp_data$death_count, breaks=20)
plot(wp_data$tmmx_f, wp_data$death_count)

wp_loess <- loess(death_count ~ tmmx_f, data = wp_data, span=0.25)
smoothed25 <- predict(wp_loess)
plot(wp_data$death_count, x=wp_data$tmmx_f, main="Loess Smoothing and Prediction", xlab="tmmx_f", ylab="daily death count")
lines(smoothed25, x=wp_data$tmmx_f, col="red")

##########DLNM practice
library(splines)
varknots <- equalknots(n_data$tmmx_f,fun="bs",df=5,degree=2)
lagknots <- logknots(2, 3)
cb3.temp <- crossbasis(n_data$tmmx_f, lag=2, argvar=list(fun="bs",
                                                         knots=varknots), arglag=list(knots=lagknots))



model3 <- glm(death_count ~ cb3.temp + ns(time, 7*14) + dow,
              family=quasipoisson(), n_data)
pred3.temp <- crosspred(cb3.temp, model3, cen=21, by=1)
plot(pred3.temp, xlab="Temperature", zlab="RR", theta=200, phi=40, lphi=30,
     main="3D graph of temperature effect")

################### example of lpmatrix
library(mgcv)
library(mgcViz)
n <- 200
sig <- 2
dat <- gamSim(1,n=n,scale=sig)

b <- gam(y ~ s(x0) + s(I(x1^2)) + s(x2) + offset(x3), data = dat)

newd <- data.frame(x0=(0:30)/30, x1=(0:30)/30, x2=(0:30)/30, x3=(0:30)/30)

Xp <- predict(b, newd, type="lpmatrix")

xn <- c(.341,.122,.476,.981) ## want prediction at these values
x0 <- 1         ## intercept column
dx <- 1/30      ## covariate spacing in `newd'
for (j in 0:2) { ## loop through smooth terms
  cols <- 1+j*9 +1:9      ## relevant cols of Xp
  i <- floor(xn[j+1]*30)  ## find relevant rows of Xp
  w1 <- (xn[j+1]-i*dx)/dx ## interpolation weights
  ## find approx. predict matrix row portion, by interpolation
  x0 <- c(x0,Xp[i+2,cols]*w1 + Xp[i+1,cols]*(1-w1))
}
dim(x0)<-c(1,28) 
fv <- x0%*%coef(b) + xn[4];fv    ## evaluate and add offset
se <- sqrt(x0%*%b$Vp%*%t(x0));se ## get standard error
## compare to normal prediction
predict(b,newdata=data.frame(x0=xn[1],x1=xn[2],
                             x2=xn[3],x3=xn[4]),se=TRUE)



