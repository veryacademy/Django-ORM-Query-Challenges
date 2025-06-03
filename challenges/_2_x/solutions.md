# 🟡 Solution ch_2_1 – Get the First and Last 5 Added Products
```python
    # Approach 1: Query Once, Slice in Memory
    def list(self, request):
        queryset = Product.objects.filter(is_active=True).order_by("id")
        total = queryset.count()

        first_five = list(queryset[:5])
        last_five = list(queryset[max(total - 5, 0) :])

        products = list({p.id: p for p in first_five + last_five}.values())

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # Approach 2.1:
    def list(self, request):
        products = list(
            Product.objects.filter(is_active=True).order_by("id")[:5]
        ) + list(Product.objects.filter(is_active=True).order_by("-id")[:5])
        products = list({p.id: p for p in products}.values())

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # Approach 2.2:
    def list(self, request):
        first_five = Product.objects.filter(is_active=True).order_by("id")[:5]
        last_five = Product.objects.filter(is_active=True).order_by("-id")[:5]

        combined = list({p.id: p for p in list(first_five) + list(last_five)}.values())

        # Sort the result by ID (ascending)
        products = sorted(combined, key=lambda p: p.id)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # Approach 2.3:
    def list(self, request):
        # Query for the first five active products ordered by ID ascending
        first_five_queryset = Product.objects.filter(is_active=True).order_by("id")[:5]

        # Query for the last five active products ordered by ID descending
        last_five_queryset = Product.objects.filter(is_active=True).order_by("-id")[:5]

        # Combine the two querysets using .union()
        # By default, union() performs a UNION DISTINCT, removing duplicates.
        # If you needed UNION ALL, you'd use .union(..., all=True)
        combined_products = first_five_queryset.union(last_five_queryset)

        # The combined_products is now a QuerySet, which can be directly serialized.
        serializer = ProductSerializer(combined_products, many=True)
        return Response(serializer.data)
```

# 🔵 Solution ch_2_2 – Retrieve Orders from the Last 30 Days
```python
def list(self, request):
    thirty_days_ago = now() - timedelta(days=30)
    orders = Order.objects.filter(created_at__gte=thirty_days_ago)

    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
```

# 🟣 Solution ch_2_3 – Find Products in Multiple Categories (IDs: 1, 4, 8, 11)
```python
    def list(self, request):
        category_ids = [1, 4, 8, 11]
        products = Product.objects.filter(category_id__in=category_ids)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
```

# 🟢 Solution ch_2_4 – List Products Priced Between 50 and 1000
```python
    def list(self, request):
        products = Product.objects.filter(price__gte=50, price__lte=1000)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
```

# 🟠 Solution ch_2_5 – Exclude Products Priced 19.99 and Under 100
```python
    def list(self, request):
        products = Product.objects.exclude(price=19.99).filter(price__lt=100)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
```

# 🟡 Solution ch_2_6 – Find Users Named janedoe or johndoe
```python
    def list(self, request):
        users = User.objects.filter(username__in=["janedoe", "johndoe"]).only(
            "username", "email"
        )

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
```

# 🔵 Solution ch_2_7 – Get Products Starting with the Letter 'W'
```python
    def list(self, request):
        products = Product.objects.filter(name__startswith="W")
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
```

# 🟣 Solution ch_2_8 – Find Products Ending with the Letter 'E'
```python
    def list(self, request):
        products = Product.objects.filter(name__iendswith="e")
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
```

# 🟢 Solution ch_2_9 – Show the Top 10 Most Expensive Active Products
```python
   def list(self, request):
        products = Product.objects.filter(is_active=True).order_by("-price")[:10]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

```

# 🟠 Solution ch_2_10 – Find Users with Emails Ending in 'example.com'
```python
   def list(self, request):
        users = User.objects.filter(email__endswith="example.com")
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
```

# 🟡 Solution ch_2_11 – Return the 20th most expensive product
```python
    def list(self, request):
        products = Product.objects.order_by("-price")[19:20]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
```

# 🔵 Solution ch_2_12 – Fetch Products with No Description
```python
```

# 🟣 Solution ch_2_13 – List All Promotion Events That Have Ended
```python
```

# 🟢 Solution ch_2_14 – List all Unique Categories Related to a Product
```python
```
