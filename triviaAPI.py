from pytrivia import Category, Diffculty, Type, Trivia
import time

from config import question_points_easy, question_points_medium, question_points_hard, question_points_time_coef, game_difficulty, game_category

class TriviaAPI:
    def __init__(self):
        self.question = dict()
        self.accept_answers = True
        self.points = 0
        self.time_elapsed = int(time.time())

    def generateQuestion(self):
        my_api = Trivia(True)
        self.question = my_api.request(1, game_category, game_difficulty, Type.Multiple_Choice)

        self.accept_answers = True

        self.time_elapsed = int(time.time())

        if self.question['results'][0]['difficulty'] == 'easy':
            self.points = question_points_easy
        elif self.question['results'][0]['difficulty'] == 'medium':
            self.points = question_points_medium
        elif self.question['results'][0]['difficulty'] == 'hard':
            self.points = question_points_hard

        print(self.question['results'][0]['correct_answer'])

    def getPoints(self):
        self.points = self.points - question_points_time_coef * (int(time.time()) - self.time_elapsed)
        return self.points

    def setAccept_answersOff(self):
        self.accept_answers = False

    def getAccept_answers(self):
        return self.accept_answers

    def getQuestion(self):
        return self.question['results'][0]['question']

    def getAnswer(self):
        return self.question['results'][0]['correct_answer']

    def getCategory(self):
        return self.question['results'][0]['category']
