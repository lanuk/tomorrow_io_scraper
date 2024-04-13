from sqlalchemy import create_engine, insert, MetaData

def connect_to_db():
    print("Creating connection to db:", end=" ")
    host = "weather_db"
    dbname = "mydatabase"
    user = "user"
    password = "password"
    port = "5432"
    engine = create_engine(
        f"postgresql://{user}:{password}@{host}:{port}/{dbname}")
    print("Complete")
    return engine


def create_table(engine, table):
    table.drop(engine, checkfirst=True)
    table.create(engine, checkfirst=True)


def load_data(engine, table, data):
    success = 0
    for row in data:
        insert_stmt = insert(table).values(row)
        with engine.connect() as conn:
            conn.execute(insert_stmt)
            conn.commit()
            success += 1
    print("Successfully loaded " + str(success) + " out of " +
        str(len(data)) + " rows.")