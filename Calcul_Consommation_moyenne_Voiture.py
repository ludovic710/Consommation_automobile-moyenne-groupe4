"""
Ce module définit la classe Voiture pour représenter les objets voitures.

La classe Voiture possède des attributs tels que la marque, le modèle, le kilométrage
et la quantité de carburant utilisée. Elle offre des méthodes pour parcourir des kilomètres,
ajouter du carburant et calculer la consommation moyenne de carburant.
"""

class Voiture:
    """
    Classe représentant une voiture.

   :param str marque: La marque de la voiture.
    :param str modele: Le modèle de la voiture.

    :ivar marque: La marque de la voiture.
    :ivar modele: Le modèle de la voiture.
    :ivar float kilometrage: Le total de kilomètres parcourus, initialisé à 0.
    :ivar float carburant_utilise: La quantité totale de carburant utilisé, initialisée à 0.
    """
    ## Méthode d'initialisation, appelée lors de la création d'une nouvelle instance
    def __init__(self, marque, modele):


        """
        Initialisation d'une nouvelle instance de :class:`Voiture`.

        :param str marque: Marque de la voiture.
        :param str modele: Modèle de la voiture.
        """
    
        self.marque = marque  
        self.modele = modele 
        self.kilometrage = (0)
        self.carburant_utilise = (0)

    # Méthode pour ajouter des kilomètres au compteur de la voiture
    def parcourir(self, km):
        """
        Ajoute des kilomètres au compteur de la voiture.

        :param float km: Le nombre de kilomètres à ajouter.
        """
        if km < 0:
            print("Les kilomètres doivent être un nombre positif.")
        else:
            self.kilometrage += km

    # Méthode pour ajouter du carburant
    def ajouter_carburant(self, litres):
       """
        Ajoute du carburant à la voiture.

        :param float litres: La quantité de carburant à ajouter.
        """
        
        if litres < 0:
            print("La quantité de carburant doit être un nombre positif.")
        else:
            self.carburant_utilise += litres
            # Ajout de la quantité de carburant à l'attribut d'instance carburant_utilise

    # Méthode pour calculer la consommation moyenne de gasoil
    def gasoil_burn(self):
        """
        Calcule la consommation moyenne de carburant.

        :return: La consommation moyenne de carburant formatée en litres aux 100 km.
        :rtype: str
        """
        
        if self.kilometrage == 0:
            return "Aucun kilomètre parcouru. Impossible de calculer la consommation."
        consommation_moyenne = (self.carburant_utilise / self.kilometrage) * 100
        return f"Consommation moyenne : {consommation_moyenne:.2f} litres aux 100 km"


# Utilisation de la classe
ma_voiture = Voiture(
    "Peugeot", "208"
)  # Création d'une nouvelle instance de la classe Voiture
ma_voiture.parcourir(500)  # Appel de la méthode parcourir pour ajouter 500 km
ma_voiture.ajouter_carburant(
    30
)  # Appel de la méthode ajouter_carburant pour ajouter 30 litres de carburant
print(ma_voiture.gasoil_burn())  # Affichage de la consommation moyenne de gasoil

"""
.. comment::

   Le mot-clé ``self`` en Python est utilisé dans les classes pour faire référence à l'instance actuelle de la classe.
   Il permet d'accéder et de manipuler les attributs spécifiques à chaque objet créé à partir de la classe,
   garantissant que les méthodes agissent sur les données propres à chaque instance plutôt que sur des variables globales.
   En bref, ``self`` est un moyen de se référer à l'objet actuel dans une classe.
"""
