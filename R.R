
library(readxl)
used_cars <- read_excel("C:/Users/Clarence Sahibdeen/Desktop/Assignment/used.cars.xlsx")
View(used_cars)

#test
str(used_cars)
head(used_cars)


#print(used_cars)


#Transmission count graph
counts_t <- table(used_cars$transmission)
barplot(counts_t,xlab = "Type of Transmission", main="Transmission count")

x <- counts_t
labels <-  c("Auto","Manual")

piepercent<- round(100*x/sum(x), 1)

# Give the chart file a name.
png(file = "transmission.jpg")

# Plot the chart.
pie(x, labels = piepercent, main = "transmission",col = rainbow(length(x)))
legend("topright", c("Auto","Manual"), cex = 0.8,
       fill = rainbow(length(x)))
