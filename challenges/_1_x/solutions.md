# Challenge Solutions

# 🟡 Solution ch_1_1 – Retrieve all active products only

This returns full model instances with all fields loaded.
Useful when you need access to the entire model or its methods.

```python
Product.objects.all().filter(is_active=True).order_by("-name")
```

# 🟢 Solution ch_1_2 – Select Product Names and Prices Only

This returns full model instances with only selected fields loaded (`name` and `price`).
It's useful for optimizing performance when you don’t need the entire model.

```python
Product.objects.only("name", "price").order_by("-price")
```

# 🔵 Solution ch_1_3 – Get the First Product Created

This fetches the very first product based on its creation timestamp.

```python
Product.objects.order_by("created_at").first()
```

# 🟡 Solution ch_1_4 – Get the Most Recently Added Product

This retrieves the last product added by ordering on the creation timestamp in descending order.

```python
Product.objects.order_by("-created_at").first()
Product.objects.order_by("created_at").last()
```

# 🟢 Solution ch_1_5 – Retrieve All Exclude Active Products

This uses `.exclude()` to filter out active products from the queryset.

```python
Product.objects.exclude(is_active=True)
```

# 🔵 Solution ch_1_6 – Filter Price == 19.99 and Exclude Category == 3

This chains a `.filter()` and `.exclude()` to build the desired query.

```python
Product.objects.filter(price=19.99).exclude(category=3)
```














# 🟢 Solution 2 – Use `.only()` to Limit Fields (Model Instances)


Fetch only selected fields: id, name, slug, description, price.
Still returns model instances, with only specified fields loaded.

```python
products = (
    Product.objects.filter(is_active=True)
    .only("id", "name", "slug", "description", "price")
    .order_by("name")
)
```

You still get model instances, but accessing any field outside of `.only()`
will trigger additional database queries (lazy loading).


# 🔵 Solution 3 – Use `.values()` to Return Raw Data


Fetch and return selected fields as dictionaries (not model instances).
```python
products = Product.objects.filter(is_active=True).values(
    "id", "name", "slug", "description", "price"
).order_by("name")

return Response(products)
```

