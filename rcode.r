# Load the mtcars dataset
data(mtcars)

# Fit a linear regression model
model <- lm(mpg ~ wt, data = mtcars)

# Display summary of the linear regression model
summary(model)
