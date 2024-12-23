import subprocess

# List of locations to test

locations = [
    ## BY 50 USA STATES
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
    "Missouri", "Montana", "Nebraska", "Nevada", "NewHampshire", "NewJersey",
    "NewMexico", "NewYork", "NorthCarolina", "NorthDakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "RhodeIsland", "SouthCarolina",
    "SouthDakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
    "Washington", "WestVirginia", "Wisconsin", "Wyoming", 
    
    ## BY COMMON SERVER LOCATIONS
    "mexico", "canada", "london", "sydney", "tokyo", "frankfurt",
    "paris", "madrid", "singapore", "hongkong", "seoul", "amsterdam", "milan",
    "dublin", "warsaw", "osaka", "jakarta", "bangalore", "istanbul", "dubai",
    "santiago", "buenosaires", "cape", "johannesburg", "toronto", "seoul", "ny",
    "river",

    ## BY MAJOR CITIES IN THE USA
    "NewYork", "LosAngeles", "Chicago", "Houston", "Philadelphia", 
    "Phoenix", "SanAntonio", "SanDiego", "Dallas", "SanJose", 
    "Austin", "Jacksonville", "SanFrancisco", "Indianapolis", 
    "Columbus", "FortWorth", "Charlotte", "Seattle", "Denver", 
    "ElPaso", "Detroit", "Washington", "Boston", "Memphis", 
    "Nashville", "Portland", "OklahomaCity", "LasVegas", 
    "Baltimore", "Louisville", "Milwaukee", "Albuquerque", 
    "Tucson", "Fresno", "Sacramento", "KansasCity", "LongBeach", 
    "Mesa", "Atlanta", "ColoradoSprings", "VirginiaBeach", 
    "Raleigh", "Omaha", "Miami", "Oakland", "Minneapolis", 
    "Tulsa", "Wichita", "NewOrleans", "Arlington",

    ## BY ALL 195 COUNTRIES
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "AntiguaAndBarbuda", "Argentina", "Armenia", "Australia", 
    "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", 
    "Bhutan", "Bolivia", "BosniaAndHerzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "BurkinaFaso", "Burundi", 
    "CaboVerde", "Cambodia", "Cameroon", "Canada", "CentralAfricanRepublic", "Chad", "Chile", "China", "Colombia", 
    "Comoros", "Congo(Congo-Brazzaville)", "CostaRica", "Croatia", "Cuba", "Cyprus", "Czechia(CzechRepublic)", 
    "DemocraticRepublicOfTheCongo", "Denmark", "Djibouti", "Dominica", "DominicanRepublic", "Ecuador", "Egypt", 
    "ElSalvador", "EquatorialGuinea", "Eritrea", "Estonia", "Eswatini(fmr.Swaziland)", "Ethiopia", "Fiji", "Finland", 
    "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", 
    "Guyana", "Haiti", "HolySee", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", 
    "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", 
    "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", 
    "Malaysia", "Maldives", "Mali", "Malta", "MarshallIslands", "Mauritania", "Mauritius", "Mexico", "Micronesia", 
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar(Burma)", "Namibia", "Nauru", "Nepal", 
    "Netherlands", "NewZealand", "Nicaragua", "Niger", "Nigeria", "NorthKorea", "NorthMacedonia", "Norway", "Oman", 
    "Pakistan", "Palau", "PalestineState", "Panama", "PapuaNewGuinea", "Paraguay", "Peru", "Philippines", "Poland", 
    "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "SaintKittsAndNevis", "SaintLucia", "SaintVincentAndTheGrenadines", 
    "Samoa", "SanMarino", "SaoTomeAndPrincipe", "SaudiArabia", "Senegal", "Serbia", "Seychelles", "SierraLeone", 
    "Singapore", "Slovakia", "Slovenia", "SolomonIslands", "Somalia", "SouthAfrica", "SouthKorea", "SouthSudan", "Spain", 
    "SriLanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", 
    "Togo", "Tonga", "TrinidadAndTobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "UnitedArabEmirates", 
    "UnitedKingdom", "UnitedStatesOfAmerica", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe",

    ## MAJOR STATES AND CITIES IN CANADA
    "Alberta", "Calgary", "Edmonton", "RedDeer", "Lethbridge",
    "BritishColumbia", "Vancouver", "Victoria", "Surrey", "Burnaby",
    "Manitoba", "Winnipeg", "Brandon", "Steinbach",
    "NewBrunswick", "Fredericton", "Moncton", "SaintJohn",
    "NewfoundlandandLabrador", "StJohns", "CornerBrook", "MountPearl",
    "NovaScotia", "Halifax", "Sydney", "Dartmouth",
    "Ontario", "Toronto", "Ottawa", "Mississauga", "Hamilton", "London",
    "PrinceEdwardIsland", "Charlottetown", "Summerside",
    "Quebec", "Montreal", "QuebecCity", "Laval", "Gatineau",
    "Saskatchewan", "Saskatoon", "Regina", "PrinceAlbert",
    "NorthwestTerritories", "Yellowknife", "HayRiver",
    "Nunavut", "Iqaluit", "RankinInlet",
    "Yukon", "Whitehorse", "DawsonCity",

    ## MAJOR STATES AND CITIES IN MEXICO
    "Aguascalientes", "AguascalientesCity",
    "BajaCalifornia", "Tijuana", "Mexicali", "Ensenada",
    "BajaCaliforniaSur", "LaPaz", "CaboSanLucas",
    "Campeche", "CampecheCity", "CiudadDelCarmen",
    "Chiapas", "TuxtlaGutierrez", "SanCristobalDeLasCasas",
    "Chihuahua", "ChihuahuaCity", "CiudadJuarez",
    "Coahuila", "Saltillo", "Torreon", "Monclova",
    "Colima", "ColimaCity", "Manzanillo",
    "Durango", "DurangoCity", "GomezPalacio",
    "Guanajuato", "Leon", "GuanajuatoCity", "Irapuato",
    "Guerrero", "Acapulco", "Chilpancingo",
    "Hidalgo", "Pachuca", "Tulancingo",
    "Jalisco", "Guadalajara", "PuertoVallarta",
    "MexicoState", "Toluca", "Naucalpan", "Ecatepec",
    "MexicoCity",  # Federal District
    "Michoacan", "Morelia", "Uruapan",
    "Morelos", "Cuernavaca", "Cuautla",
    "Nayarit", "Tepic",
    "NuevoLeon", "Monterrey", "SanPedroGarzaGarcia",
    "Oaxaca", "OaxacaCity", "PuertoEscondido",
    "Puebla", "PueblaCity", "Cholula",
    "Queretaro", "SantiagoDeQueretaro",
    "QuintanaRoo", "Cancun", "PlayaDelCarmen",
    "SanLuisPotosi", "SanLuisPotosiCity",
    "Sinaloa", "Culiacan", "Mazatlan",
    "Sonora", "Hermosillo", "CiudadObregon",
    "Tabasco", "Villahermosa",
    "Tamaulipas", "CiudadVictoria", "Reynosa", "Matamoros",
    "Tlaxcala", "TlaxcalaCity",
    "Veracruz", "VeracruzCity", "Xalapa",
    "Yucatan", "Merida", "Valladolid",
    "Zacatecas", "ZacatecasCity", "Fresnillo",

    ### EUROPE
    # Albania
    "Berat", "Diber", "Durres", "Elbasan", "Fier", 
    "Gjirokaster", "Korce", "Kukes", "Lezhe", "Shkoder", 
    "Tirana", "Vlore", "Tirana", "Durres", "Vlore", "Shkoder", "Fier", 
    "Elbasan", "Korce", "Berat", "Gjirokaster", "Lezhe",
    "Kukes", "Pogradec", "Lushnje", "Sarande", "Kamza",
    
    # Andorra
    "AndorraLaVella", "EscaldesEngordany", "Encamp", "SantJuliaDeLoria", 
    "LaMassana", "Ordino", "Canillo", "AndorraLaVella", "EscaldesEngordany", "Encamp", "SantJuliaDeLoria", 
    "LaMassana", "Ordino", "Canillo",
    
    # Austria
    "Burgenland", "Carinthia", "LowerAustria", "UpperAustria", 
    "Salzburg", "Styria", "Tyrol", "Vorarlberg", "Vienna",
    "Vienna", "Graz", "Linz", "Salzburg", "Innsbruck", 
    "Klagenfurt", "Villach", "Wels", "SanktPolten", "Dornbirn", 
    "Bregenz", "Eisenstadt", "Leoben", "Kapfenberg", "Steyr", 
    "Hallstatt",  # Famous village
    
    # Belarus
    "BrestRegion", "GomelRegion", "GrodnoRegion", "MogilevRegion", 
    "MinskRegion", "VitebskRegion",
    "Minsk", "Gomel", "Mogilev", "Vitebsk", "Hrodna", 
    "Brest", "Babruysk", "Baranovichi", "Pinsk", "Orsha", 
    "Mazyr", "Lida", "Polotsk", "Novopolotsk",
    
    # Belgium
    "Flanders", "Wallonia", "BrusselsCapitalRegion",
    "Antwerp", "AntwerpCity", "Mechelen", "Turnhout",
    "EastFlanders", "Ghent", "Aalst", "SintNiklaas",
    "FlemishBrabant", "Leuven", "Vilvoorde",
    "Limburg", "Hasselt", "Genk", "Tongeren",
    "WestFlanders", "Bruges", "Kortrijk", "Ostend",
    "Hainaut", "Charleroi", "Mons", "LaLouviere",
    "Liege", "LiegeCity", "Verviers", "Seraing",
    "Luxembourg", "Arlon", "Bastogne", "Virton",
    "Namur", "NamurCity", "Dinant", "Andenne",
    "WalloonBrabant", "Wavre", "OttigniesLouvainLaNeuve",
    "Brussels", "Anderlecht", "Ixelles", "Schaerbeek",
    
    # Bosnia and Herzegovina
    "FederationOfBosniaAndHerzegovina", "RepublikaSrpska", "BrckoDistrict",
    "Sarajevo", "Mostar", "Tuzla", "Zenica", "Bihac",
    "BanjaLuka", "Prijedor", "Doboj", "Trebinje",
    "Brcko",
    
    # Bulgaria
    "Bulgaria", "Sofia", "Plovdiv", "Varna", "Burgas",
    
    # Croatia
    "Croatia", "Zagreb", "Split", "Rijeka", "Osijek",
    
    # Czech Republic (Czechia)
    "Czechia", "Prague", "Brno", "Ostrava", "Plzen",
    
    # Denmark
    "Denmark", "Copenhagen", "Aarhus", "Odense", "Aalborg",
    
    
    # Finland
    "Finland", "Helsinki", "Espoo", "Tampere", "Turku",
    
    # France
    "France", "Paris", "Marseille", "Lyon", "Toulouse", "Nice",
    
    # Germany
    "Germany", "Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt",
    
    # Greece
    "Greece", "Athens", "Thessaloniki", "Patras", "Heraklion",
    
    # Hungary
    "Hungary", "Budapest", "Debrecen", "Szeged", "Miskolc",
    
    # Iceland
    "Iceland", "Reykjavik", "Akureyri", "Keflavik",
    
    # Ireland
    "Ireland", "Dublin", "Cork", "Limerick", "Galway",
    
    # Italy
    "Italy", "Rome", "Milan", "Naples", "Turin", "Florence",
    
    # Latvia
    "Latvia", "Riga", "Daugavpils", "Liepaja", "Jelgava",
    
    # Lithuania
    "Lithuania", "Vilnius", "Kaunas", "Klaipeda", "Siauliai",
    
    # Luxembourg
    "Luxembourg", "LuxembourgCity", "EschSurAlzette", "Differdange",
    
    # Malta
    "Malta", "Valletta", "Birkirkara", "Mosta", "Qormi",
    
    # Netherlands
    "Netherlands", "Amsterdam", "Rotterdam", "TheHague", "Utrecht",
    
    # Norway
    "Norway", "Oslo", "Bergen", "Trondheim", "Stavanger",
    
    # Poland
    "Poland", "Warsaw", "Krakow", "Lodz", "Wroclaw", "Poznan",
    
    # Portugal
    "Portugal", "Lisbon", "Porto", "Amadora", "Braga",
    
    # Romania
    "Romania", "Bucharest", "ClujNapoca", "Timisoara", "Iasi",
    
    # Russia
    "Russia", "Moscow", "SaintPetersburg", "Novosibirsk", "Yekaterinburg", "Kazan",
    
    # Serbia
    "Serbia", "Belgrade", "NoviSad", "Nis", "Kragujevac",
    
    # Slovakia
    "Slovakia", "Bratislava", "Kosice", "Presov", "Zilina",
    
    # Slovenia
    "Slovenia", "Ljubljana", "Maribor", "Celje", "Kranj",
    
    # Spain
    "Spain", "Madrid", "Barcelona", "Valencia", "Seville", "Bilbao",
    
    # Sweden
    "Sweden", "Stockholm", "Gothenburg", "Malmo", "Uppsala",
    
    # Switzerland
    "Switzerland", "Zurich", "Geneva", "Basel", "Lausanne",
    
    # Turkey (European side)
    "Turkey", "Istanbul", "Edirne", "Tekirdag",
    
    # Ukraine
    "Ukraine", "Kyiv", "Kharkiv", "Odessa", "Dnipro",
    
    # United Kingdom
    "UnitedKingdom", "London", "Manchester", "Birmingham", "Glasgow", "Liverpool"

    ## BASED ON BONK FLAGS

    # Estonia
    "HarjuCounty", "HiiuCounty", "IdaViruCounty", "JogevaCounty", 
    "JarvaCounty", "LaaneCounty", "LaaneViruCounty", "ParnuCounty", 
    "PolvaCounty", "RaplaCounty", "SaareCounty", "TartuCounty", 
    "ValgaCounty", "ViljandiCounty", "VoruCounty",
    "Tallinn", "Tartu", "Narva", "Parnu", "KohtlaJarve",
    "Viljandi", "Rakvere", "Kuressaare", "Valga", "Voru",
    "Paide", "Sillamae", "Maardu", "Jogeva", "Rapla",

    #Algeria
    "Adrar", "Chlef", "Laghouat", "OumElBouaghi", "Batna", "Bejaia", 
    "Biskra", "Bechar", "Blida", "Bouira", "Tamanrasset", "Tebessa", 
    "Tlemcen", "Tiaret", "TiziOuzou", "Algiers", "Djelfa", "Jijel", 
    "Setif", "Saida", "Skikda", "SidiBelAbbes", "Annaba", "Guelma", 
    "Constantine", "Medea", "Mostaganem", "M'Sila", "Mascara", "Ouargla", 
    "Oran", "ElBayadh", "Illizi", "BordjBouArreridj", "Boumerdes", 
    "ElTarf", "Tindouf", "Tissemsilt", "ElOued", "Khenchela", 
    "SoukAhras", "Tipaza", "Mila", "AinDefla", "Naama", "AinTemouchent", 
    "Ghardaia", "Relizane", "Timimoun", "BordjBadjiMokhtar", "OuledDjellal", 
    "BeniAbbes", "InSalah", "InGuezzam", "Touggourt", "Djanet", "ElM'Ghair", 
    "ElMenia",
    "Algiers", "Oran", "Constantine", "Annaba", "Blida", 
    "Batna", "Setif", "TiziOuzou", "Bejaia", "Biskra", 
    "Tlemcen", "Djelfa", "Ghardaia", "Laghouat", "Bouira", 
    "Skikda", "Saida", "Mostaganem", "ElOued", "Relizane", 
    "Mascara", "Guelma", "Tipaza", "Khenchela", "Ouargla", 
    "AinTemouchent", "Tamanrasset", "Bechar", "Tebessa",

    #Brazil
    "Acre", "Alagoas", "Amapa", "Amazonas", "Bahia", 
    "Ceara", "DistritoFederal", "EspiritoSanto", "Goias", 
    "Maranhao", "MatoGrosso", "MatoGrossoDoSul", "MinasGerais", 
    "Para", "Paraiba", "Parana", "Pernambuco", "Piaui", 
    "RioDeJaneiro", "RioGrandeDoNorte", "RioGrandeDoSul", 
    "Rondonia", "Roraima", "SantaCatarina", "SaoPaulo", 
    "Sergipe", "Tocantins",
    "SaoPaulo", "RioDeJaneiro", "Brasilia", "Salvador", "Fortaleza", 
    "BeloHorizonte", "Manaus", "Curitiba", "Recife", "PortoAlegre", 
    "Belem", "Goiania", "Guarulhos", "Campinas", "SaoLuis", 
    "Maceio", "Natal", "Teresina", "CampoGrande", "JoaoPessoa", 
    "Cuiaba", "Aracaju", "Florianopolis", "Palmas", "BoaVista", 
    "Macapa", "PortoVelho", "Vitoria", "Sorocaba", "Uberlandia",

    #Ecuador
    "Azuay", "Bolivar", "Canar", "Carchi", "Chimborazo", 
    "Cotopaxi", "ElOro", "Esmeraldas", "Galapagos", "Guayas", 
    "Imbabura", "Loja", "LosRios", "Manabi", "MoronaSantiago", 
    "Napo", "Orellana", "Pastaza", "Pichincha", "SantaElena", 
    "SantoDomingoDeLosTsachilas", "Sucumbios", "Tungurahua", "ZamoraChinchipe",
    "Quito", "Guayaquil", "Cuenca", "SantoDomingo", "Machala", 
    "Manta", "Portoviejo", "Ambato", "Riobamba", "Loja", 
    "Esmeraldas", "Ibarra", "Latacunga", "Tena", "Puyo", 
    "Macas", "PuertoAyora", "NuevaLoja", "Zamora", "Babahoyo",

    #Italy
    "Abruzzo", "AostaValley", "Apulia", "Basilicata", "Calabria", 
    "Campania", "EmiliaRomagna", "FriuliVeneziaGiulia", "Lazio", "Liguria", 
    "Lombardy", "Marche", "Molise", "Piedmont", "Sardinia", 
    "Sicily", "Tuscany", "TrentinoAltoAdige", "Umbria", "Veneto",
    "Rome", "Milan", "Naples", "Turin", "Palermo", 
    "Genoa", "Bologna", "Florence", "Bari", "Catania", 
    "Venice", "Verona", "Messina", "Padua", "Trieste", 
    "Taranto", "Brescia", "Parma", "Modena", "ReggioCalabria", 
    "Perugia", "Ravenna", "Livorno", "Cagliari", "Foggia", 
    "Salerno", "Ferrara", "Sassari", "Monza", "Pescara", 
    "Syracuse", "Bergamo", "Forli", "Trento", "Vicenza",

    #United Kingdom
    "England", "Scotland", "Wales", "NorthernIreland",
    
    # Major Regions in England
    "EastMidlands", "EastofEngland", "London", "NorthEastEngland", 
    "NorthWestEngland", "SouthEastEngland", "SouthWestEngland", 
    "WestMidlands", "YorkshireAndTheHumber",
    
    # Major Cities in England
    "London", "Manchester", "Birmingham", "Leeds", "Liverpool", 
    "Newcastle", "Sheffield", "Bristol", "Nottingham", "Leicester", 
    "Southampton", "Portsmouth", "Coventry", "Brighton", "Hull",
    
    # Major Regions in Scotland
    "CentralScotland", "HighlandsAndIslands", "NortheastScotland", 
    "SouthernScotland", "WestScotland",
    
    # Major Cities in Scotland
    "Edinburgh", "Glasgow", "Aberdeen", "Dundee", "Stirling", 
    "Inverness", "Perth",
    
    # Major Regions in Wales
    "NorthWales", "MidWales", "SouthWales",
    
    # Major Cities in Wales
    "Cardiff", "Swansea", "Newport", "Bangor", "Wrexham",
    
    # Major Regions in Northern Ireland
    "Antrim", "Armagh", "Down", "Fermanagh", "Londonderry", "Tyrone",
    
    # Major Cities in Northern Ireland
    "Belfast", "Derry", "Lisburn", "Newry", "BangorNI",

    #Netherlands
    "Drenthe", "Flevoland", "Friesland", "Gelderland", 
    "Groningen", "Limburg", "NorthBrabant", "NorthHolland", 
    "Overijssel", "SouthHolland", "Utrecht", "Zeeland",
    "Amsterdam", "Rotterdam", "TheHague", "Utrecht", "Eindhoven", 
    "Tilburg", "GroningenCity", "Almere", "Breda", "Nijmegen", 
    "Enschede", "Haarlem", "Arnhem", "Zwolle", "Leeuwarden", 
    "Maastricht", "Delft", "Leiden", "Amersfoort", "Apeldoorn",
    "DenBosch", "Middelburg", "Emmen", "Heerlen", "Hengelo",

    #Switzerland
    "Aargau", "AppenzellAusserrhoden", "AppenzellInnerrhoden", "BaselLandschaft", 
    "BaselStadt", "Bern", "Fribourg", "Geneva", "Glarus", 
    "Graubunden", "Jura", "Lucerne", "Neuchatel", "Nidwalden", 
    "Obwalden", "Schaffhausen", "Schwyz", "Solothurn", 
    "StGallen", "Thurgau", "Ticino", "Uri", "Valais", 
    "Vaud", "Zug", "Zurich",
    "ZurichCity", "GenevaCity", "Basel", "BernCity", "Lausanne", 
    "Lucerne", "StGallenCity", "Lugano", "Biel", "Winterthur", 
    "Thun", "SchaffhausenCity", "Chur", "FribourgCity", "Sion", 
    "NeuchatelCity", "SolothurnCity", "Bellinzona", "Aarau", "ZugCity",

    #Ukraine
    "CherkasyOblast", "ChernihivOblast", "ChernivtsiOblast", "DnipropetrovskOblast", 
    "DonetskOblast", "IvanoFrankivskOblast", "KharkivOblast", "KhersonOblast", 
    "KhmelnytskyiOblast", "KirovohradOblast", "KyivOblast", "LuhanskOblast", 
    "LvivOblast", "MykolaivOblast", "OdessaOblast", "PoltavaOblast", 
    "RivneOblast", "SumyOblast", "TernopilOblast", "VinnytsiaOblast", 
    "VolynOblast", "ZakarpattiaOblast", "ZaporizhzhiaOblast", "ZhytomyrOblast", 
    "AutonomousRepublicOfCrimea", "KyivCity", "SevastopolCity",
    "Kyiv", "Kharkiv", "Odessa", "Dnipro", "Donetsk", 
    "Zaporizhzhia", "Lviv", "KryvyiRih", "Mykolaiv", "Mariupol", 
    "Vinnytsia", "Kherson", "Cherkasy", "Poltava", "Chernivtsi", 
    "Sumy", "Ternopil", "IvanoFrankivsk", "Zhytomyr", "Luhansk", 
    "Uzhhorod", "Rivne", "Lutsk", "Simferopol", "BilaTserkva",

    #Turkey
    "AegeanRegion", "BlackSeaRegion", "CentralAnatoliaRegion", 
    "EasternAnatoliaRegion", "MarmaraRegion", "MediterraneanRegion", 
    "SoutheasternAnatoliaRegion",
    "Adana", "Adiyaman", "Afyonkarahisar", "Agri", "Aksaray", 
    "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", "Aydin", 
    "Balikesir", "Bartin", "Batman", "Bayburt", "Bilecik", "Bingol", 
    "Bitlis", "Bolu", "Burdur", "Bursa", "Canakkale", "Cankiri", 
    "Corum", "Denizli", "Diyarbakir", "Duzce", "Edirne", "Elazig", 
    "Erzincan", "Erzurum", "Eskisehir", "Gaziantep", "Giresun", 
    "Gumushane", "Hakkari", "Hatay", "Igdir", "Isparta", "Istanbul", 
    "Izmir", "Kahramanmaras", "Karabuk", "Karaman", "Kars", "Kastamonu", 
    "Kayseri", "Kirikkale", "Kirklareli", "Kirsehir", "Kilis", 
    "Kocaeli", "Konya", "Kutahya", "Malatya", "Manisa", "Mardin", 
    "Mersin", "Mugla", "Mus", "Nevsehir", "Nigde", "Ordu", "Osmaniye", 
    "Rize", "Sakarya", "Samsun", "Sanliurfa", "Siirt", "Sinop", 
    "Sirnak", "Sivas", "Tekirdag", "Tokat", "Trabzon", "Tunceli", 
    "Usak", "Van", "Yalova", "Yozgat", "Zonguldak",
    "Istanbul", "Ankara", "Izmir", "Bursa", "Antalya", 
    "Adana", "Gaziantep", "Konya", "Sanliurfa", "Diyarbakir", 
    "Mersin", "Kayseri", "Eskisehir", "Samsun", "Trabzon", 
    "Denizli", "Malatya", "Van", "Sivas", "Erzurum",

    #Chile
    "AricaAndParinacotaRegion", "TarapacaRegion", "AntofagastaRegion", 
    "AtacamaRegion", "CoquimboRegion", "ValparaisoRegion", 
    "MetropolitanRegion", "OHigginsRegion", "MauleRegion", 
    "NubleRegion", "BiobioRegion", "AraucaniaRegion", 
    "LosRiosRegion", "LosLagosRegion", "AysenRegion", "MagallanesRegion",
    "Santiago", "Valparaiso", "VinaDelMar", "Antofagasta", "Arica", 
    "Iquique", "LaSerena", "Coquimbo", "Copiapo", "Rancagua", 
    "Talca", "Chillan", "Concepcion", "Temuco", "PuertoMontt", 
    "Osorno", "Valdivia", "PuntaArenas", "Coyhaique",

    #Ireland
    "Carlow", "Cavan", "Clare", "Cork", "Donegal", 
    "Dublin", "Galway", "Kerry", "Kildare", "Kilkenny", 
    "Laois", "Leitrim", "Limerick", "Longford", "Louth", 
    "Mayo", "Meath", "Monaghan", "Offaly", "Roscommon", 
    "Sligo", "Tipperary", "Waterford", "Westmeath", "Wexford", "Wicklow",
    "Dublin", "CorkCity", "LimerickCity", "GalwayCity", "WaterfordCity", 
    "Drogheda", "Swords", "Dundalk", "Bray", "Navan", 
    "Ennis", "KilkennyCity", "CarlowTown", "Tralee", "Athlone", 
    "Letterkenny", "Clonmel", "WexfordTown", "SligoTown", "Castlebar", 
    "Mullingar", "Tullamore", "Ballina", "Newbridge",

    #South Korea
    "GyeonggiProvince", "GangwonProvince", "NorthChungcheongProvince", 
    "SouthChungcheongProvince", "NorthJeollaProvince", "SouthJeollaProvince", 
    "NorthGyeongsangProvince", "SouthGyeongsangProvince", "JejuProvince",
    "Seoul", "Busan", "Incheon", "Daegu", "Daejeon", 
    "Gwangju", "Ulsan",
    "Seoul", "Busan", "Incheon", "Daegu", "Daejeon", 
    "Gwangju", "Ulsan", "Suwon", "Yongin", "Goyang", 
    "Seongnam", "Bucheon", "Cheongju", "Jeonju", "JejuCity", 
    "Changwon", "Pohang", "Gimhae", "Hwaseong", "Jinju", 
    "Pyeongtaek", "Ansan", "Anyang", "Gwangmyeong", "Cheonan", 
    "Jecheon", "Mokpo", "Yeosu", "Gunsan", "Tongyeong",

    #Germany
    "BadenWurttemberg", "Bavaria", "Berlin", "Brandenburg", 
    "Bremen", "Hamburg", "Hesse", "LowerSaxony", 
    "MecklenburgVorpommern", "NorthRhineWestphalia", "RhinelandPalatinate", 
    "Saarland", "Saxony", "SaxonyAnhalt", "SchleswigHolstein", 
    "Thuringia",
    "Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", 
    "Stuttgart", "Dusseldorf", "Dresden", "Leipzig", "Bremen", 
    "Hanover", "Nuremberg", "Essen", "Dortmund", "Duisburg", 
    "Bochum", "Karlsruhe", "Mannheim", "Wiesbaden", "Mainz", 
    "Augsburg", "Freiburg", "Monchengladbach", "Kiel", "Lubeck", 
    "Magdeburg", "Potsdam", "Rostock", "Erfurt", "Saarbrucken",

    #Russia
    "Moscow", "SaintPetersburg", "Sevastopol",
    "AmurOblast", "ArkhangelskOblast", "AstrakhanOblast", 
    "BelgorodOblast", "BryanskOblast", "ChelyabinskOblast", 
    "IrkutskOblast", "IvanovoOblast", "KaliningradOblast", 
    "KalugaOblast", "KemerovoOblast", "KirovOblast", 
    "KostromaOblast", "KurganOblast", "KurskOblast", 
    "LeningradOblast", "LipetskOblast", "MagadanOblast", 
    "MoscowOblast", "MurmanskOblast", "NizhnyNovgorodOblast", 
    "NovgorodOblast", "NovosibirskOblast", "OmskOblast", 
    "OrenburgOblast", "OryolOblast", "PenzaOblast", 
    "PskovOblast", "RostovOblast", "RyazanOblast", 
    "SakhalinOblast", "SamaraOblast", "SaratovOblast", 
    "SmolenskOblast", "SverdlovskOblast", "TambovOblast", 
    "TverOblast", "TomskOblast", "TulaOblast", 
    "TyumenOblast", "UlyanovskOblast", "VladimirOblast", 
    "VolgogradOblast", "VologdaOblast", "VoronezhOblast", 
    "YaroslavlOblast",
    "Adygea", "AltaiRepublic", "Bashkortostan", "Buryatia", 
    "Chechnya", "Chuvashia", "Dagestan", "Ingushetia", 
    "KabardinoBalkaria", "Kalmykia", "KarachayCherkessia", 
    "Karelia", "Khakassia", "Komi", "MariEl", "Mordovia", 
    "NorthOssetiaAlania", "SakhaRepublic(Yakutia)", 
    "Tatarstan", "Tuva", "Udmurtia",
    "AltaiKrai", "KamchatkaKrai", "KhabarovskKrai", 
    "KrasnodarKrai", "KrasnoyarskKrai", "PermKrai", 
    "PrimorskyKrai", "StavropolKrai", "ZabaykalskyKrai",
    "ChukotkaAutonomousOkrug", "KhantyMansiAutonomousOkrug", 
    "NenetsAutonomousOkrug", "YamaloNenetsAutonomousOkrug",
    "JewishAutonomousOblast",
    "Moscow", "SaintPetersburg", "Novosibirsk", "Yekaterinburg", "Kazan", 
    "NizhnyNovgorod", "Chelyabinsk", "Samara", "Omsk", "RostovonDon", 
    "Ufa", "Krasnoyarsk", "Perm", "Voronezh", "Volgograd", 
    "Krasnodar", "Sochi", "Vladivostok", "Murmansk", "Kaliningrad", 
    "Irkutsk", "Tomsk", "Arkhangelsk", "Tyumen", "Yakutsk", 
    "Chita", "UlanUde", "Petrozavodsk", "Saransk", "Grozny",

    #Iran
    "Alborz", "Ardabil", "Bushehr", "ChaharmahalAndBakhtiari", "EastAzerbaijan", 
    "Fars", "Gilan", "Golestan", "Hamadan", "Hormozgan", 
    "Ilam", "Isfahan", "Kerman", "Kermanshah", "Khuzestan", 
    "KohgiluyehAndBoyerAhmad", "Kurdistan", "Lorestan", "Markazi", 
    "Mazandaran", "NorthKhorasan", "Qazvin", "Qom", 
    "RazaviKhorasan", "Semnan", "SistanAndBaluchestan", 
    "SouthKhorasan", "Tehran", "WestAzerbaijan", "Yazd", "Zanjan",
    "Tehran", "Mashhad", "Isfahan", "Karaj", "Tabriz", 
    "Shiraz", "Ahvaz", "Qom", "Kermanshah", "Urmia", 
    "Rasht", "Zahedan", "Ardabil", "BandarAbbas", "Yazd", 
    "Zanjan", "Kerman", "Hamadan", "Gorgan", "Khorramabad", 
    "Sanandaj", "Sari", "Bojnord", "Bushehr", "Birjand",

    #Pakistan
    "Balochistan", "KhyberPakhtunkhwa", "Punjab", "Sindh",
    "AzadJammuAndKashmir", "GilgitBaltistan",
    "IslamabadCapitalTerritory",
    "Islamabad", "Karachi", "Lahore", "Faisalabad", "Rawalpindi", 
    "Peshawar", "Quetta", "Multan", "Sialkot", "Gujranwala", 
    "Hyderabad", "Sukkur", "Bahawalpur", "Mardan", "Mingora", 
    "Mirpur", "Muzaffarabad", "Gilgit", "Skardu", "Abbottabad", 
    "Nawabshah", "DeraGhaziKhan", "DeraIsmailKhan", "Sahiwal",

    #Romania
    "Alba", "Arad", "Arges", "Bacau", "Bihor", 
    "BistritaNasaud", "Botosani", "Brasov", "Braila", "Buzau", 
    "CarasSeverin", "Calarasi", "Cluj", "Constanta", "Covasna", 
    "Dambovita", "Dolj", "Galati", "Giurgiu", "Gorj", 
    "Harghita", "Hunedoara", "Ialomita", "Iasi", "Ilfov", 
    "Maramures", "Mehedinti", "Mures", "Neamt", "Olt", 
    "Prahova", "Salaj", "SatuMare", "Sibiu", "Suceava", 
    "Teleorman", "Timis", "Tulcea", "Valcea", "Vaslui", "Vrancea", 
    "Bucharest",
    "Bucharest", "ClujNapoca", "Timisoara", "Iasi", "Constanta", 
    "Craiova", "Brasov", "Galati", "Ploiesti", "Oradea", 
    "Braila", "Arad", "Pitesti", "Sibiu", "Bacau", 
    "TarguMures", "BaiaMare", "Buzau", "Botosani", "Suceava", 
    "Radauti", "Focsani", "Targoviste", "Deva", "Slatina",

    #Spain
    "Andalusia", "Aragon", "Asturias", "BalearicIslands", "BasqueCountry", 
    "CanaryIslands", "Cantabria", "CastileAndLeon", "CastileLaMancha", 
    "Catalonia", "Extremadura", "Galicia", "LaRioja", "MadridCommunity", 
    "MurciaRegion", "Navarre", "ValencianCommunity", "Ceuta", "Melilla",
    "Alava", "Albacete", "Alicante", "Almeria", "Asturias", "Avila", 
    "Badajoz", "BalearicIslands", "Barcelona", "Burgos", "Caceres", 
    "Cadiz", "Cantabria", "Castellon", "CiudadReal", "Cordoba", 
    "Cuenca", "Girona", "Granada", "Guadalajara", "Guipuzcoa", 
    "Huelva", "Huesca", "Jaen", "LaRioja", "LasPalmas", "Leon", 
    "Lleida", "Lugo", "Madrid", "Malaga", "Murcia", "Navarre", 
    "Ourense", "Palencia", "Pontevedra", "Salamanca", "SantaCruzDeTenerife", 
    "Segovia", "Seville", "Soria", "Tarragona", "Teruel", "Toledo", 
    "Valencia", "Valladolid", "Zamora", "Zaragoza",
    "Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza", 
    "Malaga", "Murcia", "Palma", "LasPalmasDeGranCanaria", "Bilbao", 
    "Alicante", "Cordoba", "Valladolid", "Vigo", "Gijon", 
    "L'HospitaletDeLlobregat", "ACoruna", "Granada", "VitoriaGasteiz", 
    "Elche", "Oviedo", "SantaCruzDeTenerife", "Pamplona", "Santander", 
    "Almeria", "SanSebastian", "Burgos", "Salamanca", "Huelva", 
    "Logrono", "Badajoz", "Tarragona", "Lleida", "Cadiz", "Toledo",

    #Morocco
    "TangierTetouanAlHoceima", "Oriental", "FesMeknes", "RabatSaleKenitra", 
    "BeniMellalKhenifra", "CasablancaSettat", "MarrakechSafi", 
    "DraaTafilalet", "SoussMassa", "GuelmimOuedNoun", 
    "LaayouneSakiaElHamra", "DakhlaOuedEdDahab",
    "Casablanca", "Rabat", "Fes", "Marrakech", "Tangier", 
    "Agadir", "Meknes", "Oujda", "Kenitra", "Tetouan", 
    "Safi", "Nador", "Settat", "Laayoune", "Mohammedia", 
    "ElJadida", "BeniMellal", "Khouribga", "Ouarzazate", 
    "Inezgane", "Taroudant", "Dakhla", "Errachidia", "Guelmim",

    #Peru
    "Amazonas", "Ancash", "Apurimac", "Arequipa", "Ayacucho", 
    "Cajamarca", "Callao", "Cusco", "Huancavelica", "Huanuco", 
    "Ica", "Junin", "LaLibertad", "Lambayeque", "LimaRegion", 
    "Loreto", "MadredeDios", "Moquegua", "Pasco", "Piura", 
    "Puno", "SanMartin", "Tacna", "Tumbes", "Ucayali", 
    "LimaMetropolitanArea",
    "Lima", "Arequipa", "Trujillo", "Chiclayo", "Iquitos", 
    "Piura", "Cusco", "Chimbote", "Huancayo", "Tacna", 
    "Ica", "Juliaca", "Pucallpa", "Ayacucho", "Cajamarca", 
    "Puno", "Tarapoto", "Moquegua", "Tumbes", "Huaraz", 
    "PuertoMaldonado", "Callao", "Sullana", "Huanuco", 
    "TingoMaria",

    #Uruguay
    "Artigas", "Canelones", "CerroLargo", "Colonia", "Durazno", 
    "Flores", "Florida", "Lavalleja", "Maldonado", "Montevideo", 
    "Paysandu", "RioNegro", "Rivera", "Rocha", "Salto", 
    "SanJose", "Soriano", "Tacuarembo", "TreintaYTres",
    "Montevideo", "Salto", "Paysandu", "LasPiedras", "Rivera", 
    "Maldonado", "Tacuarembo", "Melo", "Mercedes", "Artigas", 
    "Minas", "CanelonesCity", "FloridaCity", "DuraznoCity", 
    "RochaCity", "SanJoseDeMayo", "TreintaYTresCity", "FrayBentos", 
    "ColoniaDelSacramento", "Piriapolis",

    #Latvia
    "KurzemeRegion", "LatgaleRegion", "RigaRegion", "VidzemeRegion", "ZemgaleRegion",
    "Riga", "Daugavpils", "Liepaja", "Jelgava", "Jurmala", 
    "Ventspils", "Rezekne", "Valmiera", "Jekabpils", "Ogre", 
    "Tukums", "Salaspils", "Cesis", "Saldus", "Bauska",

    #Australia
    "NewSouthWales", "Victoria", "Queensland", "WesternAustralia", 
    "SouthAustralia", "Tasmania",
    "AustralianCapitalTerritory", "NorthernTerritory",
    "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", 
    "Hobart", "Canberra", "Darwin", "GoldCoast", "Newcastle", 
    "Wollongong", "Geelong", "Townsville", "Cairns", "Toowoomba", 
    "Ballarat", "Bendigo", "Albury", "Launceston", "Mackay", 
    "Rockhampton", "Bundaberg", "Mandurah", "Bunbury",

    #China
    "Anhui", "Fujian", "Gansu", "Guangdong", "Guizhou", 
    "Hainan", "Hebei", "Heilongjiang", "Henan", "Hubei", 
    "Hunan", "Jiangsu", "Jiangxi", "Jilin", "Liaoning", 
    "Qinghai", "Shaanxi", "Shandong", "Shanxi", "Sichuan", 
    "Yunnan", "Zhejiang", "Taiwan",
    "Guangxi", "InnerMongolia", "Ningxia", "Tibet", "Xinjiang",
    "Beijing", "Chongqing", "Shanghai", "Tianjin",
    "HongKong", "Macau",
    "Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chongqing", 
    "Tianjin", "Wuhan", "Chengdu", "Hangzhou", "XiAn", 
    "Nanjing", "Shenyang", "Qingdao", "Dalian", "Harbin", 
    "Zhengzhou", "Changsha", "Kunming", "Jinan", "Fuzhou", 
    "Nanning", "Urumqi", "Lhasa", "MacauCity", "HongKongCity",

    #India
    "AndhraPradesh", "ArunachalPradesh", "Assam", "Bihar", "Chhattisgarh", 
    "Goa", "Gujarat", "Haryana", "HimachalPradesh", "Jharkhand", 
    "Karnataka", "Kerala", "MadhyaPradesh", "Maharashtra", "Manipur", 
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "TamilNadu", "Telangana", "Tripura", 
    "UttarPradesh", "Uttarakhand", "WestBengal",
    "AndamanAndNicobarIslands", "Chandigarh", "DadraAndNagarHaveliAndDamanAndDiu", 
    "Delhi", "JammuAndKashmir", "Ladakh", "Lakshadweep", "Puducherry",
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", 
    "Kolkata", "Ahmedabad", "Pune", "Surat", "Jaipur", 
    "Lucknow", "Kanpur", "Nagpur", "Visakhapatnam", "Thiruvananthapuram", 
    "Bhopal", "Patna", "Ranchi", "Bhubaneswar", "Amritsar", 
    "ChandigarhCity", "Coimbatore", "Agra", "Vadodara", "Madurai", 
    "Indore", "Jodhpur", "Raipur", "Dehradun", "Shimla", 
    "Imphal", "Shillong", "Aizawl", "Kohima", "Itanagar", 
    "Gangtok", "PuducherryCity", "PortBlair", "Srinagar", "Leh",

    #Japan
    "Hokkaido",
    "Aomori", "Iwate", "Miyagi", "Akita", "Yamagata", "Fukushima",
    "Ibaraki", "Tochigi", "Gunma", "Saitama", "Chiba", 
    "Tokyo", "Kanagawa",
    "Niigata", "Toyama", "Ishikawa", "Fukui", "Yamanashi", 
    "Nagano", "Gifu", "Shizuoka", "Aichi",
    "Mie", "Shiga", "Kyoto", "Osaka", "Hyogo", 
    "Nara", "Wakayama",
    "Tottori", "Shimane", "Okayama", "Hiroshima", "Yamaguchi",
    "Tokushima", "Kagawa", "Ehime", "Kochi",
    "Fukuoka", "Saga", "Nagasaki", "Kumamoto", "Oita", 
    "Miyazaki", "Kagoshima", "Okinawa",
    "Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo", 
    "Fukuoka", "Kobe", "Kyoto", "Hiroshima", "Sendai", 
    "ChibaCity", "SaitamaCity", "Kawasaki", "Kitakyushu", "Naha", 
    "NiigataCity", "OkayamaCity", "Matsuyama", "KagoshimaCity", "NagasakiCity",

    #MiddleEast
    "Bahrain", "Cyprus", "Egypt", "Iran", "Iraq", "Israel", "Jordan", 
    "Kuwait", "Lebanon", "Oman", "Palestine", "Qatar", "SaudiArabia", 
    "Syria", "Turkey", "UnitedArabEmirates", "Yemen",
    "Manama", "Muharraq",
    "Nicosia", "Limassol", "Larnaca", "Paphos",
    "Cairo", "Alexandria", "Giza", "Luxor", "Aswan", "PortSaid",
    "Tehran", "Mashhad", "Isfahan", "Shiraz", "Tabriz", "Qom",
    "Baghdad", "Basra", "Mosul", "Erbil", "Karbala", "Najaf",
    "Jerusalem", "TelAviv", "Haifa", "Eilat", "Nazareth",
    "Amman", "Irbid", "Zarqa", "Aqaba",
    "KuwaitCity", "Hawalli",
    "Beirut", "Tripoli", "Sidon", "Byblos",
    "Muscat", "Salalah", "Sohar", "Nizwa",
    "GazaCity", "Ramallah", "Nablus", "Hebron",
    "Doha", "AlRayyan", "AlKhor",
    "Riyadh", "Jeddah", "Mecca", "Medina", "Dammam", "Abha", "Tabuk",
    "Damascus", "Aleppo", "Homs", "Latakia", "Hama",
    "Istanbul", "Ankara", "Izmir", "Antalya", "Bursa", "Adana",
    "AbuDhabi", "Dubai", "Sharjah", "AlAin", "Ajman",
    "Sana'a", "Aden", "Taiz", "Hodeidah", "Mukalla",

    #Africa
    "Algeria", "Egypt", "Libya", "Morocco", "Sudan", "Tunisia", "WesternSahara",
    "Cairo", "Alexandria", "Algiers", "Tunis", "Khartoum", "Tripoli", "Marrakech", "Casablanca",
    "Benin", "BurkinaFaso", "CapeVerde", "IvoryCoast", "Gambia", "Ghana", "Guinea", "GuineaBissau", 
    "Liberia", "Mali", "Mauritania", "Niger", "Nigeria", "Senegal", "SierraLeone", "Togo",
    "Lagos", "Accra", "Dakar", "Abidjan", "Ouagadougou", "Freetown", "Bamako", "Niamey", "Monrovia",
    "Burundi", "Comoros", "Djibouti", "Eritrea", "Ethiopia", "Kenya", "Madagascar", "Malawi", 
    "Mauritius", "Mozambique", "Rwanda", "Seychelles", "Somalia", "SouthSudan", "Tanzania", "Uganda", "Zambia", "Zimbabwe",
    "Nairobi", "AddisAbaba", "Kampala", "DarEsSalaam", "Antananarivo", "Harare", "Maputo", "Kigali", "Juba",
    "Angola", "Cameroon", "CentralAfricanRepublic", "Chad", "Congo", "DemocraticRepublicOfCongo", 
    "EquatorialGuinea", "Gabon", "SaoTomeAndPrincipe",
    "Kinshasa", "Brazzaville", "Luanda", "Libreville", "Yaounde", "Bangui", "N'Djamena", "Malabo",
    "Botswana", "Eswatini", "Lesotho", "Namibia", "SouthAfrica",
    "Johannesburg", "CapeTown", "Durban", "Pretoria", "Windhoek", "Maseru", "Gaborone", "Mbabane",

    #Central America
    "Belize", "CostaRica", "ElSalvador", "Guatemala", "Honduras", "Nicaragua", "Panama",
    "BelizeCity", "Belmopan", "OrangeWalk", "SanIgnacio",
    "SanJose", "Alajuela", "Cartago", "Heredia", "Liberia", 
    "SanSalvador", "SantaAna", "SanMiguel", "Soyapango",
    "GuatemalaCity", "AntiguaGuatemala", "Quetzaltenango", "Escuintla",
    "Tegucigalpa", "SanPedroSula", "LaCeiba", "Choloma", "ElProgreso",
    "Managua", "Leon", "Granada", "Masaya", "Chinandega",
    "PanamaCity", "Colon", "David", "Santiago", "LaChorrera",

    #South Asia
    "Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal", "Pakistan", "SriLanka",
    "Kabul", "Kandahar", "Herat", "MazarEISharif", "Jalalabad",
    "Dhaka", "Chittagong", "Khulna", "Sylhet", "Rajshahi", 
    "Thimphu", "Paro", "Punakha", "Phuentsholing",
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", 
    "Ahmedabad", "Pune", "Jaipur", "Lucknow",
    "Male", "AdduCity",
    "Kathmandu", "Pokhara", "Lalitpur", "Biratnagar", "Bharatpur",
    "Karachi", "Lahore", "Islamabad", "Rawalpindi", "Peshawar", "Quetta",
    "Colombo", "Kandy", "Jaffna", "Galle", "Batticaloa",

    #East Asia
    "China", "Japan", "Mongolia", "NorthKorea", "SouthKorea", "Taiwan",
    "Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chongqing", 
    "Tianjin", "XiAn", "Hangzhou", "Chengdu", "Wuhan", 
    "Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo", 
    "Fukuoka", "Kyoto", "Kobe", "Hiroshima", "Sendai",
    "Ulaanbaatar", "Erdenet", "Darkhan", "Choibalsan",
    "Pyongyang", "Nampo", "Kaesong", "Hamhung", "Chongjin",
    "Seoul", "Busan", "Incheon", "Daegu", "Daejeon", 
    "Gwangju", "Ulsan", "Suwon", "Jeonju",
    "Taipei", "Kaohsiung", "Taichung", "Tainan", "Hsinchu",
]

print(len(locations))
result = []  # List to store working servers
base_url = "b2{location}{number}.bonk.io"

def ping_server(server):
    try:
        # Use subprocess to execute the ping command
        response = subprocess.run(
            ["ping", "-c", "1", server],  # On Windows, replace "-c" with "-n"
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # If return code is 0, the ping was successful
        return response.returncode == 0
    except Exception as e:
        print(f"Error pinging {server}: {e}")
        return False

def test_server(location):
    number = 1
    while True:
        server = base_url.format(location=location, number=number)
        if ping_server(server):
            print(f"Success: {server}")
            if server.lower() not in [s.lower() for s in result]:
                result.append(server)  # Add working server to the result list
            number += 1  # Increment the server number
        else:
            print(f"Failed: {server}")
            break  # Stop testing for this country if a server fails

# Test all countries
for place in locations:
    test_server(place)

# Print the final list of working servers
print("\nWorking servers:")
for server in result:
    print(server.lower())
