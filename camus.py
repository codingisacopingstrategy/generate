import random

natuurbeschrijving = [
    'Een onweerslucht in augustus.',
    'Een dag met afwisselend wolken en zonneschijn.',
    'Elk vleugje wind is laaiend heet.',
    'Een koude met gele schitteringen.',
    'Die prachtige doorschijnende zon van gisteren.',
    'De baai trillend van licht.',
    'De zon op de kaden en de haven die danst van licht.',
    'Grijze lucht. Maar het licht dringt er doorheen.',
    'Prachtig is het licht dat uit de hemel neerdaalt.',
    'Beneden de rimpelloze zee.'
]

doorzetten = [
    'Geen enkele faktor van dit probleem uit de weg gaan.',
    'De moeilijkheden van de eenzaamheid dienen volledig te worden behandeld.',
    'Zich volledig inzetten.'
    'Wij zullen het klaarspelen.'
    ]

dood = [
    'Met doodslag is het laatste woord gesproken.',
    'Oog in oog kunnen sterven, zonder bitterheid.',
    'De dood die aan het spel en aan het heldendom hun ware zin geeft.',
    'Hij sterft zonder een enkele frase, de ogen vol tranen.'
    ]



def write(subject, verbosity = 0):
    tekst = ''
    random.shuffle(subject)
    for sentence in subject:
        tekst += sentence + ' '
        if random.random() > verbosity:
            break
    return tekst

print write(natuurbeschrijving,0.6) + write(doorzetten,0.7) + write(dood,0)
