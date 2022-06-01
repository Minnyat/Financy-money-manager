from App.model.database import Money_database

tt = Money_database()
tt.modify_user_information(budget = 1000)
print(tt.get_user_information())