import gradio as gr
import requests

API_URL = "http://localhost:8080"

# User functions
def create_user(name, email):
    try:
        resp = requests.post(f"{API_URL}/users", json={"name": name, "email": email})
        if resp.status_code == 201:
            return f"✅ User Created!\n{resp.json()}"
        return f"❌ Error: {resp.text}"
    except Exception as e:
        return f"❌ Connection Error: {str(e)}"

def get_all_users():
    try:
        resp = requests.get(f"{API_URL}/users")
        users = resp.json()
        return str(users) if users else "No users found"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Product functions
def create_product(name, price, stock):
    try:
        resp = requests.post(f"{API_URL}/products", json={
            "name": name, "price": float(price), "stock": int(stock)
        })
        if resp.status_code == 201:
            return f"✅ Product Created!\n{resp.json()}"
        return f"❌ Error: {resp.text}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def get_all_products():
    try:
        resp = requests.get(f"{API_URL}/products")
        return str(resp.json())
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Order functions
def create_order(user_id, product_id, quantity):
    try:
        resp = requests.post(f"{API_URL}/orders", json={
            "userId": int(user_id),
            "productId": product_id,
            "quantity": int(quantity)
        })
        if resp.status_code == 201:
            return f"✅ Order Created!\n{resp.json()}"
        return f"❌ Error: {resp.text}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def get_all_orders():
    try:
        resp = requests.get(f"{API_URL}/orders")
        return str(resp.json())
    except Exception as e:
        return f"❌ Error: {str(e)}"

# UI Design
with gr.Blocks(title="E-Commerce Microservices") as demo:
    gr.Markdown("# 🛒 E-Commerce Microservices Dashboard")
    gr.Markdown("### Yunnan University | Software Service Engineering")
    
    with gr.Tab("👤 User Service"):
        gr.Markdown("### Create User")
        with gr.Row():
            name = gr.Textbox(label="Name")
            email = gr.Textbox(label="Email")
        user_create_btn = gr.Button("Create User", variant="primary")
        user_output = gr.Textbox(label="Result", lines=5)
        user_create_btn.click(create_user, [name, email], user_output)
        
        gr.Markdown("### View All Users")
        user_get_btn = gr.Button("Get All Users")
        users_list = gr.Textbox(label="Users", lines=10)
        user_get_btn.click(get_all_users, [], users_list)
    
    with gr.Tab("📦 Product Service"):
        gr.Markdown("### Create Product")
        with gr.Row():
            p_name = gr.Textbox(label="Product Name")
            p_price = gr.Number(label="Price")
        p_stock = gr.Number(label="Stock", precision=0)
        product_create_btn = gr.Button("Create Product", variant="primary")
        product_output = gr.Textbox(label="Result", lines=5)
        product_create_btn.click(create_product, [p_name, p_price, p_stock], product_output)
        
        gr.Markdown("### View All Products")
        product_get_btn = gr.Button("Get All Products")
        products_list = gr.Textbox(label="Products", lines=10)
        product_get_btn.click(get_all_products, [], products_list)
    
    with gr.Tab("📋 Order Service"):
        gr.Markdown("### Create Order")
        with gr.Row():
            user_id = gr.Textbox(label="User ID")
            product_id = gr.Textbox(label="Product ID")
        quantity = gr.Textbox(label="Quantity")
        order_create_btn = gr.Button("Create Order", variant="primary")
        order_output = gr.Textbox(label="Result", lines=5)
        order_create_btn.click(create_order, [user_id, product_id, quantity], order_output)
        
        gr.Markdown("### View All Orders")
        order_get_btn = gr.Button("Get All Orders")
        orders_list = gr.Textbox(label="Orders", lines=10)
        order_get_btn.click(get_all_orders, [], orders_list)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
