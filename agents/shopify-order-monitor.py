#!/usr/bin/env python3
"""
Shopify Order Monitor
Checks for new paid orders and alerts Captain
"""
import json
import subprocess
from datetime import datetime

def check_shopify_orders():
    """Pull orders and identify unpaid/undelivered"""
    
    # Get Shopify token from env
    import os
    token = os.getenv('SHOPIFY_ADMIN_ACCESS_TOKEN', '')
    domain = os.getenv('SHOPIFY_STORE_DOMAIN', 'd0xuix-cn.myshopify.com')
    
    # Curl shopify API
    cmd = f'''curl -s "https://{domain}/admin/api/2026-07/orders.json?status=any&limit=100" \
      -H "X-Shopify-Access-Token: {token}"'''
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    data = json.loads(result.stdout)
    
    alert = {
        "timestamp": datetime.now().isoformat(),
        "action": "order_monitor",
        "orders": []
    }
    
    for order in data.get('orders', []):
        if order['financial_status'] == 'paid':
            alert["orders"].append({
                "order_number": order['order_number'],
                "customer": order['customer']['email'] if order.get('customer') else 'Guest',
                "amount": order['total_price'],
                "currency": order['currency'],
                "created": order['created_at'],
                "fulfillment": order['fulfillment_status'],
                "needs_delivery": order['fulfillment_status'] not in ['fulfilled', 'partial']
            })
    
    # Log alert
    with open('data/order_alerts.json', 'w') as f:
        json.dump(alert, f, indent=2)
    
    return alert

if __name__ == "__main__":
    alert = check_shopify_orders()
    print(f"✓ Found {len(alert['orders'])} paid orders")
    for order in alert['orders']:
        if order['needs_delivery']:
            print(f"  🔴 Order #{order['order_number']}: {order['amount']} {order['currency']} - NOT DELIVERED")

