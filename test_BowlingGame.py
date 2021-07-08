import unittest
import BowlingGame

class test_BowlingGame(unittest.TestCase):

    def throw_many(self, game, number_of_times, pins):
        for _ in range(number_of_times):
            game.throw(pins)  #corrected indentation

    def test_all_gutters(self):
        game = BowlingGame()
        self.throw_many(game, 20, 0)
        game.calculate_score()
        self.assertEquals(game.score, 0)

    def test_perfect_game(self):
        game = BowlingGame()
        self.throw_many(game, 12, 10)
        game.calculate_score()
        self.assertEquals(game.score, 300)

    def test_all_ones(self):
        game = BowlingGame()
        number_of_times = 20
        pins = 1
        self.throw_many(game, number_of_times, pins)
        game.calculate_score()
        self.assertEquals(game.score, 20)

    def test_different_throws(self):
        game = BowlingGame()
        game.throw(6)
        game.throw(0)
        game.throw(7)
        game.throw(0)
        game.throw(2)
        for _ in range(15):
            game.throw(0)     #Corrected indentation
        game.calculate_score()
        self.assertEquals(game.score, 15)

    def test_for_spare(self):
        game = BowlingGame()
        game.throw(4)
        game.throw(6)
        game.throw(7)
        game.throw(0)
        for _ in range(16):
            game.throw(0)
        game.calculate_score()
        self.assertEquals(game.score, 24)

    def test_for_strike(self):
        game = BowlingGame()
        game.throw(10)
        game.throw(4)
        game.throw(2)
        self.throw_many(game, 17, 0)
        game.calculate_score()
        self.assertEquals(game.score, 22)

    # Testing to see that the score begins with zero
    def test_ScoreZero():
        ball = 0
        assert game.score() == 0
    '''This function takes the ball number which is at 0 and ensures that the score is 0
        :param ball: This is the base
        :param game.score(): This is the exponent
        :assert: The result of the test
    '''

    # Totalling the Score
    def test_CanAddScore(bowlinggame):
        bowlinggame.calculate_score(ball)
    '''This function takes the ball and calculates the score using the number of the ball
        :param test_CanAddScore: This is the base
        :param bowlinggame: This is the exponent
        :calculate_score: The result of the calculation
    '''

    # Testing to see if it's a Perfect Game
    def test_PerfectGame():
        self.throw_many(12, 10)
        retVal = game.score(300)
        assert retVal == "300"
    '''This function takes the max times the ball is thrown and returns with the max score
        :param self.throw_many(12, 10): This is the base
        :param retVal = game.score(300): This is the exponent
        :assert: The result of the calculation
    '''

    # Testing to see if all balls went into the Gutter
    def test_AllGutter():
        retVal = game.score(0)
        assert retVal == "0"
    '''This function takes the game score and returns a value of 0 to show that all balls thrown into gutter
        :param retVal: This is the base
        :param game.score(0): This is the exponent
        :assert: The result returns a "0"
    '''

    # Testing to see if score is all ones
    def test_AllOnes():
        retVal = game.score(0)
        assert retVal == "20"
    '''This function takes the game score and returns a value of 20 to show that all balls thrown for one score
        :param retVal: This is the base
        :param game.score(0): This is the exponent
        :assert: The result returns a "20"
    '''

    # Test standard game
    def test_simple_game(self):
        for pins in [6, 2, 2, 9, 5, 3, 3, 1,
                     5, 6, 2, 8, 8, 4, 4, 2, 4, 5, 2]:
            self.game.throw(pins)
        self.assertEqual(81, self.game.score())
    '''This function takes the pins scored and returns a total to match the result
        :param pins: This is the base
        :param self.game.throw(pins): This is the exponent
        :assert: The result returns an "81"
    '''

    #Help function to allow user to generate output of the above functions - need to add function within brackets ()
    print_help()