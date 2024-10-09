class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # use single list to rep 3*3 board, 
        #biến _ sẽ nhận các giá trị từ 0 đến 8
        #self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.current_winner = None #keep track of winner

    def print_board(self):
        #in ra bàn cờ của trò chơi(Tic-Tac-Toe)
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            #Khi i = 0: self.board[0*3:(0+1)*3] => self.board[0:3] => ['X', 'O', ' ']
            #Khi i = 1: self.board[1*3:(1+1)*3] => self.board[3:6] => ['X', ' ', 'O']
            #Khi i = 2: self.board[2*3:(2+1)*3] => self.board[6:9] => [' ', 'X', 'O']
            #[['X', 'O', ' '], ['X', ' ', 'O'], [' ', 'X', 'O']]
            #for row in [['X', 'O', ' '], ['X', ' ', 'O'], [' ', 'X', 'O']]:
            # trong ba lần lặp, row sẽ lần lượt có giá trị:
            # Lần 1: row = ['X', 'O', ' ']
            # Lần 2: row = ['X', ' ', 'O']
            # Lần 3: row = [' ', 'X', 'O']
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod #phương thức này không cần tham chiếu đến đối tượng (self), 
    #có thể được gọi mà không cần phải tạo một instance của lớp chứa nó.
    def print_board_nums():
        # what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1) * 3)] for j in range(3)]
        #for j in range(3): Vòng lặp này chạy ba lần, từ 0 đến 2. Mỗi giá trị của j đại diện cho một hàng trong bàn cờ.
        # range(j*3, (j+1) * 3),Đối với mỗi hàng, range được sử dụng để tạo ra ba số tương ứng với ba ô trong hàng đó:
        #str(i): Mỗi số được chuyển đổi thành chuỗi để dễ dàng hiển thị sau này.
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |') #[['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] == letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
            
        return False
        

    
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'
            


        if print_game:
            print('It\'s a tie!')









