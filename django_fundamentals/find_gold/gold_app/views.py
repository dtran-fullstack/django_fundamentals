from django.shortcuts import render, redirect
import random
from datetime import datetime

GOLD = {
    "farm":(10,20),
    "cave":(5,10),
    "house":(2,5),
    "casino":(0,50),
}

def index(request):
    if "total_gold" not in request.session or "activities" not in request.session:
        request.session['total_gold'] = 0
        request.session['activities']  = []
    return render(request,'index.html')    


def reset(request):
    request.session.clear()
    return redirect('/')

def process(request):
    if request.method == 'GET':
        return redirect('/')

    print (request.POST)
    # store the POST request when the form is submitted. 
    source_name = request.POST['source']
    # retrieve the amount which source can give in the GOLD dictionary, source_name is used for key
    source = GOLD[source_name]
    # random generate amount of gold from source
    gold_find = random.randint(source[0], source[1])
    # record time stamp when submit the form
    time_stamp = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    # construct message for activities logs
    log = f"Earned {gold_find} from the {source_name}! ({time_stamp})"

    result = "earn"

    # deal with special case where I can lose money in casino
    if source_name == "casino":
        if random.randint(0,1) > 0:
            log = f"Lost {gold_find} in {source_name}! ({time_stamp})"
            gold_find = gold_find * (-1)
            result = "lose"
    
    request.session['total_gold'] += gold_find
    request.session['activities'].append({"log":log, "result":result})
    return redirect('/')

