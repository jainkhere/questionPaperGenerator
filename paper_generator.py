import docx

class generator:
    def __init__(self):
        self.doc = docx.Document()

    def write_to_doc(self, questions):
        i = 1
        for question in questions:
            ques_text = question["statement"] + " (" + question["marks"] + " marks)"
            self.doc.add_paragraph("(id: " + str(question["id"]) + ") " "Q" + str(i) + ". " + ques_text)
            i += 1

        try:
            self.doc.save("Exam_paper.docx")
            return True
        except Exception:
            return False
