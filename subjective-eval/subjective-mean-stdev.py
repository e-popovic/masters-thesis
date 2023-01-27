import statistics
import os

class Evaluation:
  def __init__(self, age, sex, eyesight):
    self.age = age
    self.sex =  sex
    self.eyesight = eyesight
    self.data = {}

class Result:
    def __init__(self, name, first_grade):
        self.name = name
        self.all_grades = [first_grade]

all_evaluations = []
results = []
file_results = open("subjectve_mean+stdev.txt", "a")

for filename in os.scandir('odgovori'): 
    if filename.is_file():
        
        file = open(filename.path, 'r')
        Lines = file.readlines()

        line_count = 0
        max_val = -50
        min_val = 50
        abs_limit = 0
        for line in Lines:   
            new_line = line.strip()
            if (line_count >= 2):
                img_data = new_line.split('|')
                eval_value = int(img_data[1])
                img_names = img_data[0].split(':')  
                eval_value -= 50
                if (max(img_names, key=len) != img_names[0]):
                    eval_value *= -1
                if (eval_value > max_val):
                    max_val = eval_value
                if (eval_value < min_val):
                    min_val = eval_value
            if (line_count == 48): 
                abs_limit = abs(max_val) if abs(max_val) > abs(min_val) else abs(min_val)            
            line_count += 1

        line_count = 0
        for line in Lines:   
            new_line = line.strip()
            if (line_count == 0):
                evaluator_data = new_line.split('/')
                new_eval =  Evaluation(evaluator_data[0], evaluator_data[1], evaluator_data[2])
            elif (line_count >= 2):
                img_data = new_line.split('|')
                eval_value = int(img_data[1])
                img_names = img_data[0].split(':')

                name_change_array = max(img_names, key=len).split('-', maxsplit=1)
                if (int(name_change_array[0]) > 2):
                    new_name = str(int(name_change_array[0]) - 1) + '-' + name_change_array[1]
                else:
                    new_name = max(img_names, key=len) 
                eval_value -= 50
                if (max(img_names, key=len) != img_names[0]):
                    eval_value *= -1
                new_eval.data[new_name] = (eval_value - abs_limit * -1) / (abs_limit * 2) * 100 - 50          
            line_count += 1
        all_evaluations.append(new_eval)

for evaluation in all_evaluations:
    # if (evaluation.sex == 'f'):       # uncomment to choose only female/male results
        for key in evaluation.data:
            exists = False
            for result in results:
                if (result.name == key):
                    result.all_grades.append(evaluation.data[key])
                    exists = True       
            if (exists == False):
                new_result_entry = Result(key, evaluation.data[key])
                results.append(new_result_entry)   

# result file row:
# image-name|mean|stdev
for result in results:
    file_results.write(result.name + '|' + str(statistics.mean(result.all_grades)) + '|' + str(statistics.stdev(result.all_grades)) + '\n')