#Created by Seth Adams
print("How many credits are you taking? ");
credits = int(input());
if credits >= 12:
    tuition = credits * 580 + 650 + 250;
else:
    print("Do you want to pay the activity fee? (Yes/No)");
    response = input();
    if response == "Yes":
        activityFee = True;
    else:
        activityFee = False;
    if activityFee == True:
        tuition = credits * 580 + 650 + 250;
    else:
        tuition = credits * 580 + 650;
print("Your tuition will cost $" + str(tuition));
exit();