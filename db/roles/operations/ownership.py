from db.connection import exec_msar_func


def transfer_database_ownership(new_owner_oid, conn):
    return exec_msar_func(conn, 'transfer_database_ownership', new_owner_oid).fetchone()[0]