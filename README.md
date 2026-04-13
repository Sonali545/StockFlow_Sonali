# StockFlow – Backend Case Study (Bynry)

This repository contains my solution for the Backend Engineering Intern case study.

The case study is based on a B2B inventory management system called **StockFlow**, where businesses can manage products across multiple warehouses and suppliers.

---

## 🚀 What I have implemented

I have divided the solution into three parts:

### 1. Code Review & Debugging
- Identified issues in the given API
- Explained their impact in real-world scenarios
- Provided a corrected version with improvements

### 2. Database Design
- Designed schema for companies, products, warehouses, inventory, and suppliers
- Handled relationships like:
  - Products across multiple warehouses
  - Supplier mapping
  - Inventory tracking
- Included assumptions and missing requirement questions

### 3. Low Stock Alert API
- Implemented endpoint to detect low stock products
- Considered:
  - Product threshold
  - Recent sales activity
  - Multiple warehouses
- Included supplier details for reordering

---

## 🛠️ Tech Stack

Since no tech stack was specified, I chose:

- **Python (Flask)** for backend APIs  
- **PostgreSQL (SQL)** for database design  

I chose Python because I have worked on backend systems and ML-based applications using it. Flask helped me keep the implementation simple and focus on logic.

For the database, I used SQL because inventory systems are relational in nature and require constraints like unique SKUs and proper relationships.

---

## 🤔 Assumptions

Some requirements were not clearly defined, so I assumed:

- Recent sales means activity in the last 30 days  
- Each product has a stock threshold  
- A product can have one or more suppliers  
- Inventory is tracked per warehouse  

---

## ⚠️ Edge Cases Considered

- Missing input data  
- Duplicate SKU entries  
- No recent sales activity  
- Products without suppliers  
- Empty warehouse data  

---

## 💡 Key Focus

- Keeping the solution simple and understandable  
- Maintaining data consistency  
- Writing clean and readable code  
- Thinking from a real-world SaaS perspective  

---

## 🔄 Note

The solution is not dependent on a specific framework and can be adapted to other backend technologies if needed.

---

## 👩‍💻 Author

Sonali Kamble  
