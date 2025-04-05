"""Deze module bevat Enums met de verschillende filter categoriën die gebruikt
kunnen worden in de activiteitenbank.
"""
from enum import Enum


class Activiteitengebied(Enum):
    """Het activiteitengebied waarbinnen de activiteit valt.
    """
    buitenleven = 4
    expressie = 5
    identiteit = 7
    internationaal = 8
    samenleving = 9
    sport_en_spel = 10
    uitdagende_scoutingtechnieken = 11
    veilig_en_gezond = 12


class Duur(Enum):
    """De tijdsduur van de activiteit.
    """
    vijf_tot_vijftien_min = 14
    vijftien_tot_dertig_min = 15
    dertig_min_tot_een_uur = 17
    een_tot_twee_uur = 18
    twee_tot_drie_uur = 19
    halve_dag = 20
    hele_dag = 21
    meerdere_dagdelen = 22


class Groepsgrootte(Enum):
    """Groepsgrootte voor de activiteit in personen.
    """
    een_tot_acht = 24
    acht_tot_vijftien = 25
    vijftien_of_meer = 26
    groepsactiviteit = 27
    # toevoeging(en) tijdens COVID-19
    individueel = 115


class Leeftijdsgroep(Enum):
    """Leeftijdsgroep waarvoor de activiteit geschikt is.
    Elke leeftijdsgroep heeft een 'extra'. Hier staan activiteiten die wel 
    binnen de leeftijdsgroep vallen, maar om een of andere reden niet in de 
    hoofdcategorie ingedeeld zijn.
    """
    bevers = 29
    bevers_extra = 58
    welpen = 30
    welpen_extra = 59
    scouts = 31
    scouts_extra = 60
    explorers = 32
    explorers_extra = 61
    rovers = 33
    rovers_extra = 62
    kader = 34
    kader_extra = 63
    alle_leeftijden = 35
    alle_leeftijden_extra = 64


class Locatie(Enum):
    """De locatie waar de activiteit zich afspeelt.
    """
    binnen = 37
    bos = 38
    buiten = 39
    grasveld = 40
    op_en_om_het_water = 41
    overig = 42
    rondom_het_clubhuis = 43
    stad = 44
    # toevoeging(en) tijdens COVID-19
    online = 113
    anderhalve_meter = 118

class Award(Enum):
    """Award waarvoor de activiteit als onderdeel gebruikt kan worden.
    """
    development_award = 46
    nature_award = 47


class Voorbereidingstijd(Enum):
    """De tijdsduur van het voorbereiden van de activiteit.
    """
    vijf_tot_vijftien_min = 49
    vijftien_tot_dertig_min = 50
    dertig_min_tot_een_uur = 51
    een_tot_twee_uur = 52
    twee_tot_drie_uur = 53
    halve_dag = 54
    hele_dag = 55
    geen = 77


class Kampduur(Enum):
    """De tijdsduur van het kamp.
    """
    weekend = 66
    week = 67
    midweek = 70
    nacht = 136


class Toekomstthema(Enum):
    """Het toekomstthema waarbinnen de activiteit valt.
    """
    open_en_divers = 95
    samenwerken_en_verbinden = 101
    trots_en_zichtbaar = 104
    vrijwilligers = 107
    ontwikkeling_en_uitdaging = 110

