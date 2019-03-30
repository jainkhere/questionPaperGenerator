from questions_store import question_info

class selector:

    def select(self, questions, easy, medium, hard):
        easy_questions = self.find_subset(list(filter(lambda x : x["difficulty"] == "easy", questions)), easy)
        medium_questions = self.find_subset(list(filter(lambda x: x["difficulty"] == "medium", questions)), medium)
        hard_questions = self.find_subset(list(filter(lambda x: x["difficulty"] == "hard", questions)), hard)
        return easy_questions + medium_questions + hard_questions

    def find_subset(self, questions, total):
        '''
        The below function finds different subsets in the list of questions with marks summing up to the total marks
        for that particular section
        :param questions: list of questions
        :param total: total marks that should constitute the given section
        :return: list of selected questions
        '''
        n = len(questions)
        dp = []
        for i in range(n):
            ques_info = question_info(None, False, 0)
            dp.append([ques_info for j in range(total+1)])
        ques_info_zero = question_info(None, True, 0)
        dp[0][0] = ques_info_zero

        if int(questions[0]["marks"]) <= total:
            dp[0][int(questions[0]["marks"])] = question_info(questions[0]["id"], True, questions[0]["marks"])

        for i in range(1, n):
            for j in range(total + 1):
                if int(questions[i]["marks"]) <= j:
                    dp[i][j] = question_info(questions[i]["id"],
                                             dp[i-1][j - int(questions[i]["marks"])].is_selected or dp[i-1][j].is_selected,
                                             questions[i]["marks"])
                else:
                    dp[i][j] = dp[i-1][j]


        '''
        Get any one of the possible subset 
        if there exists one.
        Otherwise, raises an exception
        '''
        ques_ids = []
        if dp[n-1][total].is_selected:
            i = n - 1
            while total > 0 and i >= 0:
                while dp[i][total].is_selected and i >= 0:
                    i -= 1
                i += 1
                ques_ids.append(dp[i][total].question_id)
                total -= int(dp[i][total].question_marks)
                i -= 1
        else:
            raise ValueError('No possible subset exists according to given percentages')

        return list(filter(lambda x: x["id"] in ques_ids, questions))
