from otree.api import *
import random


doc = """
Job Crafting Online Experiment --- Mai
"""


class C(BaseConstants):
    NAME_IN_URL = 'j_c'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_task():
    return models.IntegerField(
        choices=[
            [1, "A"],
            [2, "B"],
            [3, "C"],
            [4, "D"],
            [5, "E"]],
        label="",
        widget=widgets.RadioSelect,
    )





class Player(BasePlayer):
    #   Demographics
    age = models.IntegerField(label="Please enter your age:", min=18, max=100)
    gender = models.IntegerField(label="Please indicate your physical gender:",
                                 choices=[
                                     [0, "Male"],
                                     [1, "Female"],
                                 ])
    education = models.IntegerField(label="Please indicate your educational level:",
                                    choices=[
                                        [1, "Elementary School"],
                                        [2, "Middle School"],
                                        [3, "High School"],
                                        [4, "Under Graduate"],
                                        [5, "Post Graduate"],
                                        [0, "None"],
                                        [66, "Prefer not to tell"]
                                    ])
    
    field = models.IntegerField(label="Please select your field of study:",
                                choices=[
                                    [1, 'Arts & Humanities'],
                                    [2, 'Engineering and Technology'],
                                    [3, 'Life Sciences & Medicine'],
                                    [4, 'Natural Sciences'],
                                    [5, 'Social Sciences & Management'],
                                    [0, "None"],
                                    [66, "Prefer not to tell"]
                                ])
    
    #   Heights and weights

    heights = models.IntegerField(label="Please indicate your height in centimeter")
    weights = models.IntegerField(label="Please indicate your weight in kilogram")


    #   Well-being
    wb1 = models.IntegerField(label="I feel bursting with energy answering those questions",
                              choices=[
                                [1, "Strongly disagree"],
                                [2, "Disagree"],
                                [3, "Neutral"],
                                [4, "Agree"],
                                [5, "Strongly agree"]],
                              widget=widgets.RadioSelect)
    wb2 = models.IntegerField(label="I was enthusiastic about answering those questions",
                              choices=[
                                  [1, "Strongly disagree"],
                                  [2, "Disagree"],
                                  [3, "Neutral"],
                                  [4, "Agree"],
                                  [5, "Strongly agree"]],
                              widget=widgets.RadioSelect)
    wb3 = models.IntegerField(label="I was immersed in answering those questions",
                              choices=[
                                  [1, "Strongly disagree"],
                                  [2, "Disagree"],
                                  [3, "Neutral"],
                                  [4, "Agree"],
                                  [5, "Strongly agree"]],
                              widget=widgets.RadioSelect)
    wb1_r = models.IntegerField(label="I feel bursting with energy answering those questions",
                                choices=[
                                    [1, "Strongly disagree"],
                                    [2, "Disagree"],
                                    [3, "Neutral"],
                                    [4, "Agree"],
                                    [5, "Strongly agree"]],
                                widget=widgets.RadioSelect)
    wb2_r = models.IntegerField(label="I was enthusiastic about answering those questions",
                                choices=[
                                    [1, "Strongly disagree"],
                                    [2, "Disagree"],
                                    [3, "Neutral"],
                                    [4, "Agree"],
                                    [5, "Strongly agree"]],
                                widget=widgets.RadioSelect)
    wb3_r = models.IntegerField(label="I was immersed in answering those questions",
                                choices=[
                                    [1, "Strongly disagree"],
                                    [2, "Disagree"],
                                    [3, "Neutral"],
                                    [4, "Agree"],
                                    [5, "Strongly agree"]],
                                widget=widgets.RadioSelect)



    #   Timeout at end
    tout = models.BooleanField(initial=False)





def creating_session(subsession):
    import itertools
    qualitative = itertools.cycle([True, False])
    for player in subsession.get_players():
        player.qualitative = next(qualitative)


def set_fields(player, fields):
    for f in fields:
        if player.field_maybe_none(f) is None:
            exec('player.{} = False'.format(f))


# PAGES
class Welcome(Page):
    pass


class Instructions(Page):
    pass


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'field','heights','weights']


# Question 1

class Question1(Page):
    q1 = make_task()
    form_model = 'player'
    form_fields = ['q1', 'resure()']
    timeout_seconds = 120




class WB(Page):
    form_model = 'player'
    form_fields = ['wb1', 'wb2', 'wb3']



def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'quantitative', 'age', 'gender', 'education', 'field',
           'st_avg', 'wb_avg', 'wb_r_avg', 'extra_time', 'intime_set1', 'intime_set2',
           'preference', 'correct', 'payoff']
    for p in players:
        participant = p.participant
        session = p.session
        if p.field_maybe_none('st1') is None:
            p.st1 = 0
        if p.field_maybe_none('st2') is None:
            p.st2 = 0
        if p.field_maybe_none('st3') is None:
            p.st3 = 0
        if p.field_maybe_none('st4') is None:
            p.st4 = 0
        if p.field_maybe_none('st5') is None:
            p.st5 = 0
        if p.field_maybe_none('st6') is None:
            p.st6 = 0
        if p.field_maybe_none('st7') is None:
            p.st7 = 0
        if p.field_maybe_none('st8') is None:
            p.st8 = 0
        if p.field_maybe_none('wb1') is None:
            p.wb1 = 0
        if p.field_maybe_none('wb2') is None:
            p.wb2 = 0
        if p.field_maybe_none('wb3') is None:
            p.wb3 = 0
        if p.field_maybe_none('wb1_r') is None:
            p.wb1_r = 0
        if p.field_maybe_none('wb2_r') is None:
            p.wb2_r = 0
        if p.field_maybe_none('wb3_r') is None:
            p.wb3_r = 0
        st_avg = (p.st1 + p.st2 + p.st3 + p.st4 + p.st5 + p.st6 + p.st7 + p.st8)/8
        wb_avg = (p.wb1 + p.wb2 + p.wb3)/3
        wb_r_avg = (p.wb1_r + p.wb2_r + p.wb3_r)/3
        yield [session.code, participant.code,  p.qualitative, p.age, p.gender, p.education, p.field,
               st_avg, wb_avg, wb_r_avg, p.extra_time, p.intime_set1, p.intime_set2,
               p.preference, p.correct, p.payoff]


page_sequence = [Welcome, Instructions, Demographics, Question1, WB]
