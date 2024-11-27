books = {}
borrowed_books = set()


while True:
    record = input("Enter book title and days borrowed (press 'done' when you finish): ")
    if record.lower() == 'done':
        break
    
    title, days_borrowed = record.split(" - ", 1) 
    days_borrowed = int(days_borrowed)
    
    
    if title in books:
        books[title] += days_borrowed
    else:
        books[title] = days_borrowed
    borrowed_books.add(title)
    

most = max(books, key=books.get)
least = min(books, key=books.get)

avg = sum(books.values()) / len(books)

unique = list(borrowed_books)

sorted = sorted(books.items(), key=lambda x: x[1], reverse=True) 

print(f"Most borrowed book: {most} with {books[most]} days")
print(f"Least borrowed book: {least} with {books[least]} days")
print(f"Average borrowing time: {avg} days")
print("Unique borrowed book titles: ",unique)
print("Books sorted by borrowing duration (most to least):")
for name, days in sorted:
    print(f"{name} = {days} days")