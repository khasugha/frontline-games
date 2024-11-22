from app import create_app, db
from app.models import User, Product, Category, Order, OrderItem, ShoppingCart, Payment

app = create_app()

def seed_data():
    with app.app_context():
        # Drop and recreate all tables (for development/testing only)
        db.drop_all()
        db.create_all()

        # 1. Seed Users
        admin = User(username="admin", email="admin@example.com", is_admin=True)
        admin.set_password("admin123")
        user1 = User(username="user1", email="user1@example.com")
        user1.set_password("password123")

        db.session.add_all([admin, user1])
        db.session.commit()  # Commit users to assign their IDs

        # Fetch user IDs
        admin_id = admin.user_id
        user1_id = user1.user_id

        # 2. Seed Categories
        category1 = Category(name="Magic")
        category2 = Category(name="Pokemon")
        category3 = Category(name="Yu-Gi-Oh")

        db.session.add_all([category1, category2, category3])
        db.session.commit()  # Commit categories to assign their IDs

        # Fetch category IDs
        category1_id = category1.category_id
        category2_id = category2.category_id
        category3_id = category3.category_id

        # 3. Seed Products
        product1 = Product(
            name="Magic Booster Pack",
            description="A booster pack of Magic: The Gathering cards.",
            price=9.99,
            stock_quantity=100,
            category_id=category1_id,
            image_url="images/products/Magic_IMH_BP.png",
        )
        product2 = Product(
            name="Pokémon Starter Deck",
            description="A starter deck of Pokémon cards.",
            price=14.99,
            stock_quantity=50,
            category_id=category2_id,
            image_url="images/products/PKMN_VV_SD.png",
        )
        product3 = Product(
            name="Yu-Gi-Oh! Structure Deck",
            description="A Yu-Gi-Oh! structure deck. Includes 40 cards.",
            price=19.99,
            stock_quantity=30,
            category_id=category3_id,
            image_url="images/products/YGO_SD_SC.png",
        )

        db.session.add_all([product1, product2, product3])
        db.session.commit()  # Commit products to assign their IDs

        # Fetch product IDs
        product1_id = product1.product_id
        product2_id = product2.product_id
        product3_id = product3.product_id

        # 4. Seed Orders
        order1 = Order(user_id=user1_id, total_price=24.98, status="Pending")

        db.session.add(order1)
        db.session.commit()  # Commit orders to assign their IDs

        # Fetch order ID
        order1_id = order1.order_id

        # 5. Seed Order Items
        order_item1 = OrderItem(order_id=order1_id, product_id=product1_id, quantity=1, price=9.99)
        order_item2 = OrderItem(order_id=order1_id, product_id=product2_id, quantity=1, price=14.99)

        db.session.add_all([order_item1, order_item2])

        # 8. Seed Payments
        payment1 = Payment(order_id=order1_id, payment_method="Credit Card", payment_status="Paid", transaction_id="txn_12345")
        db.session.add(payment1)

        # Final commit
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
