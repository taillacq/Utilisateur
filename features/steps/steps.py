from behave import *

# This should be added to environment.py
# from steps.actionwords import Actionwords
#
# def before_scenario(context, scenario):
#     context.actionwords = Actionwords()

use_step_matcher('re')


@given(r'G_open_session "(.*)" "(.*)" "(.*)" "(.*)"')
def impl(context, device_type, wrt_element_type, wrt_negation = "", user_type = ""):
    context.actionwords.g_open_session(device_type, wrt_element_type, wrt_negation, user_type, context.text)

@when(r'W_open_module "(.*)"')
def impl(context, element_value):
    context.actionwords.w_open_module(element_value)

@when(r'W_add_element "(.*)" "(.*)"')
def impl(context, element_type, element_value):
    context.actionwords.w_add_element(element_type, element_value)

@when(r'W_insert_element "(.*)" "(.*)"')
def impl(context, element_type, wrt_additional_informations):
    context.actionwords.w_insert_element(element_type, wrt_additional_informations)

@when(r'W_assign_element "(.*)" "(.*)" "(.*)" "(.*)"')
def impl(context, element_type, element_value, element_status = "", wrt_additional_informations = ""):
    context.actionwords.w_assign_element(element_type, element_value, element_status, wrt_additional_informations)

@then(r'T_create_element "(.*)" "(.*)" "(.*)" "(.*)"')
def impl(context, element_type, element_value, wrt_additional_informations, wrt_negation = ""):
    context.actionwords.t_create_element(element_type, element_value, wrt_additional_informations, wrt_negation)



























































































































































































































































































































































































































