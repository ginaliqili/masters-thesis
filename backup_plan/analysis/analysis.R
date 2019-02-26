require(mgcv)

########### READING IN DATA AND SUBSETTING #####################

# read in data, change date column to date type
data <- read.csv(file="G:/My Drive/Year 2/Thesis/Backup_Plan/all_data/all_data_weather_mortality_population_dow.csv", header=TRUE, sep=",")
data$date <- as.Date(data$date, "%m/%d/%Y")

# subset data by summer months and climate regions
summer_months <- c('04', '05', '06', '07', '08', '09')
data <- subset(data, format.Date(date, "%m") %in% summer_months)

# subset again, keep tempeartures about 60 degrees only
data <- data[ which(data$tmmx_f >=60), ]

n_data <- data[which(data$clim_div=='NORTHERN'),]
tw_data <- data[which(data$clim_div=='TIDEWATER'),]
cm_data <- data[which(data$clim_div=='CENTRAL MOUNTAIN'),]
wp_data <- data[which(data$clim_div=='WESTERN PIEDMONT'),]
ep_data <- data[which(data$clim_div=='EASTERN PIEDMONT'),]
swm_data <- data[which(data$clim_div=='SOUTHWESTERN MOUNTAIN'),]

############ NORTHERN CLIMATE DIVISION #######################
hist(n_data$death_count, breaks=20)
plot(n_data$tmmx_f, n_data$death_count)

tapply(n_data$death_count, cut(n_data$tmmx_f, seq(60, 110, by=5)), mean)
tapply(tw_data$death_count, cut(tw_data$tmmx_f, seq(60, 110, by=5)), mean)
tapply(cm_data$death_count, cut(cm_data$tmmx_f, seq(60, 110, by=5)), mean)
tapply(ep_data$death_count, cut(ep_data$tmmx_f, seq(60, 110, by=5)), mean)
tapply(wp_data$death_count, cut(wp_data$tmmx_f, seq(60, 110, by=5)), mean)
tapply(swm_data$death_count, cut(swm_data$tmmx_f, seq(60, 110, by=5)), mean)

n_gam <- gam(death_count ~ dow + s(heat_index) + s(time) + offset(log(tot_pop)), family=poisson, data=n_data, method="REML", all.terms=TRUE)
plot(n_gam, rug=TRUE, pch=1, cex=1, shade=TRUE, shade.col="lightblue", seWithMean=TRUE, trans=exp)
coef(n_gam)

n_gam <- gam(death_count ~ dow + s(tmmx_f) + s(rmax) + s(time) + offset(log(tot_pop)), family=poisson, data=n_data, method="REML", all.terms=TRUE)
plot(n_gam, rug=TRUE, pch=1, cex=1, shade=TRUE, shade.col="lightblue", seWithMean=TRUE, trans=exp)
coef(n_gam)

n_glm <- glm(death_count ~ heat_index + dow + year, offset=log(tot_pop), data=n_data, family="poisson")
n_glm2 <- glm(death_count ~ rmax + offset(log(tot_pop)), family=poisson, data=n_data1979_1987)

########### TIDEWATER CLIMATE DIVISION #######################
hist(tw_data$death_count, breaks=20)
plot(tw_data$tmmx_f, tw_data$death_count)

tw_loess <- loess(death_count ~ tmmx_f, data = tw_data, span=0.25)
smoothed25 <- predict(tw_loess)
plot(tw_data$death_count, x=tw_data$tmmx_f, main="Loess Smoothing and Prediction", xlab="tmmx_f", ylab="daily death count")
lines(smoothed25, x=tw_data$tmmx_f, col="red")

# tried to adjust k to make rmax significant but can't
tw_gam <- gam(death_count ~ dow + s(tmmx_f) + s(rmax) + s(time) + offset(log(tot_pop)), family=poisson, data=tw_data, method="REML", all.terms=TRUE)
tw_gam <- gam(death_count ~ dow + s(heat_index) + s(time) + offset(log(tot_pop)), family=poisson, data=tw_data, method="REML", all.terms=TRUE)
plot(tw_gam, rug=TRUE,pch=1, cex=1, shade=TRUE, shade.col="lightblue", seWithMean=TRUE, trans=exp)

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

cm_gam <- gam(death_count ~ dow + s(heat_index) + s(time) + offset(log(tot_pop)), family=poisson, data=cm_data, method="REML", all.terms=TRUE)
cm_gam <- gam(death_count ~ dow + s(tmmx_f) + s(rmax) + s(time) + offset(log(tot_pop)), family=poisson, data=cm_data, method="REML", all.terms=TRUE)

########### WESTERN PIEDMONT CLIMATE DIVISION #######################
hist(wp_data$death_count, breaks=20)
plot(wp_data$tmmx_f, wp_data$death_count)

wp_loess <- loess(death_count ~ tmmx_f, data = wp_data, span=0.25)
smoothed25 <- predict(wp_loess)
plot(wp_data$death_count, x=wp_data$tmmx_f, main="Loess Smoothing and Prediction", xlab="tmmx_f", ylab="daily death count")
lines(smoothed25, x=wp_data$tmmx_f, col="red")

wp_gam <- gam(death_count ~ dow + s(heat_index) + s(time) + offset(log(tot_pop)), family=poisson, data=wp_data, method="REML", all.terms=TRUE)
wp_gam <- gam(death_count ~ dow + s(tmmx_f) + s(rmax) + s(time) + offset(log(tot_pop)), family=poisson, data=wp_data, method="REML", all.terms=TRUE)

########### EASTERN PIEDMONT CLIMATE DIVISION #######################
hist(ep_data$death_count, breaks=20)
plot(ep_data$tmmx_f, ep_data$death_count)

ep_gam <- gam(death_count ~ dow + s(heat_index) + s(time) + offset(log(tot_pop)), family=poisson, data=ep_data, method="REML", all.terms=TRUE)
ep_gam <- gam(death_count ~ dow + s(tmmx_f) + s(rmax) + s(time) + offset(log(tot_pop)), family=poisson, data=ep_data, method="REML", all.terms=TRUE)

########### SOUTHWESTERN MOUNTAIN CLIMATE DIVISION #######################
hist(swm_data$death_count, breaks=20)
plot(swm_data$tmmx_f, swm_data$death_count)

swm_gam <- gam(death_count ~ dow + s(heat_index) + s(time) + offset(log(tot_pop)), family=poisson, data=swm_data, method="REML", all.terms=TRUE)
swm_gam <- gam(death_count ~ dow + s(tmmx_f) + s(rmax) + s(time) + offset(log(tot_pop)), family=poisson, data=swm_data, method="REML", all.terms=TRUE)






