import question_selector
import paper_generator
from questions_store import questions_store


def create_exam_paper(total, easy, medium, hard):
    questions = questions_store("data/questions.json").load_questions()
    selector = question_selector.selector()

    try:
        selected_questions = selector.select(questions, easy, medium, hard)
    except ValueError as e:
        print(e)
        print("Unable to create Question Paper")
        exit()

    generator = paper_generator.generator()
    if generator.write_to_doc(selected_questions) == True:
        print("Question paper generated successfully! Please check the output folder")
    else:
        print("Error occurred while generating the Question Paper")

if __name__ == "__main__":
    total = int(input("Please enter Total marks: "))
    section_percentages = list(map(int, input("Please enter space separated percentages of easy, medium and hard questions in order: ").split()))
    if sum(section_percentages) != 100:
        print("Incorrect division of sections! Please provide correct divisions")
        exit()

    # Get section wise marks from percentage values
    section_marks = list(map(lambda x : (total * x)//100, section_percentages))
    create_exam_paper(total, section_marks[0], section_marks[1], section_marks[2])


