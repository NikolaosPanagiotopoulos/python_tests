#σε αυτό το παράδειγμα θα δημιουργήσουμε κλάσεις και αντικείμενα
#ορισμός κλάσης
class Piece:
    #ιδιότητες
    color=None;
    type=None;
    xposition=None;
    yposition=None;
    active=None;
    #μέθοδοι
    def move(self,x,y):
        self.xposition=x;
        self.yposition=y;
        print("Piece now at " + str(self.xposition) + str(self.yposition));
#κυρίως πρόγραμμα
#δημιουργία αντικειμένου
white_pawn_1=Piece()
#ορίζουμε τιμές για τις ιδιότητες του αντικειμένου
white_pawn_1.xposition="A"
white_pawn_1.yposition="2"
#κλήση μεθόδου του αντικειμένου
white_pawn_1.move("A","3")
