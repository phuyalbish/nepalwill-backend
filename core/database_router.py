# class DatabaseRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == "app_using_mysql":
#             return "mysql"
#         elif model._meta.app_label == "app_using_postgresql":
#             return "postgresql"
#         return "default"

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == "app_using_mysql":
#             db = "mysql"
#         elif model._meta.app_label == "app_using_postgresql":
#             db = "postgresql"
#         else:
#             db = "default"
#         return db

#     def allow_relation(self, obj1, obj2, **hints):
#         db_set = {"default", "mysql", "postgresql"}
#         if obj1._state.db in db_set and obj2._state.db in db_set:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, _, **hints):
#         if app_label == "app_using_mysql":
#             db == "mysql"
#         elif app_label == "app_using_postgresql":
#             db == "postgresql"
#         else:
#             db == "default"
#         return db
