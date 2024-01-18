from otree.api import *
import random
import math
import json
import sys


doc = """
Decision Making over Obsesity
"""


class C(BaseConstants):
    NAME_IN_URL = 'j_c'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


dict_values = {
    'q01': {
        'initial_value': 30,    # Updated initial_value for Option 1
        'v1': 85,
        'v2': 14,
        'v3': 0.86
    },
    'q02': {
        'initial_value': 40,    # Updated initial_value for Option 2
        'v1': 55,
        'v2': 25,
        'v3': 0.75
    },
    'q03': {
        'initial_value': 67,    # Updated initial_value for Option 3
        'v1': 85,
        'v2': 35,
        'v3': 0.65
    },
    'q04': {
        'initial_value': 34,    # Updated initial_value for Option 4
        'v1': 35,
        'v2': 43,
        'v3': 0.57
    },
    'q05': {
        'initial_value': 15,    # Updated initial_value for Option 5
        'v1': 35,
        'v2': 10,
        'v3': 0.9
    },
    'q06': {
        'initial_value': 32,    # Updated initial_value for Option 6
        'v1': 55,
        'v2': 20,
        'v3': 0.8
    },
    'q07': {
        'initial_value': 83,    # Updated initial_value for Option 7
        'v1': 85,
        'v2': 35,
        'v3': 0.65
    },
    'q08': {
        'initial_value': 21,    # Updated initial_value for Option 8
        'v1': 30,
        'v2': 75,
        'v3': 0.25
    },
    'q09': {
        'initial_value': 48,    # Updated initial_value for Option 9
        'v1': 55,
        'v2': 45,
        'v3': 0.55
    },
    'q10': {
        'initial_value': 65,    # Updated initial_value for Option 10
        'v1': 65,
        'v2': 70,
        'v3': 0.3
    },
    'q11': {
        'initial_value': 25,    # Updated initial_value for Option 11
        'v1': 35,
        'v2': 25,
        'v3': 0.75
    },
    'q12': {
        'initial_value': 75,    # Updated initial_value for Option 12
        'v1': 75,
        'v2': 50,
        'v3': 0.5
    },
    'q13': {
        'initial_value': 30,    # Updated initial_value for Option 13
        'v1': 30,
        'v2': 75,
        'v3': 0.25
    },
    'q14': {
        'initial_value': 30,    # Updated initial_value for Option 14
        'v1': 50,
        'v2': 60,
        'v3': 0.4
    },
    'q15': {
        'initial_value': 53,    # Updated initial_value for Option 15
        'v1': 55,
        'v2': 55,
        'v3': 0.45
    },
    'q16': {
        'initial_value': 30,    # Updated initial_value for Option 16
        'v1': 30,
        'v2': 20,
        'v3': 0.65
    },
    'q17': {
        'initial_value': 40,    # Updated initial_value for Option 17
        'v1': 55,
        'v2': 10,
        'v3': 0.9
    },
    'q18': {
        'initial_value': 50,    # Updated initial_value for Option 18
        'v1': 80,
        'v2': 70,
        'v3': 0.3
    },
    'q19': {
        'initial_value': 70,    # Updated initial_value for Option 19
        'v1': 70,
        'v2': 35,
        'v3': 0.65
    },
    'q20': {
        'initial_value': 27,    # Updated initial_value for Option 20
        'v1': 30,
        'v2': 35,
        'v3': 0.65
    },
    'q21': {
        'initial_value': 16,    # Updated initial_value for Option 21
        'v1': 30,
        'v2': 35,
        'v3': 0.65
    }
}



# Calculate discounting rate
for q_key in dict_values:
    initial_value = dict_values[q_key]['initial_value']
    v1 = dict_values[q_key]['v1']
    v2 = dict_values[q_key]['v2']
    v3 = dict_values[q_key]['v3']
    k = round(-(math.log(initial_value/v1)/v2), 4)
    h = round(-((math.log(initial_value/v1))*(1-v3)/v2), 4)
    dict_values[q_key][2] = k
    dict_values[q_key][3] = h
    dict_values[q_key][1] = 1




# Questions
def question(v1, v2, v3):
    return models.IntegerField(
        choices=[
            [1, "Take the money and go away."],
            [2, f"Get {v1} euro by yourself in {v2} days."],
            [3, f"Take part in a lottery that will have a {v3} probability to get {v1} euro."]
            ],
        label="",
        widget=widgets.RadioSelect,
    
    ) 




class Player(BasePlayer):
    inivalue = {q_key: dict_values[q_key]['initial_value'] for q_key in dict_values}
    #   Demographics
    age = models.IntegerField(label="Please enter your age:", min=18, max=100, initial = 23)
    gender = models.IntegerField(label="Please indicate your physical gender:",
                                 choices=[
                                     [0, "Male"],
                                     [1, "Female"]],
                                initial = 1
                                 )
    education = models.IntegerField(label="Please indicate your educational level:",
                                    choices=[
                                        [1, "Elementary School"],
                                        [2, "Middle School"],
                                        [3, "High School"],
                                        [4, "Under Graduate"],
                                        [5, "Post Graduate"],
                                        [0, "None"],
                                        [66, "Prefer not to tell"]],
                                    initial = 1
                                    )
    
    field = models.IntegerField(label="Please indicate your field of study:",
                                choices=[
                                    [1, 'Arts & Humanities'],
                                    [2, 'Engineering and Technology'],
                                    [3, 'Life Sciences & Medicine'],
                                    [4, 'Natural Sciences'],
                                    [5, 'Social Sciences & Management'],
                                    [0, "None"],
                                    [66, "Prefer not to tell"]],
                                initial = 1
                                )
    
    vegan = models.IntegerField(label="Please indicate your diet style:",
                                choices=[
                                    [1, 'Vegan'],
                                    [2, 'Vegetarian'],
                                    [3, 'None of above']],
                                initial = 1
                                )
    
    #   Heights and weights

    heights = models.IntegerField(label="Please indicate your height in centimeter", initial = 182)
    weights = models.IntegerField(label="Please indicate your weight in kilogram", initial = 75)


    # Questions

    #[1, "Take the money and go away."],
    #[2, f"Get {v1} euro by yourself in {v2} days."],
    #[3, f"Take part in a lottery that will have a {v3} probability to get {v1} euro."]
    qem = question(100, 100, 100)

    q01 = question(85, 14, 0.86)
    q02 = question(55, 25, 0.75)
    q03 = question(85, 35, 0.65)
    q04 = question(35, 43, 0.57)
    q05 = question(35, 10, 0.9)
    q06 = question(55, 20, 0.8)
    q07 = question(85, 35, 0.65)
    q08 = question(30, 75, 0.25)
    q09 = question(55, 45, 0.55)
    q10 = question(65, 70, 0.3)
    q11 = question(35, 25, 0.75)
    q12 = question(75, 50, 0.5)
    q13 = question(30, 75, 0.25)
    q14 = question(50, 60, 0.4)
    q15 = question(55, 55, 0.45)
    q16 = question(30, 20, 0.65)
    q17 = question(55, 10, 0.9)
    q18 = question(80, 70, 0.3)
    q19 = question(70, 35, 0.65)
    q20 = question(30, 35, 0.65)
    q21 = question(30, 35, 0.65)
    
    # BMI
    
    def status(self):
        bmi = self.weights/((self.heights/100)**2)
        status = "thin"
        if bmi >= 18.5 and bmi < 24.9:
            status = "healthy"
        elif bmi >= 25.0 and bmi < 29.9:
            status = "overweight"
        elif bmi >= 30.0:
            status = "obesed"

        return status
        
    #   Exponential discounting rate
    def discounting(self):
        sum = 0
        for q_key in dict_values:
    
            sum += dict_values[q_key][getattr(self, q_key, 'u')]

        return round(sum/21, 3)

        


def data_out(players):
    # header row
    yield ['session', 'participant_code', 'id_in_group', 'status', 'discounting']
    for p in players:
        participant = p.participant
        session = p.session
        status = p.status
        discounting = p.discounting
        yield [session.code, participant.code, p.status , p.id_in_group, p.discounting]


# PAGES
class Welcome(Page):
    pass


class Instructions(Page):
    pass


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'field','heights','weights','vegan']




# Example Question
class Question0(Page):
    form_model = 'player'
    form_fields = ['qem']




# Questions
class Question1(Page):
    form_model = 'player'
    form_fields = ['q01']

    timeout_seconds = 120


class Question2(Page):
    form_model = 'player'
    form_fields = ['q02']
    timeout_seconds = 120

class Question3(Page):
    form_model = 'player'
    form_fields = ['q03']
    timeout_seconds = 120

class Question4(Page):
    form_model = 'player'
    form_fields = ['q04']
    timeout_seconds = 120

class Question5(Page):
    form_model = 'player'
    form_fields = ['q05']
    timeout_seconds = 120

class Question6(Page):
    form_model = 'player'
    form_fields = ['q06']
    timeout_seconds = 120

class Question7(Page):
    form_model = 'player'
    form_fields = ['q07']
    timeout_seconds = 120

class Question8(Page):
    form_model = 'player'
    form_fields = ['q08']
    timeout_seconds = 120

class Question9(Page):
    form_model = 'player'
    form_fields = ['q09']
    timeout_seconds = 120

class Question10(Page):
    form_model = 'player'
    form_fields = ['q10']
    timeout_seconds = 120

class Question11(Page):
    form_model = 'player'
    form_fields = ['q11']
    timeout_seconds = 120

class Question12(Page):
    form_model = 'player'
    form_fields = ['q12']
    timeout_seconds = 120

class Question13(Page):
    form_model = 'player'
    form_fields = ['q13']
    timeout_seconds = 120

class Question14(Page):
    form_model = 'player'
    form_fields = ['q14']
    timeout_seconds = 120

class Question15(Page):
    form_model = 'player'
    form_fields = ['q15']
    timeout_seconds = 120

class Question16(Page):
    form_model = 'player'
    form_fields = ['q16']
    timeout_seconds = 120

class Question17(Page):
    form_model = 'player'
    form_fields = ['q17']
    timeout_seconds = 120

class Question18(Page):
    form_model = 'player'
    form_fields = ['q18']
    timeout_seconds = 120

class Question19(Page):
    form_model = 'player'
    form_fields = ['q19']
    timeout_seconds = 120

class Question20(Page):
    form_model = 'player'
    form_fields = ['q20']
    timeout_seconds = 120

class Question21(Page):
    form_model = 'player'
    form_fields = ['q21']
    timeout_seconds = 120




class Discountingrate(Page):
    form_model = 'player'
    pass



class End(Page):
    pass



page_sequence = [
    Welcome,
    Instructions,
    Demographics,
    Question0,
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6,
    Question7,
    Question8,
    Question9,
    Question10,
    Question11,
    Question12,
    Question13,
    Question14,
    Question15,
    Question16,
    Question17,
    Question18,
    Question19,
    Question20,
    Question21,
    Discountingrate,
    End
]

