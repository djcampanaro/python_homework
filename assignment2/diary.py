import traceback

try:
    with open('diary.txt', 'a') as diary:
        more_input = True
        first_question = True
        while more_input == True:
            if first_question == True:
                entry = input('What happened today? ')
                first_question = False
            elif first_question == False:
                entry = input('What else? ')
            if entry == 'done for now':
                diary.write(f'done for now \n\n')
                more_input = False
            else:
                diary.write(f'{entry} \n')
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")