from Question import Question


quiz_questions =[
    "Which continent is the largest?\n(a) Africa\n(b) Asia\n(c) America\n(d) Europe\n\n",
    "Which element has 12 proton?\n(a) Carbon\n(b) Aluminium\n(c) Magnesium\n(d) Copper\n\n",
    "Where is Boqojjii located?\n(a) Harerge\n(b) Welega\n(c) Guji\n(d) Arsi\n\n",
    "Which one is cultural dance of Oromo Walloo?\n(a) Kumkummee\n(b) Daddadayisaa\n(c) Tirrii\n(d) None \n\n",
    "Where is Haro wanci located?\n(a) Near Ambo\n(b) Near Adama\n(c) near Shambu\n(d) Near Shashamane\n\n",
]


questions =[
    Question(quiz_questions[0], "b"),
    Question(quiz_questions[1], "a"),
    Question(quiz_questions[2], "d"),
    Question(quiz_questions[3], "d"),
    Question(quiz_questions[4], "a"),
]


def Test(questions):
    score =0
    for question in questions:
        answer =input(question.prompt)
        if answer == question.answer:
            score += 1
    print ("You have answered "+ str(score)+"/"+str(len(questions)))

Test(questions)
