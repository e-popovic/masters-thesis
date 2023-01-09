import os

class Evaluation:
  def __init__(self, age, sex, eyesight):
    self.age = age
    self.sex =  sex
    self.eyesight = eyesight
    self.data = {}
    self.pomocnavar = {}        # nenormalizirani podaci

class Result:
    def __init__(self, name, number_of_evals, sum_of_evals):
        self.name = name
        self.number_of_evals = number_of_evals
        self.sum_of_evals =  sum_of_evals

all_evaluations = []
results = []
file_results = open("subjectve_avg_calculated.txt", "a")

# ucitavanje podataka svih evaluatora
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
            # evaluation data
            if (line_count >= 2):      # ignoriramo prvi podatak, dok ljudi skuze kak funkcionira evaluiranje
                img_data = new_line.split('|')
                eval_value = int(img_data[1])
                img_names = img_data[0].split(':')

                # podaci: -50 (editana je bolja) <--> +50 (originalna je bolja)     
                eval_value -= 50
                if (max(img_names, key=len) != img_names[0]):
                    eval_value *= -1
                if (eval_value > max_val):
                    max_val = eval_value
                if (eval_value < min_val):
                    min_val = eval_value

            if (line_count == 48):  # zadnja linija zavrsena
                abs_limit = abs(max_val) if abs(max_val) > abs(min_val) else abs(min_val)
            
            line_count += 1

        line_count = 0
        for line in Lines:   
            new_line = line.strip()

            # evaluator personal info
            if (line_count == 0):
                evaluator_data = new_line.split('/')
                new_eval =  Evaluation(evaluator_data[0], evaluator_data[1], evaluator_data[2])

            # evaluation data
            elif (line_count >= 2):      # ignoriramo prvi podatak, dok ljudi skuze kak funkcionira evaluiranje
                img_data = new_line.split('|')
                eval_value = int(img_data[1])
                img_names = img_data[0].split(':')

                name_change_array = max(img_names, key=len).split('-', maxsplit=1)
                if (int(name_change_array[0]) > 2):
                    new_name = str(int(name_change_array[0]) - 1) + '-' + name_change_array[1]
                else:
                    new_name = max(img_names, key=len)

                # podaci: -50 (editana je bolja) <--> +50 (originalna je bolja)  
                # spremi u dict, key=ime editane slike   
                eval_value -= 50
                if (max(img_names, key=len) != img_names[0]):
                    eval_value *= -1
                
                new_eval.pomocnavar[new_name] = eval_value       # nenormalizirani podaci

                # (xi – min(x)) / (max(x) – min(x)) * 100
                new_eval.data[new_name] = (eval_value - abs_limit * -1) / (abs_limit * 2) * 100 - 50
           
            line_count += 1
        all_evaluations.append(new_eval)

        # print(new_eval.pomocnavar)    # nenormalizirani podaci
        # print(new_eval.data)
        # print(max_val)
        # print(min_val)

# iz evaluacija iscitaj sve rezultate
for evaluation in all_evaluations:
    for key in evaluation.data:
        exists = False

        for result in results:
            if (result.name == key):
                result.number_of_evals +=1
                result.sum_of_evals += evaluation.data[key]
                exists = True
        
        if (exists == False):
            new_result_entry = Result(key, 1, evaluation.data[key])
            results.append(new_result_entry)

# count = 0
# for evaluation in all_evaluations:
#     if (evaluation.sex == 'f'):
#         count+=1
# print(count) 

for result in results:
    file_results.write(result.name + '|' + str(result.sum_of_evals / result.number_of_evals) + '\n')