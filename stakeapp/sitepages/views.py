# views.py
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from .forms import EntryForm
from .models import *

# Create your views here.

def Home(request):
    prizes = Prize.objects.all()
    data = {
        'ptitle': 'Stake App - Home',
        'prizes': prizes
    }
    return render(request,'sitepages/index.html',data)

def About(request):
    data = {'ptitle': 'Stake App - About'}
    return render(request,'sitepages/about.html',data)

def Contact(request):
    data = {'ptitle': 'Stake App - Contact'}
    return render(request,'sitepages/contact.html',data)


def Weekly_prize(request):
    prizes = Prize.objects.all()
    data = {
        'ptitle': 'Stake App - Weekly Grand Prizes',
        'prizes': prizes
    }
    return render(request,'sitepages/weekly_grand_prize.html',data)



@login_required
def prize_detail(request, prize_id):
    prize = get_object_or_404(Prize, id=prize_id)
    data = {
        'prize': prize,
        'ptitle': f'Prize Detail - {prize.name}'  # Include dynamic page title
    }
    return render(request, 'sitepages/prize_detail.html', data)





@login_required
def enter_to_win(request, prize_id):
    prize = get_object_or_404(Prize, id=prize_id)
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.prize = prize
            entry.save()
            return redirect('sitepages:entry_success', entry_id=entry.id)
    else:
        form = EntryForm()
    return render(request, 'sitepages/enter_to_win.html', {'form': form, 'prize': prize, 'ptitle': prize.name})


# views.py
def entry_success(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    account_details = AccountDetails.objects.first()  # Assuming you have only one set of account details
    return render(request, 'sitepages/entry_success.html', {'entry': entry, 'account_details': account_details})




@login_required
def entry_success(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    account = AccountDetails.objects.first()  # Get the first account details entry (you can modify this as needed)
    
    # Send email to the user
    send_mail(
        'Prize Entry Successful',
        f'Congratulations {entry.first_name},\n\n'
        f'You have successfully entered for the prize: {entry.prize.name}.\n'
        f'Your tracking number is {entry.tracking_number}.\n\n'
        f'Please make your payment to the following account details:\n'
        f'Account Name: {account.account_name}\n'
        f'Account Number: {account.account_number}\n'
        f'Bank Name: {account.bank_name}\n\n'
        f'Thank you for participating!Once your payment is received you will receive another mail with details on how to receive your prize.',
        settings.DEFAULT_FROM_EMAIL,
        [entry.email],
        fail_silently=False,
    )
    
    return render(request, 'sitepages/entry_success.html', {'entry': entry, 'account': account})

