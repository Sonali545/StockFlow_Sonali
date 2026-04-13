# Part 3: Low Stock Alert API

# Assumptions:
# - Recent sales means last 30 days
# - Each product has a threshold field
# - Each product has at least one supplier

@app.route('/api/companies/<int:company_id>/alerts/low-stock', methods=['GET'])
def low_stock_alerts(company_id):
    alerts = []

    # Get all warehouses of the company
    warehouses = Warehouse.query.filter_by(company_id=company_id).all()

    for warehouse in warehouses:
        # Get inventory for each warehouse
        inventories = Inventory.query.filter_by(warehouse_id=warehouse.id).all()

        for inv in inventories:
            product = Product.query.get(inv.product_id)

            if not product:
                continue

            threshold = product.threshold

            # Get recent sales (assumed function)
            recent_sales = get_recent_sales(product.id)

            # Skip if no recent sales
            if recent_sales == 0:
                continue

            # Check low stock condition
            if inv.quantity < threshold:
                
                # Get supplier (assumed function)
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


# Helper functions (basic assumptions)

def get_recent_sales(product_id):
    # Example logic: return average daily sales
    # In real system, this would query sales table
    return 2  # placeholder value


def estimate_days(stock, daily_sales):
    if daily_sales == 0:
        return None
    return stock // daily_sales


def get_supplier(product_id):
    # Example: fetch first supplier
    ps = ProductSupplier.query.filter_by(product_id=product_id).first()
    
    if not ps:
        return None

    supplier = Supplier.query.get(ps.supplier_id)

    return {
        "id": supplier.id,
        "name": supplier.name,
        "contact_email": supplier.contact_email
    }
