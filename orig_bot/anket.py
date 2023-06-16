from tinydb import TinyDB

db = TinyDB('answers_db.json')
class Anket:
    def __init__(self, config):
        self.config = config
        self.length = len(config)


    def add_answers(self, answers: list):
        scores = 0
        for answer in answers:
            db.insert(answer)
            question_number = answer['questionNumber']
            qtype = self.config[question_number].get('type')
            right_answer = self.config[question_number].get('answer')
            qanswer = answer['answerText']
            if qtype == 'closed':
                scores += 1 if qanswer == right_answer else 0
        return scores

    def get_question(self, k):
        return self.config[k].get('text')