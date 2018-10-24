from Bio import Align


aligner = Align.PairwiseAligner()


arq = open('../data/training_data.csv')

tabela = arq.readlines()

for i in range(1,len(tabela)):
	s1 = tabela[i]
	s1 = s1.split(',')
	pr1 = s1[2]
	rt1 = s1[3]
	for j in range(i+1,len(tabela)):		
		s2 = tabela[j]
		s2 = s2.split(',')
		pr2 = s2[2]
		rt2 = s2[3]
		prscore = aligner.score(pr1,pr2)
		rtscore = aligner.score(rt1,rt2)
		print(s1[0],end=',')
		print(s2[0],end=',')
		print(prscore,end=',')
		print(rtscore)
	
		

arq.close()
