import App
tt = App.model.database.Database()
m= tt.getHistoryOnDate("20220524")
print(m)