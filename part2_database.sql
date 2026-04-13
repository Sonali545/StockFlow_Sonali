-- Part 2: Database Design

-- Companies table
-- Stores different businesses using the system
CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- Warehouses
-- Each company can have multiple warehouses
CREATE TABLE warehouses (
    id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(id),
    name TEXT NOT NULL
);

-- Products
-- SKU is kept unique as per requirement
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    sku TEXT UNIQUE,
    price DECIMAL,
    threshold INT
);

-- Inventory
-- Keeps track of product quantity in each warehouse
CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    warehouse_id INT REFERENCES warehouses(id),
    quantity INT
);

-- Suppliers
CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    contact_email TEXT
);

-- Product-Supplier mapping
-- A product can have multiple suppliers
CREATE TABLE product_suppliers (
    product_id INT REFERENCES products(id),
    supplier_id INT REFERENCES suppliers(id),
    PRIMARY KEY (product_id, supplier_id)
);

-- Inventory logs
-- Used to track changes in stock over time
CREATE TABLE inventory_logs (
    id SERIAL PRIMARY KEY,
    product_id INT,
    warehouse_id INT,
    change INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bundles
-- Represents products made up of other products
CREATE TABLE bundles (
    bundle_id INT REFERENCES products(id),
    product_id INT REFERENCES products(id),
    quantity INT
);

-- Assumptions / Questions

-- What defines "recent sales"? (for example: last 7 days or 30 days)
-- Can a product have multiple suppliers? (assumed yes)
-- Are bundles allowed to contain other bundles?
-- Should inventory updates happen in real-time or batch?
