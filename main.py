History={}
APi="xyz"
i=1
def update(x,y,i){
    History[f"user{i}"]=x
    History[f"bot{i}"]=y
    i+=1
}

def chat(input,instruction){
    #model initialization block
    model=0# just for logic dev
    model=[instruction]
    #if i=4
    for j in range(3:0:-1):
      context="User",History[f"user{i-j}"] ,"Bot",History[f"bot{i-j}"]

    input1=f"{context} User {input}"
    response=model(input1)
    update(input,response)
    return response
}

def Thinking_Model(input){
    ins="Defined as thinking logic"
    res , instruction =chat(input,ins)
    mainres=chat(res,instruction)
    resturn mainres
}
