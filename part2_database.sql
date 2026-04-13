-- Part 2: Database Design

-- Companies table
CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- Warehouses (each company can have multiple)
CREATE TABLE warehouses (
    id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(id),
    name TEXT NOT NULL
);

-- Products
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    sku TEXT UNIQUE,
    price DECIMAL,
    threshold INT
);

-- Inventory (product in multiple warehouses)
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

-- Product-Supplier mapping (many-to-many)
CREATE TABLE product_suppliers (
    product_id INT REFERENCES products(id),
    supplier_id INT REFERENCES suppliers(id),
    PRIMARY KEY (product_id, supplier_id)
);

-- Inventory change logs
CREATE TABLE inventory_logs (
    id SERIAL PRIMARY KEY,
    product_id INT,
    warehouse_id INT,
    change INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bundles (product composed of other products)
CREATE TABLE bundles (
    bundle_id INT REFERENCES products(id),
    product_id INT REFERENCES products(id),
    quantity INT
);

-- Assumptions / Questions:
-- 1. What defines "recent sales"? (7 days or 30 days)
-- 2. Can a product have multiple suppliers? (assumed yes)
-- 3. Are bundles nested (bundle inside bundle)?
-- 4. Should inventory updates be real-time?
