# Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7.
# Могут ли два билета подряд быть удачными?

def ticketNumberSum(ticketNumber):
  sum = 0
  while ticketNumber > 0:
    # вычислить остаток от деления на число 10
    ticket = ticketNumber % 10
    # добавить в переменную sum
    sum += ticket
    # в ticketNumber записать число, сокращенное в 10 раз (отбрасывает у числа последнюю цифру)
    ticketNumber = ticketNumber // 10
  return sum

for ticketNumber in range (1000000):
  if ticketNumberSum(ticketNumber) % 7 == 0 and ticketNumberSum(ticketNumber+1) % 7 == 0:
    print("Удачные автобусные билеты, идущие подряд, следующие: ", ticketNumber, ticketNumber+1)