answer={'привет':'и тебе привет','как дела?':"лучше всех",'пока':'увидимся'}
def  get_answer(question,answer):
	return answer[question]
	


word=input('write word ')
print(get_answer(word,answer).upper())
