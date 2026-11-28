# Generates the Holvi demo pages in site/demos/holvi/ (English), fi/ and sv/.
# The output is plain static HTML; this script is only a convenience for editing.
# Run:  python src/demos/holvi.py
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2] / "site" / "demos" / "holvi"
VER = "3"  # bump when CSS or JS changes, so browsers fetch the new files
LANGS = ["en", "fi", "sv"]
PAGES = ["index", "menu", "story", "visit"]

ARROW = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11M11 5.5 15.5 10 11 14.5" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'
MARK = '<svg viewBox="0 0 22 26" aria-hidden="true"><path d="M2 25V11a9 9 0 0 1 18 0v14M7 25V12a4 4 0 0 1 8 0v13" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>'

T = {
 "en": dict(
  name="English", skip="Skip to content", menu_btn="Menu", lang_label="Language",
  nav_menu="Menu", nav_story="The vault", nav_visit="Hours and directions", book="Book a table",
  t_index="Holvi | Wood-fire restaurant in Kruununhaka, Helsinki",
  d_index="Holvi cooks fish, rye and lamb over a birch fire in an 1888 granite cellar in Kruununhaka, Helsinki. A fictional restaurant, made as a portfolio demo.",
  t_menu="Menu | Holvi, Helsinki", d_menu="This week's menu at Holvi: fish, lamb and vegetables cooked over birch, in the embers or in smoke. Fictional restaurant, portfolio demo.",
  t_story="The vault | Holvi, Helsinki", d_story="The story of Holvi's 1888 granite cellar, its birch fire, and the producers it cooks from. Fictional restaurant, portfolio demo.",
  t_visit="Book a table | Holvi, Helsinki", d_visit="Book a table at Holvi, open Tuesday to Saturday from 17.00 in Kruununhaka, Helsinki. Fictional restaurant, portfolio demo.",
  h1=["Fish, rye and lamb", "cooked over birch,", "under a granite vault."],
  lead="Holvi seats 38 in an 1888 merchant&rsquo;s cellar in Kruununhaka. One wood fire, one short menu that follows the catch, and a kitchen you can see from every table.",
  read_menu="Read this week&rsquo;s menu", tonight="Open Tuesday to Saturday from 17.00.",
  alt_fire="A cook leaning over the open fire in a dark kitchen",
  plates_h="From the fire this week", plates_note="The menu changes every Tuesday, when the boats and the farms tell us what there is.",
  p1=("Whitefish over birch", "Siika, brown butter, pickled cucumber", "Whole fish, charred over the fire, on a black plate"),
  p2=("&Aring;land lamb shoulder", "Juniper, celeriac baked in the embers", "Lamb cooking on a grill above the embers"),
  p3=("Beef from Ruovesi", "Smoked bone sauce, charred onion", "A cook pouring sauce over a plated dish at the pass"),
  full_menu="See the full menu",
  vault_h="Four metres under Liisankatu",
  vault_p1="The cellar was cut in 1888 to keep a grain merchant&rsquo;s stock cool through the summer. The walls are local granite, the ceiling is three brick vaults, and the temperature down here barely moves all year.",
  vault_p2="We put the fire where the loading hatch used to be, so the smoke goes straight up and out, and the room smells of birch rather than of cooking.",
  facts=[("Seats", "38"), ("Fire", "Birch, all night"), ("Menu", "New every Tuesday")],
  vault_link="How the vault became a kitchen", alt_vault="The dining room under arched granite ceilings, lit by low lamps",
  close_h="Tables from 17.00, Tuesday to Saturday.",
  close_p="We keep six seats at the kitchen counter for walk-ins every night. For the rest of the room, booking is safest on Fridays and Saturdays.",
  addr_foot="Liisankatu, Kruununhaka, Helsinki<br>Tuesday to Saturday from 17.00",
  credit="Designed and built by Julius Nordman, JN Design.",
  fiction="Holvi is a fictional restaurant, made as a portfolio demo. The menu, prices and history are invented. The booking form sends nothing.",
  f_pages="Pages", f_photos="Photos on Unsplash",
  photos=["Cooking in the dark", "Arched stone dining room", "Fish on a black plate", "Grill over fire", "Sauce at the pass", "At the table", "Fire in the stove"],
  # menu
  menu_h1="This week&rsquo;s menu", menu_lead="Written every Tuesday. Everything meets the same birch fire, in one of four ways, so you can choose by that too.",
  legend="Show dishes cooked", f_all="Any way", fire=dict(flame="Over the flame", embers="In the embers", smoke="Smoked", raw="With no fire"),
  courses=["To start", "From the fire", "After"], empty="Nothing in this course is cooked that way this week.",
  menu_foot="Prices include VAT. Tell us about allergies when you book and we will cook around them; most dishes can be made without gluten or dairy.",
  tasting_label="Tasting menu", tasting_h="By the fire",
  tasting_p="Seven courses chosen by the kitchen on the night, served to the whole table. Ask for it when you book, by 17.00 on the day.",
  tasting_1="Seven courses", tasting_2="With paired wines", alt_grill="Meat cooking on a grill over open flames",
  # story
  story_h1="A grain cellar with a fire in it", story_lead="How a storeroom from 1888 became a kitchen, and where the food comes from.",
  alt_vault2="Guests at tables under the arched stone ceiling", alt_stove="Birch logs burning in an iron stove", alt_grill2="Meat on a grill above open flames", alt_table="A guest eating at a dark table",
  c1_h="The room was built to stay cold",
  c1_p1="A grain merchant had the cellar cut into the bedrock in 1888. Granite walls a metre thick, three brick vaults, one hatch to the street. Through the war it stored potatoes for the block. By the 1990s it held bicycles.",
  c1_p2="When we opened it up in 2023 we kept everything that was there and added one thing: a steel firebox where the hatch had been, with a flue that runs up the old shaft.",
  c2_h="One fire, four ways of cooking",
  c2_p1="The fire is lit at three in the afternoon and burns birch until close. Fish and steaks go over the flame. Roots and lamb sit in the embers for hours. Herring and cheese take the smoke. A few things never meet it at all, because raw is sometimes the best way.",
  c2_p2="There is no gas line in the kitchen. When the fire is low, the menu waits.",
  c3_h="Where it comes from",
  c3_p="Most of what we cook is caught or grown within a day&rsquo;s drive. We buy whole animals and whole fish, so the menu follows what each one gives.",
  producers=[("Lake Saimaa", "Vendace and pike-perch, by net"), ("The Kvarken", "Whitefish and Baltic herring"), ("&Aring;land", "Lamb, grazed on the outer islands"), ("Ruovesi", "Grass-fed beef"), ("Sipoo", "Roots, beets and apples")],
  story_close_h="Come down and sit by the fire.", story_close_p="Open Tuesday to Saturday from 17.00. Six counter seats are kept for walk-ins.",
  # visit
  visit_h1="Book a table", visit_lead="For up to six people. For seven or more, or for the whole vault, write to us and we will plan it together.",
  your_table="Your table", l_date="Date", h_date="Tuesday to Saturday", l_time="Time", o_time="Choose a time",
  l_guests="Guests", o_guests="How many?", guest1="guest", guestN="guests", l_name="Name", l_email="Email", ph_email="name@example.com",
  l_notes="Allergies or anything we should know", optional="(optional)", submit="Request the table", demo_note="This is a demo. Nothing is sent.",
  done_h="Your request is in", done_p="In a real booking we would confirm by email within the hour. This demo sends nothing.",
  side_label="Hours and directions", hours_h="Opening hours", hours_cap="Opening hours, kitchen closes one hour earlier",
  days=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], closed="Closed",
  span=lambda a, b: f"{a} to {b}", kitchen_note="The kitchen takes its last orders an hour before we close.",
  find_h="Finding us", address="Holvi<br>Liisankatu, Kruununhaka<br>Helsinki",
  find_p="Ten minutes&rsquo; walk north-east of the Cathedral. Look for the iron door down six granite steps. The vault has no lift; tell us if stairs are hard and we will help you down.",
 ),
 "fi": dict(
  name="Suomi", skip="Siirry sisältöön", menu_btn="Valikko", lang_label="Kieli",
  nav_menu="Ruokalista", nav_story="Kellari", nav_visit="Aukioloajat ja sijainti", book="Varaa pöytä",
  t_index="Holvi | Avotuliravintola Kruununhaassa, Helsingissä",
  d_index="Holvi kokkaa kalaa, ruista ja lammasta koivutulella vuoden 1888 graniittikellarissa Kruununhaassa. Kuvitteellinen ravintola, tehty portfoliodemoksi.",
  t_menu="Ruokalista | Holvi, Helsinki", d_menu="Holvin tämän viikon ruokalista: kalaa, lammasta ja kasviksia koivun liekeillä, hiilloksessa tai savussa. Kuvitteellinen ravintola, portfoliodemo.",
  t_story="Kellari | Holvi, Helsinki", d_story="Tarina Holvin vuoden 1888 graniittikellarista, sen koivutulesta ja tuottajista. Kuvitteellinen ravintola, portfoliodemo.",
  t_visit="Varaa pöytä | Holvi, Helsinki", d_visit="Varaa pöytä Holvista, avoinna tiistaista lauantaihin klo 17.00 alkaen Kruununhaassa. Kuvitteellinen ravintola, portfoliodemo.",
  h1=["Kalaa, ruista ja lammasta", "koivun liekeillä,", "graniittiholvin alla."],
  lead="Holvissa on 38 paikkaa vuonna 1888 louhitussa kauppiaan kellarissa Kruununhaassa. Yksi puutuli, lyhyt saaliin mukaan elävä ruokalista ja keittiö, joka näkyy jokaiseen pöytään.",
  read_menu="Lue tämän viikon ruokalista", tonight="Avoinna tiistaista lauantaihin klo 17.00 alkaen.",
  alt_fire="Kokki kumartuu avotulen ylle pimeässä keittiössä",
  plates_h="Tällä viikolla tulelta", plates_note="Ruokalista vaihtuu joka tiistai sen mukaan, mitä veneet ja tilat tuovat.",
  p1=("Siikaa koivun liekeillä", "Ruskistettua voita, suolakurkkua", "Kokonainen kala hiillostettuna mustalla lautasella"),
  p2=("Ahvenanmaan lampaanlapa", "Katajaa, hiilloksessa paahdettua juuriselleriä", "Lihaa grillissä hiillosten yllä"),
  p3=("Ruoveden naudanlihaa", "Savustettu luukastike, hiillostettu sipuli", "Kokki kaataa kastiketta annokselle"),
  full_menu="Katso koko ruokalista",
  vault_h="Neljä metriä Liisankadun alla",
  vault_p1="Kellari louhittiin vuonna 1888 viljakauppiaan varastoksi, joka pysyi viileänä kesänkin yli. Seinät ovat paikallista graniittia, katossa on kolme tiiliholvia, eikä lämpötila täällä alhaalla juuri vaihtele vuoden aikana.",
  vault_p2="Tuli on paikassa, jossa ennen oli lastausluukku, joten savu nousee suoraan ylös ja ulos, ja sali tuoksuu koivulta eikä ruoanlaitolta.",
  facts=[("Paikkoja", "38"), ("Tuli", "Koivua koko illan"), ("Ruokalista", "Uusi joka tiistai")],
  vault_link="Näin holvista tuli keittiö", alt_vault="Ruokasali graniittiholvien alla, valaistuna matalilla lampuilla",
  close_h="Pöytiä klo 17.00 alkaen, tiistaista lauantaihin.",
  close_p="Pidämme joka ilta kuusi keittiötiskin paikkaa vapaana ilman varausta tuleville. Muualle saliin varaus on varminta perjantaisin ja lauantaisin.",
  addr_foot="Liisankatu, Kruununhaka, Helsinki<br>Tiistaista lauantaihin klo 17.00 alkaen",
  credit="Suunnitellut ja toteuttanut Julius Nordman, JN Design.",
  fiction="Holvi on kuvitteellinen ravintola, tehty portfoliodemoksi. Ruokalista, hinnat ja historia ovat keksittyjä. Varauslomake ei lähetä mitään.",
  f_pages="Sivut", f_photos="Kuvat Unsplashista",
  photos=["Ruoanlaittoa pimeässä", "Kiviholvinen ruokasali", "Kala mustalla lautasella", "Grilli tulen päällä", "Kastike annokselle", "Pöydän ääressä", "Tuli kamiinassa"],
  menu_h1="Tämän viikon ruokalista", menu_lead="Kirjoitetaan joka tiistai. Kaikki kohtaa saman koivutulen yhdellä neljästä tavasta, joten voit valita senkin mukaan.",
  legend="Näytä annokset, jotka on kypsennetty", f_all="Kaikki", fire=dict(flame="Liekeillä", embers="Hiilloksessa", smoke="Savustettuna", raw="Ilman tulta"),
  courses=["Aluksi", "Tulelta", "Lopuksi"], empty="Tämän osion annoksia ei tällä viikolla kypsennetä näin.",
  menu_foot="Hinnat sisältävät arvonlisäveron. Kerro allergioista varauksen yhteydessä, niin kokkaamme niiden mukaan; useimmat annokset voi tehdä gluteenittomina tai maidottomina.",
  tasting_label="Maistelumenu", tasting_h="Tulen ääressä",
  tasting_p="Seitsemän ruokalajia keittiön valitsemana illan mukaan, koko pöydälle. Pyydä sitä varatessasi, viimeistään klo 17.00 samana päivänä.",
  tasting_1="Seitsemän ruokalajia", tasting_2="Viinipaketin kanssa", alt_grill="Lihaa grillissä avoimen tulen yllä",
  story_h1="Viljakellari, jossa palaa tuli", story_lead="Miten vuoden 1888 varastohuoneesta tuli keittiö, ja mistä ruoka tulee.",
  alt_vault2="Ruokailijoita pöydissä kivisen holvikaton alla", alt_stove="Koivuhalkoja palamassa rautakamiinassa", alt_grill2="Lihaa grillissä avotulen yllä", alt_table="Ruokailija pimeän pöydän ääressä",
  c1_h="Huone rakennettiin pysymään kylmänä",
  c1_p1="Viljakauppias louhitutti kellarin kallioon vuonna 1888. Metrin paksuiset graniittiseinät, kolme tiiliholvia, yksi luukku kadulle. Sodan aikana siellä säilytettiin korttelin perunat. 1990-luvulla siellä seisoivat polkupyörät.",
  c1_p2="Kun avasimme sen vuonna 2023, säilytimme kaiken, mitä siellä oli, ja lisäsimme yhden asian: teräksisen tulipesän entisen luukun paikalle ja hormin, joka nousee vanhaa kuilua pitkin.",
  c2_h="Yksi tuli, neljä tapaa kokata",
  c2_p1="Tuli sytytetään kolmelta iltapäivällä, ja koivu palaa sulkemiseen asti. Kala ja pihvit menevät liekkien päälle. Juurekset ja lammas viipyvät hiilloksessa tunteja. Silakka ja juusto saavat savun. Muutama asia ei kohtaa tulta lainkaan, koska joskus raakana on parasta.",
  c2_p2="Keittiössä ei ole kaasua. Kun tuli on matalalla, ruokalista odottaa.",
  c3_h="Mistä ruoka tulee",
  c3_p="Suurin osa ruoasta on pyydetty tai kasvatettu päivän ajomatkan päässä. Ostamme kokonaisia eläimiä ja kokonaisia kaloja, joten ruokalista seuraa sitä, mitä kukin antaa.",
  producers=[("Saimaa", "Muikkua ja kuhaa, verkolla"), ("Merenkurkku", "Siikaa ja silakkaa"), ("Ahvenanmaa", "Lammasta ulkosaarten laitumilta"), ("Ruovesi", "Laiduntanutta naudanlihaa"), ("Sipoo", "Juureksia, punajuurta ja omenoita")],
  story_close_h="Tule alas istumaan tulen ääreen.", story_close_p="Avoinna tiistaista lauantaihin klo 17.00 alkaen. Kuusi tiskipaikkaa pidetään vapaana ilman varausta tuleville.",
  visit_h1="Varaa pöytä", visit_lead="Enintään kuudelle. Jos teitä on seitsemän tai enemmän, tai haluat koko holvin, kirjoita meille, niin suunnitellaan yhdessä.",
  your_table="Pöytäsi", l_date="Päivä", h_date="Tiistaista lauantaihin", l_time="Aika", o_time="Valitse aika",
  l_guests="Vieraita", o_guests="Kuinka monta?", guest1="vieras", guestN="vierasta", l_name="Nimi", l_email="Sähköposti", ph_email="nimi@example.com",
  l_notes="Allergiat tai muuta, mitä meidän pitäisi tietää", optional="(valinnainen)", submit="Lähetä pöytäpyyntö", demo_note="Tämä on demo. Mitään ei lähetetä.",
  done_h="Pyyntösi on vastaanotettu", done_p="Oikeassa varauksessa vahvistaisimme sen sähköpostilla tunnin sisällä. Tämä demo ei lähetä mitään.",
  side_label="Aukioloajat ja sijainti", hours_h="Aukioloajat", hours_cap="Aukioloajat, keittiö sulkeutuu tuntia aiemmin",
  days=["Sunnuntai", "Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai"], closed="Suljettu",
  span=lambda a, b: f"{a}–{b}", kitchen_note="Keittiö ottaa viimeiset tilaukset tuntia ennen sulkemista.",
  find_h="Näin löydät meille", address="Holvi<br>Liisankatu, Kruununhaka<br>Helsinki",
  find_p="Kymmenen minuutin kävely Tuomiokirkolta koilliseen. Etsi rautaovi kuuden graniittiportaan alta. Holvissa ei ole hissiä; kerro, jos portaat ovat hankalia, niin autamme sinut alas.",
 ),
 "sv": dict(
  name="Svenska", skip="Hoppa till innehållet", menu_btn="Meny", lang_label="Språk",
  nav_menu="Meny", nav_story="Källaren", nav_visit="Öppettider och hitta hit", book="Boka bord",
  t_index="Holvi | Restaurang med öppen eld i Kronohagen, Helsingfors",
  d_index="Holvi lagar fisk, råg och lamm över björkeld i en granitkällare från 1888 i Kronohagen, Helsingfors. En påhittad restaurang, gjord som portfoliodemo.",
  t_menu="Meny | Holvi, Helsingfors", d_menu="Veckans meny på Holvi: fisk, lamm och grönsaker över björkeld, i glöden eller i rök. Påhittad restaurang, portfoliodemo.",
  t_story="Källaren | Holvi, Helsingfors", d_story="Historien om Holvis granitkällare från 1888, dess björkeld och producenterna. Påhittad restaurang, portfoliodemo.",
  t_visit="Boka bord | Holvi, Helsingfors", d_visit="Boka bord på Holvi, öppet tisdag till lördag från 17.00 i Kronohagen, Helsingfors. Påhittad restaurang, portfoliodemo.",
  h1=["Fisk, råg och lamm", "lagat över björkeld,", "under ett granitvalv."],
  lead="Holvi har 38 platser i en köpmans källare från 1888 i Kronohagen. En vedeld, en kort meny som följer fångsten och ett kök som syns från varje bord.",
  read_menu="Läs veckans meny", tonight="Öppet tisdag till lördag från 17.00.",
  alt_fire="En kock lutar sig över den öppna elden i ett mörkt kök",
  plates_h="Från elden den här veckan", plates_note="Menyn byts varje tisdag efter vad båtarna och gårdarna har att ge.",
  p1=("Sik över björkeld", "Brynt smör, inlagd gurka", "Hel fisk, grillad över elden, på ett svart fat"),
  p2=("Åländsk lammbog", "En, rotselleri bakad i glöden", "Kött på grillen över glöden"),
  p3=("Nötkött från Ruovesi", "Rökt bensås, grillad lök", "En kock häller sås över en tallrik"),
  full_menu="Se hela menyn",
  vault_h="Fyra meter under Elisabetsgatan",
  vault_p1="Källaren höggs ut 1888 för att hålla en spannmålshandlares lager svalt genom sommaren. Väggarna är av lokal granit, taket består av tre tegelvalv och temperaturen här nere ändras knappt under året.",
  vault_p2="Elden står där lastluckan förr fanns, så röken går rakt upp och ut, och rummet doftar björk snarare än matos.",
  facts=[("Platser", "38"), ("Eld", "Björk hela kvällen"), ("Meny", "Ny varje tisdag")],
  vault_link="Så blev valvet ett kök", alt_vault="Matsalen under valv av granit, upplyst av låga lampor",
  close_h="Bord från 17.00, tisdag till lördag.",
  close_p="Vi håller sex platser vid köksdisken lediga för gäster utan bokning varje kväll. För resten av rummet är det säkrast att boka på fredagar och lördagar.",
  addr_foot="Elisabetsgatan, Kronohagen, Helsingfors<br>Tisdag till lördag från 17.00",
  credit="Designad och byggd av Julius Nordman, JN Design.",
  fiction="Holvi är en påhittad restaurang, gjord som portfoliodemo. Menyn, priserna och historien är uppdiktade. Bokningsformuläret skickar ingenting.",
  f_pages="Sidor", f_photos="Foton från Unsplash",
  photos=["Matlagning i mörkret", "Matsal med stenvalv", "Fisk på svart fat", "Grill över eld", "Sås vid passet", "Vid bordet", "Eld i kaminen"],
  menu_h1="Veckans meny", menu_lead="Skrivs varje tisdag. Allt möter samma björkeld på ett av fyra sätt, så du kan välja efter det också.",
  legend="Visa rätter som tillagas", f_all="Alla", fire=dict(flame="Över lågan", embers="I glöden", smoke="Rökt", raw="Utan eld"),
  courses=["Till att börja", "Från elden", "Efteråt"], empty="Inget i den här delen tillagas så den här veckan.",
  menu_foot="Priserna inkluderar moms. Berätta om allergier när du bokar så lagar vi maten efter dem; de flesta rätter kan göras utan gluten eller mjölk.",
  tasting_label="Avsmakningsmeny", tasting_h="Vid elden",
  tasting_p="Sju rätter som köket väljer för kvällen, serverade till hela bordet. Be om den när du bokar, senast 17.00 samma dag.",
  tasting_1="Sju rätter", tasting_2="Med vinpaket", alt_grill="Kött på grillen över öppen eld",
  story_h1="En spannmålskällare med en eld i", story_lead="Hur ett förråd från 1888 blev ett kök, och var maten kommer ifrån.",
  alt_vault2="Gäster vid borden under det välvda stentaket", alt_stove="Björkved som brinner i en järnkamin", alt_grill2="Kött på grillen över öppen eld", alt_table="En gäst som äter vid ett mörkt bord",
  c1_h="Rummet byggdes för att hålla sig kallt",
  c1_p1="En spannmålshandlare lät hugga ut källaren i berget 1888. Meterstjocka granitväggar, tre tegelvalv, en lucka mot gatan. Under kriget förvarade kvarteret sin potatis där. På 1990-talet stod cyklarna där.",
  c1_p2="När vi öppnade den 2023 behöll vi allt som fanns där och lade till en sak: en eldstad av stål där luckan hade suttit, med en rökkanal som går upp genom det gamla schaktet.",
  c2_h="En eld, fyra sätt att laga mat",
  c2_p1="Elden tänds klockan tre på eftermiddagen och björken brinner tills vi stänger. Fisk och biffar går över lågan. Rotfrukter och lamm ligger i glöden i timmar. Strömming och ost får röken. Några saker möter den aldrig, eftersom rått ibland är bäst.",
  c2_p2="Det finns ingen gas i köket. När elden är låg får menyn vänta.",
  c3_h="Var maten kommer ifrån",
  c3_p="Det mesta vi lagar är fångat eller odlat inom en dags bilresa. Vi köper hela djur och hela fiskar, så menyn följer vad var och en ger.",
  producers=[("Saimen", "Siklöja och gös, med nät"), ("Kvarken", "Sik och strömming"), ("Åland", "Lamm som betat i ytterskärgården"), ("Ruovesi", "Gräsbetat nötkött"), ("Sibbo", "Rotfrukter, rödbetor och äpplen")],
  story_close_h="Kom ner och sätt dig vid elden.", story_close_p="Öppet tisdag till lördag från 17.00. Sex platser vid disken hålls lediga för gäster utan bokning.",
  visit_h1="Boka bord", visit_lead="För upp till sex personer. För sju eller fler, eller hela valvet, skriv till oss så planerar vi det tillsammans.",
  your_table="Ditt bord", l_date="Datum", h_date="Tisdag till lördag", l_time="Tid", o_time="Välj en tid",
  l_guests="Gäster", o_guests="Hur många?", guest1="gäst", guestN="gäster", l_name="Namn", l_email="E-post", ph_email="namn@example.com",
  l_notes="Allergier eller annat vi borde veta", optional="(valfritt)", submit="Skicka bordsförfrågan", demo_note="Det här är en demo. Inget skickas.",
  done_h="Din förfrågan är mottagen", done_p="I en riktig bokning skulle vi bekräfta via e-post inom en timme. Den här demon skickar ingenting.",
  side_label="Öppettider och hitta hit", hours_h="Öppettider", hours_cap="Öppettider, köket stänger en timme tidigare",
  days=["Söndag", "Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag"], closed="Stängt",
  span=lambda a, b: f"{a}–{b}", kitchen_note="Köket tar sista beställningarna en timme innan vi stänger.",
  find_h="Hitta hit", address="Holvi<br>Elisabetsgatan, Kronohagen<br>Helsingfors",
  find_p="Tio minuters promenad nordost om Domkyrkan. Leta efter järndörren sex granittrappsteg ner. Valvet har ingen hiss; säg till om trappor är svåra så hjälper vi dig ner.",
 ),
}

# (fire, price, {lang: (name, finnish-subname-or-None, description)})
COURSES = [
 [
  ("smoke", "6", dict(en=("Rye bread and cultured butter", "Ruisleipä", "Baked here each morning, served warm with cultured butter and flaky salt."),
                      fi=("Ruisleipä ja hapatettu voi", None, "Leivotaan täällä joka aamu ja tarjoillaan lämpimänä hapatetun voin ja hiutalesuolan kanssa."),
                      sv=("Rågbröd och syrat smör", "Ruisleipä", "Bakas här varje morgon och serveras varmt med syrat smör och flingsalt."))),
  ("smoke", "14", dict(en=("Hot-smoked Baltic herring", "Savusilakka", "Smoked over alder at the table, with egg butter and potato crisps."),
                       fi=("Savusilakat", None, "Savustetaan lepällä pöydässä, munavoin ja perunalastujen kanssa."),
                       sv=("Varmrökt strömming", "Savusilakka", "Röks över al vid bordet, med äggsmör och potatischips."))),
  ("flame", "16", dict(en=("Vendace fried in rye flour", "Muikut", "Small lake fish from Saimaa, eaten whole, with lemon and garlic mayonnaise."),
                       fi=("Ruisjauhoissa paistetut muikut", None, "Pieniä Saimaan järvikaloja, syödään kokonaisina, sitruunan ja valkosipulimajoneesin kanssa."),
                       sv=("Siklöja stekt i rågmjöl", "Muikut", "Små insjöfiskar från Saimen, äts hela, med citron och vitlöksmajonnäs."))),
  ("embers", "15", dict(en=("Beetroot baked in the coals", "Hiillostettu punajuuri", "Smoked curd, toasted rye crumbs, dill oil."),
                        fi=("Hiilloksessa paahdettu punajuuri", None, "Savurahkaa, paahdettua ruismurua, tilliöljyä."),
                        sv=("Rödbeta bakad i glöden", "Hiillostettu punajuuri", "Rökt kvarg, rostade rågsmulor, dillolja."))),
  ("raw", "17", dict(en=("Pike-perch, cured", "Graavattu kuha", "Cured in salt and spruce tips, with cucumber and horseradish cream."),
                     fi=("Graavattu kuha", None, "Graavattu suolassa ja kuusenkerkissä, kurkun ja piparjuurikerman kanssa."),
                     sv=("Gravad gös", "Graavattu kuha", "Gravad i salt och granskott, med gurka och pepparrotskräm."))),
 ],
 [
  ("flame", "32", dict(en=("Whitefish over birch", "Siika", "Cooked on the bone, with brown butter, pickled cucumber and new potatoes."),
                       fi=("Siikaa koivun liekeillä", None, "Kypsennetään ruodoillaan, ruskistetun voin, suolakurkun ja uusien perunoiden kanssa."),
                       sv=("Sik över björkeld", "Siika", "Tillagas på benet, med brynt smör, inlagd gurka och färskpotatis."))),
  ("embers", "36", dict(en=("&Aring;land lamb shoulder", "Lampaanlapa", "Slow-cooked overnight beside the fire, juniper, celeriac baked in the embers."),
                        fi=("Ahvenanmaan lampaanlapa", None, "Haudutetaan yön yli tulen vieressä, katajaa, hiilloksessa paahdettua juuriselleriä."),
                        sv=("Åländsk lammbog", "Lampaanlapa", "Långkokt över natten bredvid elden, en, rotselleri bakad i glöden."))),
  ("flame", "38", dict(en=("Beef from Ruovesi", "Naudan entrecôte", "Grass-fed, aged four weeks, with smoked bone sauce and charred onion."),
                       fi=("Ruoveden naudan entrecôte", None, "Laiduntanutta, neljä viikkoa kypsytettyä, savustetun luukastikkeen ja hiillostetun sipulin kanssa."),
                       sv=("Entrecôte från Ruovesi", "Naudan entrecôte", "Betesdjur, mörat i fyra veckor, med rökt bensås och grillad lök."))),
  ("embers", "27", dict(en=("Celeriac steak", "Juuriselleri", "Whole root cooked in the ashes, brown butter, hazelnuts, pickled chanterelles."),
                        fi=("Juuriselleripihvi", None, "Kokonainen juuri kypsennettynä tuhkassa, ruskistettua voita, hasselpähkinöitä, säilöttyjä kantarelleja."),
                        sv=("Rotselleristek", "Juuriselleri", "Hel rot tillagad i askan, brynt smör, hasselnötter, inlagda kantareller."))),
 ],
 [
  ("raw", "12", dict(en=("Buttermilk pudding", "Piimävanukas", "Sea buckthorn and toasted oats."),
                     fi=("Piimävanukas", None, "Tyrniä ja paahdettua kauraa."),
                     sv=("Kärnmjölkspudding", "Piimävanukas", "Havtorn och rostad havre."))),
  ("embers", "12", dict(en=("Ember-roasted apple", "Hiillostettu omena", "Rye ice cream and burnt honey."),
                        fi=("Hiilloksessa paahdettu omena", None, "Ruisjäätelöä ja poltettua hunajaa."),
                        sv=("Äpple rostat i glöden", "Hiillostettu omena", "Rågglass och bränd honung."))),
  ("smoke", "13", dict(en=("Cheese from Lapland", "Leipäjuusto", "Warmed by the fire, with cloudberry jam."),
                       fi=("Leipäjuusto", None, "Lämmitetty tulen ääressä, lakkahillon kanssa."),
                       sv=("Lappländsk brödost", "Leipäjuusto", "Värmd vid elden, med hjortronsylt."))),
 ],
]

PHOTO_URLS = [
 "https://unsplash.com/photos/a-person-cooking-food-on-a-grill-in-the-dark-JKJmdRDfPfk",
 "https://unsplash.com/photos/people-dining-in-a-restaurant-with-arched-stone-ceilings-NyWkEHSVLx0",
 "https://unsplash.com/photos/fried-fish-on-black-round-plate-_o5mOJ3lOCA",
 "https://unsplash.com/photos/person-cooking-on-grill-with-fire-Aqot8S_Keb8",
 "https://unsplash.com/photos/chef-pouring-sauce-over-plated-steak-MaWMfm-HCqQ",
 "https://unsplash.com/photos/person-holding-stainless-steel-spoon-and-fork-eating-on-black-table--g5jWce3HUQ",
 "https://unsplash.com/photos/a-close-up-of-a-fire-burning-in-a-stove-hwMmAIMOzxU",
]


def build(lang):
    s = T[lang]
    up = "" if lang == "en" else "../"            # path back to the demo root
    out = ROOT if lang == "en" else ROOT / lang
    out.mkdir(parents=True, exist_ok=True)

    def img(name, alt, sizes, w, h, eager=False):
        load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
        return (f'<img src="{up}assets/img/{name}-1800.jpg" srcset="{up}assets/img/{name}-900.jpg 900w, {up}assets/img/{name}-1800.jpg 1800w" '
                f'sizes="{sizes}" width="{w}" height="{h}" alt="{alt}" {load}>')

    def href(target_lang, page):
        here = "" if lang == "en" else "../"
        there = "" if target_lang == "en" else f"{target_lang}/"
        return f"{here}{there}{page}.html"

    def page(slug, body):
        cur = lambda p: ' aria-current="page"' if p == slug else ''
        alts = "\n".join(f'  <link rel="alternate" hreflang="{l}" href="https://jnwebdesign.com/demos/holvi/{"" if l == "en" else l + "/"}{"" if slug == "index" else slug + ".html"}">' for l in LANGS)
        switch = "".join(
            f'<a href="{href(l, slug)}" lang="{l}" hreflang="{l}" aria-label="{T[l]["name"]}"{" aria-current=\"true\"" if l == lang else ""}>{l.upper()}</a>'
            for l in LANGS)
        preload = (f'<link rel="preload" as="image" href="{up}assets/img/fire-1800.jpg" '
                   f'imagesrcset="{up}assets/img/fire-900.jpg 900w, {up}assets/img/fire-1800.jpg 1800w" imagesizes="(max-width: 960px) 100vw, 45vw">'
                   if slug == "index" else "")
        photos = "\n".join(f'          <li><a href="{u}">{t}</a></li>' for u, t in zip(PHOTO_URLS, s["photos"]))
        html = f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{s["t_" + slug]}</title>
  <meta name="description" content="{s["d_" + slug]}">
  <meta name="author" content="Julius Nordman, JN Design">
  <meta name="theme-color" content="#13110f">
{alts}
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 22 26'%3E%3Crect width='22' height='26' fill='%2313110f'/%3E%3Cpath d='M2 25V11a9 9 0 0 1 18 0v14M7 25V12a4 4 0 0 1 8 0v13' fill='none' stroke='%239db3a4' stroke-width='1.8'/%3E%3C/svg%3E">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@400..700&display=swap">
  <link rel="stylesheet" href="{up}assets/vendor/lenis.css">
  <link rel="stylesheet" href="{up}assets/css/style.css?v={VER}">
  {preload}
  <script>
    /* Respect reduced motion. Add ?motion=1 to the URL to force animation on for a demo (kept for this tab). */
    (function (root) {{
      var force = /[?&]motion=1\\b/.test(location.search);
      try {{
        if (force) sessionStorage.setItem('holvi-motion', '1');
        else force = sessionStorage.getItem('holvi-motion') === '1';
      }} catch (e) {{}}
      if (force) root.classList.add('force-motion');
      var reduce = !force && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      if (reduce) {{ root.classList.add('reduce-motion'); return; }}
      root.classList.add('intro');
      setTimeout(function () {{ root.classList.remove('intro'); }}, 3000);
    }})(document.documentElement);
  </script>
</head>
<body>
  <a class="skip-link" href="#main">{s["skip"]}</a>

  <header class="site-header">
    <div class="wrap site-header__inner">
      <a class="wordmark" href="index.html" aria-label="Holvi">{MARK}Holvi</a>
      <nav id="site-nav" class="site-nav" aria-label="{s["menu_btn"]}">
        <ul>
          <li><a href="menu.html"{cur("menu")}>{s["nav_menu"]}</a></li>
          <li><a href="story.html"{cur("story")}>{s["nav_story"]}</a></li>
          <li><a href="visit.html"{cur("visit")}>{s["nav_visit"]}</a></li>
          <li class="site-nav__book"><a href="visit.html#book">{s["book"]}</a></li>
        </ul>
      </nav>
      <nav class="lang" aria-label="{s["lang_label"]}">{switch}</nav>
      <a class="btn btn--solid btn--small site-header__cta" href="visit.html#book">{s["book"]}</a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
        <span class="menu-toggle__bars" aria-hidden="true"></span>
        <span class="visually-hidden">{s["menu_btn"]}</span>
      </button>
    </div>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer">
    <div class="wrap site-footer__grid">
      <div class="site-footer__brand">
        <a class="wordmark" href="index.html">{MARK}Holvi</a>
        <p>{s["addr_foot"]}</p>
        <p class="site-footer__credit">{s["credit"]}</p>
        <p>{s["fiction"]}</p>
      </div>
      <div>
        <h2>{s["f_pages"]}</h2>
        <ul>
          <li><a href="menu.html">{s["nav_menu"]}</a></li>
          <li><a href="story.html">{s["nav_story"]}</a></li>
          <li><a href="visit.html">{s["nav_visit"]}</a></li>
          <li><a href="visit.html#book">{s["book"]}</a></li>
        </ul>
      </div>
      <div>
        <h2>{s["f_photos"]}</h2>
        <ul>
{photos}
        </ul>
      </div>
    </div>
  </footer>

  <script src="{up}assets/vendor/gsap.min.js" defer></script>
  <script src="{up}assets/vendor/ScrollTrigger.min.js" defer></script>
  <script src="{up}assets/vendor/lenis.min.js" defer></script>
  <script src="{up}assets/js/main.js?v={VER}" defer></script>
</body>
</html>
'''
        (out / f"{slug}.html").write_text(html, encoding="utf-8", newline="\n")

    # ---- Home
    lines = "\n".join(f'            <span class="hero__line"><span>{l}</span></span>' for l in s["h1"])
    def plate(key, photo, w, h):
        n, sub, alt = s[key]
        return f'''          <li class="plate">
            <div class="arch">{img(photo, alt, "(max-width: 640px) 100vw, 30vw", w, h)}</div>
            <div class="plate__body">
              <h3 class="plate__name">{n}</h3>
              <span class="plate__price">{ {"p1": "32", "p2": "36", "p3": "38"}[key] } &euro;</span>
              <p class="plate__fi">{sub}</p>
            </div>
          </li>'''
    facts = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in s["facts"])
    page("index", f'''    <section class="hero" aria-labelledby="hero-title">
      <div class="wrap hero__grid">
        <div class="hero__text">
          <h1 id="hero-title" class="hero__title">
{lines}
          </h1>
          <p class="hero__lead">{s["lead"]}</p>
          <div class="hero__actions">
            <a class="btn btn--solid" href="visit.html#book">{s["book"]} {ARROW}</a>
            <a class="text-link" href="menu.html">{s["read_menu"]}</a>
          </div>
          <p class="tonight" data-tonight data-state="closed" aria-live="polite">
            <span class="tonight__dot" aria-hidden="true"></span>
            <span data-tonight-text>{s["tonight"]}</span>
          </p>
        </div>
        <div class="hero__media">
          <div class="arch hero__arch">
            {img("fire", s["alt_fire"], "(max-width: 960px) 100vw, 45vw", 1800, 2250, eager=True)}
          </div>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="plates-title">
      <div class="wrap">
        <div class="section__head">
          <h2 id="plates-title" class="section__title">{s["plates_h"]}</h2>
          <p class="section__note">{s["plates_note"]}</p>
        </div>
        <ul class="plates">
{plate("p1", "fish", 1800, 2250)}
{plate("p2", "grill", 1800, 2710)}
{plate("p3", "sauce", 1800, 1800)}
        </ul>
        <p class="section__more"><a class="text-link" href="menu.html">{s["full_menu"]} {ARROW}</a></p>
      </div>
    </section>

    <section class="section" aria-labelledby="vault-title" style="padding-top:0">
      <div class="wrap vault">
        <div class="arch">{img("vault", s["alt_vault"], "(max-width: 960px) 100vw, 40vw", 1800, 2700)}</div>
        <div class="vault__text">
          <h2 id="vault-title">{s["vault_h"]}</h2>
          <p>{s["vault_p1"]}</p>
          <p>{s["vault_p2"]}</p>
          <dl class="facts">{facts}</dl>
          <a class="text-link" href="story.html">{s["vault_link"]} {ARROW}</a>
        </div>
      </div>
    </section>

    <section class="close on-lime" aria-labelledby="close-title">
      <div class="wrap close__grid">
        <h2 id="close-title">{s["close_h"]}</h2>
        <div>
          <p>{s["close_p"]}</p>
          <a class="btn btn--solid" href="visit.html#book">{s["book"]} {ARROW}</a>
        </div>
      </div>
    </section>''')

    # ---- Menu
    courses = []
    for title, dishes in zip(s["courses"], COURSES):
        rows = []
        for fire, price, names in dishes:
            n, sub, desc = names[lang]
            sub_html = f' <span class="dish__fi" lang="fi">{sub}</span>' if sub else ""
            rows.append(f'''              <li class="dish" data-fire="{fire}">
                <h3 class="dish__name">{n}{sub_html}</h3>
                <span class="dish__price">{price} &euro;</span>
                <p class="dish__desc">{desc}</p>
                <span class="dish__fire">{s["fire"][fire]}</span>
              </li>''')
        courses.append(f'''          <section class="course" aria-label="{title}">
            <h2 class="course__title">{title}</h2>
            <ul class="dishes">
{chr(10).join(rows)}
            </ul>
            <p class="menu-empty" hidden>{s["empty"]}</p>
          </section>''')
    buttons = f'<button type="button" data-fire="all" aria-pressed="true">{s["f_all"]}</button>' + "".join(
        f'\n          <button type="button" data-fire="{k}" aria-pressed="false">{s["fire"][k]}</button>' for k in ["flame", "embers", "smoke", "raw"])
    page("menu", f'''    <div class="on-lime menu-page">
      <section class="page-head">
        <div class="wrap">
          <h1 class="page-title">{s["menu_h1"]}</h1>
          <p class="page-lead">{s["menu_lead"]}</p>
        </div>
      </section>
      <div class="wrap">
        <fieldset class="fire-filter" data-fire-filter>
          <legend>{s["legend"]}</legend>
          {buttons}
        </fieldset>
        <p class="visually-hidden" data-filter-status aria-live="polite"></p>
        <div class="menu-layout">
          <div>
{chr(10).join(courses)}
            <p class="menu-foot">{s["menu_foot"]}</p>
          </div>
          <aside class="menu-side" aria-label="{s["tasting_label"]}">
            <div class="arch">{img("grill", s["alt_grill"], "(max-width: 960px) 45vw, 30vw", 1800, 2710)}</div>
            <div class="tasting">
              <h2>{s["tasting_h"]}</h2>
              <p>{s["tasting_p"]}</p>
              <div class="tasting__price"><span>{s["tasting_1"]}</span><strong>79 &euro;</strong></div>
              <div class="tasting__price"><span>{s["tasting_2"]}</span><strong>139 &euro;</strong></div>
            </div>
          </aside>
        </div>
      </div>
    </div>''')

    # ---- Story
    producers = "\n".join(f"            <li><strong>{a}</strong><span>{b}</span></li>" for a, b in s["producers"])
    page("story", f'''    <section class="page-head">
      <div class="wrap">
        <h1 class="page-title">{s["story_h1"]}</h1>
        <p class="page-lead">{s["story_lead"]}</p>
      </div>
    </section>

    <div class="wrap">
      <div class="wide-photo">{img("vault", s["alt_vault2"], "100vw", 1800, 2700)}</div>

      <section class="chapter" aria-labelledby="c1">
        <div class="chapter__media"><div class="arch">{img("stove", s["alt_stove"], "(max-width: 960px) 100vw, 40vw", 1800, 1200)}</div></div>
        <div>
          <h2 id="c1">{s["c1_h"]}</h2>
          <p>{s["c1_p1"]}</p>
          <p>{s["c1_p2"]}</p>
        </div>
      </section>

      <section class="chapter chapter--flip" aria-labelledby="c2">
        <div class="chapter__media"><div class="arch">{img("grill", s["alt_grill2"], "(max-width: 960px) 100vw, 40vw", 1800, 2710)}</div></div>
        <div>
          <h2 id="c2">{s["c2_h"]}</h2>
          <p>{s["c2_p1"]}</p>
          <p>{s["c2_p2"]}</p>
        </div>
      </section>

      <section class="chapter" aria-labelledby="c3">
        <div class="chapter__media"><div class="arch">{img("table", s["alt_table"], "(max-width: 960px) 100vw, 40vw", 1800, 2700)}</div></div>
        <div>
          <h2 id="c3">{s["c3_h"]}</h2>
          <p>{s["c3_p"]}</p>
          <ul class="producers">
{producers}
          </ul>
        </div>
      </section>
    </div>

    <section class="close on-lime" aria-labelledby="close-title">
      <div class="wrap close__grid">
        <h2 id="close-title">{s["story_close_h"]}</h2>
        <div>
          <p>{s["story_close_p"]}</p>
          <a class="btn btn--solid" href="visit.html#book">{s["book"]} {ARROW}</a>
        </div>
      </div>
    </section>''')

    # ---- Visit
    times = "".join(f"<option>{h}.{m}</option>" for h in range(17, 22) for m in ("00", "30"))
    guests = "".join(f'<option>{n} {s["guest1"] if n == 1 else s["guestN"]}</option>' for n in range(1, 7))
    hours = {2: ("17.00", "23.00"), 3: ("17.00", "23.00"), 4: ("17.00", "23.00"), 5: ("17.00", "00.00"), 6: ("17.00", "00.00")}
    rows = "\n".join(
        f'              <tr data-day="{d}"><th scope="row">{s["days"][d]}</th><td>{s["span"](*hours[d]) if d in hours else s["closed"]}</td></tr>'
        for d in [1, 2, 3, 4, 5, 6, 0])
    page("visit", f'''    <section class="page-head">
      <div class="wrap">
        <h1 class="page-title">{s["visit_h1"]}</h1>
        <p class="page-lead">{s["visit_lead"]}</p>
      </div>
    </section>

    <div class="wrap visit-grid">
      <section id="book" aria-labelledby="book-title">
        <h2 id="book-title" class="panel-title">{s["your_table"]}</h2>
        <form id="book-form" class="form" novalidate>
          <div class="field">
            <label for="date">{s["l_date"]}</label>
            <input id="date" name="date" type="date" required aria-describedby="date-hint date-error">
            <span id="date-hint" class="field__hint">{s["h_date"]}</span>
            <span id="date-error" class="field__error"></span>
          </div>
          <div class="field">
            <label for="time">{s["l_time"]}</label>
            <select id="time" name="time" required aria-describedby="time-error"><option value="">{s["o_time"]}</option>{times}</select>
            <span id="time-error" class="field__error"></span>
          </div>
          <div class="field">
            <label for="guests">{s["l_guests"]}</label>
            <select id="guests" name="guests" required aria-describedby="guests-error"><option value="">{s["o_guests"]}</option>{guests}</select>
            <span id="guests-error" class="field__error"></span>
          </div>
          <div class="field">
            <label for="name">{s["l_name"]}</label>
            <input id="name" name="name" type="text" autocomplete="name" required aria-describedby="name-error">
            <span id="name-error" class="field__error"></span>
          </div>
          <div class="field field--full">
            <label for="email">{s["l_email"]}</label>
            <input id="email" name="email" type="email" autocomplete="email" required placeholder="{s["ph_email"]}" aria-describedby="email-error">
            <span id="email-error" class="field__error"></span>
          </div>
          <div class="field field--full">
            <label for="notes">{s["l_notes"]} <span class="field__hint">{s["optional"]}</span></label>
            <textarea id="notes" name="notes"></textarea>
          </div>
          <div class="form__actions">
            <button class="btn btn--solid" type="submit">{s["submit"]} {ARROW}</button>
            <p class="form__note">{s["demo_note"]}</p>
          </div>
        </form>
        <div id="book-done" class="form-done" tabindex="-1" hidden>
          <h3>{s["done_h"]}</h3>
          <p><span data-summary></span> {s["done_p"]}</p>
        </div>
      </section>

      <aside class="visit-side" aria-label="{s["side_label"]}">
        <section aria-labelledby="hours-title">
          <h2 id="hours-title" class="panel-title">{s["hours_h"]}</h2>
          <table class="hours" data-hours>
            <caption class="visually-hidden">{s["hours_cap"]}</caption>
            <tbody>
{rows}
            </tbody>
          </table>
          <p style="margin-top:1rem">{s["kitchen_note"]}</p>
        </section>
        <section aria-labelledby="find-title">
          <h2 id="find-title" class="panel-title">{s["find_h"]}</h2>
          <address class="address">{s["address"]}</address>
          <p style="margin-top:1rem">{s["find_p"]}</p>
        </section>
      </aside>
    </div>''')


if __name__ == "__main__":
    for l in LANGS:
        build(l)
    print("built", ", ".join(LANGS))
