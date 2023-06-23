from nicegui import ui
import os

lunarDays = []
dates = []
personalNumbers = []
planets = []
mansions = []
lunarSigns = []
solarSigns = []

day1 = ''
day2 = ''
day3 = ''
day4 = ''
day5 = ''
day6 = ''
day7 = ''
day8 = ''
day9 = ''
day10 = ''
day11 = ''
day12 = ''
day13 = ''
day14 = ''
day15 = ''
day16 = ''
day17 = ''
day18 = ''
day19 = ''
day20 = ''
day21 = ''
day22 = ''
day23 = ''
day24 = ''
day25 = ''
day26 = ''
day27 = ''
day28 = ''
day29 = ''
day30 = ''
day31 = ''
pn1 = ''
pn2 = ''
pn3 = ''
pn4 = ''
pn5 = ''
pn6 = ''
pn7 = ''
pn8 = ''
pn9 = ''
sun = ''
moon = ''
mars = ''
mercury = ''
jupiter = ''
venus = ''
saturn = ''
mansion1 = ''
mansion2 = ''
mansion3 = ''
mansion4 = ''
mansion5 = ''
mansion6 = ''
mansion7 = ''
mansion8 = ''
mansion9 = ''
mansion10 = ''
mansion11 = ''
mansion12 = ''
mansion13 = ''
mansion14 = ''
mansion15 = ''
mansion16 = ''
mansion17 = ''
mansion18 = ''
mansion19 = ''
mansion20 = ''
mansion21 = ''
mansion22 = ''
mansion23 = ''
mansion24 = ''
mansion25 = ''
mansion26 = ''
mansion27 = ''
mansion28 = ''
aries = ''
taurus = ''
gemini = ''
cancer = ''
leo = ''
virgo = ''
libra = ''
scorpio = ''
sagittarius = ''
capricorn = ''
aquarius = ''
pisces = ''

ageLabels = ["Day 1: Gambling | Luck | Strategy", "Day 2: Gain a winning strategy","Day 3: Talismans | War","Day 4: Love | Bonds","Day 5: Gaining affection of Authority","Day 6 Beneficial Judgment","Day 7: Scrying","Day 8: Burying | Shadow Work","Day 9: Familial Joy | Home Care","Day 10: Epileptic Cure","Day 11: DM Obeisance","Day 12: DM Affection","Day 13: Increase of resources","Day 14: Dealing with Spirits","Day 15: Speaking with Demons","Day 16: Man’s love for woman","Day 17: Stopping a ship from sailing","Day 18: Woman’s confession","Day 19: Opening Locks","Day 20: Eliminating Enemies","Day 21: Avoiding Gossip, Rumors & Insults","Day 22: Unbinding","Day 23: Fishing","Day 24: Accepting Consequence","Day 25: Unbinding a couple","Day 26: Persuading Authority","Day 27: Love","Day 28: Love","Day 29: Destruction"]

dateLabels = ["1st", "2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31st"]

dateInfluences = ["[[Archetype 1#Influences|Influences]]","[[Archetype 2#Influences|Influences]]","[[Archetype 3#Influences|Influences]]","[[Archetype 4#Influences|Influences]]","[[Archetype 5#Influences|Influences]]","[[Archetype 6#Influences|Influences]]","[[Archetype 7#Influences|Influences]]","[[Archetype 8#Influences|Influences]]","[[Archetype 9#Influences|Influences]]","[[Archetype 1#Influences|Influences]]","[[Archetype 2#Influences|Influences]]","[[Archetype 3#Influences|Influences]]","[[Archetype 4#Influences|Influences]]","[[Archetype 5#Influences|Influences]]","[[Archetype 6#Influences|Influences]]","[[Archetype 7#Influences|Influences]]","[[Archetype 8#Influences|Influences]]","[[Archetype 9#Influences|Influences]]","[[Archetype 1#Influences|Influences]]","[[Archetype 2#Influences|Influences]]","[[Archetype 3#Influences|Influences]]","[[Archetype 4#Influences|Influences]]","[[Archetype 5#Influences|Influences]]","[[Archetype 6#Influences|Influences]]","[[Archetype 7#Influences|Influences]]","[[Archetype 8#Influences|Influences]]","[[Archetype 9#Influences|Influences]]","[[Archetype 9#Influences|Influences]]","[[Archetype 2#Influences|Influences]]","[[Archetype 3#Influences|Influences]]","[[Archetype 4#Influences|Influences]]"]

planetLabels = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]

planetInfluences = ["[[Book of Shadows/MOD/Fleeting/Astrology/Planets/Sun#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Planets/Moon#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Planets/Mars#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Planets/Mercury#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Planets/Jupiter#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Planets/Venus#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Planets/Saturn#Influences|Influences]]"]

personalNumberLabels = ["PN1", "PN2", "PN3", "PN4", "PN5", "PN6", "PN7", "PN8", "PN9"]

personalNumbersInfluences = ["[[Archetype 1#Influences|Influences]]", "[[Archetype 2#Influences|Influences]]", "[[Archetype 3#Influences|Influences]]", "[[Archetype 4#Influences|Influences]]", "[[Archetype 5#Influences|Influences]]", "[[Archetype 6#Influences|Influences]]", "[[Archetype 7#Influences|Influences]]", "[[Archetype 8#Influences|Influences]]", "[[Archetype 9#Influences|Influences]]"]

mansionLabels = [
"1 Al-Sharatain",
"2 Al-Butain",
"3 Al-Thurraya",
"4 Al-Dabaran",
"5 Al-Haqa",
"6 Al-Hana",
"7 Al-Dhira",
"8 Al-Nathrah",
"9 Al-Tarf",
"10 Al-Jabhah",
"11 Al-Zubrah",
"12 Al-Sarfah",
"13 Al-Awwa",
"14 Al-Simak",
"15 Al-Ghafr",
"16 Al-Zubana",
"17 Al-Iklil",
"18 Al-Qalb",
"19 Al-Shaulah",
"20 Al-Na'am",
"21 Al-Baldah",
"22 Sa'd al-Dhabih",
"23 Sa'd Bula",
"24 Sa'd al-Su'ud",
"25 Sa'd al-Akhbiya",
"26 Al Fargh al-Awwal",
"27 Al Fargh al-Thani",
"28 Batu al-Hut"]

waxingInfluences = ["[[Al-Sharatain#Waxing|Waxing Influences]]","[[Al-Butain#Waxing|Waxing Influences]]","[[Al-Thurraya#Waxing|Waxing Influences]]","[[Al-Dabaran#Waxing|Waxing Influences]]","[[Al-Haqa#Waxing|Waxing Influences]]","[[Al-Hana#Waxing|Waxing Influences]]","[[Al-Dhira#Waxing|Waxing Influences]]","[[Al-Nathrah#Waxing|Waxing Influences]]","[[Al-Tarf#Waxing|Waxing Influences]]","[[Al-Jabhah#Waxing|Waxing Influences]]","[[Al-Zubrah#Waxing|Waxing Influences]]","[[Al-Sarfah#Waxing|Waxing Influences]]","[[Al-Awwa#Waxing|Waxing Influences]]","[[Al-Simak#Waxing|Waxing Influences]]","[[Al-Ghafr#Waxing|Waxing Influences]]","[[Al-Zubana#Waxing|Waxing Influences]]","[[Al-Iklil#Waxing|Waxing Influences]]","[[Al-Qalb#Waxing|Waxing Influences]]","[[Al-Shaulah#Waxing|Waxing Influences]]","[[Al-Na'am#Waxing|Waxing Influences]]","[[Al-Baldah#Waxing|Waxing Influences]]","[[Sa'd al-Dhabih#Waxing|Waxing Influences]]","[[Sa'd Bula#Waxing|Waxing Influences]]","[[Sa'd al-Su'ud#Waxing|Waxing Influences]]","[[Sa'd al-Akhbiyah#Waxing|Waxing Influences]]","[[Al Fargh al-Awwal#Waxing|Waxing Influences]]","[[Al Fargh al-Thani#Waxing|Waxing Influences]]","[[Batu al-Hut#Waxing|Waxing Influences]]"]

waningInfluences = ["[[Al-Sharatain#Waning|Waning Influences]]","[[Al-Butain#Waning|Waning Influences]]","[[Al-Thurraya#Waning|Waning Influences]]","[[Al-Dabaran#Waning|Waning Influences]]","[[Al-Haqa#Waning|Waning Influences]]","[[Al-Hana#Waning|Waning Influences]]","[[Al-Dhira#Waning|Waning Influences]]","[[Al-Nathrah#Waning|Waning Influences]]","[[Al-Tarf#Waning|Waning Influences]]","[[Al-Jabhah#Waning|Waning Influences]]","[[Al-Zubrah#Waning|Waning Influences]]","[[Al-Sarfah#Waning|Waning Influences]]","[[Al-Awwa#Waning|Waning Influences]]","[[Al-Simak#Waning|Waning Influences]]","[[Al-Ghafr#Waning|Waning Influences]]","[[Al-Zubana#Waning|Waning Influences]]","[[Al-Iklil#Waning|Waning Influences]]","[[Al-Qalb#Waning|Waning Influences]]","[[Al-Shaulah#Waning|Waning Influences]]","[[Al-Na'am#Waning|Waning Influences]]","[[Al-Baldah#Waning|Waning Influences]]","[[Sa'd al-Dhabih#Waning|Waning Influences]]","[[Sa'd Bula#Waning|Waning Influences]]","[[Sa'd al-Su'ud#Waning|Waning Influences]]","[[Sa'd al-Akhbiyah#Waning|Waning Influences]]","[[Al Fargh al-Awwal#Waning|Waning Influences]]","[[Al Fargh al-Thani#Waning|Waning Influences]]","[[Batu al-Hut#Waning|Waning Influences]]"]

lunarLabels = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

lunarInfluences = ["[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Aries#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Taurus#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Gemini#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Cancer#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Leo#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Virgo#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Libra#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Scorpio#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Sagittarius#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Capricorn#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Aquarius#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Pisces#Influences|Influences]]"]

solarLabels = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

solarInfluences = ["[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Aries#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Taurus#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Gemini#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Cancer#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Leo#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Virgo#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Libra#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Scorpio#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Sagittarius#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Capricorn#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Aquarius#Influences|Influences]]","[[Book of Shadows/MOD/Fleeting/Astrology/Zodiac/Pisces#Influences|Influences]]"]


ui.label('Energy map generator')

month = ui.input(label='Month')

def lunarDaySection():
  ui.label("Lunar Day")
  with ui.grid(rows=2, columns=10):
    
    day1 = ui.checkbox("1")
    ui.checkbox("1")
    day2 = ui.checkbox("2")
    day3 = ui.checkbox("3")
    day4 = ui.checkbox("4")
    day5 = ui.checkbox("5")
    day6 = ui.checkbox("6")
    day7 = ui.checkbox("7")
    day8 = ui.checkbox("8")
    day9 = ui.checkbox("9")
    day10 = ui.checkbox("10")
    
    day11 = ui.checkbox("11")
    day12 = ui.checkbox("12")
    day13 = ui.checkbox("13")
    day14 = ui.checkbox("14")
    day15 = ui.checkbox("15")
    day16 = ui.checkbox("16")
    day17 = ui.checkbox("17")
    day18 = ui.checkbox("18")
    day19 = ui.checkbox("19")
    day20 = ui.checkbox("20")
    
    day21 = ui.checkbox("21")
    day22 = ui.checkbox("22")
    day23 = ui.checkbox("23")
    day24 = ui.checkbox("24")
    day25 = ui.checkbox("25")
    day26 = ui.checkbox("26")
    day27 = ui.checkbox("27")
    day28 = ui.checkbox("28")
    day29 = ui.checkbox("29")
    day30 = ui.checkbox("30")

  lunarDays.append(day1)
  lunarDays.append(day2)
  lunarDays.append(day3)
  lunarDays.append(day4)
  lunarDays.append(day5)
  lunarDays.append(day6)
  lunarDays.append(day7)
  lunarDays.append(day8)
  lunarDays.append(day9)
  lunarDays.append(day10)
  lunarDays.append(day11)
  lunarDays.append(day12)
  lunarDays.append(day13)
  lunarDays.append(day14)
  lunarDays.append(day15)
  lunarDays.append(day16)
  lunarDays.append(day17)
  lunarDays.append(day18)
  lunarDays.append(day19)
  lunarDays.append(day20)
  lunarDays.append(day21)
  lunarDays.append(day22)
  lunarDays.append(day23)
  lunarDays.append(day24)
  lunarDays.append(day25)
  lunarDays.append(day26)
  lunarDays.append(day27)
  lunarDays.append(day28)
  lunarDays.append(day29)
  lunarDays.append(day30)
  
  return(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10,day11,day12,day13,day14,day15,day16,day17,day18,day19,day20,day21,day22,day23,day24,day25,day26,day27,day28,day29,day30)

def dateSection():
  ui.label("Date")
  with ui.grid(rows=2, columns=10):
    
    day1 = ui.checkbox("1")
    day2 = ui.checkbox("2")
    day3 = ui.checkbox("3")
    day4 = ui.checkbox("4")
    day5 = ui.checkbox("5")
    day6 = ui.checkbox("6")
    day7 = ui.checkbox("7")
    day8 = ui.checkbox("8")
    day9 = ui.checkbox("9")
    day10 = ui.checkbox("10")
    
    day11 = ui.checkbox("11")
    day12 = ui.checkbox("12")
    day13 = ui.checkbox("13")
    day14 = ui.checkbox("14")
    day15 = ui.checkbox("15")
    day16 = ui.checkbox("16")
    day17 = ui.checkbox("17")
    day18 = ui.checkbox("18")
    day19 = ui.checkbox("19")
    day20 = ui.checkbox("20")
    
    day21 = ui.checkbox("21")
    day22 = ui.checkbox("22")
    day23 = ui.checkbox("23")
    day24 = ui.checkbox("24")
    day25 = ui.checkbox("25")
    day26 = ui.checkbox("26")
    day27 = ui.checkbox("27")
    day28 = ui.checkbox("28")
    day29 = ui.checkbox("29")
    day30 = ui.checkbox("30")
    day31 = ui.checkbox("31")

  dates.append(day1)
  dates.append(day2)
  dates.append(day3)
  dates.append(day4)
  dates.append(day5)
  dates.append(day6)
  dates.append(day7)
  dates.append(day8)
  dates.append(day9)
  dates.append(day10)
  dates.append(day11)
  dates.append(day12)
  dates.append(day13)
  dates.append(day14)
  dates.append(day15)
  dates.append(day16)
  dates.append(day17)
  dates.append(day18)
  dates.append(day19)
  dates.append(day20)
  dates.append(day21)
  dates.append(day22)
  dates.append(day23)
  dates.append(day24)
  dates.append(day25)
  dates.append(day26)
  dates.append(day27)
  dates.append(day28)
  dates.append(day29)
  dates.append(day30)
  dates.append(day31)

  return(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10,day11,day12,day13,day14,day15,day16,day17,day18,day19,day20,day21,day22,day23,day24,day25,day26,day27,day28,day29,day30,day31)

def personalNumberSection():
  ui.label("Personal Number")

  with ui.grid(columns= 9):
    pn1 = ui.checkbox("1")
    pn2 = ui.checkbox("2")
    pn3 = ui.checkbox("3")
    
    pn4 = ui.checkbox("4")
    pn5 = ui.checkbox("5")
    pn6 = ui.checkbox("6")
    
    pn7 = ui.checkbox("7")
    pn8 = ui.checkbox("8")
    pn9 = ui.checkbox("9")

  personalNumbers.append(pn1)
  personalNumbers.append(pn2)
  personalNumbers.append(pn3)
  personalNumbers.append(pn4)
  personalNumbers.append(pn5)
  personalNumbers.append(pn6)
  personalNumbers.append(pn7)
  personalNumbers.append(pn8)
  personalNumbers.append(pn9)

  return pn1,pn2,pn3,pn4,pn5,pn6,pn7,pn8,pn9

def planetSection():
  ui.label("Planets")
  # TODO add avatar images
  with ui.grid(columns=7):
    sun = ui.checkbox("Sun")
    moon = ui.checkbox("Moon")
    mars = ui.checkbox("Mars")
    mercury = ui.checkbox("Mercury")
    jupiter = ui.checkbox("Jupiter")
    venus = ui.checkbox("Venus")
    saturn = ui.checkbox("Saturn")
    
  planets.append(sun)
  planets.append(moon)
  planets.append(mars)
  planets.append(mercury)
  planets.append(jupiter)
  planets.append(venus)
  planets.append(saturn)

  return sun, moon, mars, mercury, jupiter, venus, saturn

def mansionSection():
  ui.label("Lunar Mansions")

  with ui.grid(columns=7):
    mansion1 = ui.checkbox("1 Alnath / Al-Sharatain")
    mansion2 = ui.checkbox("2 Albotain / Al-Butain")
    mansion3 = ui.checkbox("3 Athoray / Al-Thuraiya")
    mansion4 = ui.checkbox("4 Aldebaran / Al-Dabaran")
    mansion5 = ui.checkbox("5 Almices / Al-Haqa")
    mansion6 = ui.checkbox("6 Althaya / Al-Hana")
    mansion7 = ui.checkbox("7 Aldirah / Al-Dhira")
    mansion8 = ui.checkbox("8 Annathru / Al-Nathrah")
    mansion9 = ui.checkbox("9 Atarf / Al-Tarf")
    mansion10 = ui.checkbox("10 Alegba / Al-Jabhah")
    mansion11 = ui.checkbox("11 Azobra Al-Zabrah")
    mansion12 = ui.checkbox("12 Acarfa / Al-Sarfah")
    mansion13 = ui.checkbox("13 Alahue / Al-Awwa")
    mansion14 = ui.checkbox("14 Azimech / Al-Simak")
    mansion15 = ui.checkbox("15 Algarfa / Al-Ghafr")
    mansion16 = ui.checkbox("16 Azubene / Al-Zubana")
    mansion17 = ui.checkbox("17 Alichil / Al-iklil")
    mansion18 = ui.checkbox("18 Alcalb / Al-Qalb")
    mansion19 = ui.checkbox("19 Exaula / Al-Shaulah")
    mansion20 = ui.checkbox("20 Nahaym")
    mansion21 = ui.checkbox("21 Elbelda / Al-Baldah")
    mansion22 = ui.checkbox("22 Caadaldeba / Sa’d al-Dhabi")
    mansion23 = ui.checkbox("23 Caaddebolach / Sa’d Bula")
    mansion24 = ui.checkbox("24 Caadacohot Sa’d Saad")
    mansion25 = ui.checkbox("25 Caadaahaebia / Sa’d al-Akhbiyah")
    mansion26 = ui.checkbox("26 Almiquedan / Al-Fargh")
    mansion27 = ui.checkbox("27 Algarfalmaeharl / Al-Fargh al-Thani")
    mansion28 = ui.checkbox("28 Arreche / Batn al-Hut")

  mansions.append(mansion1)
  mansions.append(mansion2)
  mansions.append(mansion3)
  mansions.append(mansion4)
  mansions.append(mansion5)
  mansions.append(mansion6)
  mansions.append(mansion7)
  mansions.append(mansion8)
  mansions.append(mansion9)
  mansions.append(mansion10)
  mansions.append(mansion11)
  mansions.append(mansion12)
  mansions.append(mansion13)
  mansions.append(mansion14)
  mansions.append(mansion15)
  mansions.append(mansion16)
  mansions.append(mansion17)
  mansions.append(mansion18)
  mansions.append(mansion19)
  mansions.append(mansion20)
  mansions.append(mansion21)
  mansions.append(mansion22)
  mansions.append(mansion23)
  mansions.append(mansion24)
  mansions.append(mansion25)
  mansions.append(mansion26)
  mansions.append(mansion27)
  mansions.append(mansion28)
  
  return mansion1, mansion2, mansion3, mansion4, mansion5, mansion6, mansion7, mansion8, mansion9, mansion10, mansion11, mansion12, mansion13, mansion14, mansion15, mansion16, mansion17, mansion18, mansion19, mansion20, mansion21, mansion22, mansion23, mansion24, mansion25, mansion26, mansion27, mansion28

def lunarSignSection():
  ui.label("Lunar Sign")

  with ui.grid(columns=4):
    aries = ui.checkbox("Aries")
    taurus = ui.checkbox("Taurus")
    gemini = ui.checkbox("Gemini")
    cancer = ui.checkbox("Cancer")
    leo = ui.checkbox("Leo")
    virgo = ui.checkbox("Virgo")
    libra = ui.checkbox("Libra")
    scorpio = ui.checkbox("Scorpio")
    sagittarius = ui.checkbox("Sagittarius")
    capricorn = ui.checkbox("Capricorn")
    aquarius = ui.checkbox("Aquarius")
    pisces = ui.checkbox("Pisces")
    
  lunarSigns.append(aries)
  lunarSigns.append(taurus)
  lunarSigns.append(gemini)
  lunarSigns.append(cancer)
  lunarSigns.append(leo)
  lunarSigns.append(virgo)
  lunarSigns.append(libra)
  lunarSigns.append(scorpio)
  lunarSigns.append(sagittarius)
  lunarSigns.append(capricorn)
  lunarSigns.append(aquarius)
  lunarSigns.append(pisces)
  
  return aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces

def solarSignSection():
  ui.label("Solar Sign")
  with ui.grid(columns=4):
    aries = ui.checkbox("Aries")
    taurus = ui.checkbox("Taurus")
    gemini = ui.checkbox("Gemini")
    cancer = ui.checkbox("Cancer")
    leo = ui.checkbox("Leo")
    virgo = ui.checkbox("Virgo")
    libra = ui.checkbox("Libra")
    scorpio = ui.checkbox("Scorpio")
    sagittarius = ui.checkbox("Sagittarius")
    capricorn = ui.checkbox("Capricorn")
    aquarius = ui.checkbox("Aquarius")
    pisces = ui.checkbox("Pisces")

  solarSigns.append(aries)
  solarSigns.append(taurus)
  solarSigns.append(gemini)
  solarSigns.append(cancer)
  solarSigns.append(leo)
  solarSigns.append(virgo)
  solarSigns.append(libra)
  solarSigns.append(scorpio)
  solarSigns.append(sagittarius)
  solarSigns.append(capricorn)
  solarSigns.append(aquarius)
  solarSigns.append(pisces)
  
  return aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces

def log():
  for day in range(len(lunarDays)-1):
        temp = lunarDays[day]
        tempVal = temp.get()
        if tempVal == 1:
          print(f"{ageLabels[day]}")
          ui.markdown(ageLabels[day])
          
  for date in range(len(dates)-1):
      temp = dates[date]
      tempVal = temp.get()
      if tempVal == 1:
        print(f"{dateLabels[date]}")
        
  for number in range(len(personalNumbers)-1):
      temp = personalNumbers[number]
      tempVal = temp.get()
      if tempVal == 1:
        print(f"{personalNumberLabels[number]}")
        
  for mansion in range(len(mansions)-1):
      temp = mansions[mansion]
      tempVal = temp.get()
      if tempVal == 1:
        print(f"{mansionLabels[mansion]}")
        
  for planet in range(len(planets)-1):
      temp = planets[planet]
      tempVal = temp.get()
      if tempVal == 1:
        print(f"{planetLabels[planet]}")
        
  for lunar in range(len(lunarSigns)-1):
      temp = lunarSigns[lunar]
      tempVal = temp.get()
      if tempVal == 1:
        print(f"{lunarLabels[lunar]}")

def run():
  lunarDays.append(lunarDaySection())
  dates.append(dateSection())
  personalNumbers.append(personalNumberSection())
  mansions.append(mansionSection())
  lunarSigns.append(lunarSignSection())
  solarSigns.append(solarSignSection())
  ui.button("Submit")
  ui.run()

# ui.switch("1")
# lunarDaySection()
# ui.run()
run()