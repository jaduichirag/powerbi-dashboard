-- Total Sales by Region
SELECT Region, SUM(Sales) as Total_Sales
FROM sales
GROUP BY Region;
