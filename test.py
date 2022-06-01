from App.model.database import Money_database

tt = Money_database()
tt.modify_user_information(budget = 103)
print(tt.get_user_information())