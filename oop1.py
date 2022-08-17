#σε αυτό το παράδειγμα θα δημιουργήσουμε κλάσεις και αντικείμενα
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
        print("Piece is at "+str(self.xposition)+str(self.yposition));
#κυρίως πρόγραμμα        
#δημιουργία αντικειμένου
white_pawn_1=Piece("white","pawn","A","2","True")
#κλήση μεθόδου του αντικειμένου
white_pawn_1.print_position()
white_pawn_1.move("A","3")
white_pawn_1.print_position()
