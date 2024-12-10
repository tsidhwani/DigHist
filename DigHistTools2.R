# Load necessary libraries
library(ggplot2)

file_path <- "/Users/tapansidhwani/Downloads/historical_trade_data.csv"
trade_data <- read.csv(file_path)


print("example rows:")
print(head(trade_data))

print("dataset structure:")
print(str(trade_data))

filtered_data <- subset(trade_data, Exports > 200000)
print("rows over 200000:")
print(head(filtered_data))

trade_data$Trade_Balance <- trade_data$Exports - trade_data$Imports
print("dataset with Trade_Balance")
print(head(trade_data))


ggplot(trade_data, aes(x = Year, y = Trade_Balance)) +
  geom_line(color = "blue", linewidth = 1) +
  labs(
    title = "Trade Balance Over Time",
    x = "Year",
    y = "Trade Balance"
  ) +
  theme_minimal()


