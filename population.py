"""
יש N תנינים.
לכל תנין יש שנת לידה ושנת פטירה.
כתבו אלגוריתם שמקבל כקלט N זוגות של מספרים שמתארים את שנת הלידה ושנת הפטירה של כל תנין.
האלגוריתם מחשב ומחזיר את השנה שבה חיו הכי הרבה תנינים בו זמנית. אם יש כמה שנים כאלה, ניתן להחזיר אחת מהן.
"""

items = ((1900, 1950),
         (1920, 1970),
         (1930, 1960),
         (1932, 1962),
         (1945, 1971),
         (1922, 1946),
         (1925, 1965))

# Create a list of birth/death events. Each event is a tuple containing year and 1 if birth, -1 if death
events = []
for item in items:
    events.append((item[0], 1))
    events.append((item[1], -1))

# Sort the events based on year
events.sort(key=lambda x: x[0])

# Iterate on the events list. Maintain current population by adding the event's second element for each event.
# Each time new high record found - update record year and population.
max_population = 0
cur_population = 0
year = None
for event in events:
    cur_population += event[1]
    if cur_population > max_population:
        max_population = cur_population
        year = event[0]

print('The maximum population was {} in year {}'.format(max_population, year))
