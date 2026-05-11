"""
Semi-Manual Test Script for E-Commerce Microservices
Tests all 3 services through API Gateway
"""
import requests
import sys

BASE_URL = "http://localhost:8080"
PASS = "✅ PASS"
FAIL = "❌ FAIL"

def test_full_flow():
    print("=" * 50)
    print("SEMI-MANUAL TEST SUITE - E-Commerce Backend")
    print("=" * 50)
    all_passed = True

    # Test 1: Create User
    print("\n[TEST 1] Create User...")
    try:
        resp = requests.post(f"{BASE_URL}/users", json={
            "name": "Test User",
            "email": "test@ynu.edu.cn"
        })
        if resp.status_code == 201:
            user = resp.json()
            user_id = user.get('id')
            print(f"{PASS} User created: ID={user_id}, Name={user['name']}")
        else:
            print(f"{FAIL} Status: {resp.status_code}, Body: {resp.text}")
            all_passed = False
            user_id = None
    except Exception as e:
        print(f"{FAIL} Connection error: {e}")
        all_passed = False
        user_id = None

    # Test 2: Create Product
    print("\n[TEST 2] Create Product...")
    try:
        resp = requests.post(f"{BASE_URL}/products", json={
            "name": "Laptop",
            "price": 999.99,
            "stock": 10
        })
        if resp.status_code == 201:
            product = resp.json()
            product_id = product.get('id')
            print(f"{PASS} Product created: ID={product_id}, Name={product['name']}, Price=${product['price']}")
        else:
            print(f"{FAIL} Status: {resp.status_code}, Body: {resp.text}")
            all_passed = False
            product_id = None
    except Exception as e:
        print(f"{FAIL} Connection error: {e}")
        all_passed = False
        product_id = None

    # Test 3: Create Order
    print("\n[TEST 3] Create Order (calls User + Product)...")
    if user_id and product_id:
        try:
            resp = requests.post(f"{BASE_URL}/orders", json={
                "userId": user_id,
                "productId": product_id,
                "quantity": 2
            })
            if resp.status_code == 201:
                order = resp.json()
                print(f"{PASS} Order created: ID={order['id']}, Total=${order['totalPrice']}, Status={order['status']}")
            else:
                print(f"{FAIL} Status: {resp.status_code}, Body: {resp.text}")
                all_passed = False
        except Exception as e:
            print(f"{FAIL} Connection error: {e}")
            all_passed = False
    else:
        print(f"{FAIL} Skipped - User or Product not created")

    # Test 4: Get All Users
    print("\n[TEST 4] Get All Users...")
    try:
        resp = requests.get(f"{BASE_URL}/users")
        if resp.status_code == 200:
            users = resp.json()
            print(f"{PASS} Found {len(users)} user(s)")
        else:
            print(f"{FAIL} Status: {resp.status_code}")
            all_passed = False
    except Exception as e:
        print(f"{FAIL} Connection error: {e}")
        all_passed = False

    # Test 5: Get All Products
    print("\n[TEST 5] Get All Products...")
    try:
        resp = requests.get(f"{BASE_URL}/products")
        if resp.status_code == 200:
            products = resp.json()
            print(f"{PASS} Found {len(products)} product(s)")
        else:
            print(f"{FAIL} Status: {resp.status_code}")
            all_passed = False
    except Exception as e:
        print(f"{FAIL} Connection error: {e}")
        all_passed = False

    # Test 6: Get All Orders
    print("\n[TEST 6] Get All Orders...")
    try:
        resp = requests.get(f"{BASE_URL}/orders")
        if resp.status_code == 200:
            orders = resp.json()
            print(f"{PASS} Found {len(orders)} order(s)")
        else:
            print(f"{FAIL} Status: {resp.status_code}")
            all_passed = False
    except Exception as e:
        print(f"{FAIL} Connection error: {e}")
        all_passed = False

    # Summary
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 ALL TESTS PASSED!")
    else:
        print("⚠️  SOME TESTS FAILED!")
    print("=" * 50)

if __name__ == "__main__":
    test_full_flow()
