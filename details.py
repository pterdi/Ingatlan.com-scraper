# Getting details

# Variables and lists

ids = scraped_data['id'].tolist()

spec = []
built = []
comfort = []
energycertificate = []
floor = []
buildingfloors = []
lift = []
innerheight = []
heating = []
ac = []
furnished = []
utilities = []
moveintime = []
minrenttime = []
disabledfriendly = []
bathroom = []
orientation = []
view = []
garden = []
attic = []
mechanized = []
pet = []
smoking = []
parking = []

# Scraping details

start_time = time()
for id in ids:
  URL_details = 'https://ingatlan.com/' + id
  page_details = Request(URL_details, headers={'User-Agent': 'Mozilla/5.0'})
  sleep(randint(1,5))
  webpage_details = urlopen(page_details).read()
  soup_details = BeautifulSoup(webpage_details, 'html.parser')

  # Spec

  if soup_details.find('td', text = 'Ingatlan állapota') is None:
    spec_elem = 'nincs megadva'
  else:
    spec_elem = soup_details.find('td', text = 'Ingatlan állapota').findNext('td').text
  spec.append(spec_elem)

  # Built

  if soup_details.find('td', text = 'Építés éve') is None:
    built_elem = 'nincs megadva'
  else:
    built_elem = soup_details.find('td', text = 'Építés éve').findNext('td').text
  built.append(built_elem)

  # Comfort

  if soup_details.find('td', text = 'Komfort') is None:
    comfort_elem = 'nincs megadva'
  else:
    comfort_elem = soup_details.find('td', text = 'Komfort').findNext('td').text
  comfort.append(comfort_elem)

  # Energy certificate

  if soup_details.find('td', text = 'Energiatanúsítvány') is None:
    energycertificate_elem = 'nincs megadva'
  else:
    energycertificate_elem = soup_details.find('td', text = 'Energiatanúsítvány').findNext('td').text
  energycertificate.append(energycertificate_elem)

  # Floor

  if soup_details.find('td', text = 'Emelet') is None:
    floor_elem = 'nincs megadva'
  else:
    floor_elem = soup_details.find('td', text = 'Emelet').findNext('td').text
  floor.append(floor_elem)

  # Building floors

  if soup_details.find('td', text = 'Épület szintjei') is None:
    buildingfloors_elem = 'nincs megadva'
  else:
    buildingfloors_elem = soup_details.find('td', text = 'Épület szintjei').findNext('td').text
  buildingfloors.append(buildingfloors_elem)

  # Lift

  if soup_details.find('td', text = 'Lift') is None:
    lift_elem = 'nincs megadva'
  else:
    lift_elem = soup_details.find('td', text = 'Lift').findNext('td').text
  lift.append(lift_elem)

  # Inner height

  if soup_details.find('td', text = 'Belmagasság') is None:
    innerheight_elem = 'nincs megadva'
  else:
    innerheight_elem = soup_details.find('td', text = 'Belmagasság').findNext('td').text
  innerheight.append(innerheight_elem)

  # Heating

  if soup_details.find('td', text = 'Fűtés') is None:
    heating_elem = 'nincs megadva'
  else:
    heating_elem = soup_details.find('td', text = 'Fűtés').findNext('td').text
  heating.append(heating_elem)

  # AC

  if soup_details.find('td', text = 'Légkondicionáló') is None:
    ac_elem = 'nincs megadva'
  else:
    ac_elem = soup_details.find('td', text = 'Légkondicionáló').findNext('td').text
  ac.append(ac_elem)

  # Furnished
  
  if soup_details.find('td', text = 'Bútorozott') is None:
    furnished_elem = 'nincs megadva'
  else:
    furnished_elem = soup_details.find('td', text = 'Bútorozott').findNext('td').text
  furnished.append(furniture_elem)

  # Utilities

  if soup_details.find('td', text = 'Rezsiköltség') is None:
    utilities_elem = 'nincs megadva'
  else:
    utilities_elem = soup_details.find('td', text = 'Rezsiköltség').findNext('td').text
  utilities.append(utilities_elem)

  # Move in time

  if soup_details.find('td', text = 'Költözhető') is None:
    moveintime_elem = 'nincs megadva'
  else:
    moveintime_elem = soup_details.find('td', text = 'Költözhető').findNext('td').text
  moveintime.append(moveintime_elem)

  # Min rent time

  if soup_details.find('td', text = 'Min. bérleti idő') is None:
    minrenttime_elem = 'nincs megadva'
  else:
    minrenttime_elem = soup_details.find('td', text = 'Min. bérleti idő').findNext('td').text
  minrenttime.append(minrenttime_elem)

  # Disabled friendly

  if soup_details.find('td', text = 'Akadálymentesített') is None:
    disabledfriendly_elem = 'nincs megadva'
  else:
    disabledfriendly_elem = soup_details.find('td', text = 'Akadálymentesített').findNext('td').text
  disabledfriendly.append(disabledfriendly_elem)

  # Bathroom

  if soup_details.find('td', text = 'Fürdő és WC') is None:
    bathroom_elem = 'nincs megadva'
  else:
    bathroom_elem = soup_details.find('td', text = 'Fürdő és WC').findNext('td').text
  bathroom.append(bathroom_elem)

  # Orientation

  if soup_details.find('td', text = 'Tájolás') is None:
    orientation_elem = 'nincs megadva'
  else:
    orientation_elem = soup_details.find('td', text = 'Tájolás').findNext('td').text
  orientation.append(orientation_elem)

  # View

  if soup_details.find('td', text = 'Kilátás') is None:
    view_elem = 'nincs megadva'
  else:
    view_elem = soup_details.find('td', text = 'Kilátás').findNext('td').text
  view.append(view_elem)

  # Garden

  if soup_details.find('td', text = 'Kertkapcsolatos') is None:
    garden_elem = 'nincs megadva'
  else:
    garden_elem = soup_details.find('td', text = 'Kertkapcsolatos').findNext('td').text
  garden.append(garden_elem)

  # Attic

  if soup_details.find('td', text = 'Tetőtér') is None:
    attic_elem = 'nincs megadva'
  else:
    attic_elem = soup_details.find('td', text = 'Tetőtér').findNext('td').text
  attic.append(attic_elem)

  # Mechanized

  if soup_details.find('td', text = 'Gépesített') is None:
    mechanized_elem = 'nincs megadva'
  else:
    mechanized_elem = soup_details.find('td', text = 'Gépesített').findNext('td').text
  mechanized.append(mechanized_elem)

  # Pet

  if soup_details.find('td', text = 'Kisállat') is None:
    pet_elem = 'nincs megadva'
  else:
    pet_elem = soup_details.find('td', text = 'Kisállat').findNext('td').text
  pet.append(pet_elem)

  # Smoking

  if soup_details.find('td', text = 'Dohányzás') is None:
    smoking_elem = 'nincs megadva'
  else:
    smoking_elem = soup_details.find('td', text = 'Dohányzás').findNext('td').text
  smoking.append(smoking_elem)
  # Parking

  if soup_details.find('td', text = 'Parkolás') is None:
    parking_elem = 'nincs megadva'
  else:
    parking_elem = soup_details.find('td', text = 'Parkolás').findNext('td').text
  parking.append(parking_elem)

scraped_details = pd.DataFrame({'id':ids,'spec':spec,'built':built,'comfort':comfort,'energycertificate':energycertificate,'floor':floor,'buildingfloors':buildingfloors,'lift':lift,'innerheight':innerheight,'heating':heating,'ac':ac,'furnished':furnished,'utilities':utilities,'moveintime':moveintime,'minrenttime':minrenttime,'disabledfriendly':disabledfriendly,'bathroom':bathroom,'orientation':orientation,'view':view,'garden':garden,'attic':attic,'mechanized':mechanized,'pet':pet,'smoking':smoking,'parking':parking})

scraped_datawithdetails = pd.merge(scraped_data,scraped_details, on='id')

scraped_datawithdetails
