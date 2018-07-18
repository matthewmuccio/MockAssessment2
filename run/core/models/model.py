#!/usr/bin/env python3


from core.models import mapper


def get_item_data(item_name):
    return mapper.get_item_data(item_name)