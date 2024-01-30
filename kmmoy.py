# Définition de la classe Voiture
class Voiture:
    # Méthode d'initialisation, appelée lors de la création d'une nouvelle instance
    def __init__(self, marque, modele):
        self.marque = marque            # Attribut d'instance pour la marque de la voiture
        self.modele = modele            # Attribut d'instance pour le modèle de la voiture
        self.kilometrage = 0            # Attribut d'instance pour le kilométrage initialisé à zéro
        self.carburant_utilise = 0      # Attribut d'instance pour la quantité de carburant initialisée à zéro
 
    # Méthode pour ajouter des kilomètres au compteur de la voiture
    def parcourir(self, km):
        if km < 0:
            print("Les kilomètres doivent être un nombre positif.")
        else:
            self.kilometrage += km      # Ajout de kilomètres à l'attribut d'instance kilometrage
 
    # Méthode pour ajouter du carburant
    def ajouter_carburant(self, litres):
        if litres < 0:
            print("La quantité de carburant doit être un nombre positif.")
        else:
            self.carburant_utilise += litres   # Ajout de la quantité de carburant à l'attribut d'instance carburant_utilise
 
    # Méthode pour calculer la consommation moyenne de gasoil
    def Gasoil_burn(self):
        if self.kilometrage == 0:
            return "Aucun kilomètre parcouru. Impossible de calculer la consommation."
        consommation_moyenne = (self.carburant_utilise / self.kilometrage) * 100
        return f"Consommation moyenne : {consommation_moyenne:.2f} litres aux 100 km"
 
# Utilisation de la classe
ma_voiture = Voiture("Peugeot", "208")  # Création d'une nouvelle instance de la classe Voiture
ma_voiture.parcourir(500)                # Appel de la méthode parcourir pour ajouter 500 km
ma_voiture.ajouter_carburant(30)         # Appel de la méthode ajouter_carburant pour ajouter 30 litres de carburant
print(ma_voiture.Gasoil_burn())          # Affichage de la consommation moyenne de gasoil
 
 
 
 
# Le mot-clé self en Python est utilisé dans les classes pour faire référence à l'instance actuelle de la classe.
# Il permet d'accéder et de manipuler les attributs spécifiques à chaque objet créé à partir de la classe,
#garantissant que les méthodes agissent sur les données propres à chaque instance plutôt que sur des variables globales.
# En bref, self est un moyen de se référer à l'objet actuel dans une classe.