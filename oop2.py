#σε αυτό το παράδειγμα θα δημιουργήσουμε κλάσεις και αντικείμενα
#Θα βάλουμε δομές δεδομένων λίστες και σε κάθε λίστα
#θα προσθέσουμε πολλά αντικείμενα
#με τη συνάρτηση append()
#ορισμός κλάσης
class Piece:
    #ιδιότητες
    color=None;
    type=None;
    xposition=None;
    yposition=None;
    active=None;
    #κατασσκευαστής
    def __init__(self,color,type,xpos,ypos,active):
        self.color=color
        self.type=type
        self.xposition=xpos
        self.yposition=ypos
        self.active=active
    #μέθοδοι
    def move(self,x,y):
        self.xposition=x;
        self.yposition=y;
        print("Piece now at " + str(self.xposition) + str(self.yposition));
    def print_position(self):
        print(self.color+" "+self.type+" at "+str(self.xposition)+str(self.yposition)+" "+str(self.active));
#κυρίως πρόγραμμα
#δημιουργούμε 2 κενές λίστες μία για τα μαύρα και μία για τα άσπρα κομμάτια
white_pieces=[]
black_pieces=[]
#θα προσθέσουμε πιόνια
#θέσεις στον άξονα Χ
xpositions=["A","B","C","D","E","F","G","H"]
#για κάθε θέση στον άξονα Χ θα φτιάξουμε ενα λευκό και ενα μαύρο πιόνι
for i in range(8):
    piece=Piece("white","pawn",xpositions[i],2,True)
    white_pieces.append(piece)
    piece=Piece("black","pawn",xpositions[i],7,True)
    black_pieces.append(piece)
#θα φτιάξουμε λίστα για να τοποθετήσουμε τα υπόλοιπα κομμάτια με σωστή σειρά
#δημιουργία κομματιών
#σειρά κομματιών
piece_order=["rook","equus","bishop","queen","king","bishop","equus","rook"]
#για κάθε θέση στον άξονα Χ, θα επιλεχθεί και θα  δημιουργήσουμε το κατάλληλο κομμάτι
for k in range(8):
    piece=Piece("white",piece_order[k],xpositions[k],1,True)
    white_pieces.append(piece)
    piece=Piece("black",piece_order[k],xpositions[k],8,True)
    black_pieces.append(piece)
#εμφάνιση των αντικειμένων
for j in range(len(white_pieces)):
    white_pieces[j].print_position()
print("------------------------------")
for m in range(len(black_pieces)):
    black_pieces[m].print_position()
print("------------------------------")

