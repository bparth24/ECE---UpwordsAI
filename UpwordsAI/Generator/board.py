# -*- coding: utf-8 -*-

'''
it will use to genearte next move and handle the board so methos will be

to generate board String[][]
getstatus from rack and board
generateword
validate(word,score,timing)
check upwordrules

'''
class Board:
    
    #DEBUG_ERRORS = True
    Debug_errors = True
    BOARD_SIZE = 10      #   Size in # of squares.
    START_POSITION = [(4, 4), (4, 5), (5, 4), (5, 5)]
    
    '''
    Initialize the board, create the squares matrix.
    '''
    def __init__(self):
        

    '''
    Returns the temporary tiles on the board and returns them as a list.
    '''
    def removeTempTiles(self):
        inPlay = []
        for x in range(Board.BOARD_SIZE):
            for y in range(Board.BOARD_SIZE):
                if self.tiles[x][y][0] != None and not self.tiles[x][y][0].locked:     
                    inPlay.append(self.tiles[x][y][0])
                    self.tiles[x][y] = (None, self.tiles[x][y][1])
        
        #   Remove the locks the player can play again
        self.columnLock = -1
        self.rowLock = -1
        
        return inPlay
    
    '''
    
    This function works by going through all tentative tiles on the board, validating the move and then processing the play.
    The return value is a tuple of (tiles, points) with the former being returned tiles in a move failure and the latter being the score in the case of success.
    
    In success, the tiles are locked, in failure, the tiles are removed entirely.
    
    Validation Rules:
    1) At least one tile must be tentative.
    2) All tentative tiles must lie on one line.
    3) On the first turn, one tile must be located on square START_POSITION.
    4) Linear word must be unbroken (including locked tiles)
    5) On every other turn, at least one crossword must be formed.
    6) All words formed must be inside the dictionary.
    
    '''
    def play(self, isFirstTurn = True):
        
        #   Collect all tentative tiles.
        inPlay = []
        for x in range(Board.BOARD_SIZE):
            for y in range(Board.BOARD_SIZE):
                if self.tiles[x][y][0] != None and not self.tiles[x][y][0].locked:
                    inPlay.append((x, y))
        
        #   Validation step one: There must be at least one tile played.
        if len(inPlay) <= 0:
            #   Fail
            if Board.Debug_errors:
                print('Play requires at least one tile.')
            return ([], -1)
        
        #   Validation step two: Tiles must be played on a straight line.
        col = inPlay[0][0]
        row = inPlay[0][1]
        inAcol = True
        inArow = True
        for (x, y) in inPlay:
            if(x != col):
                inAcol = False
            if(y != row):
                inArow = False
        
        if not inArow and not inAcol:
            #   Fail, remove tiles and return
            if Board.Debug_errors:
                print('All tiles must be placed along a line.')
            return (self.removeTempTiles(), -1)
        
        #   Validation step three: If isFirstMove, then one tile must be on START_POSITION
        if not Board.START_POSITION in inPlay and inFirstMove:
            return(self.removeTempTiles(), -1)
        
        
        #   Validation step four: Word created is unbroken.
        unbroken = True
        left = col
        right = col
        top = row
        bottom = row
        
        
        #   Determine the span of the word in either up/down or left/right directions.
        for (x, y) in inPlay:
            if x < left:
                left = x
            elif x > right:
                right = x
            if y < top:
                top = y
            elif y > bottom:
                botootm = y
        
        
        #   Confirm that the span is unbroken
        if inAcol:
            for y in range(top, bottom + 1):
                if self.tiles[col][y][0] == None:
                    unbroken = False
        elif inArow:
            for x in range(left, right + 1):
                if self.tiles[x][row][0] == None:
                    unbroken = False
        
        if not unbroken:
            return(self.removeTempTiles(), -1)
        
        
        #   Validation steps five and six:
        (totalScore, spellings, seedRation) = self.validateWords(isFirstMove, inPlay = inPlay)
        
    
        if spellings != None:
            for spelling in spellings:
                self.wordfreq.wordPlayed(spelling)
            
            self.wordfreq.save()
            
            
        #   Lock tiles played
        for (x, y) in inPlay:
            self.tiles[x][y][0].locked = True
        
        
        #   Remove the locks on the board.
        self.columnLock = -1
        self.rowLock = -1
        
        return (None, totalScore)