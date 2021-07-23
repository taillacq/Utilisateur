from features.steps.actionwords import Actionwords

def before_all(context):
    context.actionwords = Actionwords()

def after_all(context):
    pass