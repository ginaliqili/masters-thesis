require(mgcv)
require(gratia)
require(plyr)
options(scipen=99)
require(slines)
########### READING IN DATA AND SUBSETTING #####################

# read in data, change date column to date type
data <- read.csv(file="G:/My Drive/Year 2/Thesis/Data/1979-1988/all_data/all_data_weather_mortality_population_dow_lags.csv", header=TRUE, sep=",")
data$date <- as.Date(data$date, format="%Y-%m-%d")
data$month <- as.factor(format.Date(data$date, format="%m"))
# replace all -999s with NA (these are the lag values that don't exist)
data[data==-999] <-NA

# seasonal variation/long term trend
data_agg_year <- aggregate(data$death_count, by=list(year=data$year), FUN=mean)
data_agg_month <- aggregate(data$death_count, by=list(month=data$month), FUN=mean)
plot(data_agg_year$year, data_agg_year$x, pch=1, xlab="Year", ylab="Average Number of Daily Deaths")
plot(data_agg_month$month, data_agg_month$x, pch=1, xlab="Month", ylab="Average Number of Daily Deaths")

# binning temperatures
tapply(data$tmmx_f, cut(data$death_count, seq(0, 100, by=5)), mean)

# subset data by summer months and climate regions
summer_months <- c('04', '05', '06', '07', '08', '09')
data <- subset(data, format.Date(date, "%m") %in% summer_months)

# subset again, keep tempeartures about 60 degrees only
#data <- data[ which(data$tmmx_f >=60), ]

# reorder dow factor to be Sunday-Saturday, also change value to abbreviations
data$dow <- factor(data$dow, levels=c("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"))
data$dow_abbrev <- mapvalues(data$dow, 
                               from=c("Sunday","Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"), 
                               to=c("Su","M","T", "W", "Th", "F", "Sa"))

n_data <- data[which(data$clim_div=='NORTHERN'),]
tw_data <- data[which(data$clim_div=='TIDEWATER'),]
cm_data <- data[which(data$clim_div=='CENTRAL MOUNTAIN'),]
wp_data <- data[which(data$clim_div=='WESTERN PIEDMONT'),]
ep_data <- data[which(data$clim_div=='EASTERN PIEDMONT'),]
swm_data <- data[which(data$clim_div=='SOUTHWESTERN MOUNTAIN'),]

# seasonal variation and long term plots for each of the climate divisions
data_agg_year <- aggregate(swm_data$death_count, by=list(year=swm_data$year), FUN=mean)
data_agg_month <- aggregate(swm_data$death_count, by=list(month=swm_data$month), FUN=mean)
plot(data_agg_year$year, data_agg_year$x, pch=1, xlab="Year", ylab="Average Number of Daily Deaths")
plot(data_agg_month$month, data_agg_month$x, pch=1, xlab="Month", ylab="Average Number of Daily Deaths")

############ NORTHERN CLIMATE DIVISION #######################
library(stargazer)
hist(n_data$death_count, breaks=20)
plot(n_data$tmmx_f, n_data$death_count)
summary(n_data)
stargazer(n_data, type="text")


n_gam <- gam(death_count ~ dow_abbrev + s(heat_index) + s(heat_index_lag_1) + month + year + offset(log(tot_pop)), family=poisson, data=n_data, method="REML")
n_gam <- gam(death_count ~ dow_abbrev + s(heat_index) + s(heat_index_lag_1) + s(doy) + year + offset(log(tot_pop)), family=poisson, data=n_data, method="REML")

n_gam <- gam(death_count ~ dow_abbrev + s(heat_index) + month + year + offset(log(tot_pop)), family=poisson, data=n_data, method="REML")
n_gam <- gam(death_count ~ dow_abbrev + s(heat_index_lag_1) + month + year + offset(log(tot_pop)), family=poisson, data=n_data, method="REML")
n_gam <- gam(death_count ~ dow_abbrev + s(tmmx_f) + s(tmmx_lag_1) + s(rmax) + s(rmax_lag_1) + month + year + offset(log(tot_pop)), family=poisson, data=n_data, method="REML")
plot(n_gam, rug=TRUE, pch=1, cex=1, shade=TRUE, shade.col="lightblue", seWithMean=TRUE, trans=exp)
coef(n_gam)
plot(n_gam, xlab="Heat Index", ylab="Partial Effect of Heat Index on Daily Deaths")
plot(n_gam, xlab="Max Temp", ylab="Partial Effect of Max Temp on Daily Deaths")

n_deriv <- derivatives(n_gam, "s(heat_index)", n=300)
draw(n_deriv)
print(n_deriv, n=300)

n_glm <- glm(death_count ~ heat_index +  heat_index_lag_1 + dow_abbrev + year + month, offset=log(tot_pop), data=n_data, family="poisson")
n_glm2 <- glm(death_count ~ heat_index +  heat_index_lag_1 + dow_abbrev + year + ns(doy, df=3), offset=log(tot_pop), data=n_data, family="poisson")
exp(8.379e-04)
# 95% CI
exp(8.379e-04 - 1.96*3.936e-04)# 1 unit increase
exp(8.379e-04 + 1.96*3.936e-04) # 1 unit increase, this looks problematic

n_glm <- glm(death_count ~ tmmx_f + tmmx_lag_1 + rmax + rmax_lag_1 + dow_abbrev + year + month, offset=log(tot_pop), data=n_data, family="poisson")
exp(2.522e-03)
exp(2.522e-03 - 1.96*1.009e-03)
exp(2.522e-03 + 1.96*1.009e-03)

########### TIDEWATER CLIMATE DIVISION #######################
hist(tw_data$death_count, breaks=20)
plot(tw_data$tmmx_f, tw_data$death_count)
summary(tw_data)
stargazer(tw_data, type="text")

# tried to adjust k to make rmax significant but can't
tw_gam <- gam(death_count ~ dow_abbrev + s(heat_index) + s(heat_index_lag_1) + year + month + offset(log(tot_pop)), family=poisson, data=tw_data, method="REML")
tw_gam <- gam(death_count ~ dow_abbrev + s(tmmx_f) + s(tmmx_lag_1) + s(rmax) + s(rmax_lag_1) + year + month + offset(log(tot_pop)), family=poisson, data=tw_data, method="REML")

plot(tw_gam, rug=TRUE,pch=1, cex=1, shade=TRUE, shade.col="lightblue", seWithMean=TRUE, trans=exp)
plot(tw_gam, xlab="Max Temp", ylab="Partial Effect of Max Temp on Daily Deaths")

tw_glm <- glm(death_count ~ dow_abbrev + heat_index + heat_index_lag_1 + year + month + offset(log(tot_pop)),data=tw_data, family=poisson)
exp(1.790e-02)
exp(1.790e-02 - 1.96*8.510e-03)
exp(1.790e-02 + 1.96*8.510e-03)
summary(tw_glm)
tw_glm <- glm(death_count ~ dow_abbrev + tmmx_f + tmmx_lag_1 + rmax + rmax_lag_1 + year + month + offset(log(tot_pop)),data=tw_data)
exp(4.861e-02)
exp(1.790e-02 - 1.96*2.710e-02)
exp(1.790e-02 + 1.96*2.710e-02)
# keep in mind these test statistics are approximate -- a good way to check if a term is significant is if you can't
# draw a horizontal line through the 95% CI
summary(tw_gam)
summary(tw_glm)
# we see from the partial effect plots that the s(tmmx_f) is non-linear.
plot(tw_gam)
gam.check(tw_gam)

tw_deriv <- derivatives(tw_gam, "s(heat_index)", n=300)
# positive derivative of smooth term tmmx_f from range 83.4-99.7
print(tw_deriv, n=300)
draw(tw_deriv)
# get the temperature at which mortality effect is greatest
print(tw_deriv[tw_deriv$derivative==max(tw_deriv$derivative),])
# see how much factor increase compared to 60 deg threshold
tw_pred100 <- predict(tw_gam, data.frame(dow_abbrev="M", 
                                      tmmx_f=100,
                                      rmax=mean(tw_data$rmax),
                                      time=mean(tw_data$time), 
                                      tot_pop=mean(tw_data$tot_pop)))
tw_pred126 <- predict(tw_gam, data.frame(dow_abbrev="M", 
                                         heat_index=126,
                                         time=mean(tw_data$time), 
                                         tot_pop=mean(tw_data$tot_pop)))

# factor increase
print(tw_pred153/tw_pred126)



########### CENTRAL MOUNTAIN CLIMATE DIVISION #######################
hist(cm_data$death_count, breaks=20)
plot(cm_data$tmmx_f, cm_data$death_count)

cm_gam <- gam(death_count ~ dow_abbrev + s(tmmx_f) + s(rmax) + month + year + offset(log(tot_pop)), family=poisson, data=cm_data, method="REML")
cm_gam <- gam(death_count ~ dow_abbrev + s(heat_index) + s(heat_index_lag_1) + month + year + offset(log(tot_pop)), family=poisson, data=cm_data, method="REML")
draw(cm_gam)
cm_deriv <- derivatives(cm_gam, "s(rmax)", n=300)
plot(cm_gam)
# positive derivative of smooth term tmmx_f from range 83.4-99.7
print(cm_deriv, n=300)
draw(cm_deriv)
########### WESTERN PIEDMONT CLIMATE DIVISION #######################
hist(wp_data$death_count, breaks=20)
plot(wp_data$tmmx_f, wp_data$death_count)

wp_gam <- gam(death_count ~ dow_abbrev + s(heat_index) + s(heat_index_lag_1) + month + year + offset(log(tot_pop)), family=poisson, data=wp_data, method="REML")
wp_gam <- gam(death_count ~ dow_abbrev + s(tmmx_f) + s(tmmx_lag_1) + s(rmax) + s(rmax_lag_1) + month + year + offset(log(tot_pop)), family=poisson, data=wp_data, method="REML")

wp_glm <- glm(death_count ~ dow_abbrev + heat_index + heat_index_lag_1 + month + year + offset(log(tot_pop)), family=poisson, data=wp_data)
exp(7.183e-04)
exp(7.183e-04 - 1.96*7.183e-04)
exp(7.183e-04 + 1.96*7.183e-04)

wp_glm <- glm(death_count ~ dow_abbrev + tmmx_f + tmmx_lag_1 + rmax + rmax_lag_1 + month + year + offset(log(tot_pop)), family=poisson, data=wp_data)
exp(1.389e-03)
exp(1.389e-03 - 1.96*1.274e-03)
exp(1.389e-03 + 1.96*1.274e-03)


draw(wp_gam)
wp_deriv <- derivatives(wp_gam, "s(heat_index)", n=300)

plot(wp_gam, xlab="Heat Index", ylab="Partial Effect of Heat Index on Daily Deaths")
plot(wp_gam, xlab="Max Temp", ylab="Partial Effect of Max Temp on Daily Deaths")
# positive derivative of smooth term tmmx_f from range 83.4-99.7
print(wp_deriv, n=300)
draw(wp_deriv)

# get the temperature at which mortality effect is greatest
print(wp_deriv[wp_deriv$derivative==max(wp_deriv$derivative),])
# see how much factor increase compared to 60 deg threshold
wp_pred153 <- predict(wp_gam, data.frame(dow_abbrev="M", 
                                         heat_index=153,
                                         time=mean(wp_data$time), 
                                         tot_pop=mean(wp_data$tot_pop)))
wp_pred126 <- predict(wp_gam, data.frame(dow_abbrev="M", 
                                        heat_index=126,
                                        time=mean(wp_data$time), 
                                        tot_pop=mean(wp_data$tot_pop)))

# factor increase
print(wp_pred110/wp_pred60)

########### EASTERN PIEDMONT CLIMATE DIVISION #######################
hist(ep_data$death_count, breaks=20)
plot(ep_data$tmmx_f, ep_data$death_count)

ep_gam <- gam(death_count ~ dow_abbrev + s(heat_index) + s(heat_index_lag_1) + month + year + offset(log(tot_pop)), family=poisson, data=ep_data, method="REML")
ep_gam <- gam(death_count ~ dow_abbrev + s(tmmx_f) + s(tmmx_lag_1) + s(rmax) + s(rmax_lag_1) + month + year + offset(log(tot_pop)), family=poisson, data=ep_data, method="REML")

plot(ep_gam, xlab="Heat Index", ylab="Partial Effect of Heat Index on Daily Deaths")
plot(ep_gam, xlab="Max Temp", ylab="Partial Effect of Max Temp on Daily Deaths")

ep_glm <- gam(death_count ~ dow_abbrev + heat_index + heat_index_lag_1 + month + year + offset(log(tot_pop)), family=poisson, data=ep_data)
exp(1.811e-04 - 1.96*3.233e-04)
exp(1.811e-04 + 1.96*3.233e-04)

ep_glm <- gam(death_count ~ dow_abbrev + tmmx_f + tmmx_lag_1 + rmax + rmax_lag_1 + month + year + offset(log(tot_pop)), family=poisson, data=ep_data)


draw(ep_gam)
ep_deriv <- derivatives(ep_gam, "s(heat_index)", n=300)
# positive derivative of smooth term tmmx_f from range 83.4-99.7
print(ep_deriv, n=300)
draw(ep_deriv)

########### SOUTHWESTERN MOUNTAIN CLIMATE DIVISION #######################
hist(swm_data$death_count, breaks=20)
plot(swm_data$tmmx_f, swm_data$death_count)

swm_gam <- gam(death_count ~ dow_abbrev + s(heat_index) + s(heat_index_lag_1) + month + year + offset(log(tot_pop)), family=poisson, data=swm_data, method="REML")
swm_gam <- gam(death_count ~ dow_abbrev + s(tmmx_f) + s(rmax) + month + year + offset(log(tot_pop)), family=poisson, data=swm_data, method="REML")
swm_deriv <- derivatives(swm_gam, "s(heat_index)", n=300)
print(swm_deriv, n=300)
draw(swm_deriv)
draw(swm_gam)
plot(swm_gam)
# get the temperature at which mortality effect is greatest
print(swm_deriv[swm_deriv$derivative==max(swm_deriv$derivative),])
# see how much factor increase compared to 60 deg threshold
swm_pred150 <- predict(tw_gam, data.frame(dow_abbrev="M", 
                                         heat_index=150, 
                                         time=mean(swm_data$time), 
                                         tot_pop=mean(swm_data$tot_pop)))
swm_pred126 <- predict(tw_gam, data.frame(dow_abbrev="M", 
                                        heat_index=126, 
                                        time=mean(swm_data$time), 
                                        tot_pop=mean(swm_data$tot_pop)))

# factor increase
print(swm_pred150/swm_pred126)




