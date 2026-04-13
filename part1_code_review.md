## Part 1: Code Review & Debugging

### Issues I identified

1. No input validation  
The API directly accesses fields like `data['name']`. If any field is missing, the application may crash.

2. SKU uniqueness not checked  
SKU is expected to be unique, but there is no validation before inserting into the database.

3. Multiple commits  
Product and inventory are committed separately. If the second operation fails, the product will exist without inventory, causing inconsistency.

4. Product tied to a single warehouse  
The product model includes `warehouse_id`, but based on requirements, a product can be stored in multiple warehouses.

5. No error handling  
There is no proper error handling or rollback. If something fails, partial data may remain in the database.

6. Price handling  
Price is taken directly, which may cause precision issues if stored as float.

7. Optional fields not handled  
The code assumes all fields are present, which may not always be true.

### Impact in production

- Data inconsistency (product without inventory)  
- Duplicate SKUs causing confusion  
- Application crashes due to missing input fields  
- Incorrect handling of products across multiple warehouses  

### Fixed Version

```python
@app.route('/api/products', methods=['POST'])
def create_product():
    try:
        data = request.json

        # Validate required fields
        required_fields = ['name', 'sku', 'price']
        for field in required_fields:
            if field not in data:
                return {"error": f"{field} is required"}, 400

        # Check SKU uniqueness
        existing = Product.query.filter_by(sku=data['sku']).first()
        if existing:
            return {"error": "SKU already exists"}, 400

        # Create product (not tied to warehouse)
        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=Decimal(str(data['price']))
        )

        db.session.add(product)
        db.session.flush()  # get product id without committing

        # Optional inventory creation
        if 'warehouse_id' in data and 'initial_quantity' in data:
            inventory = Inventory(
                product_id=product.id,
                warehouse_id=data['warehouse_id'],
                quantity=data.get('initial_quantity', 0)
            )
            db.session.add(inventory)

        db.session.commit()

        return {"message": "Product created", "product_id": product.id}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
