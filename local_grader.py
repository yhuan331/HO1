#!/usr/bin/env python3

"""
Do a local practice grading.
The score you recieve here is not an actual score,
but gives you an idea on how prepared you are to submit to the autograder.
"""

import os
import sys

import pandas
import numpy

import autograder.assignment
import autograder.question
import autograder.style

THIS_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
DATA_PATH = os.path.join(THIS_DIR, 'synthetic_covid_data.csv')

class HO1(autograder.assignment.Assignment):
    def __init__(self, **kwargs):
        super().__init__(
            name = 'Practice Grading for Hands-On 1',
            additional_data = {
                'synthetic_data': pandas.read_csv(DATA_PATH, index_col = 'id')
            }, questions = [
                T0A(1, "Task 0.A (select_column)"),
                T0B(1, "Task 0.B (filter_rows)"),
                T0C(1, "Task 0.C (add_column)"),
                T0D(1, "Task 0.D (drop_column)"),
                T0E(1, "Task 0.E (concat_frames)"),
                T1A(1, "Task 1.A (count_infected)"),
                T1B(1, "Task 1.B (count_symptomatic)"),
                T1C(1, "Task 1.C (mean_days)"),
                T2A(1, "Task 2.A (fraction_infected)"),
                T2B(1, "Task 2.B (fraction_symptomatic)"),
                T2C(1, "Task 2.C (count_special_uninfected)"),
                T2D(1, "Task 2.D (fraction_isoantigenic)"),
                T3A(1, "Task 3.A (add_isoantigenic_column)"),
                T4A(1, "Task 4.A (prep_scatter)"),
                T5A(1, "Task 5.A (rmse)"),
                autograder.style.Style(kwargs.get('input_dir'), max_points = 1),
            ], **kwargs)

class T0A(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.select_column(synthetic_data, 'titer')
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, pandas.Series)):
            self.fail("Answer must be a column.")
            return

        self.full_credit()

class T0B(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.filter_rows(synthetic_data, 'titer', 32)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")
            return

        self.full_credit()

class T0C(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.add_column(pandas.DataFrame(), 'test', [])
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")
            return

        self.full_credit()

class T0D(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.drop_column(synthetic_data.copy(), 'titer')
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")
            return

        self.full_credit()

class T0E(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.concat_frames(pandas.DataFrame(), pandas.DataFrame())
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")
            return

        self.full_credit()

class T1A(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.count_infected(synthetic_data)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (int, numpy.integer))):
            self.fail("Answer must be an integer.")
            return

        self.full_credit()

class T1B(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.count_symptomatic(synthetic_data)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (int, numpy.integer))):
            self.fail("Answer must be an integer.")
            return

        self.full_credit()

class T1C(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.mean_days(synthetic_data)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (float, numpy.float64, numpy.float32))):
            self.fail("Answer must be a float.")
            return

        self.full_credit()

class T2A(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.fraction_infected(synthetic_data)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (float, numpy.float64, numpy.float32))):
            self.fail("Answer must be a float.")
            return

        self.full_credit()

class T2B(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.fraction_symptomatic(synthetic_data)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (float, numpy.float64, numpy.float32))):
            self.fail("Answer must be a float.")
            return

        self.full_credit()

class T2C(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.count_special_uninfected(synthetic_data)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (int, numpy.integer))):
            self.fail("Answer must be an integer.")
            return

        self.full_credit()

class T2D(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.fraction_isoantigenic(synthetic_data)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (float, numpy.float64, numpy.float32))):
            self.fail("Answer must be a float.")
            return

        self.full_credit()

class T3A(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.add_isoantigenic_column(synthetic_data)
        if (self.check_not_implemented(result)):
            return

        if ('isoantigenic' not in result):
            self.fail("Isoantigenic column is missing.")
            return

        self.full_credit()

class T4A(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        result = submission.__all__.prep_scatter(synthetic_data, 'days_before_symptoms',
                'titer', 'X', 'Y')

        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, pandas.DataFrame)):
            self.fail("Answer must be a DataFrame.")
            return

        self.full_credit()

class T5A(autograder.question.Question):
    def score_question(self, submission, synthetic_data):
        predictions = [1, 1, 0, 0]
        labels = [1, 0, 1, 0]

        result = submission.__all__.rmse(predictions, labels)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (float, numpy.float64, numpy.float32))):
            self.fail("Answer must be a float.")
            return

        self.full_credit()

def main(path):
    assignment = HO1(input_dir = path)
    result = assignment.grade()
    print(result.report())

def _load_args(args):
    exe = args.pop(0)
    if (len(args) != 1 or ({'h', 'help'} & {arg.lower().strip().replace('-', '') for arg in args})):
        print("USAGE: python3 %s <submission path (.py or .ipynb)>" % (exe), file = sys.stderr)
        sys.exit(1)

    path = os.path.abspath(args.pop(0))

    return path

if (__name__ == '__main__'):
    main(_load_args(list(sys.argv)))
