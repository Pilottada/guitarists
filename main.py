#! /usr/bin/env python3

from guitarists import check_guitarist, check_band #adding_process
from csv_maker import csv_creator
import csv

check_guitarist("Kirk Hammet")
check_guitarist("Young Signorino")
check_band("Guns'n Roses")
check_band("Ricchi e Poveri")
#adding_process()
csv_creator()

