import random #Importerar biblioteket random för att kunna dra slumpmässiga kort.
#Definerar en klass som representerar spelet

class Kortspel:
#en dictionary som representerar värdet av varje kort
    kort_värden: dict[str,int]= {
       " ess": 1,
       "2":2,
       "3":3,
       "4":4,
       "5":5,
       "6":6,
       "7":7,
       "8":8,
       "9":9,
       "10":10,
       "Knekt":11,
       "Dam":12,
       "kung":13
       }
    
#-Den här metoden startar spelarens och datorns poäng.
    def __init__(self) -> None:
        self.spelarens_poäng = 0# spelarens poäng startar med 0
        self.datorns_poäng = 0# datorns poäng startar med 0
        self.spelare_förlorade= False #flagga för att kontrollera om spelaren har förlorat.

    def dra_kort(self) -> tuple[str,int] : #metod för att dra ett slumpmässigt kort och retunerar en tupel som innehåller kortets namn och dess värde
        kort_namn: str = random.choice(list(self.kort_värden)) #slumpmässigt kort
        kort_värde: int = self.kort_värden[kort_namn]# Hämtar värdet utav kortet
        return kort_namn,kort_värde
    
    #metod för spelarens tur, där får den dra kort tills hen väljer att sluta eller går över 21
    def spela_spelare(self)-> None:
        while True: # loop tills att spelaren antigen får över 21 eller slutar.
            kort_namn, kort_värde = self.dra_kort()# drar ett kort
            self.spelarens_poäng += kort_värde# lägger till kortets värde till spelarens poäng
            print(f"Du drog {kort_namn} ({kort_värde}), din totala poäng är {self.spelarens_poäng}")

            if self.spelarens_poäng > 21:
                print("Du fick mer än 21, Datorn vinner!")
                self.spelare_förlorade = True
                return# avslutar spelaren tur
            
            fortsätta: str = input("Vill dra ett till kort? (ja/nej): ").lower()# frågar spelaren om den vill dra ett till kort
            if fortsätta != "ja":# om svaret inte är lika med ja så avslutas loopen.
                break

#metod för datorns tur, där datorn slår spelarens poäng eller har minst fått 17 poäng.
    def spela_dator(self) -> None:
        while self.datorns_poäng < 17 and self.datorns_poäng < self.spelarens_poäng:
            kort_namn, kort_värde = self.dra_kort()
            self.datorns_poäng += kort_värde
            print(f"Datorn drog { kort_namn} ({kort_värde}), datorns totala poäng är nu {self.datorns_poäng}")

#metod för att avgöra ve, som vann, den jämför spelarens och datorns poäng 
    def avgör_vinnare(self) -> None:
        #kontrollerar om spelaren förlorade och då skrivs inget mer
        if self.spelare_förlorade:
            #om flaggan går över till true så kommer programmet att hoppa över resten av koden och då skrivs inte samma text 2 gånger. 
            #så self.spelare_ är en felhantering, i med att jag märkte att det skrev dubbelt meddelande när datorn vann
            return
        
        if self.spelarens_poäng > 21:
            print("Du fick mer än 21. Datorn vinner")
        elif self.datorns_poäng > 21:# om datorns poäng går över 21 så vinner spelaren och detta skrivs ut för spelaren.
            print(" Datorn fick mer än 21. Du vinner!")
        elif self.datorns_poäng >= self.spelarens_poäng:# om datorns poäng är högre eller lika med spelarens så vinner datornoch det skrivs ut.
            print("Datorn vinner!")
        else:# om spelarens poäng är högre, vinner spelaren.
            print("Du vinner")

#här startar spelet genom att skapa en instans av klassen Kortspel.
if __name__ == "__main__":
    spel = Kortspel()#här skapas ett objekt av klassen Kortspel.
#spelarens tur att dra kort
    spel.spela_spelare()
# om spelaren inte har förlorat, alltså att den har 21 eller mindre poäng så är det datorns tur att dra.
    if not spel.spelare_förlorade:
        print("Nu är det datorns tur")
        spel.spela_dator()
# avgör vem som vann spelet.
    spel.avgör_vinnare()