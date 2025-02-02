import os
import time

# Path to ADB executable
ADB_PATH = "adb"

# List of passwords
words = [
    "Abilities", "Absences", "Abundances", "Academics", "Academies", "Accents", "Acceptances", 
    "Accesses", "Accidents", "Accommodations", "Accomplishments", "Accordances", "Accountabilities", 
    "Accountants", "Accounts", "Accumulations", "Accuracies", "Accusations", "Accused", "Achievements", 
    "Acquisitions", "Actions", "Activations", "Activists", "Activities", "Actors", "Actresses", 
    "Adaptations", "Addictions", "Additions", "Addresses", "Adjustments", "Administrations", 
    "Administrators", "Admissions", "Adolescents", "Adoptions", "Adults", "Advances", "Advantages", 
    "Adventures", "Advertisements", "Advertisings", "Advice", "Advocates", "Affairs", "Affections", 
    "Aftermaths", "Afternoons", "Agencies", "Agendas", "Agents", "Aggressions", "Agreements", 
    "Agricultures", "Alarms", "Albums", "Alerts", "Aliens", "Alignments", "Allegations", "Alliances", 
    "Allies", "Allocations", "Allowances", "Alternatives", "Aluminium", "Amateurs", "Ambassadors", 
    "Ambitions", "Ambulances", "Amendments", "Amounts", "Analogies", "Analyses", "Analysts", 
    "Ancestors", "Anchors", "Angels", "Angers", "Angles", "Animals", "Animations", "Ankles", 
    "Anniversaries", "Announcements", "Answers", "Anxieties", "Apartments", "Apologies", "Apparatus", 
    "Appeals", "Appearances", "Appetites", "Apples", "Applicants", "Applications", "Appointments", 
    "Appreciations", "Approaches", "Approvals", "Aprils", "Architects", "Architectures", "Archives", 
    "Arenas", "Arguments", "Armies", "Arrangements", "Arrays", "Arrests", "Arrivals", "Arrows", 
    "Articles", "Artists", "Artworks", "Aspects", "Aspirations", "Assaults", "Assemblies", "Assertions", 
    "Assessments", "Assets", "Assignments", "Assistances", "Assistants", "Associations", "Assumptions", 
    "Assurances", "Asylums", "Athletes", "Atmospheres", "Attachments", "Attacks", "Attempts", 
    "Attendances", "Attentions", "Attitudes", "Attorneys", "Attractions", "Attributes", "Auctions", 
    "Audiences", "Audits", "Augusts", "Authorities", "Authors", "Autonomies", "Autumns", "Availabilities", 
    "Averages", "Awards", "Awarenesses", "Babies", "Backdrops", "Backgrounds", "Backings", "Backups", 
    "Bacterias", "Badges", "Balances", "Ballets", "Balloons", "Ballots", "Bananas", "Banners", 
    "Bargains", "Barrels", "Barriers", "Baseballs", "Basements", "Basketballs", "Baskets", "Basses", 
    "Bathrooms", "Batteries", "Battlefields", "Battles", "Beaches", "Beasts", "Beauties", "Bedrooms", 
    "Beginnings", "Behalves", "Behaviours", "Beings", "Beliefs", "Benches", "Benchmarks", "Beneficiaries", 
    "Benefits", "Betters", "Biases", "Bicycles", "Biographies", "Biologies", "Birthdays", "Births", 
    "Biscuits", "Bishops", "Blades", "Blames", "Blankets", "Blanks", "Blasts", "Blends", "Blessings", 
    "Blocks", "Bloods", "Boards", "Bookings", "Boosts", "Borders", "Bosses", "Bottles", "Boundaries", 
    "Brains", "Branches", "Brands", "Breaches", "Breads", "Breakdowns", "Breakfasts", "Breaks", 
    "Breakthroughs", "Breathings", "Breaths", "Breeds", "Brethren", "Bricks", "Brides", "Bridges", 
    "Broadbands", "Broadcasters", "Broadcasts", "Browsers", "Brushes", "Bubbles", "Buddies", "Budgets", 
    "Buffers", "Buildings", "Bullets", "Bunches", "Burdens", "Bureaucracies", "Burials", "Bushes", 
    "Businesses", "Businessmen", "Butters", "Buttons", "Cabinets", "Cabins", "Cables", "Calculations", 
    "Cameras", "Campaigns", "Campings", "Campus", "Canals", "Candidates", "Candles", "Canvas", 
    "Capabilities", "Capacities", "Capitalisms", "Capitals", "Captains", "Captures", "Carbons", 
    "Careers", "Cargoes", "Carpets", "Carriages", "Carrots", "Cartoons", "Cashes", "Casinos", "Castles", 
    "Catalogues", "Catches", "Categories", "Cattle", "Causes", "Cautions", "Ceilings", "Celebrations", 
    "Celebrities", "Cemeteries", "Centres", "Centuries", "Ceremonies", "Certainties", "Certificates", 
    "Chains", "Chairmen", "Chairs", "Challenges", "Chambers", "Champions", "Championships", "Chances", 
    "Changes", "Channels", "Chapters", "Characteristics", "Characters", "Charges", "Charities", "Charms", 
    "Charters", "Charts", "Chases", "Cheats", "Checks", "Cheeks", "Cheers", "Cheeses", "Chemicals", 
    "Chemistries", "Chests", "Chickens", "Chiefs", "Childhoods", "Chocolates", "Choices", "Choirs", 
    "Chunks", "Churches", "Cigarettes", "Cinemas", "Circles", "Circuits", "Circulations", 
    "Circumstances", "Cities", "Citizens", "Citizenships", "Civilians", "Civilizations", "Claims", 
    "Clarities", "Clashes", "Classes", "Classics", "Classifications", "Classrooms", "Clauses", "Clerks", 
    "Clicks", "Clients", "Cliffs", "Climates", "Climbs", "Clinics", "Clocks", "Closes", "Closures", 
    "Clothes", "Clothings", "Cloths", "Clouds", "Clusters", "Coaches", "Coalitions", "Coasts", "Cocktails", 
    "Coffees", "Coincidences", "Collaborations", "Collapses", "Colleagues", "Collections", "Collectors", 
    "Colleges", "Collisions", "Colonies", "Colours", "Columnists", "Columns", "Combats", "Combinations", 
    "Comedies", "Comforts", "Comics", "Commanders", "Commands", "Commentaries", "Commentators", 
    "Comments", "Commerces", "Commercials", "Commissioners", "Commissions", "Commitments", "Committees", 
    "Commodities", "Communications", "Communities", "Companies", "Companions", "Comparisons", 
    "Compassions", "Compensations", "Competences", "Competitions", "Competitors", "Complaints", 
    "Completions", "Complexes", "Complexities", "Compliances", "Complications", "Components", 
    "Composers", "Compositions", "Compounds", "Compromises", "Computers", "Concentrations", 
    "Conceptions", "Concepts", "Concerns", "Concerts", "Concessions", "Conclusions", "Concretes", 
    "Conditions", "Conducts", "Conferences", "Confessions", "Confidences", "Configurations", 
    "Confirmations", "Conflicts", "Confrontations", "Confusions", "Congregations", "Connections", 
    "Consciences", "Consciousnesses", "Consensus", "Consents", "Consequences", "Conservations", 
    "Conservatives", "Considerations", "Consistencies", "Conspiracies", "Constituencies", 
    "Constitutions", "Constraints", "Constructions", "Consultants", "Consultations", "Consumers", 
    "Consumptions", "Contacts", "Containers", "Contempts", "Contenders", "Contentions", "Contents", 
    "Contests", "Contexts", "Continents", "Contractors", "Contracts", "Contradictions", "Contraries", 
    "Contrasts", "Contributions", "Contributors", "Controls", "Controversies", "Conveniences", 
    "Conventions", "Conversations", "Conversions", "Convictions", "Cookers", "Cookings", "Coordinations", 
    "Coordinators", "Copies", "Coppers", "Copyrights", "Corners", "Corporations", "Corrections", 
    "Correlations", "Correspondences", "Correspondents", "Corridors", "Corruptions", "Costumes", 
    "Cottages", "Cottons", "Councillors", "Councils", "Counsellings", "Counsellors", "Counterparts", 
    "Counters", "Counties", "Countries", "Countrysides", "Counts", "Couples", "Courages", "Courses", 
    "Courtesies", "Courts", "Cousins", "Coverages", "Covers", "Cracks", "Crafts", "Crashes", "Creams", 
    "Creations", "Creativities", "Creators", "Creatures", "Credibilities", "Credits", "Crises", "Criteria", 
    "Criticisms", "Critics", "Critiques", "Crosses", "Crowds", "Crowns", "Cruises", "Crystals", "Cultures", 
    "Cupboards", "Curiosities", "Currencies", "Currents", "Curricula", "Curtains", "Custodies", "Customers", 
    "Customs", "Cuttings", "Cycles", "Dairies", "Damages", "Dancers", "Dances", "Dancings", "Dangers", 
    "Darknesses", "Databases", "Daughters", "Deadlines", "Dealers", "Debates", "Debris", "Debuts", "Decades", 
    "Decembers", "DecisionMakings", "Decisions", "Declarations", "Declines", "Decorations", "Decreases", 
    "Dedications", "Defaults", "Defeats", "Defects", "Defences", "Defenders", "Deficiencies", "Deficits", 
    "Definitions", "Degrees", "Delays", "Delegates", "Delegations", "Delights", "Deliveries", "Demands", 
    "Democracies", "Demons", "Demonstrations", "Denials", "Densities", "Dentists", "Departments", 
    "Departures", "Dependences", "Deployments", "Deposits", "Depressions", "Depths", "Deputies", "Descents", 
    "Descriptions", "Deserts", "Designers", "Designs", "Desires", "Desktops", "Destinations", 
    "Destructions", "Details", "Detections", "Detectives", "Detentions", "Determinations", 
    "Developments", "Devices", "Devils", "Diagnoses", "Diagrams", "Dialogues", "Diamonds", "Diaries", 
    "Dictators", "Dictionaries", "Differences", "Difficulties", "Dignities", "Dilemmas", "Dimensions", 
    "Dinners", "Diplomats", "Directions", "Directories", "Directors", "Disabilities", "Disadvantages", 
    "Disagreements", "Disappointments", "Disciplines", "Disclosures", "Discounts", "Discourses", 
    "Discoveries", "Discretions", "Discussions", "Dishes", "Dislikes", "Dismissals", "Disorders", 
    "Displays", "Disposals", "Disputes", "Disruptions", "Distances", "Distinctions", "Distresses", 
    "Distributions", "Districts", "Diversities", "Divides", "Divisions", "Divorces", "Doctors", "Doctrines", 
    "Documentaries", "Documentations", "Documents", "Dollars", "Domains", "Dominances", "Donations", "Donors", 
    "Doubts", "Downloads", "Downtowns", "Dozens", "Drafts", "Dramas", "Drawings", "Dreams", "Dresses", 
    "Drinks", "Drivers", "Drives", "Drivings", "Droughts", "Durations", "Duties", "Dynamics", "Earnings", "Earthquakes",
    "Earths", "Echoes", "Economics", "Economies", "Economists", "Editions", "Editors",
    "Educations", "Educators", "Effectivenesses", "Effects", "Efficiencies", "Efforts", "Elbows", "Elections",
    "Electricities", "Electronics", "Elements", "Elephants", "Elites", "Emails", "Embarrassments", "Embassies",
    "Emergences", "Emergencies", "Emissions", "Emotions", "Emphases", "Empires", "Employees", "Employers", 
    "Employments", "Encounters", "Encouragements", "Endeavours", "Endings", "Endorsements", "Enemies", 
    "Energies", "Enforcements", "Engagements", "Engineerings", "Engineers", "Engines", "Enquiries", "Enterprises", 
    "Entertainments", "Enthusiasms", "Enthusiasts", "Entities", "Entrances", "Entrepreneurs", "Entries", 
    "Envelopes", "Environments", "Epidemics", "Episodes", "Equalities", "Equals", "Equations", "Equipment", 
    "Equivalents", "Errors", "Escapes", "Essays", "Essences", "Establishments", "Estates", "Estimates", "Ethics", 
    "Evaluations", "Evenings", "Events", "Evidence", "Evolutions", "Examinations", "Examples", "Excellences", 
    "Exceptions", "Excesses", "Exchanges", "Excitements", "Exclusions", "Excuses", "Executives", "Exercises", 
    "Exhibitions", "Exhibits", "Exiles", "Existences", "Expansions", "Expectations", "Expeditions", "Expenditures", 
    "Expenses", "Experiences", "Experiments", "Expertises", "Experts", "Explanations", "Exploitations", 
    "Explorations", "Explosions", "Explosives", "Exports", "Exposures", "Expressions", "Extensions", "Extents", 
    "Extracts", "Extras", "Extremes", "Fabrics", "Facilities", "Factions", "Factories", "Factors", "Faculties", 
    "Failures", "Fairnesses", "Faiths", "Families", "Fantasies", "Farmers", "Farmings", "Fashions", "Faults", 
    "Favourites", "Favours", "Feathers", "Features", "Februaries", "Feedbacks", "Feelings", "Feminists", "Fences", 
    "Festivals", "Fevers", "Fibres", "Fictions", "Fields", "Fightings", "Fights", "Figures", "FilmMakers", "Filters", 
    "Finals", "Finances", "Findings", "Fingers", "Finishes", "Firefighters", "Fireworks", "Firsts", "Fishings", 
    "Fitnesses", "Fixtures", "Flames", "Flashes", "Flavours", "Fleets", "Fleshes", "Flexibilities", "Flights", 
    "Floods", "Floors", "Flours", "Flowers", "Fluids", "Flyings", "Followings", "Footages", "Footballs", "Forces", 
    "Forecasts", "Foreigners", "Forests", "Formations", "Formats", "Formulae", "Fortunes", "Forums", "Fossils", 
    "Foundations", "Founders", "Fractions", "Fragments", "Frames", "Frameworks", "Franchises", "Frauds", "Freedoms", 
    "Frequencies", "Fridays", "Fridges", "Friends", "Friendships", "Fronts", "Fruits", "Frustrations", "Functions", 
    "Fundings", "Fundraisings", "Funerals", "Furnitures", "Futures", "Galleries", "Gallons", "Gamblings", "Gamings",
    "Garages", "Gardens", "Gatherings", "Genders", "Generations", 
    "Genius", "Genres", "Gentlemen", "Geographies", "Gestures", "Ghosts", "Giants", "Glances", "Glasses", "Glimpses", 
    "Globalizations", "Globes", "Glories", "Gloves", "Goodbyes", "Goodnesses", "Governances", "Governments", "Governors", 
    "Graces", "Grades", "Graduates", "Grains", "Grandfathers", "Grandmothers", "Grandparents", "Grants", "Graphics", 
    "Grasps", "Grasses", "Graves", "Gravities", "Greenhouses", "Greens", "Griefs", "Groceries", "Grounds", "Groups", 
    "Growths", "Guarantees", "Guards", "Guerrillas", "Guesses", "Guests", "Guidances", "Guidelines", "Guides", "Guilts", 
    "Guitars", "Habitats", "Habits", "Halves", "Handfuls", "Handles", "Handlings", "Happinesses", "Harassments", "Harbours", 
    "Hardwares", "Harmonies", "Harvests", "Hazards", "Headaches", "Headlines", "Headquarters", "Healthcares", "Healths", 
    "Hearings", "Hearts", "Heatings", "Heavens", "Heights", "Helicopters", "Hellos", "Helmets", "Heritages", "Heroes", 
    "Hierarchies", "Highlights", "Highways", "Historians", "Histories", "Hobbies", "Hockeys", "Holidays", "Homelands", 
    "Homework", "Honesties", "Honours", "Horizons", "Horrors", "Horses", "Hospitals", "Hotels", "Households", "Houses", 
    "Housings", "Humanities", "Humans", "Humours", "Hungers", "Huntings", "Hurricanes", "Hurries", "Hydrogens", "Hypotheses", 
    "Ideals", "Identifications", "Identities", "Ideologies", "Ignorances", "Illusions", "Illustrations", "Imageries", 
    "Images", "Imaginations", "Immigrations", "Impacts", "Implementations", "Implications", "Importances", "Imports", 
    "Impressions", "Imprisonments", "Improvements", "Inabilities", "Incentives", "Inches", "Incidences", "Incidents", 
    "Inclusions", "Incomes", "Increases", "Independences", "Indications", "Indicators", "Indices", "Indictments", 
    "Individuals", "Industries", "Inequalities", "Infections", "Inflations", "Influences", "Information", "Infrastructures", 
    "Ingredients", "Inhabitants", "Initiatives", "Injections", "Injuries", "Injustices", "Innovations", "Inputs", "Inquiries", 
    "Insects", "Insertions", "Insiders", "Insides", "Insights", "Inspections", "Inspectors", "Inspirations", "Installations", 
    "Instances", "Instincts", "Institutes", "Institutions", "Instructions", "Instructors", "Instruments", "Insults", 
    "Insurances", "Intakes", "Integrations", "Integrities", "Intellectuals", "Intelligences", "Intensities", "Intentions", 
    "Intents", "Interactions", "Interests", "Interfaces", "Interferences", "Interiors", "Interpretations", "Intervals", 
    "Interventions", "Interviews", "Introductions", "Invasions", "Inventions", "Investigations", "Investigators", 
    "Investments", "Investors", "Invitations", "Involvements", "Ironies", "Islands", "Isolations", "Issues", "Jackets", 
    "Januaries", "Jazzes", "Jewelleries", "Joints", "Journalisms", "Journalists", "Journals", "Journeys", "Judgements", 
    "Judges", "Juices", "Julies", "Junctions", "Juries", "Jurisdictions", "Justices", "Justifications", "Keyboards", "Kidneys",
    "Kilometres", "Kingdoms", "Kisses", "Kitchens", "Knives", "Knocks", "Knowledges", 
    "Labels", "Laboratories", "Labours", "Ladders", "Landings", "Landlords", "Landmarks", "Landscapes", "Languages", 
    "Laptops", "Lasers", "Latests", "Laughs", "Laughters", "Launches", "Lawsuits", "Lawyers", "Layers", "Layouts", 
    "Leaders", "Leaderships", "Leaflets", "Leagues", "Learnings", "Leathers", "Leaves", "Lectures", "Legacies", "Legends", 
    "Legislations", "Legislatures", "Leisures", "Lemons", "Lengths", "Lessons", "Letters", "Levels", "Liberals", "Liberations", 
    "Liberties", "Libraries", "Licences", "Lifestyles", "Lifetimes", "Lightings", "Lights", "Likelihoods", "Limitations", 
    "Limits", "LineUps", "Liquids", "Listeners", "Listings", "Literacies", "Literatures", "Litres", "Litters", "Livers", 
    "Livings", "Lobbies", "Locals", "Locations", "Logics", "Lorries", "Losses", "Lotteries", "Loyalties", "Lunches", "Luxuries", 
    "Lyrics", "Machineries", "Machines", "Magazines", "Magics", "Magistrates", "Magnitudes", "Mainlands", "Mainstreams", 
    "Maintenances", "Majorities", "MakeUps", "Makings", "Managements", "Managers", "Mandates", "Manipulations", "Manners", 
    "Manufacturings", "Manuscripts", "Marathons", "Marches", "Margins", "Markers", "Marketings", "Marketplaces", "Markets", 
    "Marriages", "Masses", "Masters", "Matches", "Materials", "Mathematics", "Matters", "Maximums", "Mayors", "Meanings", 
    "Meantimes", "Measurements", "Measures", "Mechanics", "Mechanisms", "Medals", "Medications", "Medicines", "Meditations", 
    "Meetings", "Melodies", "Members", "Memberships", "Memoirs", "Memorials", "Memories", "Mentions", "Mentors", "Merchants", 
    "Mercies", "Mergers", "Merits", "Messages", "Messes", "Metals", "Metaphors", "Methodologies", "Methods", "Metres", "Middles", 
    "Midnights", "Midsts", "Migrations", "Minerals", "Miners", "Minimums", "Minings", "Ministers", "Ministries", "Minutes", 
    "Miracles", "Mirrors", "Miseries", "Missiles", "Missions", "Mistakes", "Mixtures", "Mobiles", "Mobilities", "Modifications", 
    "Momenta", "Moments", "Mondays", "Moneys", "Monitors", "Monkeys", "Monopolies", "Monsters", "Months", "Monuments", 
    "Moralities", "Morals", "Mornings", "Mortgages", "Mothers", "Motions", "Motivations", "Motives", "Motorcycles", "Motorists", 
    "Motors", "Mountains", "Mouths", "Movements", "Movies", "Muscles", "Museums", "Musicals", "Musicians", "Mysteries", 
    "Narratives", "Nationals", "Nations", "Natures", "Navigations", "Necessities", "Needles", "Negatives", "Neglects", 
    "Negotiations", "Neighbourhoods", "Neighbours", "Nerves", "Networks", "Newsletters", "Newspapers", "Niches", "Nightmares", 
    "Nights", "Noises", "Nominations", "Nominees", "Nonsenses", "Normals", "Norths", "Notebooks", "Notices", "Notions", 
    "Novelists", "Novels", "Novembers", "Numbers", "Nurseries", "Nurses", "Nursings", "Nutritions", "Obesities", "Objections", 
    "Objectives", "Objects", "Obligations", "Observations", "Observers", "Obsessions", "Obstacles", "Occasions", 
    "Occupations", "Occurrences", "Oceans", "Octobers", "Offences", "Offerings", "Offers", "Officers", "Offices", "Officials", 
    "Offspring", "Onions", "Openings", "Operas", "Operations", "Operators", "Opinions", "Opponents", "Opportunities", 
    "Opposites", "Oppositions", "Optimisms", "Options", "Oranges", "Orchestras", "Orders", "Organizations", "Organizers", 
    "Organs", "Orientations", "Originals", "Origins", "Outbreaks", "Outcomes", "Outfits", "Outings", "Outlets", "Outlines", 
    "Outlooks", "Outputs", "Outrages", "Outsiders", "Outsides", "Owners", "Ownerships", "Oxygens", "Packages", "Packets", "Painters",
    "Paintings", "Paints", "Palaces", "Panels", "Panics", "Papers", "Parades", 
    "Paragraphs", "Parallels", "Parameters", "Parents", "Parishes", "Parkings", "Parliaments", "Participants", 
    "Participations", "Parties", "Partners", "Partnerships", "Passages", "Passengers", "Passes", "Passings", "Passions", 
    "Passports", "Passwords", "Pastors", "Patches", "Patents", "Pathways", "Patiences", "Patients", "Patrols", "Patrons", 
    "Patterns", "Pauses", "Payments", "Peaces", "Peasants", "Penalties", "Pencils", "Pennies", "Pensions", "People", 
    "Peoples", "Peppers", "Percentages", "Perceptions", "Performances", "Periods", "Permissions", "Permits", "Personalities", 
    "Personnels", "Perspectives", "Petitions", "Petrols", "Phases", "Phenomena", "Philosophers", "Philosophies", "Phones", 
    "Photographers", "Photographies", "Photographs", "Photos", "Phrases", "Physicians", "Physics", "Pianos", "Pictures", 
    "Pieces", "Pilots", "Pioneers", "Pipelines", "Pirates", "Pitches", "Pities", "Placements", "Places", "Planes", "Planets", 
    "Plannings", "Plants", "Plastics", "Plates", "Platforms", "Players", "Pleasures", "Pledges", "Pockets", "Poetries", "Points", 
    "Poisons", "Police", "Policemen", "Policies", "Politicians", "Politics", "Pollutions", "Popularities", "Populations", 
    "Portfolios", "Portions", "Portraits", "Positions", "Positives", "Possessions", "Possibilities", "Posters", "Potatoes", 
    "Potentials", "Pounds", "Poverties", "Powders", "Powers", "Practices", "Practitioners", "Praises", "Prayers", "Precedents", 
    "Precisions", "Predators", "Predecessors", "Predictions", "Preferences", "Pregnancies", "Prejudices", "Premises", "Premiums", 
    "Preparations", "Prescriptions", "Presences", "Presentations", "Presents", "Preservations", "Presidencies", "Presidents", 
    "Presses", "Pressures", "Prevalences", "Preventions", "Prices", "Prides", "Priests", "Princes", "Princesses", "Principals", 
    "Principles", "Printers", "Printings", "Prints", "Priorities", "Prisons", "Privacies", "Privatizations", "Privileges", 
    "Prizes", "Probabilities", "Probes", "Problems", "Procedures", "Proceedings", "Proceeds", "Processes", "Processings", 
    "Processors", "Producers", "Produces", "Productions", "Productivities", "Products", "Professionals", "Professions", 
    "Professors", "Profiles", "Profits", "Programmes", "Programmings", "Programs", "Progresses", "Projections", "Projects", 
    "Promises", "Promotions", "Proofs", "Propagandas", "Properties", "Proportions", "Proposals", "Propositions", "Prosecutions", 
    "Prosecutors", "Prospects", "Prosperities", "Protections", "Proteins", "Protesters", "Protests", "Protocols", "Provinces", 
    "Provisions", "Psychologies", "Psychologists", "Publications", "Publicities", "Publics", "Publishings", "Pulses", "Punches", 
    "Punishments", "Pupils", "Purchases", "Purples", "Purposes", "Pursuits", "Pushes", "Puzzles", "Qualifications", "Qualities", 
    "Quantities", "Quarters", "Queens", "Queries", "Questionnaires", "Questions", "Quests", "Queues", "Quotas", "Quotations", 
    "Quotes", "Racings", "Radars", "Radiations", "Radios", "Railways", "Rallies", "Ranges", "Rankings", "Ratings", "Ratios", 
    "Reaches", "Reactions", "Readers", "Readings", "Realities", "Realizations", "Realms", "Reasonings", "Reasons", 
    "Rebellions", "Rebels", "Receipts", "Receivers", "Receptions", "Recessions", "Recipes", "Recipients", 
    "Recognitions", "Recommendations", "Reconstructions", "Recordings", "Records", "Recoveries", "Recruitments", 
    "Recruits", "Reductions", "Referees", "References", "Referendums", "Reflections", "Reforms", "Refusals", "Regards", 
    "Regimes", "Regions", "Registers", "Registrations", "Regrets", "Regulations", "Regulators", "Rehabilitations", 
    "Reigns", "Rejections", "Relations", "Relationships", "Relatives", "Releases", "Relevances", "Reliabilities", 
    "Reliefs", "Religions", "Remainders", "Remains", "Remarks", "Remedies", "Reminders", "Removals", "Rentals", "Repairs", 
    "Repeats", "Replacements", "Replies", "Reporters", "Reportings", "Reports", "Representations", "Representatives", 
    "Reproductions", "Republics", "Reputations", "Requests", "Requirements", "Rescues", "Researchers", "Researches", 
    "Reservations", "Reserves", "Residences", "Residents", "Residues", "Resignations", "Resistances", "Resolutions", 
    "Resorts", "Resources", "Respects", "Responses", "Responsibilities", "Restaurants", "Restorations", "Restraints", 
    "Restrictions", "Results", "Retails", "Retirements", "Retreats", "Returns", "Revelations", "Revenges", "Revenues", 
    "Reverses", "Reviews", "Revisions", "Revivals", "Revolutions", "Rewards", "Rhetorics", "Rhythms", "Rifles", "Rights", 
    "Rituals", "Rivals", "Rivers", "Robberies", "Robots", "Rockets", "Romances", "Rotations", "Rounds", "Routes", 
    "Routines", "Rubbers", "Rubbishes", "Rugbies", "Rulings", "Rumours", "Runners", "Runnings", "Rushes", "Sacrifices", 
    "Safeties", "Sailings", "Sailors", "Saints", "Salads", "Salaries", "Samples", "Sanctions", "Sandwiches", "Satellites", 
    "Satisfactions", "Saturdays", "Sauces", "Savings", "Scales", "Scandals", "Scares", "Scenarios", "Scenes", "Schedules", 
    "Schemes", "Scholars", "Scholarships", "Schools", "Sciences", "Scientists", "Scopes", "Scores", "Scratches", "Screams", 
    "Screenings", "Screens", "Screws", "Scripts", "Scrutinies", "Sculptures", "Searches", "Seasons", "Seconds", 
    "Secretaries", "Secrets", "Sections", "Sectors", "Securities", "Seekers", "Segments", "Selections", "Selves", 
    "Seminars", "Senators", "Sensations", "Senses", "Sensitivities", "Sentences", "Sentiments", "Separations", 
    "Septembers", "Sequences", "Series", "Servants", "Services", "Sessions", "SetUps", "Settings", "Settlements", 
    "Settlers", "Shades", "Shadows", "Shakes", "Shames", "Shapes", "Shareholders", "Shares", "Sheets", "Shells", 
    "Shelters", "Shelves", "Shifts", "Shippings", "Shirts", "Shocks", "Shootings", "Shoots", "Shoppings", "Shores", 
    "Shortages", "Shoulders", "Shouts", "Showers", "Siblings", "Sights", "Signals", "Signatures", "Significances", 
    "Silences", "Silver", "Similarities", "Simulations", "Singers", "Singings", "Singles", "Situations", "Sketches", 
    "Skiings", "Skills", "Skirts", "Skulls", "Sleeps", "Slices", "Slides", "Slogans", "Slopes", "Smartphones", "Smells", 
    "Smiles", "Smokes", "Smokings", "Snakes", "Soccers", "Societies", "Softwares", "Soldiers", "Solicitors", 
    "Solidarities", "Solids", "Solutions", "Sounds", "Sources", "Sovereignties", "Spaces", "Speakers", "Specialists", 
    "Species", "Specifications", "Specimens", "Spectacles", "Spectators", "Spectra", "Speculations", "Speeches", 
    "Speeds", "Spellings", "Spells", "Spendings", "Spheres", "Spices", "Spiders", "Spines", "Spirits", "Spites", 
    "Splits", "Spokesmen", "Spokespeople", "Sponsors", "Sponsorships", "Spoons", "Sports", "Spotlights", "Spouses", 
    "Spreads", "Springs", "Squads", "Squares", "Stabilities", "Stadiums", "Staffs", "Stages", "Stairs", "Stakes", "Stalls", 
    "Stamps", "Stances", "Standards", "Stands", "Starts", "Statements", "States", "Stations", "Statistics", "Statues", 
    "Status", "Steams", "Steels", "Stereotypes", "Sticks", "Stimuli", "Stocks", "Stomachs", "Stones", "Storages", 
    "Stores", "Stories", "Storms", "Strains", "Strands", "Strangers", "Strategies", "Streams", "Streets", "Strengths", 
    "Stresses", "Stretches", "Strikes", "Strings", "Strips", "Strokes", "Structures", "Struggles", "Students", "Studies", 
    "Studios", "Stuffs", "Styles", "Subjects", "Submissions", "Subscribers", "Subscriptions", "Subsidies", "Substances", 
    "Substitutes", "Substitutions", "Suburbs", "Successes", "Successions", "Successors", "Sufferings", "Sugars", 
    "Suggestions", "Suites", "Summaries", "Summers", "Summits", "Sundays", "Supermarkets", "Supervisions", 
    "Supervisors", "Supplements", "Supplies", "Supporters", "Supports", "Surfaces", "Surgeons", "Surgeries", "Surges", 
    "Surplus", "Surprises", "Surveillances", "Surveys", "Survivals", "Survivors", "Suspects", "Suspensions", 
    "Suspicions", "Sweaters", "Sweets", "Swimmings", "Swings", "Switches", "Swords", "Symbols", "Sympathies", 
    "Symptoms", "Syndromes", "Syntheses", "Systems", "TShirts", "Tables", "Tablets", "Tackles", "Tactics", "Talents", "Targets", "Tastes", "Taxpayers", "Teachers", 
    "Teachings", "Techniques", "Technologies", "Teenagers", "Telephones", "Televisions", "Temperatures", "Temples", 
    "Tenants", "Tendencies", "Tennis", "Tensions", "Tenures", "Terminals", "Terrains", "Territories", "Testimonies", 
    "Testings", "Textbooks", "Textures", "Thanks", "Theatres", "Thefts", "Themes", "Theologies", "Theories", "Therapies", 
    "Therapists", "Theses", "Thieves", "Things", "Thinkings", "Thirds", "Thoughts", "Threads", "Threats", "Thresholds", 
    "Throats", "Thumbs", "Thursdays", "Tickets", "Timbers", "Timings", "Tissues", "Titles", "Tobaccos", "Todays", "Toilets", 
    "Tolerances", "Tomatoes", "Tomorrows", "Tongues", "Tonights", "Tonnes", "Topics", "Tortoises", "Totals", "Touches", 
    "Tourisms", "Tourists", "Tournaments", "Towels", "Towers", "Traces", "Tracks", "Trademarks", "Trades", "Tradings", 
    "Traditions", "Traffics", "Tragedies", "Trailers", "Trails", "Trainers", "Trainings", "Trains", "Traits", "Transactions", 
    "Transcripts", "Transfers", "Transformations", "Transitions", "Transits", "Translations", "Transmissions", 
    "Transparencies", "Transportations", "Transports", "Traumas", "Travellers", "Travels", "Treasures", "Treaties", 
    "Treatments", "Trends", "Trials", "Tribes", "Tribunals", "Tributes", "Tricks", "Triggers", "Triumphs", "Troops", 
    "Trophies", "Troubles", "Trousers", "Trucks", "Trustees", "Trusts", "Truths", "Tsunamis", "Tuesdays", "Tuitions", 
    "Tunnels", "Turnouts", "Turnovers", "Twists", "Umbrellas", "Uncertainties", "Uncles", "Undergraduates", 
    "Understandings", "Underwears", "Unemployments", "Uniforms", "Unions", "Unities", "Universes", "Universities", 
    "Updates", "Upgrades", "Usages", "Utilities", "Vacations", "Vacuums", "Validities", "Valleys", "Values", "Variables", 
    "Variations", "Varieties", "Vegetables", "Vehicles", "Ventures", "Venues", "Verdicts", "Verses", "Versions", "Vessels", 
    "Veterans", "Victories", "Videos", "Viewers", "Viewpoints", "Villagers", "Villages", "Violations", "Violences", 
    "Virtues", "Viruses", "Visions", "Visitors", "Visits", "Vitamins", "Voices", "Volumes", "Volunteers", "Votings", 
    "Vulnerabilities", "Waiters", "Warehouses", "Warfares", "Warmings", "Warnings", "Warrants", "Warriors", "Washes", 
    "Washings", "Wastes", "Watches", "Waters", "Weaknesses", "Wealths", "Weathers", "Websites", "Weddings", "Wednesdays", 
    "Weekends", "Weights", "Welcomes", "Welfares", "WellBeings", "Wheels", "Whispers", "Wholes", "Widows", "Widths", 
    "Wildlives", "Willingnesses", "Windows", "Winners", "Winters", "Wisdoms", "Wishes", "Withdrawals", "Witnesses", 
    "Wonders", "Workers", "Workforces", "Workouts", "Workplaces", "Workshops", "Worlds", "Worries", "Worses", "Worships", 
    "Worsts", "Worths", "Wounds", "Wrists", "Writers", "Writings", "Wrongs", "Yellows", "Yesterdays", "Yields", "Zones"
]

#tapping the search bar is at position x & y.
SEARCH_BAR_X = 612
SEARCH_BAR_Y = 310

# Coordinates for tapping select all 
SELECT_ALL_X = 353  
SELECT_ALL_Y = 242  

# main code
def execute_adb_commands(word):
    # Send the word to the search bar
    os.system(f"{ADB_PATH} shell input text {word}")

    # Press Enter to simulate a search
    os.system(f"{ADB_PATH} shell input keyevent 66")  # Key event 66 is Enter
    time.sleep(0.1)

    # twice because buggy
    os.system(f"{ADB_PATH} shell input keyevent 66")  # Key event 66 is Enter
    time.sleep(0.1)

    # Simulate tapping the search bar (to focus on it before clearing the text)
    os.system(f"{ADB_PATH} shell input tap {SEARCH_BAR_X} {SEARCH_BAR_Y}")  # Tap the search bar
    time.sleep(0.1)


    # Simulates long tap on search bar to bring up context menu
    os.system(f"{ADB_PATH} shell input swipe {SEARCH_BAR_X} {SEARCH_BAR_Y} {SEARCH_BAR_X} {SEARCH_BAR_Y} 1000")  # Simulate a long tap (1s)
    time.sleep(0.1)

     # Simulate tapping "Select All" from the context menu
    os.system(f"{ADB_PATH} shell input tap {SELECT_ALL_X} {SELECT_ALL_Y}")  # Tap "Select All"
    time.sleep(0.1)  # Wait for the text to be selected


    # Simulate backspace to delete selected text
    os.system(f"{ADB_PATH} shell input keyevent 67")  # Backspace key event
    time.sleep(0.1)

# Loop through each word in the list
for word in words:
    execute_adb_commands(word)
    time.sleep(0.1)  # Wait a moment before processing the next word
