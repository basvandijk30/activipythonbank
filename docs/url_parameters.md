# URL parameters
## Pagination
0-indexed variabele om aan te geven waar de lijst start. Niet per pagina dus, maar per activiteit.
```js
start=0
```
## Zoekfilters
__Filter URL__: https://activiteitenbank.scouting.nl/component/k2/itemlist/filter

### Standaard parameters
```js
// Joomla
moduleId=119
Itemid=148 
// Zoekvelden
ftitle=zoekveld+titel
fitem_all=zoekveld+inhoud
```

### Filter parameters
Voor elke aangevinkte filter wordt een categorie ID meegestuurd in een array. 
```js
...&category[]=1&category[]=2...
```

#### Activiteitengebied
| id | categorie | opmerking |
|---|---|---|
|  4 | Buitenleven | |
|  5 | Expressie | |
|  7 | Identiteit | |
|  8 | Internationaal | |
|  9 | Samenleving | |
| 10 | Sport & Spel | |
| 11 | Uitdagende Scoutingtechnieken | |
| 12 | Veilig & Gezond | |

Extra parameters (kunnen niet aangevinkt worden als zoekfilter).
| id | categorie | opmerking |
|---|---|---|
| 2 | Uncategorised | Geen resultaten |
| 3 | Activiteitengebied | Naam van de set categoriën |
| 6 | Activiteit | |

#### Duur
| id | categorie | opmerking |
|---|---|---|
| 14 | 5-15 min | |
| 15 | 15-30 min | |
| 17 | 30 min - uur | |
| 18 | 1-2 uur | |
| 19 | 2-3 uur | |
| 20 | Halve dag | |
| 21 | Hele dag | |

Extra parameters (kunnen niet aangevinkt worden als zoekfilter)
| id | categorie | opmerking |
|---|---|---|
| 13 | Spelduur | Naam van de set categoriën |
| 22 | Meerdere dagdelen / opkomsten | |

#### Groepsgrootte
| id | categorie | opmerking |
|---|---|---|
| 24 | 1-8 personen | |
| 25 | 8-15 personen | |
| 26 | 15 of meer | |
| 27 | Groepsactiviteit | |
| 115 | Individueel | |

Extra parameters (kunnen niet aangevinkt worden als zoekfilter)
| id | categorie | opmerking |
|---|---|---|
| 23 | Groepsgrootte | Naam van de set categoriën |

#### Leeftijdsgroep
| id | categorie | opmerking |
|---|---|---|
| 29 | Bevers | |
| 30 | Welpen | |
| 31 | Scouts | |
| 32 | Explorers | |
| 33 | Rovers | |
| 34 | Kader | |
| 35 | Alle leeftijden | |

Extra parameters (kunnen niet aangevinkt worden als zoekfilter)
De leeftijdscategoriën in deze parameters geven andere activiteiten terug dan 29 t/m 35.
| id | categorie | opmerking |
|---|---|---|
| 28 | Leeftijdsgroep | Naam van de set categoriën |
| 58 | 5-7 bevers | |
| 59 | 7-11 welpen | |
| 60 | 11-15 scouts | |
| 61 | 15-18 explorers | |
| 62 | 18-21 roverscouts | |
| 63 | kader | |
| 64 | alle leeftijden | |

#### Locatie
| id | categorie | opmerking |
|---|---|---|
|  37 | Binnen | |
|  38 | Bos | |
|  39 | Buiten | |
|  40 | Grasveld | |
|  41 | Op & om het water | |
|  42 | Overig | |
|  43 | Rondom het clubhuis | |
|  44 | Stad | |
| 113 | Online | |
| 118 | 1,5 meter | |

Extra parameters (kunnen niet aangevinkt worden als zoekfilter)
| id | categorie | opmerking |
|---|---|---|
| 36 | Locatie | Naam van de set categoriën |

#### Awards
Extra parameters (kunnen niet aangevinkt worden als zoekfilter)
| id | categorie | opmerking |
|---|---|---|
| 45 | Awards | Naam van de set categoriën |
| 46 | Development award | |
| 47 | Nature award | |

#### Voorbereidingstijd
| id | categorie | opmerking |
|---|---|---|
| 49 | 5-15 min | |
| 50 | 15-30 min | |
| 51 | 30 min - uur | |
| 52 | 1 - 2 uur | |
| 53 | 2 - 3 uur | |
| 54 | Halve dag | |
| 55 | Hele dag | |
| 77 | Geen | |

#### Kampduur
Extra parameters (kunnen niet aangevinkt worden als zoekfilter)
| id | categorie | opmerking |
|---|---|---|
| 66 | Weekend (kampduur) | |
| 67 | Week (kampduur) | |
| 70 | Midweek (kampduur) | |
| 136 | 1 Nacht | |

#### Toekomstthema's
Extra parameters (kunnen niet aangevinkt worden als zoekfilter)
| id | categorie | opmerking |
|---|---|---|
|  89 | Toekomstthema's | Naam van de set categoriën |
|  95 | Open en divers | |
| 101 | Samenwerken en verbinden | |
| 104 | Trots en zichtbaar | |
| 107 | Vrijwilligers | |
| 110 | Ontwikkeling en uitdaging | |
| 113 | Online | |

#### Kwalificatie
| id | categorie | opmerking |
|---|---|---|
| 123 | CWO Sloep/Motorvlet | |
| 126 | CWO Buitenboordmotor | |
| 129 | CWO Roeiboot | |
| 132 | CWO Kielboot | |
| 135 | EHBO | |

#### Overig
Deze categoriën geven geen resultaten terug of hebben een onbekende functie.
| id | categorie | opmerking |
|---|---|---|
| 56 | Kampthema's | Geen resultaten |
| 72 | Stuiterbadge |Geen resultaten |
| 73 | Badges / Insignes | Geen resultaten |
| 76 | ? | Geeft alleen  "2048" terug |
| 83 | test | Geen resultaten |
