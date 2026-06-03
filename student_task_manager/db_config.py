import mysql.connector


def get_database_connection():
    connection = mysql.connector.connect(
        host = 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user = '3h38vmkG7FvmMmu.root',
        password = 'SVcuUEMbYe4TxZOS',
        database = 'student_task_manager',
        port = 4000
    )
    return connection



# def get_database_connection():
#     connection = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = 'aabid2005',
#         database = 'student_task_manager',
#     )
#     return connection