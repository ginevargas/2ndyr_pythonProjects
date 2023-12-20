# Python program that checks what horoscope corresponds a specific
# person’s birthdate.

day = int(input("Enter your day of birth: "))
month = input("Enter month of birth (e.g. april, june etc): ")

if month == 'march':
	zodiac_sign = 'Pisces' if (day < 21) else 'Aries'

elif month == 'april':
	zodiac_sign = 'Aries' if (day < 20) else 'Taurus'

elif month == 'may':
	zodiac_sign = 'Taurus' if (day < 21) else 'Gemini'

elif month == 'june':
	zodiac_sign = 'Gemini' if (day < 21) else 'Cancer'

elif month == 'july':
	zodiac_sign = 'Cancer' if (day < 23) else 'Leo'

elif month == 'august':
	zodiac_sign = 'Leo' if (day < 23) else 'Virgo'

elif month == 'september':
	zodiac_sign = 'Virgo' if (day < 23) else 'Libra'

elif month == 'october':
	zodiac_sign = 'Libra' if (day < 23) else 'Scorpio'

elif month == 'november':
	zodiac_sign = 'Scorpio' if (day < 22) else 'Sagittarius'

elif month == 'december':
	zodiac_sign = 'Sagittarius' if (day < 22) else 'Capricorn'

elif month == 'january':
	zodiac_sign = 'Capricorn' if (day < 20) else 'Aquarius'

elif month == 'february':
	zodiac_sign = 'Aquarius' if (day < 19) else 'Pisces'

print("Your Horoscope is ", zodiac_sign)