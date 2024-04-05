from demograph.models import (
    best_seller,
)  # not seen in the screenshot but needed to find best_seller class from the graph/models.py
import csv

with open("bestsellers with categories2.csv", encoding="UTF-16") as csvfile:

    reader = csv.DictReader(csvfile)
    for row in reader:
        p = best_seller(
            book_name=row["Name"],
            author=row["Author"],
            ave_user_rating=row["User Rating"],
            review_count=row["Reviews"],
            price=row["Price"],
            year=row["Year"],
            genre=["Genre"],
        )
        p.save()
