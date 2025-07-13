# 🟡 Solution ch_3_1 – Get All Products That Belong to a Specific Category Name.
```python

        # category = Category.objects.get(name=category_name)

        # products = (
        #     Product.objects.filter(category=category, is_active=True)
        #     .order_by("id")
        #     .distinct()
        # )

  products = Product.objects.filter(
            category__name=category_name,
            is_active=True,
        ).order_by("id")

```