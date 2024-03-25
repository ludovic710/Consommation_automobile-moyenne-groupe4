import pytest 
from Calcul_Consommation_moyenne_Voiture import Voiture

#Fixture 
@pytest.fixture
def the_voiture():
    return Voiture("Peugeot", "208")

# test pour vérifier l'augmentation du kilométrage
def test_parcourir_augmente_kilometrage(the_voiture):
     the_voiture.parcourir(100)
     assert the_voiture.kilometrage == 100 ## vérifie si bien égal à 100

#Test pour vérifier l'ajout correct du carburant
def test_ajouter_carburant_augmente(the_voiture):
    the_voiture.ajouter_carburant(50)
    assert the_voiture.carburant_utilise == 50
  
#Test pour essayer d'ajouter un résultat négatif 
def test_ajouter_carburant_valeur_negative(the_voiture):
    the_voiture.ajouter_carburant(-50)
    assert the_voiture.carburant_utilise == 0

#Test pour vérifier le comportement avec des valeurs négatives de kilométrage
def test_parcourir_valeur_negative(the_voiture):
    the_voiture.parcourir(-100)
    assert the_voiture.kilometrage == 0 

