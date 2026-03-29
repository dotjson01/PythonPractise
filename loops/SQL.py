# SELECT count(*) FROM customers where id IS NULL;

tables = [ 'customers', 'orders', 'product']
columns = ['id', 'create_date']

for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} is NULL')