#68ms
N =int(input())
list_num = list(map(int,input().split()))
count=0

for i in range(N):
  if list_num[i]%2 ==0:
    if list_num[i] ==2:
      count=count+1 
    else:
      pass 
  elif list_num[i]== 1:
    pass
      
  elif list_num[i]%3 ==0:
    if list_num[i]==3:
      count=count+1
    else:

      pass
  elif list_num[i]%5 ==0:
    if list_num[i]==5:
      count=count+1 
    else:
      pass

  elif list_num[i]%7 ==0:
    if list_num[i]==7:
      count=count+1 
    else:

      pass   
  elif list_num[i]%11 ==0:
    if list_num[i]==11:
      count=count+1 
    else:

      pass   
    
  elif list_num[i]%13 == 0:
    if list_num[i]==13:
      count=count+1 
    else:

      pass   
    
  elif list_num[i]%17 ==0:
    if list_num[i]==17:
      count=count+1 
    else:

      pass   

    
  elif list_num[i]%19 ==0:
    if list_num[i]==19:
      count=count+1 
    else:

      pass   

  elif list_num[i]%23==0:
    if list_num[i]==23:
      count=count+1 
    else:

      pass   


    
  elif list_num[i]%29==0:
    if list_num[i]==29:
      count=count+1 
    else:

      pass   

  elif list_num[i]%31==0:
    if list_num[i]==31:
      count=count+1 
    else:

      pass   

  elif list_num[i]%37==0:
    if list_num[i]==37:
      count=count+1 
    else:

      pass   

  elif list_num[i]%41==0:
    if list_num[i]==41:
      count=count+1 
    else:

      pass   
  elif list_num[i]%47==0:
    if list_num[i]==47:
      count=count+1 
    else:
  
      pass   
  elif list_num[i]%53==0:
    if list_num[i]==53:
      count=count+1 
    else:

      pass   
  elif list_num[i]%59==0:
    if list_num[i]==59:
      count=count+1 
    else:

      pass   
  elif list_num[i]%69==0:
    if list_num[i]==69:
      count=count+1 
    else:

      pass   

  elif list_num[i]%73==0:
    if list_num[i]==73:
      count=count+1 
    else:

      pass   
  elif list_num[i]%79==0:
    if list_num[i]==79:
      count=count+1 
    else:

      pass   
  elif list_num[i]%83==0:
    if list_num[i]==83:
      count=count+1 
    else:
  
      pass   
  elif list_num[i]%83==0:
    if list_num[i]==83:
      count=count+1 
    else:

      pass   
  elif list_num[i]%97==0:
    if list_num[i]==97:
      count=count+1 
    else:

      pass   

  else:
    count=count+1  
print(count)