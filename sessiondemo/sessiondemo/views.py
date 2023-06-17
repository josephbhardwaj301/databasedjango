from django.shortcuts import HttpResponse, render
import json
import request

def addsession(request):
    session = request.session
    data = request.GET["data"]
    request.session["1"] = data
    return render(request, "session.html", {"session": session["1"]})


def showsession(request):
    session = request.session

    print(session.get(1))
    print(request.session.items())
    return HttpResponse(str(session.get("1")))


def home(request):
    return HttpResponse("Home")


def sessioncounter(request):
    if request.session.get("counter") is None:
        counter = 0
    else:
        counter = int(request.session.get("counter"))
    counter += 1
    request.session["counter"] = counter
    return HttpResponse(str(counter))


def mcq(request):
    if request.session.get("qno") is None:
        qno = 0
    else:
        qno = 0
        qno = int(request.session.get("qno"))
        qno += 1
    questions = [("Which is the capital of UP?", "Lucknow", "Tokyo", "Paris", "Hukulganj", 1),
                 ("Which is the capital of Japan?", "Lucknow", "Tokyo", "Paris", "Hukulganj", 2),
                 ("Which is capital of Uttar Pradesh?", "Delhi", "Pune", "Kolkata", "Lucknow", 4)]
    n = len(questions)
    if request.GET:
        qno = int(request.GET["qno"])
        qno += 1
        if qno >= n:
            return HttpResponse("Quiz Over")
    for qno, correct_answer in questions:
        answer = input(f"{qno}? ")
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")
    question = questions[qno][0]
    opt1 = questions[qno][1]
    opt2 = questions[qno][2]
    opt3 = questions[qno][3]
    opt4 = questions[qno][4]
    return render(request, "counter.html",
                  {"qno": qno, "question": question, "opt1": opt1, "opt2": opt2, "opt3": opt3, "opt4": opt4})


def question(request):
    questions = [("Which is the capital of UP?", "Lucknow", "Tokyo", "Paris", "Hukulganj", 1),
                 ("Which is the capital of Japan?", "Lucknow", "Tokyo", "Paris", "Hukulganj", 2),
                 ("Which is the capital of India?", "Lucknow", "Tokyo", "Delhi", "Hukulganj", 3),
                 ("Which is the smallest (in area) of the following Union Territories?","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep",4)]
    result = ""
    noofquestions = len(questions)
    if request.session.get("score") is None:
        score = 0
    else:
        score = int(request.session.get("score"))
    if request.session.get("qno") is None:
        qno = -1
    else:
        qno = int(request.session.get("qno"))
    if request.GET:
        option = int(request.GET["opt"])
        actual_answer = questions[qno][5]
        if option == actual_answer:
            result = "Right"
            score += 1
            request.session["score"] = score
            print("Score is: ", score)
        else:
            result = "Wrong"
    print("Your answer is: ", result)
    qno += 1
    if qno > noofquestions - 1:
        # request.session.get("questions")
        request.session.pop("qno")
        request.session.pop("score")
        return render(request,"scoreresult.html",{"score":score})
        # return HttpResponse("Your answer is: ", questions)
    question = questions[qno][0]
    opt1 = questions[qno][1]
    opt2 = questions[qno][2]
    opt3 = questions[qno][3]
    opt4 = questions[qno][4]
    request.session["qno"] = qno
    request.session["score"] = score
    return render(request, "counterquestion.html",
                  {"qno": qno, "question": question, "question": question, "opt1": opt1, "opt2": opt2, "opt3": opt3,
                   "opt4": opt4, "questions": questions, "result": result, "score": score})
    return render(request,"scoreresult.html")
def boot(request):
