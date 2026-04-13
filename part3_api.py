# Part 3: Low Stock Alert API

# Assumptions:
# - "Recent sales" refers to activity in the last 30 days
# - Each product has a predefined threshold value
# - A product can have at least one supplier

@app.route('/api/companies/<int:company_id>/alerts/low-stock', methods=['GET'])
def low_stock_alerts(company_id):
    alerts = []

    # Fetch all warehouses for the given company
    warehouses = Warehouse.query.filter_by(company_id=company_id).all()

    for warehouse in warehouses:
        # Fetch inventory records for each warehouse
        inventories = Inventory.query.filter_by(warehouse_id=warehouse.id).all()

        for inv in inventories:
            product = Product.query.get(inv.product_id)

            # Skip if product not found (safety check)
            if not product:
                continue

            threshold = product.threshold

            # Get recent sales data (assumed helper function)
            recent_sales = get_recent_sales(product.id)

            # If no recent sales, skip this product
            if recent_sales == 0:
                continue

            # Check if stock is below threshold
            if inv.quantity < threshold:

                # Fetch supplier details (assumed helper function)
                supplier = get_supplier(product.id)

                alert = {
                    "product_id": product.id,
                    "product_name": product.name,
                    "sku": product.sku,
                    "warehouse_id": warehouse.id,
                    "warehouse_name": warehouse.name,
                    "current_stock": inv.quantity,
                    "threshold": threshold,
                    "days_until_stockout": estimate_days(inv.quantity, recent_sales),
                    "supplier": supplier if supplier else {}
                }

                alerts.append(alert)

    return {
        "alerts": alerts,
        "total_alerts": len(alerts)
    }


# Helper functions (basic logic for now)

def get_recent_sales(product_id):
    # Returns average daily sales (placeholder logic)
    # In a real system, this would query a sales table
    return 2


def estimate_days(stock, daily_sales):
    if daily_sales == 0:
        return None
    return stock // daily_sales


def get_supplier(product_id):
    # Fetch first available supplier for the product
    ps = ProductSupplier.query.filter_by(product_id=product_id).first()

    if not ps:
        return None

    supplier = Supplier.query.get(ps.supplier_id)

    return {
        "id": supplier.id,
        "name": supplier.name,
        "contact_email": supplier.contact_email
    }
