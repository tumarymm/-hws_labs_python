import string

def analyze_students(a):
    b = []
    c = {}
    d = set()
    vowels = set('aeiouAEIOU')
    for e in a:
        f = e["name"]
        g = e["grades"]
        h = e["comments"]
        if any(ch.isdigit() for ch in f):
            continue
        f = f.title()
        i = []
        for j in g:
            if j <= 0:
                continue
            if j % 2 == 1 and j < 10:
                i.append(sum(int(k) for k in str(j)))
            elif j % 2 == 0 and j >= 10:
                i.append(j ** 2)
            else:
                i.append(j)
        all_comments = " ".join(h)
        all_comments = all_comments.translate(str.maketrans("", "", string.punctuation))
        words = all_comments.split()
        unique_words = []
        for w in words:
            w_lower = w.lower()
            if len(w_lower) >= 4 and w_lower != w_lower[::-1] and w_lower not in unique_words:
                unique_words.append(w_lower)
        student_vowels = set(c1 for c1 in "".join(unique_words) if c1 in vowels)
        d |= student_vowels
        for w in unique_words:
            if w in c:
                c[w] += 1
            else:
                c[w] = 1
        b.append({"name": f, "processed_grades": i})
    c = {k: v for k, v in c.items() if v >= 2}
    c = dict(sorted(c.items(), key=lambda x: (-x[1], x[0])))
    students_avg = []
    for s in b:
        avg = sum(s["processed_grades"])/len(s["processed_grades"]) if s["processed_grades"] else 0
        students_avg.append((s["name"], avg))
    students_avg = sorted(students_avg, key=lambda x: (-x[1], x[0]))
    students_by_avg = [x[0] for x in students_avg]
    students_by_name_length = {}
    for s in b:
        l = len(s["name"])
        if l not in students_by_name_length:
            students_by_name_length[l] = [s["name"]]
        else:
            if s["name"] not in students_by_name_length[l]:
                students_by_name_length[l].append(s["name"])
    return {
        "students": b,
        "word_counts": c,
        "all_vowels": d,
        "students_by_avg": students_by_avg,
        "students_by_name_length": students_by_name_length
    }


def analyze_orders(a):
    b = []
    c = {}
    d = set()
    vowels = set('aeiouAEIOU')
    e = set()
    for f in a:
        g = f["customer"]
        h = f["items"]
        i = f["notes"]
        if any(ch.isdigit() for ch in g):
            continue
        g = g.title()
        processed_items = []
        for j in h:
            k = j["name"]
            l = j["price"]
            m = j["quantity"]
            if l <= 0:
                continue
            if l > 100 and m > 1:
                l = l * m
            if m % 2 == 1:
                l += sum(int(c1) for c1 in str(int(l)))
            if l > 0:
                processed_items.append({"name": k, "price": l, "quantity": m})
                e.add(k)
        notes_text = " ".join(i)
        notes_text = notes_text.translate(str.maketrans("", "", string.punctuation))
        words = notes_text.split()
        unique_words = []
        for w in words:
            w_lower = w.lower()
            if len(w_lower) >= 4 and w_lower != w_lower[::-1] and w_lower not in unique_words:
                unique_words.append(w_lower)
        order_vowels = set(c1 for c1 in "".join(unique_words) if c1 in vowels)
        d |= order_vowels
        for w in unique_words:
            if w in c:
                c[w] += 1
            else:
                c[w] = 1
        b.append({"customer": g, "processed_items": processed_items, "order_id": f["order_id"]})
    c = {k: v for k, v in c.items() if v >= 2}
    c = dict(sorted(c.items(), key=lambda x: (-x[1], x[0])))
    orders_sum = []
    for f in b:
        total = sum(item["price"] for item in f["processed_items"])
        orders_sum.append((f["order_id"], total))
    orders_sum = sorted(orders_sum, key=lambda x: (-x[1], x[0]))
    orders_by_total = [x[0] for x in orders_sum]
    orders_by_item_count = {}
    for f in b:
        l = len(f["processed_items"])
        if l not in orders_by_item_count:
            orders_by_item_count[l] = [f["order_id"]]
        else:
            if f["order_id"] not in orders_by_item_count[l]:
                orders_by_item_count[l].append(f["order_id"])
    return {
        "orders": b,
        "word_counts": c,
        "all_vowels": d,
        "unique_products": e,
        "orders_by_total": orders_by_total,
        "orders_by_item_count": orders_by_item_count
    }