# StockFlow – Backend Case Study (Bynry)

This repository contains my solution for the Backend Engineering Intern case study.

The case study is based on a B2B inventory management system called StockFlow, where businesses manage products across multiple warehouses and suppliers.

## What I implemented

### 1. Code Review & Debugging
- Identified issues in the given API
- Explained their real-world impact
- Provided a corrected version

### 2. Database Design
- Designed schema for companies, products, warehouses, inventory, and suppliers
- Handled relationships like multi-warehouse storage and supplier mapping
- Included assumptions and missing requirement questions

### 3. Low Stock Alert API
- Implemented endpoint to detect low stock products
- Considered threshold, recent sales, and multiple warehouses
- Included supplier details for reordering

## Tech Stack

- Python (Flask)
- PostgreSQL (SQL)

I chose Python because I have worked on backend and ML-based projects using it. Flask helped me focus on logic without too much setup.

I used SQL since inventory systems are relational and require proper constraints like unique SKUs and structured relationships.

## Assumptions

- Recent sales means activity in the last 30 days  
- Each product has a stock threshold  
- A product can have one or more suppliers  
- Inventory is tracked per warehouse  

## Edge Cases

- Missing input data  
- Duplicate SKU  
- No recent sales  
- Product without supplier  
- No warehouse data  

## Note

The solution is kept simple and can be adapted to other backend frameworks if needed.

## Author

Sonali Kamble
