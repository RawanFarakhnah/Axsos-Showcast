from django.shortcuts import render, redirect
from random import randrange
from datetime import datetime

# game_setup view
def game_setup(request):
    if request.method == 'GET':
        return render(request, 'setup.html')
    
    if request.method == 'POST':
        # Get POST data or use default values if missing
        player_name = request.POST.get('player_name')
        goal_gold = request.POST.get('goal_gold')
        attempts = request.POST.get('attempts')

        # Set session values
        request.session['player_name'] = 'Guest player' if not player_name else player_name
        request.session['goal_gold'] = 40 if not goal_gold else int(goal_gold)
        request.session['attempts'] = 10 if not attempts else int(attempts)
        request.session['gold'] = 0

        # Initialize activities only if not already set
        if 'activities' not in request.session:
            request.session['activities'] = []  # Initialize if not present

        return redirect('root')


# root view
def root(request):
    if 'player_name' not in request.session:
        return redirect('game_setup')
   
    activities = request.session.get('activities', [])

    if activities:
        sorted_activities = sorted(activities, key=lambda log: log['creationTime'], reverse=True)
    else:
        sorted_activities = []

    return render(request, 'index.html', {'activities': sorted_activities})


def process_money(request, location):
   if request.method == 'POST':
        min_gold = request.POST.get('min')
        max_gold = request.POST.get('max')

        #random number within range
        earned_gold = randrange(int(min_gold), int(max_gold))
        color = 'green' if earned_gold > 0 else 'red'
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
        active_log = {'building': location,
                      'earnedGold': earned_gold, 
                      'color':  color,
                      'creationTime': current_time
                    }
   
        if 'activities' not in request.session:
            request.session['activities'] = []
            
        #Update Session
        request.session['gold'] += earned_gold
        request.session['attempts'] -= 1
        request.session['activities'].append(active_log)
        
        if request.session['attempts'] <= 0:
           if request.session['gold'] >= request.session['goal_gold']:
              request.session['message'] = "🎉 You won! You reached your goal!"
           else:
              request.session['message'] = "😞 Game Over! You ran out of attempts."
           return redirect('achievement')
                       
        #Redirect back to index page
        return redirect('root')
  
def achievement(request):
     return render(request, 'end.html')

def reset(request):
    if request.method == 'POST':
        request.session.clear()
    return redirect('game_setup')
