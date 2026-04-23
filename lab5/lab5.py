from flask import Flask, jsonify
from datetime import datetime
import numpy as np
import pandas as pd
from pandas import DataFrame

app = Flask(__name__)
#1
class User:
    def __init__(self, user_id, name, email):
        self._id = user_id
        self._name = name.strip().title()
        if "@" not in email:
            raise ValueError("Қате")
        else:
            self._email = email.lower()
    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"
    def __del__(self):
        print (f"User {self._name} deleted")
#2
    @classmethod
    def from_string(cls, data: str):
        user_id, name, email = data.split(",")
        return cls(int(user_id), name, email)
@app.route("/task1")
def show_task1():
    try:
        u1 = User(1, " john doe ", "John@Example.COM")
        return jsonify({
            "message": "1-ші тапсырма сәтті орындалды!",
            "parsed_user": str(u1),
            "user_details": {
                "id": u1._id,
                "name": u1._name,
                "email": u1._email
            }
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
@app.route("/task2")
def show_task2():
    try:
        u2 = User.from_string("2, Alice Wonderland , alice@wonder.com")
        return jsonify({
            "message": "2-ші тапсырма сәтті орындалды!",
            "original_string": "2, Alice Wonderland , alice@wonder.com",
            "parsed_user": str(u2),
            "user_details": {
            "id": u2._id,
            "name": u2._name,
            "email": u2._email
        }
    })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
#3
class Product:
    def __init__(self, id, name, price, category):
        self._id = int(id)
        self._name = name
        self._price = float(price)
        self._category = category
    def __str__(self):
        return f"Product(id = {self._id}, name='{self._name}', price={self._price}, category='{self._category}')"
    def to_dict(self):
        return {"id": self._id, "name": self._name, "price": self._price, "category": self._category}
    def __eq__(self, other):
        return self._id == other._id
    def __hash__(self):
        return hash(self._id)
@app.route("/task3")
def show_task3():
    p1=Product(1,"Laptop",310000, "Technology")
    p2=Product(1,"Computer", 600000, "Technology")
    p3=Product(2,"Mouse",50000, "Technology")
    product_set = {p1, p2, p3}
    return jsonify({"product_string":str(p1),"product_dict":p1.to_dict(),"set_length":len(product_set)})
#4
class Inventory:
    def __init__(self):
        self._items = {}
    def add_product(self, product):
        if product._id not in self._items:
            self._items[product._id] = product
    def remove_product(self, product_id):
        if product_id in self._items:
            del self._items[product_id]
    def get_product(self, product_id):
        return self._items.get(product_id)
    def get_all_products(self):
        return list(self._items.values())
    def unique_products(self):
        return set(self._items.values())
    def to_dict(self):
        return self._items
#5
    def filter_by_price(self, min_price: float):
        expensive = lambda p: p._price >= min_price
        return [p for p in self._items.values() if expensive(p)]
@app.route("/task4")
def show_task4():
    my_inventory = Inventory()
    s1=Product(1,"iPhone", 435000, "Technology")
    s2=Product(1, "Samsung", 456000, "Technology")
    s3=Product(2, "Apple", 500, "Food")
    my_inventory.add_product(s1)
    my_inventory.add_product(s2)
    my_inventory.add_product(s3)
    my_inventory.remove_product(2)
    return jsonify({"total":len(my_inventory.get_all_products()),"product1":my_inventory.get_product(1).to_dict()})
@app.route("/task5")
def show_task5():
    inv = Inventory()
    inv.add_product(Product(1, "Laptop", 1200.0, "Electronics"))
    inv.add_product(Product(2, "Mouse", 25.0, "Electronics"))
    expensive = inv.filter_by_price(100.0)
    expensive_names = [p._name for p in expensive]
    return jsonify({
        "message": "5-ші тапсырма сәтті орындалды!",
        "min_price_filter": 100.0,
        "expensive_items": expensive_names
    })
#6
class Logger:
    def log_action(self, user, action:str, product, filename: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        aina = f"{timestamp};{user._id};{action};{product._id}\n"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(aina)
    def read_logs(self, filename: str):
        logs = []
        with open(filename, "r", encoding="utf-8") as f:
            for d in f:
                clean_line = d.strip()
                parts = clean_line.split(";")
                log_dict = {"timestamp": parts[0], "user_id": parts[1], "action": parts[2], "product_id": parts[3]}
                logs.append(log_dict)
        return logs
@app.route("/task6")
def show_task6():
    logger = Logger()
    filename = "test_logs.txt"
    class MockUser: # Уақытша пайдаланушы
        def __init__(self, user_id):
            self._id = user_id
    user1 = MockUser(1)
    user2 = MockUser(2)
    product1 = Product(101, "MacBook", 800000, "Electronics")
    product2 = Product(102, "AirPods", 120000, "Electronics")
    logger.log_action(user1, "view", product1, filename)
    logger.log_action(user1, "buy", product1, filename)
    logger.log_action(user2, "add_to_cart", product2, filename)
    saved_logs = logger.read_logs(filename)
    return jsonify({
        "status": "success",
        "message": "Логтар файлға жазылды және сәтті оқылды",
        "total_actions": len(saved_logs),
        "data": saved_logs
    })
#7
class Order:
    def __init__(self, order_id:int, user):
        self._products = []
        self._id = order_id
        self._user = user
    def add_product(self, product):
        self._products.append(product)
    def remove_product(self, product_id):
        for p in self._products:
            if p._id == product_id:
                self._products.remove(p)
                break
    def total_price(self):
        return sum(p._price for p in self._products)
    def __str__(self):
        return f"Order(id: {self._id}, user: {self._user}, total: {self.total_price()})"
#8
    def most_expensive_products(self, n: int):
        return sorted(self._products, key=lambda p: p._price , reverse=True)[:n]
#9
def price_stream(products):
    for p in products:
        yield p._price
@app.route("/task7")
def show_task7():
    class MockUser: # Уақытша пайдаланушы
        def __init__(self, user_id):
            self._id = user_id
    user = MockUser(777)
    p1 = Product(10, "Burger", 2500, "Food")
    p2 = Product(20, "Cola", 500, "Drink")
    p3 = Product(30, "Fries", 1000, "Food")
    my_order = Order(1, user)
    my_order.add_product(p1)
    my_order.add_product(p2)
    my_order.add_product(p3)
    my_order.remove_product(20)
    products_in_order = [{"id": p._id, "name": p._name, "price": p._price} for p in my_order._products]
    return jsonify({
        "order_info_string": str(my_order),
        "calculated_total_price": my_order.total_price(),
        "remaining_items_count": len(my_order._products),
        "items": products_in_order
    })
@app.route("/task8")
def show_task8():
    class MockUser:
        def __init__(self, user_id):
            self._id = user_id
    user = MockUser(888)
    p1 = Product(1, "Құлаққап", 15000, "Электроника")
    p2 = Product(2, "Ноутбук", 450000, "Электроника")
    p3 = Product(3, "Тінтуір", 5000, "Электроника")
    p4 = Product(4, "Смартфон", 320000, "Электроника")
    p5 = Product(5, "Қуаттағыш", 8000, "Электроника")
    my_order = Order(8, user)
    my_order.add_product(p1)
    my_order.add_product(p2)
    my_order.add_product(p3)
    my_order.add_product(p4)
    my_order.add_product(p5)
    top_2_products = my_order.most_expensive_products(2)
    all_items_data = [{"name": p._name, "price": p._price} for p in my_order._products]
    top_2_data = [{"id": p._id, "name": p._name, "price": p._price} for p in top_2_products]
    return jsonify({
        "message": "8-ші тапсырма сәтті орындалды!",
        "all_items_in_order": all_items_data,
        "top_2_most_expensive": top_2_data
    })
@app.route("/task9")
def show_task9():
    p1 = Product(1, "Алма", 500, "Тамақ")
    p2 = Product(2, "Сүт", 450, "Тамақ")
    p3 = Product(3, "Нан", 200, "Тамақ")
    p4 = Product(4, "Шоколад", 800, "Тамақ")
    my_products = [p1, p2, p3, p4]
    prices_list = list(price_stream(my_products))
    return jsonify({
        "message": "9-шы тапсырма: Генератор сәтті жұмыс істеп тұр!",
        "extracted_prices": prices_list,
        "total_sum": sum(prices_list)
    })
#10
class OrderIterator:
    def __init__(self, order):
        self.order = order
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        for ar in self.order:
            if self._index < len(ar):
                current_order = self.order[self._index]
                self._index += 1
                return current_order
            else:
                raise StopIteration
@app.route("/task10")
def show_task10():
    class MockUser:
        def __init__(self, user_id):
            self._id = user_id
    user = MockUser(1010)
    p1 = Product(1, "Пицца", 3500, "Тамақ")
    p2 = Product(2, "Сусын", 500, "Сусын")
    order1 = Order(101, user)
    order1.add_product(p1)
    order2 = Order(102, user)
    order2.add_product(p2)
    order3 = Order(103, user)
    order3.add_product(p1)
    order3.add_product(p2)
    orders_list = [order1, order2, order3]
    my_iterator = OrderIterator(orders_list)
    iterated_results = []
    for order in my_iterator:
        iterated_results.append(str(order))
    return jsonify({
        "message": "10-шы тапсырма: Итератор сәтті жұмыс істеп тұр! Цикл толық айналды.",
        "processed_orders": iterated_results,
        "total_orders_counted": len(iterated_results)
    })
#11
def get_price_array(products):
    prices = [p._price for p in products]
    prices_array = np.array(prices)
    return prices_array
@app.route("/task11")
def show_task11():
    p1 = Product(1, "Laptop", 1200.0, "Electronics")
    p2 = Product(2, "Mouse", 25.0, "Electronics")
    p3 = Product(3, "Keyboard", 75.0, "Electronics")
    products_list = [p1, p2, p3]
    prices_array = get_price_array(products_list)
    return jsonify({
        "message": "11-ші тапсырма: Numpy массиві сәтті жасалды!",
        "array_type": str(type(prices_array)),
        "array_shape": prices_array.shape,
        "array_data": prices_array.tolist()
    })
#12
def get_mean_and_median(prices_array):
    mean_price = round(np.mean(prices_array), 2)
    median_price = np.median(prices_array)
    return (mean_price, median_price)
@app.route("/task12")
def show_task12():
    prices_array = np.array([1200.0, 25.0, 450.0])
    mean_price, median_price = get_mean_and_median(prices_array)
    return jsonify({
        "message": "12-ші тапсырма сәтті орындалды!",
        "input_prices": prices_array.tolist(),
        "calculated_mean": mean_price,
        "calculated_median": median_price,
        "tuple_result": [mean_price, median_price]
    })
#13
def normalize_prices(prices_array):
    p_min = np.min(prices_array)
    p_max = np.max(prices_array)
    return (prices_array - p_min) / (p_max - p_min)
@app.route("/task13")
def show_task13():
    prices = np.array([1200.0, 25.0, 450.0])
    normalized = normalize_prices(prices)
    return jsonify({
        "original_prices": prices.tolist(),
        "normalized_prices": [round(x, 4) for x in normalized.tolist()],
        "explanation": "Ең қымбат тауар (1200) 1.0-ге, ең арзаны (25) 0.0-ге айналды."
    })
#14
def get_categories_array(products):
    return np.array([p._category for p in products])
@app.route("/task14")
def show_task14():
    p1 = Product(1, "Laptop", 1200.0, "Electronics")
    p2 = Product(2, "T-Shirt", 20.0, "Clothing")
    products = [p1, p2]
    cat_array = get_categories_array(products)
    return jsonify({
        "categories_array": cat_array.tolist(),
        "type": str(type(cat_array))
    })
 # indices = get_indices_above_1000(orders_array)
#15
def count_unique_categories(categories_array):
    unique_elements = np.unique(categories_array)
    return len(unique_elements)
@app.route("/task15")
def show_task15():
    categories = np.array(["Electronics", "Clothing", "Electronics", "Food", "Clothing"])
    unique_count = count_unique_categories(categories)
    return jsonify({
        "input_categories": categories.tolist(),
        "unique_count": int(unique_count),
        "unique_items": np.unique(categories).tolist()
    })
#16
def get_expensive_than_average(products, prices_array):
    avg = np.mean(prices_array)
    return [p for p in products if p._price > avg]
@app.route("/task16")
def show_task16():
    p1 = Product(1, "Laptop", 1200.0, "Electronics")
    p2 = Product(2, "Mouse", 25.0, "Electronics")
    p3 = Product(3, "Monitor", 450.0, "Electronics")
    products = [p1, p2, p3]
    prices = np.array([p._price for p in products])
    expensive_products = get_expensive_than_average(products, prices)
    avg_price = np.mean(prices)
    return jsonify({
        "average_price": float(avg_price),
        "expensive_products": [{"name": p._name, "price": p._price} for p in expensive_products]
    })
#17
def apply_discount(prices_array):
    return prices_array * 0.9
@app.route("/task17")
def show_task17():
    prices = np.array([1200.0, 25.0, 450.0])
    discounted = apply_discount(prices)
    return jsonify({
        "before_discount": prices.tolist(),
        "after_10_percent_discount": discounted.tolist()
    })
#18
def create_orders_2d_array(orders_list):
    prices = [o.total_price() for o in orders_list]
    return np.array(prices).reshape(-1, 1)
@app.route("/task18")
def show_task18():
    p1 = Product(1, "Laptop", 1200.0, "Electronics")
    p2 = Product(2, "Mouse", 25.0, "Electronics")
    u1 = User(1, "Aslan", "aslan@mail.com")
    u2 = User(2, "Damir", "damir@mail.com")
    o1 = Order(1, u1)
    o1.add_product(p1)
    o2 = Order(2, u2)
    o2.add_product(p1)
    o2.add_product(p2)
    orders_2d = create_orders_2d_array([o1, o2])
    return jsonify({
        "description": "2D массив (әр жол - пайдаланушы)",
        "array_2d": orders_2d.tolist(),
        "shape": orders_2d.shape
    })
#19
def get_average_per_user(orders_array):
    return np.mean(orders_array)
@app.route("/task19")
def show_task19():
    orders_array = np.array([1200.0, 1225.0]) # Массив: [1200.0, 1225.0]
    avg = get_average_per_user(orders_array)
    return jsonify({
        "input_orders": orders_array.tolist(),
        "average_purchase": float(avg)  # 1212.5
    })
#20
def indexis(order_array):
    ind = np.where(order_array > 1000)[0]
    return ind.tolist()
@app.route("/task20")
def show_task20():
    orders_array = np.array([1200.0, 900.0, 1500.0])
    indd = indexis(orders_array)
    return jsonify({
        "orders": orders_array.tolist(),
        "above_1000": indd,
    })
#21
def create_users(users_list):
    data = []
    for u in users_list:
        data.append({
            "id": u._id,
            "name": u._name,
            "email": u._email,
            "registration_date": datetime.today()
        })
    df = pd.DataFrame(data)
    return df
@app.route("/task21")
def show_task21():
    u1 = User(1, "John Doe", "jogN@example.com")
    u2 = User(2, "Alice", "alice@example.com")
    users = [u1, u2]
    df = create_users(users)
    return jsonify({
        "colums": list(df.columns),
        "data": df.to_dict(orient="records"),
    })
#22
def create_products(products_list):
    datalar = []
    for p in products_list:
        datalar.append({
            "id": p._id,
            "name": p._name,
            "category": p._category,
            "price": p._price,
        })
        return pd.DataFrame(datalar)
@app.route("/task22")
def show_task22():
    p1 = Product(1, "Laptop", 1200.0, "Electronics")
    p2 = Product(2, "T-Shirt", 20, "Clothing")
    df = create_products([p1, p2])
    return jsonify(df.to_dict(orient="records"))
#23
def create_merge(users_df, orders_df):
    merged = pd.merge(users_df, orders_df, left_on="id", right_on="user_id")
    return merged[['order_id', 'user_name', 'total']].rename(columns={'user': "user_name"})
@app.route("/task23")
def show_task23():
    users_df = pd.DataFrame({"id": [1, 2], "name": ["John", "Alice"]})
    orders_df = pd.DataFrame({"order_id": [101, 102], "user_id": [1,2], "total": [1200, 25]})
    merged = create_merge(users_df, orders_df)
    return jsonify(merged.to_dict(orient="records"))
#24
def filter_sums(df, value):
    return df[df['total'] >= value]
@app.route("/task24")
def show_task24():
    df = pd.DataFrame({
        "id": [1, 2],
        "user_name": ["John", "Alice"],
        "total": [1200, 25],
    })
    filtered = filter_sums(df, 100)
    return jsonify(filtered.to_dict(orient="records"))
#25
def group_orders_by_user(df):
    return df.groupby('user_id')['total'].sum()
@app.route("/task25")
def show_task25():
    df = pd.DataFrame({
        "id": [101, 103, 102],
        "name": ["John", "John", "Alice"],
        "total": [1200, 500, 25]
    })
    grouped = group_orders_by_user(df)
    return jsonify(grouped.to_dict(orient="records"))
#26
def get_average_order(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("user_name")["total"].mean().reset_index(name="mean_total")
@app.route("/task26")
def check_task26():
    df = pd.DataFrame({
        "order_id": [101, 103, 102],
        "user_name": ["John", "John", "Alice"],
        "total": [1200, 500, 25]
    })
    result_df = get_average_order(df) # Негізгі функцияны шақыру
    return result_df.to_dict(orient="records")
# Задача 27
def count_user_orders(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("user_name")["order_id"].count().reset_index(name="orders_count")
@app.route("/task27")
def check_task27():
    df = pd.DataFrame({
        "order_id": [101, 103, 102],
        "user_name": ["John", "John", "Alice"],
        "total": [1200, 500, 25]
    })
    result_df = count_user_orders(df) # Негізгі функцияны шақыру
    return result_df.to_dict(orient="records")
# Задача 28
def get_average_price_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("category")["price"].mean().reset_index(name="mean_price")
@app.route("/task28")
def check_task28():
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Laptop", "Mouse", "Shirt"],
        "category": ["Electronics", "Electronics", "Clothing"],
        "price": [1200, 25, 20]
    })
    result_df = get_average_price_by_category(df)
    return result_df.to_dict(orient="records")
# Задача 29
def add_discount(df: pd.DataFrame) -> pd.DataFrame:
    df["discounted_price"] = df["price"] * 0.9
    return df
@app.route("/task29")
def check_task29():
    df = pd.DataFrame({
        "id": [1, 2],
        "name": ["Laptop", "Mouse"],
        "price": [1200, 25]
    })
    result_df = add_discount(df) # Негізгі функцияны шақыру
    return result_df.to_dict(orient="records")
# Задача 30
def sort_by_price(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by="price", ascending=False)
@app.route("/task30")
def check_task30():
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Laptop", "Mouse", "Monitor"],
        "price": [1200, 25, 450]
    })
    result_df = sort_by_price(df) # Негізгі функцияны шақыру
    return result_df.to_dict(orient="records")
#31
def add_quantity_column(df: pd.DataFrame) -> pd.DataFrame:
    df_result = df.copy()
    df_result['quantity'] = 1
    return df_result
#32
def calculate_total_price(df: pd.DataFrame) -> pd.DataFrame:
    df_result = df.copy()
    df_result['total_price'] = df_result['price'] * df_result['quantity']
    return df_result
#33
def filter_by_category(df: pd.DataFrame, category_name: str) -> pd.DataFrame:
    return df[df['category'] == category_name]
#34
def count_products_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('category').size().reset_index(name='count')

@app.route('/task34')
def run_task34():
    df = pd.DataFrame([
        {"product_name": "Laptop", "category": "Electronics"},
        {"product_name": "Mouse", "category": "Electronics"},
        {"product_name": "Shirt", "category": "Clothing"}
    ])
    result = count_products_by_category(df)
    return jsonify(result.to_dict(orient="records"))
#35
def calculate_mean_price_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('category')['price'].mean().reset_index(name='mean_price')
@app.route('/task31')
def run_task31():
    data = [
        {"order_id": 101, "product_name": "Laptop", "price": 1200},
        {"order_id": 102, "product_name": "Mouse", "price": 25}
    ]
    df = pd.DataFrame(data)

    result_df = add_quantity_column(df)
    return jsonify(result_df.to_dict(orient="records"))
@app.route('/task32')
def run_task32():
    data = [
        {"order_id": 101, "product_name": "Laptop", "price": 1200, "quantity": 1},
        {"order_id": 102, "product_name": "Mouse", "price": 25, "quantity": 2}
    ]
    df = pd.DataFrame(data)
    result_df = calculate_total_price(df)
    return jsonify(result_df.to_dict(orient="records"))
@app.route('/task33')
def run_task33():
    data = [
        {"product_name": "Laptop", "category": "Electronics", "price": 1200},
        {"product_name": "T-Shirt", "category": "Clothing", "price": 20}
    ]
    df = pd.DataFrame(data)

    result_df = filter_by_category(df, "Electronics")
    return jsonify(result_df.to_dict(orient="records"))


# 35
def calculate_mean_price_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('category')['price'].mean().reset_index(name='mean_price')


@app.route('/task35')
def run_task35():
    df = pd.DataFrame([
        {"product_name": "Laptop", "category": "Electronics", "price": 1200},
        {"product_name": "Mouse", "category": "Electronics", "price": 25},
        {"product_name": "Shirt", "category": "Clothing", "price": 20}
    ])
    result = calculate_mean_price_by_category(df)
    return jsonify(result.to_dict(orient="records"))


# 36
def sort_orders_by_total(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by='total_price', ascending=False)


@app.route('/task36')
def run_task36():
    df = pd.DataFrame({"order_id": [101, 102], "total_price": [1200, 50]})
    result = sort_orders_by_total(df)
    return jsonify(result.to_dict(orient="records"))


# 37
def get_top_n_orders(df: pd.DataFrame, n=3) -> pd.DataFrame:
    return df.nlargest(n, 'total_price')


@app.route('/task37')
def run_task37():
    df = pd.DataFrame({"order_id": [101, 102, 103, 104], "total_price": [1200, 50, 500, 1500]})
    result = get_top_n_orders(df, 3)
    return jsonify(result.to_dict(orient="records"))


# 38
def merge_orders_users(users_df, orders_df):
    merged = pd.merge(orders_df, users_df, on='user_id')
    return merged[['order_id', 'user_name', 'total_price']]


@app.route('/task38')
def run_task38():
    u_df = pd.DataFrame({"user_id": [1, 2], "user_name": ["John", "Alice"]})
    o_df = pd.DataFrame({"order_id": [101, 102], "user_id": [1, 2], "total_price": [1200, 50]})
    result = merge_orders_users(u_df, o_df)
    return jsonify(result.to_dict(orient="records"))


# 39
def mean_order_per_user(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('user_name')['total_price'].mean().reset_index(name='mean_total')


@app.route('/task39')
def run_task39():
    df = pd.DataFrame({"user_name": ["John", "John", "Alice"], "total_price": [1200, 500, 50]})
    result = mean_order_per_user(df)
    return jsonify(result.to_dict(orient="records"))


# 40
def count_orders_per_user(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('user_name')['order_id'].count().reset_index(name='orders_count')


@app.route('/task40')
def run_task40():
    df = pd.DataFrame({"user_name": ["John", "John", "Alice"], "order_id": [101, 103, 102]})
    result = count_orders_per_user(df)
    return jsonify(result.to_dict(orient="records"))


# 41
def max_order_per_user(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('user_name')['total_price'].max().reset_index(name='max_order')


@app.route('/task41')
def run_task41():
    df = pd.DataFrame({"user_name": ["John", "John", "Alice"], "total_price": [1200, 500, 50]})
    result = max_order_per_user(df)
    return jsonify(result.to_dict(orient="records"))


# 42
def unique_categories_per_user(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('user_name')['category'].nunique().reset_index(name='unique_categories')


@app.route('/task42')
def run_task42():
    df = pd.DataFrame({
        "user_name": ["John", "John", "John", "Alice"],
        "category": ["Electronics", "Electronics", "Clothing", "Clothing"]
    })
    result = unique_categories_per_user(df)
    return jsonify(result.to_dict(orient="records"))


# 43
def add_vip_status(df: pd.DataFrame) -> pd.DataFrame:
    df['VIP'] = df['total_sum'] > 1000
    return df


@app.route('/task43')
def run_task43():
    df = pd.DataFrame({"user_name": ["John", "Alice"], "total_sum": [1700, 25]})
    result = add_vip_status(df)
    return jsonify(result.to_dict(orient="records"))


# 44
def complex_sort(df: pd.DataFrame) -> pd.DataFrame:
    # total_sum (кемуімен), mean_total (өсуімен)
    return df.sort_values(by=['total_sum', 'mean_total'], ascending=[False, True])


@app.route('/task44')
def run_task44():
    df = pd.DataFrame({
        "user_name": ["John", "Alice", "Bob"],
        "total_sum": [1700, 25, 1700],
        "mean_total": [850, 25, 600]
    })
    result = complex_sort(df)
    return jsonify(result.to_dict(orient="records"))


# 45
def generate_final_report(df: pd.DataFrame) -> pd.DataFrame:
    report = df.groupby('user_name').agg(
        total_orders=('order_id', 'count'),
        total_sum=('total_price', 'sum'),
        mean_total=('total_price', 'mean'),
        max_order=('total_price', 'max'),
        unique_categories=('category', 'nunique')
    ).reset_index()


    report['VIP'] = report['total_sum'] > 1000
    return report


@app.route('/task45')
def run_task45():
    data = [
        {"user_name": "John", "order_id": 101, "total_price": 1200, "category": "Electronics"},
        {"user_name": "John", "order_id": 103, "total_price": 500, "category": "Clothing"},
        {"user_name": "Alice", "order_id": 102, "total_price": 25, "category": "Clothing"}
    ]
    df = pd.DataFrame(data)
    result = generate_final_report(df)
    return jsonify(result.to_dict(orient="records"))


if __name__ == '__main__':
    app.run(debug=True)