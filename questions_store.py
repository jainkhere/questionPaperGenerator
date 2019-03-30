import json

class questions_store:
    def __init__(self, file_name):
        self.data_file = file_name

    def load_questions(self):
        self.items = []
        try:
            with open(self.data_file) as f:
                data = json.loads(f.read())
                self.items = data
                return self.items
        except Exception:
            print("Couldn't read data from store")


class question_info:

    '''
    data structure to store information about questions in the DP matrix
    '''

    def __init__(self, question_id, is_selected, question_marks):
        self.question_id = question_id
        self.question_marks = question_marks
        self.is_selected = is_selected
