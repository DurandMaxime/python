
class Question:
    def __init__(self,question, reponse, nb_question,score):
        self.question = question
        self.reponse = reponse
        self.nb_question = nb_question
        self.score = score
    def poser_question(self):
        print("  QUESTION numero "+ str(self.nb_question+1) + " : " + self.question )
        for i in range(0,4):
            print(str(i+1) + " - " + str(liste_reponses[self.nb_question][i]))
            i += 1
        self.reponse = input("Votre réponse : ")
    def verifier_reponse(self):
        if  self.reponse.lower() or str(i+1) == bonne_reponse[self.nb_question].lower():
            print("Reponse correcte ")
            return True
        else:
            print("Reponse incorrecte ")
        

bonne_reponse = ["Paris", "Rome", "Bruxelles"]
score = 0 
nb_totale_questions = 3

question1 = Question("Quelle est la capitale de la France ? ","Paris ",0, score)
question2 = Question("Quelle est la capitale de l'Italie ? ","Rome ",1, score)    
question3 = Question("Quelle est la capitale de la Belgique ? ","Bruxelles",2, score )       
liste_question = [question1, question2, question3]
    #("Quelle est la capitale de la France ?",("Marseille","Nice","Paris","Nantes"),"Paris"),
    #("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"),"Rome")
liste_reponses = (("Marseille","Nice","Paris","Nantes"),
                 ("Rome", "Venise", "Pise", "Florence"),
                 ("Anvers", "Andenne", "Louvain", "Bruxelles")
                 )                   

                     




for i in liste_question:
    i.poser_question()
    if i.verifier_reponse():
        score = score + 1


print("Score final : " + str(score))
if score > nb_totale_questions/2:
    print("Pas mal")
if score == nb_totale_questions:
    print("Excellent ! ")
if score < nb_totale_questions/2 and score != 0:
    print("Peu mieux faire ")
if score == 0:
    print("Revisez votre géographie ")