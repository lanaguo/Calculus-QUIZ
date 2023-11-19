from flask import Blueprint, render_template, request
import random

questions = Blueprint('questions', __name__)

dict_deri = {
    'n': ['0'],
    'x': ['1'],
    'x^n': ['n*(x^(n+1))', 'n*x^n+1'],
    'e^x': ['e^x'],
    'ln(x)': ['1/x'],
    'sin(n*x)': ['n*(cos(n*x))', 'n*cosn*x'],
    'cos(n*x)': ['-n*(sin(n*x))', '-n*sinn*x'],
    'tan(n*x)': ['n*sec(n*x)^2', 'nsecn*x^2'],
    'cosec(x)': ['-(cosec(x)cot(x))', '-cosecxcotx'],
    'sec(x)': ['(sec(x)tan(x))', 'secxtanx'],
    'cot(x)': ['-cosec(x)^2', '-cosecx^2'],
    'arcsin(x)': ['1/(1-x^2)^(1/2)', '1/1-x^2^1/2'],
    'arccos(x)': ['-1/(1-x^2)^(1/2)', '-1/1-x^2^1/2'],
    'arctan(x)': ['1/(1+x^2)', '1/1+x^2'],
    'n^x': ['(n^x)+ln(n)', 'n^x+lnn']
  }
# defining all rqs that this root can get (by default, only get)
@questions.route('/derivatives', methods=['GET', 'POST'])
def derivative_question():
  derivative_random = random.choice(list(dict_deri.keys()))
  return render_template("derivatives.html", question = derivative_random)
  
@questions.route('/verification_answer', methods=['GET', 'POST'])
def verification_answer():
  derivative_random = request.form.get('question')

  user_answer = None
  if request.method == 'POST':
    user_answer = request.form.get('user_answer')

  dict_deri = {
      'n': ['0'],
      'x': ['1'],
      'x^n': ['n*(x^(n+1))', 'n*x^n+1'],
      'e^x': ['e^x'],
      'ln(x)': ['1/x'],
      'sin(n*x)': ['n*(cos(n*x))', 'n*cosn*x'],
      'cos(n*x)': ['-n*(sin(n*x))', '-n*sinn*x'],
      'tan(n*x)': ['n*sec(n*x)^2', 'nsecn*x^2'],
      'cosec(x)': ['-(cosec(x)cot(x))', '-cosecxcotx'],
      'sec(x)': ['(sec(x)tan(x))', 'secxtanx'],
      'cot(x)': ['-cosec(x)^2', '-cosecx^2'],
      'arcsin(x)': ['1/(1-x^2)^(1/2)', '1/1-x^2^1/2'],
      'arccos(x)': ['-1/(1-x^2)^(1/2)', '-1/1-x^2^1/2'],
      'arctan(x)': ['1/(1+x^2)', '1/1+x^2'],
      'n^x': ['(n^x)+ln(n)', 'n^x+lnn']
  }
  def derivative(user_input):
    feedback = ""
    key_use = []
    correctAnswer = False
    if derivative_random not in key_use:
      if user_input is not None:
        user_input = user_input.replace("(", '')
        user_input = user_input.replace(")", '')
        user_input = user_input.replace(" ", "")
        if user_input in dict_deri[derivative_random]:
          correctAnswer = True
          key_use.append(derivative_random)
        else:
          key_use.append(derivative_random)
          feedback = dict_deri[derivative_random][0]
    return correctAnswer, feedback

  if user_answer is None:
    print("No answer provided")
    return render_template("verification_answer.html", correctAnswer=False)
  else:
    answer_for_user, feedback = derivative(user_answer)
    return render_template("verification_answer.html", correctAnswer = answer_for_user, feedback=feedback)

# @questions.route('/integrals')
# def integrals():
#     user_answer=None
#     if request.method == 'POST':
#       user_answer = request.form.get('user_answer')
    
#     dict_inter = {
#       'n': ['x+C'],
#       'x^n': ['((x^(n+1))/(n+1))+C', 'x^n+1/n+1+C'],
#       'sin(n*x)': ['(-cos(n*x)/n)+C', '-cosn*x/n+C'],
#       'cos(n*x)': ['(sin(n*x)/n)+C', 'sinn*x/n+C'],
#       'sec(n*x)^2': ['(tan(n*x)/n)+C', 'tann*x/n+C'],
#       'cosec(n*x)^2': ['(-cot(n*x)/n)+C', '-cotn*x/n+C'],
#       'sec(n*x)tan(n*x)': ['(sec(n*x)/n)+C', 'secn*x/n+C'],
#       'cosec(n*x)cot(n*x)': ['(-cosec(n*x)/n)+C', 'cosecn*x/n+C'],
#       'e^(n*x)': ['(e^(n*x)/n)+C', 'e^n*x/n+C'],
#       '1/n*x': ['(ln|x|/n)+C'],
#       'ln(n^x)': ['x*ln(n*x)+C', 'x*lnn*x+C'],
#       'n^x': ['(n^x/ln(n))+C', 'n^x/lnn+C']
#     }

#     def integral(user_input):
#       feedback=""
#       key_use = []
#       correctAnswer = False
#       integral_random = random.choice(list(dict_inter.keys()))
#       if integral_random not in key_use:
#         if user_input is not None:
#           user_input = user_input.replace("(", '')
#           user_input = user_input.replace(")", '')
#           user_input = user_input.replace(" ", "")
#           if user_input in dict_inter[integral_random]:
#             correctAnswer = True
#             key_use.append(integral_random)
#           else:
#             key_use.append(integral_random)
#             feedback = dict_inter[integral_random][0]
#       return correctAnswer

#    if user_answer is None:
#      print("No answer provided")
#      return render_template("derivatives.html")
#     else:
#       answer_for_user = derivative(user_answer)
#       return render_template("derivatives.html", correctAnswer = answer_for_user)
