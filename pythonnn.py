print("Вітаємо у грі!")
name = input("Впишіть своє ім'я:")
print(f"{name} - гарне ім'я! Та зареєструватись у цій грі можна лише якщо вам 13 або більше років.")
age = int(input("Вкажіть свій вік:"))
years = 13 - age
if age >= 13:
    print(f"Чудово, {name}!")
    input("Вкажіть свою пошту:")
    input("Придумайте пароль:")
    print("Реєстрацію завершео успішно! Насолоджуйтесь грою :)")
else:
    print(f"На жаль, вам ще не можна грати у цю гру :( Зустрінемось за {years} років!")