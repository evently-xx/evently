#!/usr/bin/env python

import os, sys
sys.path.append('../')
sys.path.append('../../')
import datetime


def parse_datetime(str_date):
  if str_date == None or str_date == '':
    return None

  fields = str_date.strip().split()
  date = fields[0]
  time = fields[1]

  fields = date.split('-')
  year = int(fields[0])
  month = int(fields[1])
  day = int(fields[2])

  fields = time.split(':')
  hour = int(fields[0])
  minute = int(fields[1])
  sec = int(fields[2])

  return datetime.datetime(year, month, day, hour, minute, sec)


def parse_date(str_date):
  if str_date == None or str_date == '':
    return None

  fields = str_date.strip().split('-')
  year = int(fields[0])
  month = int(fields[1])
  day = int(fields[2])

  return datetime.date(year, month, day)


def parse_time(str_time):
  if str_time == None or str_time == -1 or str_time == '':
    return None

  fields = str_time.strip().split(':')
  hour = int(fields[0])
  minute = int(fields[1])
  sec = int(fields[2])

  return datetime.time(hour, minute, sec)


def parse_category_id(category_id):
  return str(category_id).replace(';', ',')


def parse_int(value):
  if value == None or value == '':
    return None
  return int(value)
