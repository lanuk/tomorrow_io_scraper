from sqlalchemy import create_engine, insert, MetaData

def connect_to_docker_db():
    print("Creating connection to db:", end=" ")
    host = "db"
    dbname = "mydatabase"
    user = "user"
    password = "password"
    port = "5432"
    engine = create_engine(
        f"postgresql://{user}:{password}@{host}:{port}/{dbname}")
    print("Complete")
    return engine


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#      For use when testing on local machine                                  #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def connect_to_local_db():
    print("Creating connection to db:", end=" ")
    host = "localhost"
    dbname = "mydatabase"
    user = "postgres"
    password = "postgres"
    port = "5431"
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